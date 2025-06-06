# zero-iching

A template command line interface package.

### 🔢 `hexagrams_from_bits`: Waterfall Reduction

`hexagrams_from_bits` accepts any binary string and collapses it into hexagrams using a **waterfall** folding process. Starting from the full width of the input, each subsequent row is produced by XOR-ing adjacent bits. The rows shrink by one bit per step, forming a cascade until only `6 × n` bits remain. Those final bits encode the requested hexagrams. The CLI helper `hexagrams_from_uuid` simply converts a UUID to binary and delegates to this function.


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

### Visualization Demo

The `visualize_uuid` helper displays the bit chunks used to build each
hexagram alongside an ASCII rendering:

```python
from zero_iching.uuid_demo import visualize_uuid

visualize_uuid("d682da34-d320-4e72-824b-a42b0c801270", n=2)
```

The repository also includes a small `demo.py` that visualizes the waterfall
reduction for any integer:

```bash
python demo.py 123456 2
```
