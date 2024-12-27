# Example of if/else program

age = 20
if age >= 18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote.")    
    
    
 # Example of for loop
 
for number in range(1, 6):
     print(f"Number: {number}")   
     
# Example of while loop

count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1
    
# Understand Break and Continue

for i in range(1, 6):
    if i == 3:
        continue
    print(i) 
    
# Nested Loop

for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")      
        
                