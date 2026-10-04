class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]

        # sort in decreasing positions
        cars.sort(key=lambda car: -car[0])

        stack = []

        for pos, spd in cars:
            # time taken to reach end is 
            # speed = distance / time
            # time = distance / speed
            # distance = target - position
            # time = (target - position) / speed

            time = (target - pos) / spd

            if not stack:
                stack.append(time)
                continue

            # car takes longer to arrive than prev car, so start a new fleet
            if time > stack[-1]:
                stack.append(time)
                continue

        return len(stack)
                