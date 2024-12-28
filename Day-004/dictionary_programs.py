# Student Marks Tracker

students = {
    "Ali": 85,
    "Ahmed": 90,
    "Sara": 78,
}

# Get marks for a student

name = input("Enter student name:")

marks = students.get(name, "Student not found")

print(f"{name}: {marks}")



# Word Count

# Input Sentence
sentence = "hello world hello python world"

# Split sentence into words

words = sentence.split()

# Count occurrences

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
    
print("Word Count:", word_count)