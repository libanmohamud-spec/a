import pytest
from task import sort_array


def test_empty_array():
    """Test empty array"""
    assert sort_array([]) == []


def test_single_element():
    """Test single element"""
    assert sort_array([5]) == [5]


def test_sorted_array():
    """Test already sorted array"""
    assert sort_array([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    """Test reverse sorted array"""
    assert sort_array([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_unsorted_with_duplicates():
    """Test unsorted array with duplicates"""
    result = sort_array([3, 6, 8, 10, 1, 2, 1])
    assert result == [1, 1, 2, 3, 6, 8, 10]


def test_negative_numbers():
    """Test with negative numbers"""
    result = sort_array([-3, -1, -5, 2, 0, -2])
    assert result == [-5, -3, -2, -1, 0, 2]

