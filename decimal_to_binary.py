from Stack import Stack

def dec_to_bin(dec_number):
    stack = Stack(50)

    while dec_number > 0:
        rem = dec_number % 2
        stack.push(rem)
        # the floor division // rounds the result down to the nearest whole number 
        dec_number = dec_number // 2  

    bin_string = ""
    
    while not stack.is_empty():
        bin_string = bin_string + str(stack.pop())

    return bin_string

if __name__ == "__main__":
    num = int(input("Enter a decimal number: "))
    print(f"Binary representation of {num} is: ", dec_to_bin(num))



