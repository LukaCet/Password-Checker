input_string = input("Enter a phrase/word: ")
uppercase_count = 0
lowercase_count = 0
digit_count = 0
symbol_count = 0

for i in range(len(input_string)):
    if input_string[i].isupper():
        uppercase_count += 1
    elif input_string[i].islower():
        lowercase_count += 1
    elif input_string[i].isdigit():
        digit_count += 1
    else:
        symbol_count += 1

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Numbers: {digit_count}")
print(f"Symbols: {symbol_count}")
