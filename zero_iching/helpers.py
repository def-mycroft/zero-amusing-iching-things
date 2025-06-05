
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

