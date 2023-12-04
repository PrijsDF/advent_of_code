with open("2023/1/input.txt") as f:
    input = f.readlines()

digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}

spelled_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# We use these partial spelled digits to keep track of valid
# digits when looping through the values
partial_spelled_digits = [
    [d[:-len] for len in range(1, len(d))] for d in spelled_digits
]
partial_spelled_digits = {d for sublist in partial_spelled_digits for d in sublist}

sum = 0
for line in input:
    # By inniting as zero's, in case there are no digits in the line,
    # the sum will get increased by 0
    first_digit = "0"
    last_digit = "0"

    # We keep track of possible spelled digits
    spelled = ""

    for char in line:
        if char in digits:
            # If we haven't found the first digit yet, this
            # digit is the first
            if first_digit == "0":
                first_digit = char

            # We can always replace the current last digit with
            # the current digit
            last_digit = char

            # Reset the spelled digit
            spelled = ""
        else:
            spelled += char

            # First check whether we have found a new spelled digit
            if spelled in spelled_digits:
                # In this case we haven't found a digit yet
                if first_digit == "0":
                    first_digit = spelled_digits[spelled]

                # We can always update the last digit
                last_digit = spelled_digits[spelled]

            # Then check whether our partially spelled digit is (still) valid
            # If not, then we have to reset the partially spelled digit; but we have
            # to do this recursively as to not throw away potentially other spelled
            # digits; e.g. 'sevei' would fail, but we want to keep 'ei' as it might
            # be followed by 'ght'
            elif spelled not in partial_spelled_digits:
                while spelled not in partial_spelled_digits and spelled != "":
                    if len(spelled) == 1:
                        spelled = ""
                    else:
                        spelled = spelled[-(len(spelled) - 1) :]

            # We still need to check whether the current digit itself is part of the
            # partially spelled digits; in this case we continue with 'spelled'
            # being equal to the current digit. E.g. cpxb94one3threeclrnsix
            # would otherwise fail because of 'ns' failing, after which 'ix' also fails
            if char in partial_spelled_digits and spelled == "":
                spelled = char

    sum += int(first_digit + last_digit)

print(sum)
