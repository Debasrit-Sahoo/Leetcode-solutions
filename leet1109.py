class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff_arr = [0]*(n+1)
        for s, e, x in bookings:
            diff_arr[s-1] += x
            diff_arr[e] -= x
            
        for i in range(1, n):
            diff_arr[i] += diff_arr[i-1]

        diff_arr.pop()
        return diff_arr