import pytest
import os
import sys


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from quick_sort import quick_sort

def test_mk():
    if True:
        assert True
def test_quick_sort():
    # Test case 1: Sorting an already sorted list
    arr1 = [1, 2, 3, 4, 5]
    quick_sort(arr1, 0, len(arr1) - 1)
    assert arr1 == [1, 2, 3, 4, 5]

    # Test case 2: Sorting a reverse sorted list
    arr2 = [5, 4, 3, 2, 1]
    quick_sort(arr2, 0, len(arr2) - 1)
    assert arr2 == [1, 2, 3, 4, 5]

    # Test case 3: Sorting a list with duplicate elements
    arr3 = [4, 2, 6, 2, 1, 4, 3]
    quick_sort(arr3, 0, len(arr3) - 1)
    assert arr3 == [1, 2, 2, 3, 4, 4, 6]

    # Test case 4: Sorting an empty list
    arr4 = []
    quick_sort(arr4, 0, len(arr4) - 1)
    assert arr4 == []

    # Test case 5: Sorting a list with one element
    arr5 = [1]
    quick_sort(arr5, 0, len(arr5) - 1)
    assert arr5 == [1]

if __name__ == "__main__":
    pytest.main()
