# def list_sum(num_list):
#     the_sum = 0
#     for i in num_list:
#         the_sum = the_sum + i
#     return the_sum

# print(list_sum([1,3,5,7,9]))


# def list_sum(num_list):
#     if len(num_list) == 1:
#         return num_list[0]
    
#     return num_list[0] + list_sum(num_list[1:])

# print(list_sum([1,3,5,7,9]))

# def fact(n):
#     assert n >= 0, "Factorial not defined for negative values."
#     if n < 2:
#         return 1

#     return n * fact(n - 1)

# print(fact(5))

# Compute the nth number in the Fibonacci sequence.
# def fib(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
    
# for i in range(20):
#     print(fib(i), end = ' ')

# Print the moves required to solve the Towers of Hanoi puzzle.
def tower(n, src, dest, temp ):
    if n == 1:
       print("Move disk 1 from pole %s to pole %s" % (src, dest))
       return
    
    tower(n-1, src, temp, dest)
    print("Move disk %d from pole %s to pole %s" % (n, src, dest))
    #print("Move %s -> %s" % (src, dest))
    tower(n-1, temp, dest, src)

tower(4, 'A', 'C', 'B')