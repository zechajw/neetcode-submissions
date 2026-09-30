class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        records = self.store[key]

        left, right = 0, len(records) - 1

        # [1, 2, 3, 5], looking with timestamp 4

        # left = 0, right = 3, middle = 1, records[middle] <= timestamp so left = middle = 1
        # left = 1, right = 3, middle = 2, records[middle] <= timestamp so left = middle = 2
        # left = 2, right = 3, middle = 2

        res = ""
        # we want to find the highest value that is leq to timestamp
        while left <= right:
            middle = left + (right - left) // 2

            if records[middle][1] <= timestamp:
                res = records[middle][0]
                left = middle + 1
            else: # records[middle] > timestamp
                right = middle - 1
        
        return res

                
