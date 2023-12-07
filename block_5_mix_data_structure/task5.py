# 5. Implement a method to sort an array using two queues.

from collections import deque

def sort_array_with_queues(arr):
    if len(arr) <= 1:
        return arr

    # Initialize two queues
    queue1 = deque()
    queue2 = deque()

    # Enqueue elements into queue1
    for element in arr:
        queue1.append(element)

    # Sort the elements into two queues
    while queue1:
        current_min = float('inf')

        # Dequeue elements into queue2, finding the minimum value
        while queue1:
            current_element = queue1.popleft()
            current_min = min(current_min, current_element)
            queue2.append(current_element)

        # Enqueue elements back into queue1 and remove the minimum value
        while queue2:
            current_element = queue2.popleft()
            if current_element == current_min:
                arr.append(current_element)  # Enqueue to the original array
            else:
                queue1.append(current_element)

    return arr

# Example usage
if __name__ == "__main__":
    unsorted_array = [4, 2, 7, 1, 9, 3]
    sorted_array = sort_array_with_queues(unsorted_array)

    print("Original Array:", unsorted_array)
    print("Sorted Array:", sorted_array)
