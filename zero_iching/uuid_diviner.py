"""Hexagram derivation utilities from UUIDs."""

from zero_iching.helpers import uuid_to_bin

YANG_LINE = "1"
YIN_LINE = "0"


def hexagrams_from_uuid(uuid_str: str, n: int = 1, offset: int = 0):
    """Return ``n`` hexagrams derived from ``uuid_str`` starting at ``offset``.

    The UUID string is first converted to a 128-bit binary string using
    :func:`uuid_to_bin`. Six-bit chunks of this bitstream are then mapped to
    lines from bottom to top where ``1`` is a solid line (yang) and ``0`` is a
    broken line (yin).
    """
    bit_stream = uuid_to_bin(uuid_str)

    if offset < 0 or n < 1:
        raise ValueError("offset must be >= 0 and n must be >= 1")

    start = offset
    end = start + n * 6
    if end > len(bit_stream):
        raise ValueError("Requested range exceeds available bit length")

    hexagrams = []
    for i in range(n):
        bits = bit_stream[start + i * 6 : start + (i + 1) * 6]
        lines = [YANG_LINE if b == "1" else YIN_LINE for b in bits]
        hexagrams.append(''.join(lines))
    return hexagrams
