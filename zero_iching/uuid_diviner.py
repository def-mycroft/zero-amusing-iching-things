"""Hexagram derivation utilities from UUIDs."""

from zero_iching.helpers import uuid_to_bin
from zero_iching.bit_waterfall import (
    hexagrams_from_bits,
    YANG_LINE,
    YIN_LINE,
)


def hexagrams_from_uuid(uuid_str: str, n: int = 1) -> list[str]:
    """Return ``n`` hexagrams derived from ``uuid_str`` using the
    waterfall reduction algorithm."""
    bits = uuid_to_bin(uuid_str)
    return hexagrams_from_bits(bits, n=n)

