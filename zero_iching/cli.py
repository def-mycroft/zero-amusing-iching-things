"""Command line interface for zero-iching."""
import argparse
import os
from uuid import uuid4 as uuid

from jinja2 import Environment, FileSystemLoader, select_autoescape

from zero_iching import main as zero_iching_alias
from zero_iching.helpers import (
    HEX_DESC,
    HEXAGRAM_NAMES,
    HEXAGRAM_EN_NAMES,
    HEXAGRAM_SYMBOLS,
)
from zero_iching.uuid_diviner import hexagrams_from_uuid


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

    subparsers = parser.add_subparsers(dest="command")

    uuid_parser = subparsers.add_parser(
        "uuid", help="Derive hexagrams from a UUID"
    )
    uuid_parser.add_argument(
        "--uuid",
        default=None,
        help="UUID to divine from. Provide empty string to generate a random one.",
    )
    uuid_parser.add_argument(
        "-n",
        type=int,
        default=1,
        help="Number of hexagrams to produce",
    )

    game_parser = subparsers.add_parser(
        "game", help="Generate interactive Dao Field HTML"
    )
    game_parser.add_argument("--grid", action="store_true", help="Create grid html")
    game_parser.add_argument(
        "-n",
        "--size",
        type=int,
        default=64,
        help="Grid size (n x n)",
    )
    game_parser.add_argument(
        "--savegrid",
        default=None,
        help="Path to saved grid json",
    )
    game_parser.add_argument(
        "-o",
        "--output",
        default="dao_field.html",
        help="Output HTML file",
    )

    return parser


def render_uuid_hexagrams(uuid_str: str, n: int = 1) -> str:
    """Return a formatted string for ``uuid`` command output."""
    hex_list = hexagrams_from_uuid(uuid_str, n=n)
    structured = []
    for code in hex_list:
        lower = code[:3]
        upper = code[3:]
        structured.append(
            {
                "code": code,
                "lower_code": lower,
                "upper_code": upper,
                "lower_name": HEXAGRAM_NAMES.get(lower, ""),
                "upper_name": HEXAGRAM_NAMES.get(upper, ""),
                "lower_en": HEXAGRAM_EN_NAMES.get(lower, ""),
                "upper_en": HEXAGRAM_EN_NAMES.get(upper, ""),
                "lower_symbol": HEXAGRAM_SYMBOLS.get(lower, ""),
                "upper_symbol": HEXAGRAM_SYMBOLS.get(upper, ""),
                "lower_desc": HEX_DESC.get(lower, ""),
                "upper_desc": HEX_DESC.get(upper, ""),
            }
        )

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(),
    )
    template = env.get_template("uuid_output.jinja2")
    return template.render(uuid=uuid_str, hexagrams=structured)


def main(argv=None) -> int:
    """Entry point for the command line."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "uuid":
        uuid_str = args.uuid
        if uuid_str is None or uuid_str == "":
            uuid_str = str(uuid())
        output = render_uuid_hexagrams(uuid_str, n=args.n)
        print(output)
        return 0

    if args.command == "game" and args.grid:
        from zero_iching.dao_field import DaoField

        if args.savegrid:
            field = DaoField.load(args.savegrid)
        else:
            field = DaoField.generate(args.size)
        field.write_html(args.output)
        print(f"HTML written to {args.output}")
        return 0

    # Default behavior
    return zero_iching_alias()


if __name__ == "__main__":
    raise SystemExit(main())
