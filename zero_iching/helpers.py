
HEX_DESC = {
    '111': "Ch'ien moves like the clear sky: forceful, expansive, unyielding. It is the father, the origin, the light before thought. Everything begins with its power. When aligned with Ch'ien, one rides the dragon and rises. Its danger lies in arrogance; its virtue is perseverance.",
    '000': "K'un is the earth: vast, yielding, receptive. It accepts without resistance and nourishes without pride. Where Ch'ien acts, K'un allows; where Ch'ien initiates, K'un completes. It is the mother of all, and so bears the weight of the world. In her silence, all things take root.",
    '010': "K'an is water flowing in darkness, dangerous yet cleansing. It sinks deep, probing the unseen paths beneath the surface. Danger is its companion, but so is wisdom. To follow K'an is to endure difficulty and emerge clarified. Its essence is the struggle that shapes strength.",
    '101': "Li is fire: bright, clinging, consuming. It illuminates what it touches but may also burn. It seeks form, adhering to what gives it shape. To move with Li is to bring clarity and insight. Its virtue is discernment, its danger is being overtaken by its own brilliance.",
    '001': "Chen is thunder: sudden, awakening, shocking. It breaks silence and stirs all things to motion. Where it goes, fear and excitement rise together. It is the eldest son, the one who acts. Those who follow Chen must be prepared for swift change and uncertain outcomes.",
    '100': "Ken is the mountain: still, watchful, resolute. It halts movement and invites reflection. Its path is one of discipline and limits. In Ken, stillness reveals the inner landscape. When one aligns with Ken, one becomes a guardian of boundaries, unmoved by haste.",
    '110': "Sun is wind or wood: penetrating, adaptable, persuasive. It does not force, but it enters where nothing else can. Through persistence, it shapes the hardest things. Sun teaches subtle influence and quiet endurance. Its movement is steady, and its strength lies in being overlooked.",
    '011': "Tui is the lake: joyful, open, enticing. It draws others in through softness and harmony. Though it appears gentle, it has the power to erode stone over time. Tui encourages expression, connection, and delight. Yet behind its smile lies the danger of indulgence."
}


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

