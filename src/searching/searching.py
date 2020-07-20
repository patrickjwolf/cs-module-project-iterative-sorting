

# seraching_for = 7

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return True

# linear_search([1,2,3,4,5,6,7,8,9], 3)


#     return -1   # not found


# # Write an iterative implementation of Binary Search
# def binary_search(arr, target):


#     return -1  # not found


def find_value_binary(arr, value):
    first = 0
    las = (len(arr) - 1)

    found = False

    while first <= last and not found:
        # find middle using integer division
        middle = (first + last) // 2
        if arr[middle] == value:
            found = True
        else:
            if value < arr[middle]:
                # search lower half of remainder
                last = middle - 1
        else:
            # search upper half of remainder
            first = middle + 1

    return found

    find_value_binary = ([1,2,3,4,5,6,7,8,9], 8)
            
        except expression as identifier:
            pass
        else:
            pass
        finally:
            pass