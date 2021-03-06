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


def build_toolchain(toolchain_name: str, tag: typing.Optional[str], container_manager=None):
    if container_manager is None:
        container_manager = "podman"
    args = [container_manager, "build", "-f",
            f"{toolchain_name}/Dockerfile", f"{toolchain_name}/src"]
    if tag is not None:
        args.append("-t")
        args.append(tag)
    subprocess.check_call(args)


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "--only", help="Comma-separated list of toolchain that should be built (instead of all toolchains)")
arg_parser.add_argument(
    "--tag-template", help="Template that will be used to tag built images. % will be replaced by toolchain name (=directory name")
arg_parser.add_argument(
    "--write-tags", help="All tags will be printend to specified file"
)
arg_parser.add_argument(
    "--container-manager", help="Container manager to use instead of podman"
)
args = arg_parser.parse_args()

only = args.only
if only is not None:
    only = only.split(',')

selected_toolchains = calc_selected_toolchains(only)
print(f"will build {selected_toolchains}")
print(args)

tags_file = None
if args.write_tags is not None:
    tags_file = open(args.write_tags, 'w')

for toolchain in selected_toolchains:
    print(f"building {toolchain}")
    tag = None
    if args.tag_template is not None:
        tag = args.tag_template.replace('%', toolchain)
        print(f"will tag as {tag}")
        if tags_file is not None:
            print(tag, file=tags_file)
    build_toolchain(toolchain, tag, container_manager=args.container_manager)
