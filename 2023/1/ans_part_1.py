with open("2023/1/input.txt") as f:
    input = f.readlines()

digits = {'0', '1', '2', '3', '4', '5', 
          '6', '7', '8', '9', '10',}
sum = 0
for line in input:
    # By inniting as zero's, in case there are no digits in the line, 
    # the sum will get increased by 0
    first_digit = 0
    last_digit = 0
    
    for char in line:
        if char in digits:
            # If we haven't found the first digit yet, this 
            # digit is the first
            if not first_digit:
                first_digit = char
            
            # We can always replace the current last digit with 
            # the current digit
            last_digit = char

    sum += int(first_digit + last_digit)

print(sum)
