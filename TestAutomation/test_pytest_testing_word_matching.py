# Repository: https://github.com/abhisakh/QA_Engineering_Portfolio.git
# Question reference: https://masterschool.notion.site/Homework-PyTest-Testing-word-matching-1c19418319f380679886c43cc5da9a29

import pytest
from pytest_testing_word_matching import count_word_matches

#-------------------------------------------------------------------------------------------------
# Exercise 1: Basic Parameterized Tests
#-------------------------------------------------------------------------------------------------
# Use parameterization to test `count_word_matches` with multiple input combinations of `text` and `target`,
# along with their expected outputs. Write a parameterized test to validate the function across basic,
# mixed-case, and simple edge-case scenarios.
#-------------------------------------------------------------------------------------------------
# ### Test Cases:
# 1. `text="The cat sat on the mat", target="cat"` → Expect `1` (Only "cat" matches, not "cat" in "concatenate").
# 2. `text="Dog dog DOG dOg", target="dog"` → Expect `4` (Case-insensitive matches).
# 3. `text="Hello world", target="world"` → Expect `1`.
# 4. `text="hello hello HELLO", target="hello"` → Expect `3`.
# 5. `text="No matches here", target="yes"` → Expect `0` (No matches).
# 6. `text="catcat cat catdog", target="cat"` → Expect `1` (Only standalone "cat" counts, not "cat" in "catcat").
# 7. `text="a a a", target="a"` → Expect `3`.
#-------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text,target,expected",
    [
        ("The cat sat on the mat", "cat", 1),
        ("Dog dog DOG dOg", "dog", 4),
        ("Hello world", "world", 1),
        ("hello hello HELLO", "hello", 3),
        ("No matches here", "yes", 0),
        ("catcat cat catdog", "cat", 1),
        ("a a a", "a", 3),
    ],
)
def test_count_word_matches_basic(text, target, expected):
    assert count_word_matches(text, target) == expected

#-------------------------------------------------------------------------------------------------
# Exercise 2: Edge Cases Testing
#-------------------------------------------------------------------------------------------------
# Test the `count_word_matches` function using parameterized tests. Focus on empty inputs, spaces,
# and punctuation.
#-------------------------------------------------------------------------------------------------
### Test Cases:
# 1. **Empty Text**: `text="", target="word"` → Expect `0`.
# 2. **Empty Target**: `text="hello world", target=""` → Expect `0`.
# 3. **Both Empty**: `text="", target=""` → Expect `0`.
# 4. **Multiple Spaces**: `text="hello  world", target="world"` → Expect `1` (Extra spaces ignored).
# 5. **Leading/Trailing Spaces**: `text=" cat ", target="cat"` → Expect `1`.
# 6. **Punctuation Not Handled**: `text="cat,dog cat"`, `target="cat`" → Expect `1`
# 7. **Single Character**: `text="x y z", target="x"` → Expect `1`.
#-------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text,target,expected",
    [
        ("", "word", 0),
        ("hello world", "", 0),
        ("", "", 0),
        ("hello  world", "world", 1),
        (" cat ", "cat", 1),
        ("cat,dog cat", "cat", 1),
        ("x y z", "x", 1),
    ],
)
def test_count_word_matches_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected

#-------------------------------------------------------------------------------------------------
# Exercise 3: Negative Tests
#-------------------------------------------------------------------------------------------------
# Test the function for invalid inputs like None, integers, or lists to ensure it raises the
# appropriate exceptions.
#-------------------------------------------------------------------------------------------------
### Test Cases:
# 1. **None Text**: `text=None, target="word"` → Expect a `TypeError`.
# 2. **None Target**: `text="hello world", target=None` → Expect a `TypeError`.
# 3. **Integer Text**: `text=123, target="word"` → Expect a `TypeError`.
# 4. **Integer Target**: `text="hello world", target=456` → Expect a `TypeError`.
# 5. **List Text**: `text=["hello", "world"], target="world"` → Expect a `TypeError`.
# 6. **List Target**: `text="hello world", target=["world"]` → Expect a `TypeError`.
#-------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text,target",
    [
        (None, "word", TypeError),
        ("hello world", None, TypeError),
        (123, "word", TypeError),
        ("hello world", 456, TypeError),
        (["hello", "world"], "world", TypeError),
        ("hello world", ["world"], TypeError),
    ],
)
def test_count_word_matches_invalid_inputs(text, target):
    with pytest.raises((TypeError, ValueError)):
        count_word_matches(text, target)
