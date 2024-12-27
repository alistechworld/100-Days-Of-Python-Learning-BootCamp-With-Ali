### Control Flow (if/else, loops) ✨

Control flow determines the execution sequence of statements in a program based on conditions and iterations. Two fundamental concepts in control flow are decision-making (if/else) and loops.

### 1. If/Else Statements 🛤️

# Definition:

If/Else statements allow a program to make decisions based on conditions. The program checks a condition and executes specific code blocks based on whether the condition is true ✅ or false ❌.

# Syntax:

if condition:
    code block to execute if condition is true

elif another_condition:
    code block to execute if another_condition is true
else:
     code block to execute if all conditions are false


### 2. Loops 🔄

Loops are used to execute a block of code multiple times. The main types are for loop and while loop.

### For Loop 🔁
# Definition:

A for loop iterates over a sequence (e.g., list, range, or string) and executes the block of code for each item in the sequence.

Syntax:

for variable in sequence:
    # code to execute

Example

for number in range(1, 6):
    print(f"Number: {number}")

### While Loop 🔄

# Defination:
A while loop keeps executing as long as a given condition is true ✅.

Syntax:

while condition:
    # code to execute


### Key Points for Interview Preparation 📌
# Understand Conditions 🔍:

Conditions in if/else and while loops are evaluated as boolean expressions (True or False).
Be familiar with comparison operators: ==, !=, <, >, <=, >=.
Logical operators: and, or, not.

# Edge Cases ⚠️:

Test your conditions with edge cases, such as minimum and maximum values.
Example: What happens if the list is empty in a for loop?

# Avoid Infinite Loops 🚨:

Ensure your while loop has a terminating condition.
Example:
python
Copy code
while True:  # Infinite loop unless there's a break
    break
Understand Break and Continue 🛑:

break: Exits the loop immediately.
continue: Skips the current iteration and moves to the next.
Example:
python
Copy code
for i in range(1, 6):
    if i == 3:
        continue  # Skip number 3
    print(i)

# Nested Loops 🔗:

Loops can be nested inside each other.
Example:
python
Copy code
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

# Optimization 🚀:

Avoid unnecessary computations within a loop.
Example:
Instead of:
python
Copy code
for i in range(1, 1000):
    if i % 2 == 0:
        print(i)
Use:
python
Copy code
for i in range(2, 1000, 2):
    print(i)
