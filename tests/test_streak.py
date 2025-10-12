import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_example_case_one():
    """Test the first example case from the requirements."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_example_case_two():
    """Test the second example case from the requirements."""
    assert longest_positive_streak([]) == 0

def test_example_case_three():
    """Test the third example case from the requirements."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_multiple_streaks_longest_last():
    """Test with multiple streaks where the longest streak is at the end."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3]) == 3

def test_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 4, 5]) == 2

def test_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, 2, -3, 4, 5]) == 2

def test_all_positive():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    """Test a list with all non-positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -4, -5]) == 0

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0

def test_streak_at_beginning():
    """Test a streak that occurs at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 0, -1, -2]) == 3

def test_no_positive_numbers():
    """Test a list that contains no positive numbers."""
    assert longest_positive_streak([0, -1, -2, -3]) == 0