# Sorting Algorithms visualizer using python

This application is built mainly using Python. The user can choose from the dropdown menu which sorting algorithm to use as well as how visualization occurs.

- # The Project
  We built this application in order to have an easier and deeper understanding of the most important sorting algorithms using Python and tkinter library
  
 # Illustration of the Visualization:
 ![Sorting Algorithms Visualization using Python](https://user-images.githubusercontent.com/99495858/206155512-79d3ccd0-478e-4a3f-830c-4816e29e479a.gif)

# The algorithms used:

- [1.Insertion sort](https://github.com/Vincent-ondeng/Sorting_Visualizer/blob/main/algorithms/Sorting_Visualizer/algorithms/insertionSort.py)
  A simple sorting algorithm that builds the sorted array one element at a time by removing the probed element and inserting it in the place it needs to be in the final sorted array. It performs well on small lists but it is not efficient on large lists and has much lower performance than more advanced algorithms such as quicksort, heapsort or merge sort. Worst case performance is just like Bubble Sort, having O(n^2) comparisons and swaps when the array is completely reversed and also a best case performance of O(n) comparisons and O(1) swaps.

- [2.Bubble sort](https://github.com/Vincent-ondeng/Sorting_Visualizer/blob/main/algorithms/Sorting_Visualizer/algorithms/bubbleSort.py)
  is one of the simpler sorting algorithms as it repeatedly steps through the list comparing adjacent elements and swapping them in case they are not in ascending order. Worst case performance will be met when the array is entirely reversed so we would get O(n^2) comparisons and swaps. Best case would be if the array would be already sorted and it would amount to O(n) comparisons and O(1) swaps.
- [3.Counting sort](https://github.com/Vincent-ondeng/Sorting_Visualizer/blob/main/algorithms/Sorting_Visualizer/algorithms/countingSort.py)
  Is an algorithm for sorting a collection of objects according to keys that are small positive integers; that is, it is an integer sorting algorithm. It operates by counting the number of objects that possess distinct key values, and applying prefix sum on those counts to determine the positions of each key value in the output sequence.
  Worst case - O(n + k) where k is the range of the non-negative key values
  Worst-case space complexity O(n + K)
- [4.Heap sort](https://github.com/Vincent-ondeng/Sorting_Visualizer/blob/main/algorithms/Sorting_Visualizer/algorithms/heapSort.py)
  a comparison based sorting technique based on the Binary Heap data strucutre. It is similar to selection sort where we first find the maximum element and place it at the end. We repeat the process for the remaining elements. We build a max heap from the input array. At this point the largest item is stored at the root of the heap. We replace it with the last item of the heap followed by reducing the size of the heap by 1. Finally, we heapify the root of tree. We repeat the previous step until size of heap is greater than 1. Worst case complexity is O(n \* log(n)).
- [5.selection sort](https://github.com/Vincent-ondeng/Sorting_Visualizer/blob/main/algorithms/Sorting_Visualizer/algorithms/selectionSort.py)
  It divides the input list into two sublists. The first sublist starts from the left and contains the sorted elements and the second sublist contains only the unsorted elements. Once we find the minimum element from the unsorted array during an interation we remove it from the second sublist and insert it in the sorted one. Because of this the worst case performance is O(n^2) comparisons and O(n) swaps and best case is O(n^2) comparisons and O(1) swaps. So even in the best case scenario the complexity of this algorithm is quadratic. The only advantage of this algorithm is that it has the minimum number of swaps possible, n-1 in the worst case.
- [6.Quick sort](https://github.com/Vincent-ondeng/Sorting_Visualizer/blob/main/algorithms/Sorting_Visualizer/algorithms/quickSort.py)
  just like Merge Sort, it is a Divide and Conquer algorithm. It picks an element as a pivot (first, last, random) and partitions the given array around the picked pivot. In most cases the complexity is O(n _ log(n)), but in the worst case scenario it is O(n^2). Regardless, Quick Sort is in practice faster than all other O(n _ log(n)) algorthitms, because the inner loop is efficiently implemented.
- [7.Merge sort](https://github.com/Vincent-ondeng/Sorting_Visualizer/blob/main/algorithms/Sorting_Visualizer/algorithms/mergeSort.py)
  Is a Divine and Conquer algorithm. It divides the array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The worst case complexity is O(n \* log(n)). It can perform better than Quick Sort.

## Team:

- The team members of the sorting algorithm are:

Christabel Okwisa - [Github](https://github.com/chrisokwisa/Sorting_Visualizer.git)
Worked on Selection, counting, Bubble, Heap and Insertion sort

vinncent Ondeng - [Github](https://github.com/Vincent-ondeng)
creation of the landing page for the project and visualization

Dainah Wanjiku - [Github](https://github.com/dainahwanjiku)I
mplementing merge sort and quick sort

We decided on these roles because each one of us is comfortable with the roles provided.
Each person is responsible for the quality and timely completion of the task to ensure accountability that can help team members identify and address challenges such as missing resources or delays.

## LICENSE:

No copyright to the project
