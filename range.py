
# task 2

def input_int(msg, minimum, maximum):
    # Repeat until a correct value is entered
    while True:
        try:
            input_value = int(input(msg))
        except ValueError:
            print("Input value was not an integer")
        else:
            # check for the range if is correct
            if input_value > minimum or input_value < maximum:
                print(f"Input number in range {min} and {max}")
            else:
                # Retern the validated value
                return input_value
            
            
range_interval = []
for idx in range(0, 24):
    ranges = input_int("Input number in range: ", 0, 150)
    range_interval.append(ranges)