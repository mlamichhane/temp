# Sorts a sequence in ascending order using the selection sort algorithm.
def selectionSort(numList):
    n = len(numList)
    for i in range(n-1):
        # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if numList[j] < numList[smallNdx] :
                smallNdx = j
        # Swap the ith value and smallNdx value
        tmp = numList[i]
        numList[i] = numList[smallNdx]
        numList[smallNdx] = tmp

# Example usage
if __name__ == "__main__":
    theNumbers = [15, 12, 65, 10, 7]
    selectionSort(theNumbers)
    print("Sorted numbers are:", theNumbers)

