set -euxo pipefail

# GENERATED FILE DO NOT EDIT
if [ "$GITHUB_REF" = "refs/heads/master" ]
then
  TAG="latest"
elif [ "$GITHUB_REF" = "refs/heads/trying" ]
then
  TAG="dev"
else
  echo "unknown GITHUB_REF: $GITHUB_REF"
  exit 1
fi
echo $GITHUB_TOKEN | docker login ghcr.io -u $GITHUB_ACTOR --password-stdin
docker tag toolchain-gcc ghcr.io/jjs-dev/toolchain-gcc:$TAG
docker push ghcr.io/jjs-dev/toolchain-gcc:$TAG
docker tag toolchain-python3 ghcr.io/jjs-dev/toolchain-python3:$TAG
docker push ghcr.io/jjs-dev/toolchain-python3:$TAG
docker tag toolchain-gcc-cpp ghcr.io/jjs-dev/toolchain-gcc-cpp:$TAG
docker push ghcr.io/jjs-dev/toolchain-gcc-cpp:$TAG