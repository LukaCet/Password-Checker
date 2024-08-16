# Password Checker 🖥️
Checks the strength of a Password/Phrase

## Alternative Method to code:

Char Method:
```python
for char in user_input:
    if char.isupper():
        uppercase_letters += 1
    elif char.islower():
        lowercase_letters += 1
    elif char.isdigit():
        numbers += 1
    else:
        special_characters += 1
```

Longer Method:
```python
for i in range(len(user_input)):
    if user_input[i].isupper():
        uppercase_count += 1
    elif user_input[i].islower():
        lowercase_count += 1
    elif user_input[i].isdigit():
        digit_count += 1
    else:
        symbol_count += 1
```
