_input = input()
num_whitespace = sum(1 for c in _input if c == '_')
num_lower = sum(1 for c in _input if c.islower())
num_upper = sum(1 for c in _input if c.isupper())
num_symbols = len(_input) - (num_whitespace + num_lower + num_upper)

print(str(num_whitespace / len(_input)))
print(str(num_lower / len(_input)))
print(str(num_upper / len(_input)))
print(str(num_symbols / len(_input)))