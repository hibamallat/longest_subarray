binary_numbers = []

def longest_subarray(array):
    max_length = 0

    for i in range (len(array)):
        count_zeros = 0
        count_ones = 0

        for j in range(i, len(array)):

            if array[j] == 0:
                count_zeros += 1
            else:
                count_ones += 1

            if count_zeros == count_ones:
                balanced_length = j - i + 1
                max_length = max(max_length, balanced_length)

    return max_length
try:
    for i in range (10):
        num_binary = int(input("Enter a binary number:(Enter -1 to stop) "))
        if num_binary == 0 or num_binary == 1:
            binary_numbers.append(num_binary)
        elif num_binary == -1:
            break
        else:
            print("The number should be binary")

    print("The original list:", binary_numbers)
    print("Length of longest balanced subarray: ", longest_subarray(binary_numbers)) 

except ValueError:
    print("It should be a number")


