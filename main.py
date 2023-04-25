from random import randint


def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        if x >= k:
            k = x
            counts.append(k)
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


def testsort(hehe):
    for i in range(0, hehe):
        x = randint(2, 50)
        array = []
        for i in range(0, x):
            array.append(randint(0, 100))
        x = 100
        testarr = bucketsort(array, x)
        if testarr == 0:
            print(f'Got an error in this array: {array}')
        else:
            print(testarr)


print("Сколько тестов?")
tests = int(input())
testsort(tests)
