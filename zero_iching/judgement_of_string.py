

def str_to_binary_int(s: str) -> int:
    return int.from_bytes(s.encode('utf-8'), byteorder='big')


def judge(given_str):
    """Return a hexagram that is associated with a string"""
    b = str_to_binary_int(given_str)

