# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort(numList):
    n = len(numList)
    # Perform n-1 bubble operations on the sequence
    for i in range(n-1):
        # Bubble the largest item to the end.
        for j in range(0, n-i-1):
            if numList[j] > numList[j+1]: # swap the j and j+1 items.
                tmp = numList[j]
                numList[j] = numList[j+1]
                numList[j+1] = tmp

# Example usage
if __name__ == "__main__":
    theNumbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    bubbleSort(theNumbers)
    print("Sorted numbers are:", theNumbers)


    