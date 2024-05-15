# Author: Jovane Cano
# GitHub username: jovanecano
# Date: 05/14/2024
# Description:
"""This function called reverse_list reverses the order of the elements within the specified list"""

def reverse_list(list):
    """the function reverse_list reverses the order of values within a given list
        This is done without slices. Instead, a temporary variable is created to temporarily store values
        in order to allow the swapping."""

    length = len(list)

    for value in range(length // 2): # iterates the first half of  the values within list

        temp_var = list[value] # temporary variable created to store the iterated value

        list[value] = list[length - value - 1]
        # replaces the value at index "value" with the value with the corresponding index at the end of the list
        # for instance, first with last, second with second last

        list[length - value - 1] = temp_var
        # sets the value at the end of the index corresponding to the end of the list to the stored value in temp_var, rebinding


#my_list = [1, 2, 3, 4, 5]
#reverse_list(my_list)
#print(my_list)