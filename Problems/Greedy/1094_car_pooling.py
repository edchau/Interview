"""
There is a car with capacity empty seats. The vehicle only drives east 
(i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trip[i] = 
[numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi 
passengers and the locations to pick them up and drop them off are fromi and 
toi respectively. The locations are given as the number of kilometers due east 
from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all 
the given trips, or false otherwise.


"""

class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        transactions = []
        
        for p, fr, to in trips:
            transactions.append((fr, p))
            transactions.append((to, -p))
        
        # sort by destination
        transactions.sort()
        
        car = 0
        for _, p in transactions:
            car += p
            if car > capacity:
                return False
        
        return True