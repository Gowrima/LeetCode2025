int maxArea(int* height, int heightSize) {
    int start = 0, end = heightSize-1;
    int curArea = 0, maxArea = 0;

    while (start < end) {
        int curHeight = height[start] < height[end] ? height[start]:height[end];
        int curWidth = end-start;

        curArea = curHeight * curWidth;
        maxArea = curArea > maxArea?curArea:maxArea;

        if (height[start] > height[end]) {
            end--;
        } else {
            start++;
        }
    }

    return maxArea;
}