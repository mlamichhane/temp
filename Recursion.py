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

def fact(n):
    assert n >= 0, "Factorial not defined for negative values."
    if n < 2:
        return 1

    return n * fact(n - 1)

print(fact(5))