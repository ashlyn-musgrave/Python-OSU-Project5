# Name: Ashlyn Musgrave
# Course: CS261 - Data Structures
# Assignment: Assignment 5 MinHeap Implementation
# Due Date: November 29, 2023
# Description: This code demonstrates the implementation of a Minimum Heap

from dynamic_array import *

class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

# ---------------------------------------------------------------------------

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap while maintaining the heap property.

        Runtime complexity: O(log N)
        """

        # Append the new node to the end of the dynamic array
        self._heap.append(node)

        # Perform heapify-up to restore the heap property
        self._heapify_up(self._heap.length() - 1)

    def _heapify_up(self, index: int) -> None:
        """
        Restores the heap property by moving the element at the given index up the heap.
        """
        while index > 0:
            parent_index = (index - 1) // 2

            # Check if the parent is greater than the current node, swap if necessary
            if self._heap[parent_index] > self._heap[index]:
                self._swap(parent_index, index)
                index = parent_index
            else:
                break

    def _swap(self, i: int, j: int) -> None:
        """
        Swaps the elements at indices i and j in the heap.
        """
        temp = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = temp

    def is_empty(self) -> bool:
        """
        Returns True if the heap is empty; otherwise, returns False.

        Runtime complexity: O(1)
        """
        return self._heap.is_empty()

    def get_min(self) -> object:
        """
        Returns an object with the minimum key without removing it from the heap.

        Runtime complexity: O(1)
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")

        # The minimum element is always at the root of the heap (index 0)
        return self._heap[0]

    def remove_min(self) -> object:
        """
        Returns an object with the minimum key and removes it from the heap.

        Runtime complexity: O(log N)
        """
        if self.is_empty():
            raise MinHeapException("Heap is empty")

        # Save the minimum element (at the root of the heap)
        min_element = self._heap[0]

        # Replace the root with the last element in the heap
        last_element = self._heap.pop()

        # If the heap is not empty after the removal, perform heapify-down
        if not self.is_empty():
            self._heap[0] = last_element
            self._heapify_down(0)

        return min_element

    def _heapify_down(self, index: int) -> None:
        """
        Restores the heap property by moving the element at the given index down the heap.
        """
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_child_index = index

            # Compare with left child
            if left_child_index < self._heap.length() and self._heap[left_child_index] < self._heap[smallest_child_index]:
                smallest_child_index = left_child_index

            # Compare with right child
            if right_child_index < self._heap.length() and self._heap[right_child_index] < self._heap[smallest_child_index]:
                smallest_child_index = right_child_index

            # If the smallest child is the current node, the heap property is restored
            if smallest_child_index == index:
                break

            # Swap the current node with the smallest child
            self._swap(index, smallest_child_index)

            # Move to the next level in the heap
            index = smallest_child_index

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a proper MinHeap from the given DynamicArray

        Runtime Complexity: O(N)
        """
        # Clear the current content of the MinHeap
        self._heap = DynamicArray()

        # Copy the elements from the DynamicArray to the MinHeap
        for value in da:
            self._heap.append(value)

        # Starting from the last non-leaf node, perform heapify-down for each node
        last_non_leaf_index = (self._heap.length() // 2) - 1
        for i in range(last_non_leaf_index, -1, -1):
            self._heapify_down(i)

    def size(self) -> int:
        """
        Returns the number of items currently stored in the heap.

        Runtime complexity: O(1)
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the heap.

        Runtime complexity: O(1)
        """
        # Create a new empty DynamicArray to replace the existing one
        self._heap = DynamicArray()


def heapsort(arr: DynamicArray) -> None:
    """
    Sorts the content of a DynamicArray in non-ascending order using the Heapsort algorithm.

    Runtime complexity: O(N log N)
    """
    # Build the initial heap
    build_heap(arr)

    # Start from the last element
    k = arr.length() - 1

    # Continue until k reaches the beginning of the array
    while k > 0:
        # Swap the maximum element (at the root of the heap) with the last element
        arr[0], arr[k] = arr[k], arr[0]

        # Decrement k to shrink the heap portion
        k -= 1

        # Restore the heap property for the remaining heap portion
        heapify_down(arr, 0, k)

# Helper functions used in heapsort

def build_heap(arr: DynamicArray) -> None:
    """
    Builds a min heap from the given DynamicArray.
    """
    # Starting from the last non-leaf node, perform heapify-down for each node
    last_non_leaf_index = (arr.length() // 2) - 1
    for i in range(last_non_leaf_index, -1, -1):
        heapify_down(arr, i, arr.length() - 1)

def heapify_down(arr: DynamicArray, index: int, end: int) -> None:
    """
    Restores the min heap property by moving the element at the given index down the heap.
    """
    while True:
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_child_index = index

        # Compare with left child
        if left_child_index <= end and arr[left_child_index] < arr[smallest_child_index]:
            smallest_child_index = left_child_index

        # Compare with right child
        if right_child_index <= end and arr[right_child_index] < arr[smallest_child_index]:
            smallest_child_index = right_child_index

        # If the smallest child is the current node, the heap property is restored
        if smallest_child_index == index:
            break

        # Swap the current node with the smallest child
        arr[index], arr[smallest_child_index] = arr[smallest_child_index], arr[index]

        # Move to the next level in the heap
        index = smallest_child_index


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    # Your test case
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    # Call heapsort to sort the DynamicArray
    heapsort(da)
    print(f"After: {da}")


