# JJS Toolchain Database
This repository contains default toolchain set for JJS
## What is toolchain?
Toolchain is compiler or interpreter of some language.
It both contains their binaries and information about how they should be used.
## Contributing
If you want to create new toolchain, create directory for it in repo root.
Use follosing structure:
`$TOOLCHAIN_NAME/src` is Docker build context.
`$TOOLCHAIN_NAME/Dockerfile` is Dockerfile.
Use `build.py` tool to build your image.
It is recommended to pass `--only=$TOOLCHAIN_NAME` to get feedback faster.
## Guidelines
 - All images should be based on `debian:slim`
 - All toolchain should somehow pass ONLINE_JUDGE option to compiled/executed program.