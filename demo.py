"""Demo script showcasing waterfall reduction for an integer."""

import sys

from zero_iching.bit_waterfall import visualize_waterfall


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python demo.py <integer> [n_hexes]")
        return
    num = int(sys.argv[1])
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    bits = bin(num)[2:]
    print(f"Number: {num}")
    print(f"Bits  : {bits}\n")
    visualize_waterfall(bits, n=n)


if __name__ == "__main__":
    main()
