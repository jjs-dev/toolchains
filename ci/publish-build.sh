set -euxo pipefail
export DOCKER_BUILDKIT=1
mkdir out
python3 build.py --tag-template toolchain-%
