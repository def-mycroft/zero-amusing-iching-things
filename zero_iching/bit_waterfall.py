"""Utilities for deriving hexagrams from binary strings using a
waterfall reduction algorithm."""

from typing import Callable, List, Tuple

YANG_LINE = "1"
YIN_LINE = "0"


def _validate_bits(bits: str) -> None:
    if not bits or set(bits) - {"0", "1"}:
        raise ValueError("bits must be a non-empty binary string")


def waterfall_reduce(bits: str, final_len: int, op: Callable[[int, int], int] = lambda a, b: a ^ b) -> Tuple[str, List[List[int]]]:
    """Reduce ``bits`` to ``final_len`` using a triangular folding process.

    Parameters
    ----------
    bits : str
        Input binary string.
    final_len : int
        Desired output length in bits.
    op : Callable[[int, int], int], optional
        Binary operation used when folding. Defaults to XOR.

    Returns
    -------
    Tuple[str, List[List[int]]]
        Final bit string and history of rows used in the reduction.
    """
    _validate_bits(bits)
    row = [int(b) for b in bits]
    if final_len < 1 or final_len > len(row):
        raise ValueError("final_len must be between 1 and the length of bits")
    history = [row.copy()]
    while len(row) > final_len:
        row = [op(row[i], row[i + 1]) for i in range(len(row) - 1)]
        history.append(row.copy())
    return "".join(str(b) for b in row), history


def hexagrams_from_bits(bits: str, n: int = 1) -> List[str]:
    """Return ``n`` hexagrams derived from ``bits``.

    The bits are reduced using ``waterfall_reduce`` so that the
    final ``6 * n`` bits are used to form the hexagrams.  Each
    hexagram is returned as a six-character string ordered from
    bottom to top.
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    needed = 6 * n
    reduced, _ = waterfall_reduce(bits, needed)
    hexes = []
    for i in range(n):
        chunk = reduced[i * 6 : (i + 1) * 6]
        hexes.append(chunk)
    return hexes


def visualize_waterfall(bits: str, n: int = 1) -> None:
    """Print the triangular waterfall reduction and resulting hexagrams."""
    reduced, history = waterfall_reduce(bits, 6 * n)
    width = len(history[0])
    for depth, row in enumerate(history):
        indent = " " * depth
        line = "".join(str(b) for b in row)
        print(f"{indent}{line}")
    print()
    print(f"final bits: {reduced}")
    for i, hx in enumerate(hexagrams_from_bits(bits, n)):
        lower = hx[:3]
        upper = hx[3:]
        print(f"Hexagram {i+1}: {upper} over {lower} -> {hx}")

