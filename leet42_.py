def trap(height):
    l, r, tot = 0,len(height) - 1, 0
    m_left, m_right = height[l] , height[r]
    while l < r:
        if height[l] < height[r]:
            if height[l] > m_left:
                m_left = height[l]
            else:
                tot += m_left - height[l]
            l += 1
        else:
            if height[r] > m_right:
                m_right = height[r]
            else:
                tot += m_right -height[r]
            r -= 1
    return tot