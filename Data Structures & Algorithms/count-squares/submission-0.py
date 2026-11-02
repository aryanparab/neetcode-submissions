from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        # Using a defaultdict to track frequencies of points stored as tuples
        self.pts_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # Convert to tuple so it's hashable
        self.pts_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        ways = 0
        
        # Iterate through all unique points to find a diagonal counterpart
        for (x, y), count in self.pts_count.items():
            # Check if it forms a valid diagonal (sides must be equal and > 0)
            if abs(qx - x) != abs(qy - y) or qx == x or qy == y:
                continue
                
            # The other two points required to complete the square
            p1 = (x, qy)
            p2 = (qx, y)
            
            # The number of ways to form this specific square is the product of their counts
            if p1 in self.pts_count and p2 in self.pts_count:
                ways += count * self.pts_count[p1] * self.pts_count[p2]
                
        return ways