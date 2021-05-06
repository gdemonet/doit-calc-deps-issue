from pathlib import Path


DOIT_CONFIG = {"default_tasks": ["make_mod"]}

# Build directory
BUILD_DIR = Path(__file__).parent / "_build"


def make_builddir():
    BUILD_DIR.mkdir(exist_ok=True)


def task_make_builddir():
    return {"actions": [make_builddir]}


# Core "module building" task
def print_deps(mod, dependencies):
    print("%s -> %s" % (mod, dependencies))


def make_mod(mod):
    (BUILD_DIR / mod).touch()


def task_make_mod():
    for mod in MOD_IMPORTS.keys():
        yield {
            "name": mod,
            "actions": [
                (print_deps, (mod,)),
                (make_mod, (mod,)),
            ],
            "targets": [BUILD_DIR / mod],
            "task_dep": ["make_builddir"],
            "calc_dep": ["get_dep:%s" % mod],
        }

# "Dynamic" dependencies calculation
MOD_IMPORTS = {"a": ["b", "c"], "b": ["f", "g"], "c": [], "f": ["c"], "g": []}


def get_dep(mod):
    # fake implementation
    return {
        "file_dep": [BUILD_DIR / dep for dep in MOD_IMPORTS[mod]],
        "task_dep": [f"make_mod:{dep}" for dep in MOD_IMPORTS[mod]],
    }


def task_get_dep():
    """get direct dependencies for each module"""
    for mod in MOD_IMPORTS.keys():
        yield {
            "name": mod,
            "actions": [(get_dep, [mod])],
        }
