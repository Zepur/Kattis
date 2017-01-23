# keys = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'xyz']
# words = []
# num_read_lines = int(input())
# num_valid = 0
#
#
# def coconut(s):
#     global num_valid
#     valid = True
#     for q in range(len(key_presses)):
#         if s[q] not in keys[key_presses[q]]:
#             valid = False
#             break
#     if valid:
#         num_valid += 1
#
#
# for i in range(num_read_lines):
#     words.append(input())
#
# key_presses = [int(n) for n in input()]
#
# for word in words:
#     if len(word) == len(key_presses):
#         coconut(word)
#
# print(str(num_valid))

keys = {
    'a': 2,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 3,
    'f': 3,
    'g': 4,
    'h': 4,
    'i': 4,
    'j': 5,
    'k': 5,
    'l': 5,
    'm': 6,
    'n': 6,
    'o': 6,
    'p': 7,
    'q': 7,
    'r': 7,
    's': 7,
    't': 8,
    'u': 8,
    'v': 8,
    'w': 9,
    'x': 9,
    'y': 9,
    'z': 9,
    ' ': 0
}
words = []
num_read_lines = int(input())
num_valid = 0


def coconut(s):
    global num_valid
    valid = True
    for q in range(len(key_presses)):
        if keys.get(word[q]) != key_presses[q]:
            valid = False
            break
    if valid:
        num_valid += 1


for i in range(num_read_lines):
    words.append(input())

key_presses = [int(n) for n in input()]

for word in words:
    if len(word) == len(key_presses):
        coconut(word)

print(str(num_valid))
