
HEXAGRAM_NAMES = {
    '111': "ch'ien",     # ☰  Heaven
    '000': "k'un",       # ☷  Earth
    '010': "k'an",       # ☵  Water
    '101': "li",         # ☲  Fire
    '001': "chen",       # ☳  Thunder
    '100': "ken",        # ☶  Mountain
    '110': "sun",        # ☴  Wind/Wood
    '011': "tui",        # ☱  Lake
}


def uuid_to_bin(uuid_str):
    """Convert UUID string to 128-bit binary string."""
    hex_str = uuid_str.replace('-', '')
    return bin(int(hex_str, 16))[2:].zfill(128)


YANG_LINE = "---"
YIN_LINE = "- -"


def print_hexagram(hexagram_lines, scale=1):
    """Print a hexagram using text characters.

    Parameters
    ----------
    hexagram_lines : list[str]
        Sequence of six line descriptors from bottom to top. Each
        descriptor should match ``YANG_LINE`` or ``YIN_LINE``.
    scale : int, optional
        Size multiplier controlling the width and height of each line.
        ``scale`` must be a positive integer.
    """

    if len(hexagram_lines) != 6:
        raise ValueError("hexagram_lines must contain exactly 6 elements")
    if scale < 1:
        raise ValueError("scale must be >= 1")

    yang_segment = "━" * (3 * scale)
    yin_segment = "━" * scale + " " * scale + "━" * scale

    for line in reversed(hexagram_lines):
        segment = yang_segment if line.strip() == YANG_LINE else yin_segment
        for _ in range(scale):
            print(segment)

