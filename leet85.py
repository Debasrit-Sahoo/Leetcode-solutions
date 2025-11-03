def maximalRectangle(matrix):
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
            heights.pop()
            return area
        out = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if i > 0 and matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
            ret = largestRectangleArea(matrix[i])
            out = out if out > ret else ret
        return out