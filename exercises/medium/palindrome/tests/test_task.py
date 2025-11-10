import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
is_palindrome = task.is_palindrome

import pytest


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

