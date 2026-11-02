class Solution:

  def findCheapestPrice(
      self, n: int, flights: List[List[int]], src: int, dst: int, k: int
  ) -> int:
    # Build adjacency list
    fl = {}
    for f, t, p in flights:
      if f not in fl:
        fl[f] = []
      fl[f].append((t, p))

    # Memoization cache: (current_city, stops_remaining) -> min_price
    memo = {}

    def fly(current, stops_left):
      # If we reached the destination
      if current == dst:
        return 0
      # If we ran out of stops
      if stops_left < 0:
        return float("inf")

      # Check cache
      state = (current, stops_left)
      if state in memo:
        return memo[state]

      min_price = float("inf")

      # Explore neighbors
      for next_node, price in fl.get(current, []):
        sub_price = fly(next_node, stops_left - 1)
        if sub_price != float("inf"):
          min_price = min(min_price, price + sub_price)

      memo[state] = min_price
      return min_price

    result = fly(src, k)
    return result if result != float("inf") else -1