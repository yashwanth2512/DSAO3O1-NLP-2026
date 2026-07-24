import re

text = input("Enter text: ")
pattern = input("Enter pattern: ")

result = re.search(pattern, text)

if result:
    print("Pattern Found")
    print("Position:", result.start())
else:
    print("Pattern Not Found")
