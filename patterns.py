#!/usr/bin/env python3
"""Sample 16x32 Game of Life board with classic patterns."""

from __future__ import annotations


ROWS = 16
COLS = 32


def _put(grid: list[list[int]], top: int, left: int, cells: list[tuple[int, int]]) -> None:
    for dr, dc in cells:
        r = top + dr
        c = left + dc
        if 0 <= r < ROWS and 0 <= c < COLS:
            grid[r][c] = 1


PATTERNS: dict[str, list[tuple[int, int]]] = {
    # Still lifes
    "block": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "beehive": [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2)],
    "loaf": [(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 3), (3, 2)],
    "boat": [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)],
    "tub": [(0, 1), (1, 0), (1, 2), (2, 1)],
    # Oscillators
    "blinker": [(0, 0), (0, 1), (0, 2)],
    "toad": [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2)],
    "pentadecathlon": [
        (0, 3), (0, 7),
        (1, 0), (1, 1), (1, 2), (1, 4), (1, 5),
        (1, 6), (1, 8), (1, 9),
        (2, 3), (2, 7)
    ],
    "pulsar": [
        (0, 2), (0, 3), (0, 4), (0, 8), (0, 9), (0, 10),
        (2, 0), (2, 5), (2, 7), (2, 12),
        (3, 0), (3, 5), (3, 7), (3, 12),
        (4, 0), (4, 5), (4, 7), (4, 12),
        (5, 2), (5, 3), (5, 4), (5, 8), (5, 9), (5, 10),
        (7, 2), (7, 3), (7, 4), (7, 8), (7, 9), (7, 10),
        (8, 0), (8, 5), (8, 7), (8, 12),
        (9, 0), (9, 5), (9, 7), (9, 12),
        (10, 0), (10, 5), (10, 7), (10, 12),
        (12, 2), (12, 3), (12, 4), (12, 8), (12, 9), (12, 10),
    ],
    # Spaceships
    "glider": [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    "lwss": [(0, 1), (0, 4), (1, 0), (2, 0), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3)],
}


def list_samples() -> list[str]:
    return sorted(PATTERNS.keys())


def _pattern_size(cells: list[tuple[int, int]]) -> tuple[int, int]:
    max_r = max(r for r, _ in cells)
    max_c = max(c for _, c in cells)
    return max_r + 1, max_c + 1


def build_sample_grid(name: str) -> list[list[int]]:
    """Build a sample pattern with 16x32 board."""
    key = name.lower()
    if key not in PATTERNS:
        raise ValueError(f"unknown sample: {name}")

    grid = [[0] * COLS for _ in range(ROWS)]
    cells = PATTERNS[key]
    h, w = _pattern_size(cells)
    top = (ROWS - h) // 2
    left = (COLS - w) // 2
    _put(grid, top, left, cells)
    return grid


def print_grid(grid: list[list[int]], alive_char: str = "█", dead_char: str = ".") -> None:
    for row in grid:
        print("".join(alive_char if cell else dead_char for cell in row))


if __name__ == "__main__":
    print("Available samples:", ", ".join(list_samples()))
