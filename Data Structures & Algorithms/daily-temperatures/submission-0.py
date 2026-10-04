class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we keep a monotonically decreasing stack of temperature and index
        # [(30, 0)]


        # result = [1, 0, 0, 0, 0, 0, 0]
        # at (38, 1), we can resolve all previous values with a lower temperature, so (30, 0) => index 0 is curr_day - prev_day = 1
            # then the stack will be [(38, 1)]
        # at (30, 2), we cant resolve, so we just add to the stack
            # [(38, 1), (30, 2)]
        # at (36, 3), we resolve (30, 2) = 3 - 2 = 1
            # [(38, 1), (36, 3)]
        # ...

        # at the end, we will have [(40, 5), (28, 6)] => these days did not have a temperature warmer than it on a future day, so we just leave them as the default value 0

        result = [0] * len(temperatures)
        decreasing_stack = []

        for curr_day, temperature in enumerate(temperatures):
            while decreasing_stack:
                prev_day, prev_temperature = decreasing_stack[-1]
                if prev_temperature < temperature:
                    result[prev_day] = curr_day - prev_day
                    decreasing_stack.pop()
                else:
                    break

            decreasing_stack.append((curr_day, temperature))

        return result

                     