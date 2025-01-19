# test_sub_pal_per_space.py

from maximun_sub_palindrome import sub_pal_per_space  

# 1. Basic Cases
def test_multiple_palindromes():
    result = sub_pal_per_space("Madam Arora teaches malam")
    expected = [(0, 4), (6, 10), (20, 24)]
    assert result == expected, f"Expected {expected}, got {result}"

def test_no_palindromes():
    result = sub_pal_per_space("Hello world")
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"

def test_single_palindrome():
    result = sub_pal_per_space("Anna goes to school")
    expected = [(0, 3)]
    assert result == expected, f"Expected {expected}, got {result}"

# 2. Edge Cases
def test_empty_string():
    result = sub_pal_per_space("")
    expected = []
    assert result == expected, "Expected an empty list for an empty string"

def test_fewer_than_three_characters():
    result = sub_pal_per_space("Hi")
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"

def test_entirely_palindromic_string():
    result = sub_pal_per_space("madam")
    expected = [(0, 4, 5)]
    assert result == expected, f"Expected {expected}, got {result}"

# 3. Format Considerations
def test_with_spaces_and_varying_cases():
    result = sub_pal_per_space("A man a plan a canal Panama")
    expected = []
    assert result == expected, "This function only detects palindromic words, not substrings"

def test_with_non_alphabetic_characters():
    result = sub_pal_per_space("Madam @@ Arora !! Malam")
    expected = [(0, 4), (9, 13), (18, 22)]
    assert result == expected, f"Expected {expected}, got {result}"

# 4. Avoiding Duplicates
def test_avoiding_duplicates():
    result = sub_pal_per_space("Anna Anna Civic Civic")
    expected = [(0, 3), (10, 14)]
    assert result == expected, "Duplicates should not appear in the results"

def test_no_duplicates():
    result = sub_pal_per_space("Anna Anna Civic Civic")
    assert not len(result) != len(set(result)), "Duplicates found in the result"

# 5. Correct Indices
def test_correct_indices():
    s = "Madam Arora Malam"
    result = sub_pal_per_space(s)
    expected = [(0, 4), (6, 10), (12, 16)]
    assert result == expected, f"Expected {expected}, got {result}"
    for start, end in result:
        assert s[start:end + 1].lower() == s[start:end + 1][::-1].lower(), \
            f"Substring {s[start:end + 1]} is not a palindrome"

def test_no_palindromes():
    result = sub_pal_per_space("Hello world")
    assert not result, f"Expected no palindromes, but got {result}"


