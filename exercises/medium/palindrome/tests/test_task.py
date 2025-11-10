import sys
from pathlib import Path

# Add parent directory (where task.py is) to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from task import is_palindrome


def test_palindrome_simple():
    """Test simple palindrome"""
    assert is_palindrome("racecar") == True


def test_not_palindrome():
    """Test non-palindrome"""
    assert is_palindrome("foobar") == False


def test_empty_string():
    """Test empty string"""
    assert is_palindrome("") == True


def test_single_character():
    """Test single character"""
    assert is_palindrome("a") == True


def test_case_sensitive():
    """Test case sensitivity"""
    assert is_palindrome("Racecar") == False
    assert is_palindrome("racecar") == True

