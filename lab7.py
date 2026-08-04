# Text Analyzer Tool

# Input paragraph
text = input("Enter a paragraph: ")

# Initialize counters
words = 0
vowels = 0
spaces = 0
characters = len(text)

# Count vowels and spaces using string traversal
for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    if ch == " ":
        spaces += 1

# Count words
if len(text.strip()) == 0:
    words = 0
else:
    words = 1
    for ch in text:
        if ch == " ":
            words += 1

# String indexing
print("\nFirst Character:", text[0] if len(text) > 0 else "No Text")

# String slicing
print("First 10 Characters:", text[:10])

# Display results
print("\n----- Text Analysis -----")
print("Total Characters:", characters)
print("Total Words:", words)
print("Total Vowels:", vowels)
print("Total Spaces:", spaces)