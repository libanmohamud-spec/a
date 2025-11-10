import importlib.util
from pathlib import Path

# Load task module from parent directory explicitly
task_path = Path(__file__).parent.parent / "task.py"
spec = importlib.util.spec_from_file_location("task", task_path)
task = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task)
is_valid_parentheses = task.is_valid_parentheses

import pytest


def test_empty_string():
    """Test empty string"""
    assert is_valid_parentheses("") == True


def test_simple_valid():
    """Test simple valid parentheses"""
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("[]") == True
    assert is_valid_parentheses("{}") == True


def test_nested_valid():
    """Test nested valid parentheses"""
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("([{}])") == True
    assert is_valid_parentheses("({[]})") == True


def test_invalid_mismatch():
    """Test mismatched brackets"""
    assert is_valid_parentheses("(]") == False
    assert is_valid_parentheses("([)]") == False


def test_invalid_unclosed():
    """Test unclosed brackets"""
    assert is_valid_parentheses("(") == False
    assert is_valid_parentheses("([") == False


def test_invalid_extra_close():
    """Test extra closing brackets"""
    assert is_valid_parentheses(")") == False
    assert is_valid_parentheses("())") == False

