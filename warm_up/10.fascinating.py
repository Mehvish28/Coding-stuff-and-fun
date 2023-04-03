'''Given a number N. Your task is to check whether it is fascinating or not.
Fascinating Number: When a number(should contain 3 digits or more) is multiplied by 2 and 3 ,and
when both these products are concatenated with the original number, then it results in all digits from 1
to 9 present exactly once.
'''

def is_fascinating(n):
    # Check if n is a 3-digit or more number
    if n < 100:
        return False

    # Concatenate the number with its products by 2 and 3
    str_num = str(n) + str(n*2) + str(n*3)

    # Check if all digits from 1 to 9 are present exactly once
    for i in range(1, 10):
        if str(i) not in str_num:
            return False

    return True

# Get user input for the number
n = int(input("Enter a number: "))

# Call the function to check if the number is fascinating or not
if is_fascinating(n):
    print("The number is fascinating!")
else:
    print("The number is not fascinating.")
