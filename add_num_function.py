def get_nums():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1, num2

def sum_nums(n1, n2):
    return n1+n2

def print_sum(sum):
    print(f"The sum of two numbers is: {sum}")

def main():
    int1, int2 = get_nums()
    result = sum_nums(int1, int2)
    print_sum(result)

if __name__ == "__main__":
    main()
    print(f"The sum of 2 and 2 is {sum_nums(2,2)}")

