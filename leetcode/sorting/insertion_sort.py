"""In insertion sort we switch the smallest to the first"""


def insertion_sort(numbers: list) -> None:
    # swapping
    for index in range(1, len(numbers)):
        for i in range(index, 0, -1):
            if numbers[i-1] > numbers[i]:
                numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            else:
                break


def insertion_sort_shifting(numbers: list) -> None:
    for index in range(1, len(numbers)):
        current_number = numbers[index]
        for i in range(index-1, -1, -1):
            if numbers[i] > current_number:
                numbers[i+1] = numbers[i]
                if i == 0:
                    numbers[0] = current_number
            else:
                numbers[i+1] = current_number
                break


numbers = [8, 8, 0, 11, 10, 1, -9, 5, 3, 4, 2, 6]
insertion_sort_shifting(numbers)
print(numbers)
