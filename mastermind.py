N, code, guess = input().split()

test = list(code)
guess = list(guess)
correct = 0
almost = 0

for i in range(int(N)):
    if code[i] == guess[i]:
        correct += 1
        test[i] = '_'
        guess[i] = '.'

for i in range(int(N)):
    if guess[i] in test:
        almost += 1
        test[test.index(guess[i])] = '_'

print(str(correct) + ' ' + str(almost))
