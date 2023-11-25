"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""


def compute_max_area(heights):
    """
    :type heights: List[int]
    :rtype: int
    """

    max_area = 0

    for i in range(len(heights) - 1):
        for j in range(i + 1, len(heights)):
            width = j - i
            height = min(heights[i], heights[j])
            area = width * height

            if area > max_area:
                max_area = area

    return max_area
