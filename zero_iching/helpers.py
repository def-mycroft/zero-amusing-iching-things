
HEXAGRAM_NAMES = {
    '111': "Ch'ien",     # ☰  Heaven
    '000': "K'un",       # ☷  Earth
    '010': "K'an",       # ☵  Water
    '101': "Li",         # ☲  Fire
    '001': "Chen",       # ☳  Thunder
    '100': "Ken",        # ☶  Mountain
    '110': "Sun",        # ☴  Wind/Wood
    '011': "Tui",        # ☱  Lake
}

HEXAGRAM_EN_NAMES = {
    '111': 'Heaven',  # Ch'ien (Heaven)
    '000': 'Earth',  # K'un (Earth)
    '010': 'Water',  # K'an (Water)
    '101': 'Fire',  # Li (Fire)
    '001': 'Thunder',  # Chen (Thunder)
    '100': 'Mountain',  # Ken (Mountain)
    '110': 'Wind/Wood',  # Sun (Wind/Wood)
    '011': 'Lake',  # Tui (Lake)
}

HEXAGRAM_SYMBOLS = {
    '111': '☰',  # Ch'ien (Heaven)
    '000': '☷',  # K'un (Earth)
    '010': '☵',  # K'an (Water)
    '101': '☲',  # Li (Fire)
    '001': '☳',  # Chen (Thunder)
    '100': '☶',  # Ken (Mountain)
    '110': '☴',  # Sun (Wind/Wood)
    '011': '☱',  # Tui (Lake)
}



def uuid_to_bin(uuid_str):
    """Convert UUID string to 128-bit binary string."""
    hex_str = uuid_str.replace('-', '')
    return bin(int(hex_str, 16))[2:].zfill(128)


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

