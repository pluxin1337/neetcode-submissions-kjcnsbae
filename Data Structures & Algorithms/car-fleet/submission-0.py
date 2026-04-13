class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = list(zip(position, speed))
        paired.sort()
        
        stack = []
        for pos, sp in reversed(paired):
            time = float(target - pos)/sp
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)