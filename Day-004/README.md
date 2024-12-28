# 🌟 Day 4: Lists and Dictionaries in Python  

---

## 📋 **Lists in Python**  
A **list** is a collection of ordered, mutable, and indexed elements. It can hold multiple items, including numbers, strings, or other lists.  

### 🛠 **Key Features of Lists:**  
- **📌 Ordered**: Items are stored in a defined sequence.  
- **📌 Mutable**: Items can be changed after the list is created.  
- **📌 Indexed**: Access elements using their position (starting at `0`).  

### 🔍 **Example:**  
```python
# Creating a List
fruits = ["apple", "banana", "cherry"]

# Accessing Elements
print(fruits[0])  # Output: apple

# Adding Elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Removing Elements
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# Iterating Through a List
for fruit in fruits:
    print(fruit)



# 🌟 Day 4: Understanding Dictionaries in Python  

---

## 🗝 **What is a Dictionary?**  
A **dictionary** is a collection in Python used to store data in **key-value pairs**. Each key must be unique, and it maps to a corresponding value.

---

## 🛠 **Key Features of Dictionaries:**  
- **📌 Key-Value Pairs**: Data is stored as a combination of keys and their associated values.  
- **📌 Mutable**: You can add, remove, or modify items after creation.  
- **📌 Fast Access**: Retrieve values quickly using keys.  
- **📌 Unordered**: Items do not have a fixed position (since Python 3.7+, dictionaries maintain insertion order).  

---

## 🔍 **Creating a Dictionary:**  
```python
# Empty dictionary
my_dict = {}

# Dictionary with initial values
person = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore"
}
