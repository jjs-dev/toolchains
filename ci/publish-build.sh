set -euxo pipefail
export DOCKER_BUILDKIT=1
python3 build.py --tag-template toolchain-%
