name = "quazip"

version = "1.1.0.sse.1.0.0"

description = \
    """
    QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package (AKA Minizip)
    using Trolltech's Qt library.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

    #c.build_thread_count = "physical_cores"

requires = [
    "qt-5",
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"],
]

uuid = "repository.quazip"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.QUAZIP_LOCATION = "{root}"
    env.QUAZIP_ROOT = "{root}"
    env.LD_LIBRARY_PATH.append("{root}/lib64")
