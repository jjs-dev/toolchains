#!/usr/bin/env python3
# This script generated cloudbuild.yaml config based on current toolchains.
# It must be invoked each time a toolchain is added/deleted.
import os
import yaml


def emit_toolchain_build_step(toolchain_name: str):
    return {
        'name': 'gcr.io/cloud-builders/docker',
        'args': [
            'build',
            '-t',
            emit_toolchain_image_name(toolchain_name),
            '-f',
            f'{toolchain_name}/Dockerfile',
            f'{toolchain_name}/src'
        ]
    }


def emit_toolchain_image_name(toolchain_name: str):
    return f'gcr.io/jjs-dev/toolchain-{toolchain_name}'


toolchains = [item for item in os.listdir('.') if item != "." and item != ".." and (
    not item.startswith(".")) and os.path.isdir(item)]
print("Toolchains:", toolchains)


doc = {
    'steps': [emit_toolchain_build_step(toolchain) for toolchain in toolchains],
    'images': [emit_toolchain_image_name(toolchain) for toolchain in toolchains]
}
out = open('cloudbuild.yaml', 'w')
out.write(yaml.dump(doc))
