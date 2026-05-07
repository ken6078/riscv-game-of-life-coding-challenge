# RISC-V Game of Life Coding Challenge

[![Test CI](https://github.com/ken6078/riscv-game-of-life-coding-challenge/actions/workflows/test-ci.yml/badge.svg)](https://github.com/ken6078/riscv-game-of-life-coding-challenge/actions/workflows/test-ci.yml)

> This project is a submission for **Coding Challenge - Broadening the RISC-V High Precision Code Base and Reach**.

A terminal-based implementation of **Conway's Game of Life** in Python, with wraparound edges, classic pattern presets, and test coverage via `pytest`.

## Features

- Conway's Game of Life core rules
- Toroidal (wraparound) neighbor calculation
- Terminal animation mode and static final-frame mode
- Built-in classic patterns (`glider`, `pulsar`, `lwss`, etc.)
- Reproducible random initialization with `--seed`
- Unit tests for logic, CLI behavior, and pattern generation

## Project Structure

```text
.
|-- game_of_life.py        # Main CLI and simulation loop
|-- patterns.py            # Classic sample pattern definitions
|-- tests/
|   |-- test_logic.py      # Core rules and evolution tests
|   |-- test_patterns.py   # Pattern API tests
|   `-- test_cli.py        # CLI validation tests
`-- requirements-dev.txt   # Dev dependencies
```

## Iteration

This project demonstrates iteration in three places:

1. `main()` runs the simulation generation by generation.
2. `step()` iterates over every cell in the grid.
3. `count_neighbors()` iterates over the 8 neighboring cells around each cell.

This problem is naturally iterative rather than recursive, because Conway's Game of Life evolves through repeated generations.

## demo
<img width="928" height="500" alt="record" src="https://github.com/user-attachments/assets/edde8295-a34b-4862-afc3-e2189d7076c8" />


## Requirements

- Python 3.10+ (recommended)
- pip

## Quick Start

```bash
# 1) Clone
git clone https://github.com/ken6078/riscv-game-of-life-coding-challenge.git
cd riscv-game-of-life-coding-challenge

# 2) Create and activate virtual environment (recommended)
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Bash (Linux/macOS/Git Bash)
source .venv/bin/activate

# 3) Install dev dependencies (including pytest)
pip install -r requirements-dev.txt
```

Using `venv` is recommended so `pytest` and other dev dependencies stay isolated from your global Python environment.

## Usage

### Animated simulation

```bash
python game_of_life.py
```

### Run without animation (print only final frame)

```bash
python game_of_life.py --no-show --gens 50
```

### Use a fixed random seed

```bash
python game_of_life.py --seed 42 --no-show --gens 20
```

### Start from a classic pattern

```bash
python game_of_life.py --pattern glider --no-show --gens 30
```

### Customize board size and timing

```bash
python game_of_life.py --rows 20 --cols 40 --prob 0.2 --delay 0.05
```

## CLI Options

| Option | Type | Default | Description |
|---|---|---:|---|
| `--rows` | int | `16` | Number of rows |
| `--cols` | int | `32` | Number of columns |
| `--gens` | int | `128` | Number of generations to simulate |
| `--prob` | float | `0.25` | Initial alive probability (`0` to `1`) |
| `--seed` | int | `None` | Random seed for reproducibility |
| `--delay` | float | `0.1` | Delay (seconds) between frames |
| `--no-show` | flag | `False` | Disable animation; print final state only |
| `--pattern` | str | `None` | One built-in sample pattern on a 16x32 board |

## Available Patterns

Still lifes:
- `block`, `beehive`, `loaf`, `boat`, `tub`

Oscillators:
- `blinker`, `toad`, `pentadecathlon`, `pulsar`

Spaceships:
- `glider`, `lwss`

## Testing

```bash
pytest -q
```

## Notes

- `--pattern` uses a fixed **16x32** board from `patterns.py`.
- Neighbor counting wraps around edges (toroidal topology).

## License

This project is licensed under the MIT License. See LICENSE.
