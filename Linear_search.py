from Array import Array

theNumbers = [10, 51, 22, 18, 44, 31, 13, 55, 23, 64, 29]

# print(31 in theNumbers)  # prints True
# print(8 in theNumbers)   # prints False

def linearSearch(arr,target):
    n = len(arr)
    for i in range(n):
        # If the target is in the ith element, return True
        if arr[i] == target:
            return True
    
    return False # If not found, return False.

def sortedLinearSearch(arr, item):
    n = len(arr)
    for i in range(n):
        # If the target is found in the ith element, return True
        if arr[i] == item:
            return True
        # If target is larger than the ith element, it's not in the sequence.
        elif arr[i] > item:
            return False

    return False # The item is not in the sequence.

if __name__ == "__main__":
    array = Array(11)
    array = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
    print(sortedLinearSearch(array, 31))
    print(sortedLinearSearch(array, 8))
