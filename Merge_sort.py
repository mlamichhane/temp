def merge_sort(numList):
    print("Splitting ", numList)
    if len(numList) > 1:
        mid = len(numList) // 2
        left_half = numList[:mid]
        right_half = numList[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numList[k] = left_half[i]
                i = i + 1
            else:
                numList[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            numList[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            numList[k] = right_half[j]
            j = j + 1
            k = k + 1

    print("Merging ", numList)

if __name__ == "__main__":
    theNumbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(theNumbers)
    print(theNumbers)
