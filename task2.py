# Task 2

max= None
min = None
input_value = None

while True:
    inp = input("Input number in range 0-150:")
    if inp < ('0') : 
        break
    try:
        input_value=int(inp)
    except:
        print ("Invalid input")
        continue

    if max is None:
        max = input_value
        min = input_value

    if input_value>max: 
        max=input_value
    if input_value<min: 
        min=input_value
    

print ("Maximum is ", max)
print ("Minimum is ", min)