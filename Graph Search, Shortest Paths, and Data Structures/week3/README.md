# Median maintenance by Heap

The goal of this problem is to implement the `"Median Maintenance" algorithm` (covered in the Week 3 lecture on heap applications). The [text file](https://github.com/Chang-Chia-Chi/Cousera-Standford-Algorithm-Specialization/blob/main/Graph%20Search%2C%20Shortest%20Paths%2C%20and%20Data%20Structures/week3/Median.txt) contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting x_i denote the iith number of the file, the k-th median m_k is defined as the median of the numbers x_1,...,x_k
(So, if k is odd, then m_k is ((k+1)/2)-th smallest number among x_1,...,x_k, if k is even, then m_k is the (k/2)-th smallest number among x_1,...,x_k.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (m_1+m_2+m_3 + ... + m_10000) mod 10000
