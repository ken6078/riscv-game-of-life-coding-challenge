import random
import pytest

from game_of_life import count_neighbors, init_grid, step


def test_count_neighbors_wraparound():
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
    ]
    assert count_neighbors(grid, 0, 0) == 1
    assert count_neighbors(grid, 2, 2) == 1


def test_step_block_still_life_unchanged():
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    assert step(grid) == grid


def test_step_blinker_period_two():
    start = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    after_one = step(start)
    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert after_one == expected
    assert step(after_one) == start


def test_init_grid_reproducible_with_seed():
    random.seed(1234)
    a = init_grid(4, 5, 0.3)
    random.seed(1234)
    b = init_grid(4, 5, 0.3)
    assert a == b
