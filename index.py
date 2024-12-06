
def longest_subarray(array):
    max_length = 0

    for i in range (len(array)):
        count_zeros = 0
        count_ones = 0
        
        # for each start point, extend the subarray to the end
        for j in range(i, len(array)):

            if array[j] == 0:
                count_zeros += 1
            else:
                count_ones += 1

            # If the subarray has equal 0s and 1s, check its length
            if count_zeros == count_ones and array[i] != array[i+1]:
                length = j - i + 1

                # Update max_length if the current subarray is the longest found
                if length > max_length:
                    max_length = length

    return max_length

# Prepare to get binary numbers from the user
binary_numbers = []
try:
    list_size = int(input("Enter the number of binary values you want to add to the list: "))

    for i in range (list_size):
        num_binary = int(input("Enter a binary number: "))
        if num_binary == 0 or num_binary == 1:
            binary_numbers.append(num_binary)
        else:
            print("Enter binary numbers (0 or 1)")

    print(f"List of numbers you entered: {binary_numbers}")
    print(f"Length of the longest subarray with equal 0s and 1s: {longest_subarray(binary_numbers)}") 

except ValueError:
    # If they enter something that’s not a number, show this message
    print("Enter valid binary numbers (0 or 1) only")


