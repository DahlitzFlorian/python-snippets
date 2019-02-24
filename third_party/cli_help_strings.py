"""CLI HELP STRINGS
Usage:
    cli_help_strings.py
    cli_help_strings.py <name>
    cli_help_strings.py -h|--help
    cli_help_strings.py -v|--version
Options:
    <name>  Optional name argument.
    -h --help  Show this screen.
    -v --version  Show version.
"""
from docopt import docopt


def say_hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    arguments = docopt(__doc__, version="DEMO 1.0")
    if arguments["<name>"]:
        print(say_hello(arguments["<name>"]))
    else:
        print(arguments)
