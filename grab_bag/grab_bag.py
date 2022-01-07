import numbers


def find_max(*nums: numbers.Complex):
    max = 0
    for num in nums:
        max = num if num > max else max

    print(f'Max was {max}')


def sum_nums(*nums: numbers.Complex):
    sum = 0
    for num in nums:
        sum += num

    print(f'Sum is {sum}')


def count_upper_and_lower(input: str):
    ups, lows = 0, 0
    for char in input:
        if char.islower():
            lows += 1
        else:
            ups += 1

    print(f'"{input}" has {lows} lower-case and {ups} upper-case characters')


def is_pangram(input: str):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    lower = input.lower()
    for char in letters:
        if(char not in lower):
            print(f'"{input}" is NOT a pangram')
            return

    print(f'"{input}" IS a pangram')


find_max(3, 4, 1)
sum_nums(1, 2, 3)
count_upper_and_lower("HeLoo")
is_pangram('hello')
is_pangram('abcdefghijklmnopqrstuvwxyz')
is_pangram('The quick brOwn fox jumps over the lazy dog')
