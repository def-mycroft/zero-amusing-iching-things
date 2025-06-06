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
- `game` Generate interactive Dao Field HTML.

### `uuid` command
`zero-iching uuid --uuid <UUID> -n <NUM>`

- `--uuid` UUID to divine from. If an empty string is provided, a random
  UUID4 is generated.
- `-n` Number of hexagrams to produce (default: `1`).

### `game` command
`zero-iching game --grid -n <SIZE> [--savegrid PATH] [-o OUTPUT]`

- `--grid` Generate the interactive grid HTML.
- `-n`, `--size` Dimension of the square grid.
- `--savegrid` Load a starting grid from the given JSON file.
- `-o`, `--output` Destination HTML file (default: `dao_field.html`).
