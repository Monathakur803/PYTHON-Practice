# # def count_chars(s):
# #     char_count = {}
# #     for char in s:
# #         if char in char_count:
# #             char_count[char] += 1
# #         else:
# #             char_count[char] = 1
# #     return char_count

# # # Test the function
# # s = "Radhe Radhe, hope everything well!"
# # print(count_chars(s))


# def count_chars(s):
#     # Step 1: Count the number of each character in the string
#     char_count = {}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

#     # Step 2: Store the counts in a dictionary
#     # In this case, the counts are already stored in the dictionary char_count

#     return char_count

# # Test the function
# s = "Hello, World!"
# print(count_chars(s))




# # Define a string with some words
# s = "Hello, World!"

# # Split the string into a list of words
# words = s.split(" ")

# # Print the list of words
# print("List of words:", words)

# # Join the words back into a string with a space character as the separator
# s_joined = " ".join(words)

# # Print the joined string
# print("Joined string:", s_joined)



# Take input from the user
list_to_sort = list(map(int, input("Enter numbers separated by a space: ").split()))

# Traverse through all list elements
for i in range(len(list_to_sort)):
    # Find the minimum element in remaining unsorted array
    min_index = i
    for j in range(i+1, len(list_to_sort)):
        if list_to_sort[min_index] > list_to_sort[j]:
            min_index = j
            
    # Swap the found minimum element with the first element of unsorted array
    list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]

print("Sorted list is:", list_to_sort)
