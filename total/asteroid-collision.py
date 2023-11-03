class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack= []
        
        for asteroid in asteroids:
            while stack and (stack[-1] > 0 > asteroid):
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    asteroid= None
                    break
                else:
                    asteroid = None
                    break
            if asteroid:
                stack.append(asteroid)
        return stack