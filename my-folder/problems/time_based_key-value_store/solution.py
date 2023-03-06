class TimeMap:

    def __init__(self):
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timestamps.get(key, 0):
            self.timestamps[key].append((value, timestamp))
        else:
            self.timestamps[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        temp_ls = self.timestamps.get(key, 0)
        if not temp_ls or timestamp < temp_ls[0][1]:
            return ""
        
        l, r = 0, len(temp_ls)-1

        while l <= r:
            m = (l+r)//2
            if temp_ls[m][1] == timestamp:
                return temp_ls[m][0]
            elif temp_ls[m][1] > timestamp:
                r = m-1
            else:
                l = m+1
            
        return temp_ls[l-1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)