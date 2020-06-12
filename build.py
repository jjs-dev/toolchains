#!/usr/bin/env python3
import sys
import os
import typing
import argparse
import subprocess

try:
    open("./build.py")
except FileNotFoundError:
    print("run at repository root")
    exit(1)


def list_all_toolchains() -> typing.List[str]:
    l = os.listdir(".")
    return [item for item in l if item != "." and item != ".." and (not item.startswith(".")) and os.path.isdir(item)]


def calc_selected_toolchains(whitelist: typing.Optional[typing.List[str]]) -> typing.List[str]:
    all_toolchains = list_all_toolchains()
    if whitelist is None:
        return all_toolchains
    ok = True
    for toolchain in whitelist:
        if not toolchain in all_toolchains:
            print(f"unknown toolchain {toolchain}")
            ok = False
    if not ok:
        exit(1)
    return whitelist


def build_toolchain(toolchain_name: str):
    # TODO support docker
    subprocess.check_call(
        ["podman", "build", "-f", f"{toolchain_name}/Dockerfile", f"{toolchain_name}/src"])


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "--only", help="comma-separated list of toolchain that should be built (instead of all toolchains)")
args = arg_parser.parse_args()

only = args.only
if only is not None:
    only = only.split(',')

selected_toolchains = calc_selected_toolchains(only)
print(f"will build {selected_toolchains}")

for toolchain in selected_toolchains:
    print(f"building {toolchain}")
    build_toolchain(toolchain)
