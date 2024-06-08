### Quicksort Algorithm

#### Pseudocode

```python
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print(f"Sorted array: {arr}")
```

### Explanation

1. **Design Technique**:
    - Quicksort uses the **divide-and-conquer** design technique. It divides the array into two smaller sub-arrays based on a pivot element, recursively sorts the sub-arrays, and combines the sorted sub-arrays to form the final sorted array.

2. **Time Complexity**:
    - **Best Case**: O(n log n)
      - Occurs when the pivot divides the array into two nearly equal halves.
    - **Worst Case**: O(n²)
      - Occurs when the pivot is the smallest or largest element, resulting in one sub-array with n-1 elements and the other with 0 elements.

3. **Recurrence Tree Analysis**:
    - The recurrence relation for quicksort is:
      \[
      T(n) = T(k) + T(n - k - 1) + O(n)
      \]
      where \( k \) is the number of elements in one sub-array and \( n - k - 1 \) in the other.
    - **Best Case**: \( k = n/2 \)
      \[
      T(n) = 2T(n/2) + O(n)
      \]
    - **Worst Case**: \( k = 0 \)
      \[
      T(n) = T(n-1) + O(n)
      \]

4. **Backward Substitution**:
    - For the best case:
      \[
      T(n) = 2T(n/2) + cn
      \]
      Assume \( T(n) = cn \log n \):
      \[
      T(n) = 2(c(n/2) \log (n/2)) + cn = cn \log n - cn \log 2 + cn = cn \log n
      \]
    - For the worst case:
      \[
      T(n) = T(n-1) + cn
      \]
      Using substitution:
      \[
      T(n) = T(n-1) + cn = T(n-2) + c(n-1) + cn = \ldots = T(1) + c(2 + 3 + \ldots + n) = T(1) + c(n(n+1)/2 - 1)
      \]
      Therefore, \( T(n) = O(n²) \).

5. **Master's Theorem**:
    - For the best case recurrence:
      \[
      T(n) = 2T(n/2) + O(n)
      \]
      Compare with the form \( T(n) = aT(n/b) + f(n) \):
      - \( a = 2 \), \( b = 2 \), \( f(n) = O(n) \).
      - Compare \( f(n) \) with \( n^{\log_b a} = n^{\log_2 2} = n \).
      - Since \( f(n) = O(n) \) matches \( n^{\log_2 2} \):
        \[
        T(n) = O(n \log n)
        \]

### Summary
- **Design Technique**: Divide-and-conquer.
- **Best Case Time Complexity**: O(n log n).
- **Worst Case Time Complexity**: O(n²).
- **Master's Theorem Result**: T(n) = O(n log n) for the best case.

### Recurrence Tree Analysis

For a more detailed recurrence tree analysis, consider dividing the problem at different pivot positions:

- **Balanced Partition (Best Case)**:
  - Each level of recursion divides the array into two halves:
    \[
    T(n) = 2T(n/2) + cn
    \]
    \[
    \begin{array}{ccc}
    \text{Level 0:} & n & \text{work}\\
    \text{Level 1:} & 2 \cdot (n/2) = n & \text{work}\\
    \text{Level 2:} & 4 \cdot (n/4) = n & \text{work}\\
    \text{...} & ... & \text{work}\\
    \end{array}
    \]
    - The tree has \(\log n\) levels.
    - Total work: \(\sum_{i=0}^{\log n} cn = cn \log n\).

- **Skewed Partition (Worst Case)**:
  - One sub-array is empty, the other has \( n-1 \) elements:
    \[
    T(n) = T(n-1) + cn
    \]
    \[
    \begin{array}{ccc}
    \text{Level 0:} & n & \text{work}\\
    \text{Level 1:} & n-1 & \text{work}\\
    \text{Level 2:} & n-2 & \text{work}\\
    \text{...} & ... & \text{work}\\
    \end{array}
    \]
    - The tree has \( n \) levels.
    - Total work: \(\sum_{i=1}^{n} ci = O(n^2)\).

This analysis confirms the best case time complexity as \( O(n \log n) \) and the worst case time complexity as \( O(n^2) \).

