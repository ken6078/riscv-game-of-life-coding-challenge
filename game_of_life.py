import argparse
import random
import sys
import time

from patterns import build_sample_grid, list_samples


def init_grid(rows: int, cols: int, alive_prob: float) -> list[list[int]]:
    return [
        [1 if random.random() < alive_prob else 0 for _ in range(cols)]
        for _ in range(rows)
    ]


def count_neighbors(grid: list[list[int]], r: int, c: int) -> int:
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr = (r + dr) % rows
            nc = (c + dc) % cols
            total += grid[nr][nc]
    return total


def step(grid: list[list[int]]) -> list[list[int]]:
    rows = len(grid)
    cols = len(grid[0])
    nxt = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            n = count_neighbors(grid, r, c)
            if grid[r][c] == 1 and n in (2, 3):
                nxt[r][c] = 1
            elif grid[r][c] == 0 and n == 3:
                nxt[r][c] = 1
    return nxt


def render(grid: list[list[int]], generation: int) -> str:
    alive_char = "██"
    dead_char = "  "
    alive_count = sum(sum(row) for row in grid)
    cols = len(grid[0])
    lines = ["+" + "-" * cols * 2 + "+"]
    for row in grid:
        body = "".join(alive_char if cell else dead_char for cell in row)
        lines.append("|" + body + "|")

    info = f" Gen: {generation}  Alive: {alive_count} "
    if len(info) > cols * 2:
        info = info[:cols * 2]
    remain = cols * 2 - len(info)
    left = remain // 2
    right = remain - left
    lines.append("+" + "-" * left + info + "-" * right + "+")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument("--rows", type=int, default=16, help="Rows count")
    parser.add_argument("--cols", type=int, default=32, help="Cols count")
    parser.add_argument("--gens", type=int, default=128, help="Generations to simulate")
    parser.add_argument("--prob", type=float, default=0.25, help="Initial alive probability (0~1)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    parser.add_argument("--delay", type=float, default=0.1, help="Delay between frames")
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Don't show generation-by-generation animation in terminal",
    )
    parser.add_argument(
        "--pattern",
        choices=list_samples(),
        help="Use one classic sample pattern on 16x32 board",
    )
    args = parser.parse_args()

    if args.rows <= 0 or args.cols <= 0:
        print("rows/cols must be > 0", file=sys.stderr)
        return 1
    if not 0.0 <= args.prob <= 1.0:
        print("prob must be in [0, 1]", file=sys.stderr)
        return 1
    if args.delay < 0:
        print("delay must be >= 0", file=sys.stderr)
        return 1
    if args.gens <= 0:
        print("gens must be > 0", file=sys.stderr)
        return 1

    if args.seed is not None:
        random.seed(args.seed)

    if args.pattern:
        grid = build_sample_grid(args.pattern)
    else:
        grid = init_grid(args.rows, args.cols, args.prob)

    try:
        if not args.no_show:
            for gen in range(1, args.gens + 1):
                # ANSI clear screen + cursor home, works in bash and modern terminals.
                print("\x1b[2J\x1b[H", end="")
                print(render(grid, gen), flush=True)
                time.sleep(args.delay)
                grid = step(grid)
        else:
            for gen in range(1, args.gens + 1):
                grid = step(grid)
            final_gen = args.gens if args.gens > 0 else 0
            print(render(grid, final_gen))
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
