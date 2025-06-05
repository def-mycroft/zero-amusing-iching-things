# zero-iching Help

## Description
Template command line interface for zero-iching.

## Usage
`zero-iching [OPTIONS] COMMAND [ARGS]...`

## Options
- `-h`, `--help` Show this help message and exit.
- `--version` Display the version.

## Commands
- `uuid` Derive hexagrams from a UUID.

### `uuid` command
`zero-iching uuid --uuid <UUID> -n <NUM>`

- `--uuid` UUID to divine from. If an empty string is provided, a random
  UUID4 is generated.
- `-n` Number of hexagrams to produce (default: `1`).
