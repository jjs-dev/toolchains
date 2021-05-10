#!/usr/bin/env python3
# This script verifies ./ci/config.yaml based on current toolchains.
# Currently config itself must be updated manually but we at least ensure
# that it is correct
import os
import yaml

def emit_toolchain_image_name(toolchain_name: str):
    return f'toolchain-{toolchain_name}'


toolchains = [item for item in os.listdir('.') if item != "." and item != ".." and item != "ci" and (
    not item.startswith(".")) and os.path.isdir(item)]
print("Toolchains:", toolchains)

cfg = open('ci/config.yaml').read()
cfg_data = yaml.load(cfg, Loader=yaml.BaseLoader)

for toolchain in toolchains:
    image = emit_toolchain_image_name(toolchain)
    if not image in cfg_data['dockerImages']:
        print(f"Image not mentioned in config: {image}")
        exit(1)


assert len(cfg_data['dockerImages']) == len(toolchains)
