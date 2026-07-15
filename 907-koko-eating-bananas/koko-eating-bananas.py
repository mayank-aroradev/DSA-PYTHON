class Solution:
    def can_eat_all(self, piles: List[int], h: int, speed: int) -> bool:
        """Helper to calculate total hours needed at a given speed"""
        total_hours = 0
        for bananas in piles:
            # Ceiling division: math.ceil(bananas / speed)
            total_hours += (bananas + speed - 1) // speed
            if total_hours>h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxb=max(piles)
        n=len(piles)
        low=1
        high=maxb
        while low<=high:
            mid=(low+high)//2
            if self.can_eat_all(piles,h,mid):
                high=mid-1
            else:
                low=mid+1


                
            
        return low