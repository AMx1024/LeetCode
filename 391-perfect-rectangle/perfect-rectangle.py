class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        bottomx, bottomy, topx, topy = float("inf"), float("inf"), float("-inf"), float("-inf")
        area = 0
        corners = set()
        
        for rectangle in rectangles:
            x1, y1, x2, y2 = rectangle[0], rectangle[1], rectangle[2], rectangle[3]
            rect_corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]

            for corner in rect_corners:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

            bottomx = min(x1, bottomx)
            bottomy = min(y1, bottomy)
            topx = max(x2, topx)
            topy = max(y2, topy)
            area += (x2-x1) * (y2-y1)
        
        corners_expected = {(topx, topy), (topx, bottomy), (bottomx, bottomy), (bottomx, topy)}

        return (topx - bottomx) * (topy - bottomy) == area and corners == corners_expected