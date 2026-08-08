# Program to remove punctuations from a given string

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in punctuations:
        result += ch

print("String without punctuations:", result)
