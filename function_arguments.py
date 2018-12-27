def main():
    positional("Cheese", 21, "Meat")
    optional_keyword("Cheese", 21, "Meat")
    optional_keyword("Cheese", 21, arg3="Meat")
    force_keyword("Cheese", 21, arg3="Meat")
    force_keyword("Cheese", 21, "Meat")


def positional(arg1: str, arg2: int, arg3: str):
    print(arg1, arg2, arg3)


def optional_keyword(arg1: str, arg2: int, arg3: str=None):
    print(arg1, arg2, arg3)


def force_keyword(arg1: str, arg2: int, *, arg3: str=None):
    print(arg1, arg2, arg3)


if __name__ == "__main__":
    main()
