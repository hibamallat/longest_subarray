binary_list = [] #[1,1,1,0]

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
                subarray_length = j - i + 1
                max_length = max(max_length, subarray_length)

    return max_length

for i in range (10):
    num_binary = int(input("Enter a binary number: "))
    if num_binary == 0 or num_binary == 1:
        binary_list.append(num_binary)
    elif num_binary == -1:
        break
    else:
        print("The number should be binary")
        
print("The original list:", binary_list)
print("Length = ", longest_subarray(binary_list)) #length = 2  

