class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort array based off distance then return 
        # the first k points

        # Define distance function
        def distance(point):
            return point[0]**2 + point[1]**2

        # Points is sorted based off of distance
        points = sorted(points, key=distance)
        # Return first k
        return points[:k]