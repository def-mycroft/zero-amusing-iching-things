import sys
from uuid import uuid4 as _uuid4

from zero_iching import helpers
from zero_iching.uuid_diviner import hexagrams_from_uuid, YANG_LINE, YIN_LINE
from zero_iching.bit_waterfall import visualize_waterfall

helpers.YANG_LINE = YANG_LINE
helpers.YIN_LINE = YIN_LINE

HEXAGRAM_NAMES = helpers.HEXAGRAM_NAMES
HEXAGRAM_SYMBOLS = helpers.HEXAGRAM_SYMBOLS
print_hexagram = helpers.print_hexagram
uuid_to_bin = helpers.uuid_to_bin


def visualize_uuid(uuid_str: str, n: int = 1, scale: int = 1) -> None:
    """Print a visual demonstration of deriving hexagrams from a UUID."""
    bits = uuid_to_bin(uuid_str)
    print(f"UUID : {uuid_str}")
    print(f"Binary: {bits}\n")
    visualize_waterfall(bits, n=n)
    hex_list = hexagrams_from_uuid(uuid_str, n=n)
    for i, code in enumerate(hex_list):
        lower = code[:3]
        upper = code[3:]
        lower_name = HEXAGRAM_NAMES.get(lower, "")
        upper_name = HEXAGRAM_NAMES.get(upper, "")
        lower_symbol = HEXAGRAM_SYMBOLS.get(lower, "")
        upper_symbol = HEXAGRAM_SYMBOLS.get(upper, "")
        print()
        print(f"Hexagram {i + 1}: {upper_symbol} over {lower_symbol} ({upper_name}/{lower_name})")
        print_hexagram(list(code), scale=scale)


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else str(_uuid4())
    visualize_uuid(arg)
