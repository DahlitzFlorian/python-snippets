from collections import ChainMap


def main():
    command_line_args = get_command_line_args()
    config_file = get_config()
    default_config = get_default_config()

    config_dict = ChainMap(command_line_args, config_file, default_config)


def get_command_line_args() -> dict:
    pass


def get_config() -> dict:
    pass


def get_default_config() -> dict:
    pass


if __name__ == "__main__":
    main()
