from pathlib import Path


def tree(directory):
    print(f"{directory}")
    for path in sorted(directory.rglob("*")):
        depth = len(path.relative_to(directory).parts)
        spacer = "      " * (depth - 1)
        print(f"{spacer}\u2514---- {path.name}")


tree(Path().cwd())
