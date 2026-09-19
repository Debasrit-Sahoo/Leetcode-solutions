class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2: return True
        if x1 <= xCenter <= x2:
            return abs(yCenter - y1) <= radius or abs(yCenter - y2) <= radius
        if y1 <= yCenter <= y2:
            return abs(xCenter - x1) <= radius or abs(xCenter - x2) <= radius
        
        if xCenter < x1:
            if yCenter < y1:
                return math.dist((x1, y1), (xCenter, yCenter)) <= radius
            else:
                return math.dist((x1, y2), (xCenter, yCenter)) <= radius
        else:
            if yCenter < y1:
                return math.dist((x2, y1), (xCenter, yCenter)) <= radius
            else:
                return math.dist((x2, y2), (xCenter, yCenter)) <= radius