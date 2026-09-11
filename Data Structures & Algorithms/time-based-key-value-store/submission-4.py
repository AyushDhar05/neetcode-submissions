class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # if key not in self.store: return ""
        curr_list = self.store.get(key, [])
        if not curr_list: return ""

        # upper bound
        l, r = 0, len(curr_list) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            val = curr_list[mid]
            if val[1] <= timestamp: 
                res = val[0]
                l = mid + 1
            else: 
                r = mid - 1
        return res