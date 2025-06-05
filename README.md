# zero-iching

A template command line interface package.

### 🔢 `hexagrams_from_uuid`: Deriving I Ching Hexagrams from UUIDs

The `hexagrams_from_uuid` function deterministically converts a UUID string into one or more I Ching hexagrams. It operates by interpreting the UUID as a 128-bit binary stream and slicing this stream into fixed 6-bit segments, each corresponding to a hexagram composed of six yin/yang lines.

Each bit in the segment is read as a single line of the hexagram from **bottom to top**, following I Ching tradition. A `1` maps to a solid yang line (`---`), and a `0` maps to a broken yin line (`- -`). The function supports extracting multiple hexagrams by specifying the `n` parameter and allows an optional `offset` to shift the bitstream starting point.

Because UUIDs are 128-bit values, up to 21 hexagrams can be derived in a single call (`21 * 6 = 126 bits used`), with 2 bits remaining unused. This creates a structured, non-arbitrary way of interpreting UUIDs as symbols—ideal for symbolic systems, playful divination, or creative applications that blend data with ancient Chinese metaphysics.


## Installation

```bash
pip install -e .
```

## Usage

```bash
zero-iching --help
```
