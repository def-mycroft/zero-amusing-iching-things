

def uuid_to_bin(uuid_str):
    """Convert UUID string to 128-bit binary string."""
    hex_str = uuid_str.replace('-', '')
    return bin(int(hex_str, 16))[2:].zfill(128)

