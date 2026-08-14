class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key]=[]
        self.keystore[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        l = 0
        v = self.keystore.get(key,[])
        r = len(v)-1

        while l<=r:
            mid = (l+r)//2

            if v[mid][1]<=timestamp:
                res=v[mid][0]
                l=mid + 1
            else:
                r=mid - 1

        return res
            
                
        
