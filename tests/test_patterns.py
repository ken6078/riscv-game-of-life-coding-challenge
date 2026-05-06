import pytest

from patterns import COLS, ROWS, build_sample_grid, list_samples


def test_list_samples_sorted_and_contains_glider():
    names = list_samples()
    assert names == sorted(names)
    assert "glider" in names


def test_build_sample_grid_has_fixed_size_and_live_cells():
    grid = build_sample_grid("glider")
    assert len(grid) == ROWS
    assert all(len(row) == COLS for row in grid)
    alive = sum(sum(row) for row in grid)
    assert alive == 5


def test_build_sample_grid_invalid_name_raises():
    with pytest.raises(ValueError):
        build_sample_grid("not-a-real-pattern")
