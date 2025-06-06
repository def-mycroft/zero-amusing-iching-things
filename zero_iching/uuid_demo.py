import sys
from uuid import uuid4 as _uuid4

from zero_iching import helpers
from zero_iching.uuid_diviner import hexagrams_from_uuid, YANG_LINE, YIN_LINE

helpers.YANG_LINE = YANG_LINE
helpers.YIN_LINE = YIN_LINE

HEXAGRAM_NAMES = helpers.HEXAGRAM_NAMES
HEXAGRAM_SYMBOLS = helpers.HEXAGRAM_SYMBOLS
print_hexagram = helpers.print_hexagram
uuid_to_bin = helpers.uuid_to_bin


def visualize_uuid(uuid_str: str, n: int = 1, offset: int = 0, scale: int = 1) -> None:
    """Print a visual demonstration of deriving hexagrams from a UUID.

    Parameters
    ----------
    uuid_str : str
        UUID to interpret.
    n : int, optional
        Number of hexagrams to display.
    offset : int, optional
        Bit offset to start reading from.
    scale : int, optional
        Scaling factor for ``print_hexagram``.
    """
    bits = uuid_to_bin(uuid_str)
    print(f"UUID : {uuid_str}")
    print(f"Binary: {bits}\n")

    # Show the 6-bit blocks that make up the hexagrams
    blocks = [bits[i : i + 6] for i in range(0, 126, 6)]
    tail = bits[126:]
    for i, blk in enumerate(blocks):
        end = "\n" if (i + 1) % 7 == 0 else "  "
        print(f"{i:02d}:{blk}", end=end)
    if tail:
        print(f"tail:{tail}")
    else:
        print()

    hex_list = hexagrams_from_uuid(uuid_str, n=n, offset=offset)
    for i in range(0, len(hex_list), 2):
        code = hex_list[i]
        lower, upper = hex_list[i + 1]
        start = offset + (i // 2) * 6
        chunk = bits[start : start + 6]
        lower_name = HEXAGRAM_NAMES.get(lower, "")
        upper_name = HEXAGRAM_NAMES.get(upper, "")
        lower_symbol = HEXAGRAM_SYMBOLS.get(lower, "")
        upper_symbol = HEXAGRAM_SYMBOLS.get(upper, "")
        print()
        print(f"Hexagram {i // 2 + 1} bits [{start}:{start + 6}] -> {chunk}")
        print(f"  {upper_symbol} over {lower_symbol} ({upper_name}/{lower_name})")
        print_hexagram(list(code), scale=scale)


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else str(_uuid4())
    visualize_uuid(arg)
