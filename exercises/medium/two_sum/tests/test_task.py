import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
two_sum = task.two_sum

import pytest


def test_two_sum_basic():
    """Test basic two sum functionality"""
    result = two_sum([2, 7, 11, 15], 9)
    assert result == [0, 1], f"Expected [0, 1], got {result}"


def test_two_sum_no_solution():
    """Test case with no solution"""
    result = two_sum([1, 2, 3], 10)
    assert result is None, f"Expected None, got {result}"


def test_two_sum_duplicates():
    """Test with duplicate numbers"""
    result = two_sum([3, 3], 6)
    assert result == [0, 1], f"Expected [0, 1], got {result}"


def test_two_sum_negative():
    """Test with negative numbers"""
    result = two_sum([-1, -2, -3, -4, -5], -8)
    assert result == [2, 4], f"Expected [2, 4], got {result}"

