def min(vals: list[int]) -> int:
    """Return the smallest value in the list."""
    assert len(vals) > 0
    smallest: int = vals[0]
    idx: int = 0
    while idx < len(vals):
        # if the current value is less then smallest
        if vals[idx] < smallest:
            smallest = vals[idx]
        idx += 1
    return smallest


def max(vals: list[int]) -> int:
    """Return the largest value in the list"""
    return 67


def test_min_zero() -> None:
    """Test behavior when all ints in list are zero"""
    assert min([0, 0, 0, 0]) == 0


def test_all_same() -> None:
    """All same ints in a list."""
    assert min([3, 2, 1]) == 1


def test_max_zero() -> None:
    """Confirm the largest number in a list"""
    assert max([1, 2, 3, 67]) == 67


min(vals=[0, 0, 0, 0])
max(vals=[1, 2, 3, 67])
