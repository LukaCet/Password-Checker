#💻 Password Checker 🖥️
Checks the strength of a Password/Phrase

## Code in question:
```python
user_input = input("Enter a word/phrase: ")

uppercase_letters = 0
lowercase_letters = 0
numbers = 0
special_characters = 0

for char in user_input:
    if char.isupper():
        uppercase_letters += 1
    elif char.islower():
        lowercase_letters += 1
    elif char.isdigit():
        numbers += 1
    else:
        special_characters += 1


sum = uppercase_letters + lowercase_letters + numbers + special_characters

print(f"""
There are: 
- {uppercase_letters} Upper case letters
- {lowercase_letters} lower case letters
- {numbers} numbers
- {special_characters} special characters
In total there are: {sum} characters.
""")
```
