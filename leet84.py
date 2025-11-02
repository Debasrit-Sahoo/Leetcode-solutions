def largestRectangleArea(heights):
        stack = []
        heights.append(0)
        area = 0
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left -1
                area = area if area > (width*height) else width*height
            stack.append(i)
        return area