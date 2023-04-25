import pytest
from random import randint


@pytest.fixture()
def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        if x >= k:
            return 0
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


arr = []
zz = int(input())
for i in range(0, zz):
    arr.append(randint(1, 100))

yy = int(input())


def test_buckerstort():
    assert bucketsort(arr, yy) == 0


