# zero-iching

A template command line interface package.

### 🔢 `hexagrams_from_uuid`: Deriving I Ching Hexagrams from UUIDs

The `hexagrams_from_uuid` function deterministically converts a UUID string into one or more I Ching hexagrams. It interprets the UUID as a 128-bit binary stream and slices this stream into 6-bit chunks.

Each chunk is returned as two three-bit codes representing the lower and upper trigrams. Bits are ordered from **bottom to top** so that `"111"` corresponds to three solid yang lines. The trigram codes can be mapped to their traditional names via `HEXAGRAM_NAMES`.

Because UUIDs are 128-bit values, up to 21 hexagrams can be derived in a single call (`21 * 6 = 126 bits used`), with 2 bits remaining unused. This creates a structured, non-arbitrary way of interpreting UUIDs as symbols—ideal for symbolic systems, playful divination, or creative applications that blend data with ancient Chinese metaphysics.


## Installation

```bash
pip install -e .
```

## Usage

```bash
zero-iching --help
```

### Example

Derive three hexagrams from a UUID via the CLI:

```bash
zero-iching uuid --uuid 'd682da34-d320-4e72-824b-a42b0c801270' -n 3
```

The output is now formatted using a Jinja2 template and includes trigram names
and symbols.

If `--uuid` is provided with an empty string, a random UUID4 will be used.
