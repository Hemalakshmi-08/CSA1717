# Program to sort sentences in alphabetical order

# Input: number of sentences
n = int(input("Enter number of sentences: "))

sentences = []

print("\nEnter the sentences:")
for i in range(n):
    s = input(f"Sentence {i+1}: ")
    sentences.append(s)

# Sorting sentences
sentences.sort()

# Displaying sorted sentences
print("\nSentences in alphabetical order:")
for s in sentences:
    print(s)
