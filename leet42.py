def trap(height):
    total = 0
    temp = 0
    prev = 0
    for i in range(len(height)):
        if height[i] >= height[prev]:
            total += temp
            temp = 0
            prev = i
        else:
            temp += height[prev] - height[i]
    temp = 0
    nprev = len(height)- 1
    for i in range(len(height)- 1, prev -1 , -1):
        if height[i] == height[nprev]:
            continue
        if height[i] >= height[nprev]:
            total += temp
            temp = 0
            nprev = i
        else:
            temp += height[nprev] - height[i]
    return total