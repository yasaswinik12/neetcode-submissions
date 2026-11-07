import math
class Solution:
    def merge(self, points, s, m, e):
        # print(points, s, m, e)
        l1 = s
        l2 = m+1
        temp = []
        while l1 <= m and l2 <= e:
            # print("l1, l2, points[l1][2], points[l2][2]", l1, l2, points[l1][2], points[l2][2])
            if points[l1][2] < points[l2][2]:
                temp.append(points[l1])
                l1+=1
            else:
                temp.append(points[l2])
                l2 += 1
        while l1 <= m:
            temp.append(points[l1])
            l1+=1
        while l2<=e:
            temp.append(points[l2])
            l2+=1
        for i, p in enumerate(temp):
            points[s+i] = p
        return points

    def mergeSort(self, points, s, e):
        if e-s+1<=1:
            return points
        m = (s+e)//2
        self.mergeSort(points, s, m)
        self.mergeSort(points, m+1, e)
        self.merge(points, s, m, e)
        return points

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            point.append(distance)
        # print(points)
        points = self.mergeSort(points, 0, len(points)-1)
        print("points after sorting", points)
        res = []
        for i in range(k):
            res.append(points[i][:2])
        return res



        