class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while asteroid < 0 and len(stack) > 0:
                if stack[-1] < 0:
                    break
                prev_asteroid = stack.pop()
                if abs(prev_asteroid) > abs(asteroid):
                    asteroid = prev_asteroid                    
                elif abs(prev_asteroid) == abs(asteroid):
                    asteroid = None
                    break
            if asteroid:
                stack.append(asteroid)
        
        return stack
