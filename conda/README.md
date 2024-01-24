**NOTE: this hasn't been updated for a few years. Probably will not work as-is.**

On Mac, still need to download and unpack:
https://github.com/phracker/MacOSX-SDKs/releases/download/10.13/MacOSX10.9.sdk.tar.xz

And add it to conda_build_config.yaml as in
https://conda.io/docs/user-guide/tasks/build-packages/compiler-tools.html#macos-sdk

e.g.

CONDA_BUILD_SYSROOT:
  - /opt/MacOSX10.9.sdk        # [osx]