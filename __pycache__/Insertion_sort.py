# Sorts a sequence in ascending order using the insertion sort algorithm.
def insertionSort(numList):
    n = len(numList)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned.
        value = numList[i]
        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < numList[pos-1]:
            # Shift the items to the right during the search.
            numList[pos] = numList[pos-1]
            pos -= 1

        numList[pos] = value

# Example usage
if __name__ == "__main__":
    theNumbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    insertionSort(theNumbers)
    print("Sorted numbers are:", theNumbers)


