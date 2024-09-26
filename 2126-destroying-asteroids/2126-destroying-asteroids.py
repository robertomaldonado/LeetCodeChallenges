class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        sorted(asteroids)
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid
        return True