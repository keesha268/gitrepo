# Split in Half

def split_in_two(s):
    length = len(s)
    part = length // 2
    add = 0          # add 0 if it is even

    if length % 2:
        add = 1      # add 1 if it is odd

    left = s[:part + add]
    right = s[part + add:]
    return right + left


test_even_string = "kkkeee"
test_odd_string = "kkkeeee"
result_even_string = split_in_two(test_even_string)
print(result_even_string)
result_odd_string = split_in_two(test_odd_string)
print(result_odd_string)




# Unique Characters in String

def unique_char(s):
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True


test_1 = "abcde"
test_2 = "aabcde"
result_test1 = unique_char(test_1)
print(result_test1)
result_test2 = unique_char(test_2)
print(result_test2)