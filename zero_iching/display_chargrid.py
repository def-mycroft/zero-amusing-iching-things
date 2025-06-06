"""Render a hexagram as a decorative character grid."""

from zero_iching.helpers import (
    HEXAGRAM_NAMES,
    HEXAGRAM_EN_NAMES,
    print_hexagram,
)


def display_hex_chargrid(bits: str) -> None:
    """Display a hexagram in a simple character grid.

    Parameters
    ----------
    bits : str
        Six-bit binary string ordered from bottom to top.
    """
    if len(bits) != 6 or set(bits) - {"0", "1"}:
        raise ValueError("bits must be a 6-character binary string")

    lower = bits[:3]
    upper = bits[3:]
    lower_name = HEXAGRAM_NAMES.get(lower, "")
    upper_name = HEXAGRAM_NAMES.get(upper, "")
    lower_en = HEXAGRAM_EN_NAMES.get(lower, "")
    upper_en = HEXAGRAM_EN_NAMES.get(upper, "")
    print(
        f"Names: {upper_name} ({upper_en}) over {lower_name} ({lower_en})"
    )
    print(f"Binary: {bits} ({lower} | {upper})")
    # Build a simple grid using block characters
    for b in reversed(bits):
        if b == "1":
            print("⣿" * 10)
        else:
            print("⣿⣿⣿  ⣿⣿⣿")
    print()
    # Also print using the thinner print_hexagram helper
    print_hexagram(list(bits), scale=1)

