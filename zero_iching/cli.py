"""Command line interface for zero-iching."""
import argparse
import os
from zero_iching import main as zero_iching_alias


def load_help_text() -> str:
    """Load help text from CLI_HELP.md."""
    help_path = os.path.join(os.path.dirname(__file__), "CLI_HELP.md")
    try:
        with open(help_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Help documentation not found."


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    help_text = load_help_text()
    parser = argparse.ArgumentParser(
        prog="zero-iching",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="zero-iching command line interface",
        epilog=help_text,
    )
    parser.add_argument("--version", action="version", version="zero-iching 0.1.0")
    return parser


def main(argv=None) -> int:
    """Entry point for the command line."""
    parser = build_parser()
    args = parser.parse_args(argv)

    # Execute the library main function
    return zero_iching_alias()


if __name__ == "__main__":
    raise SystemExit(main())
