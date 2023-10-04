class MyHashMap:
    #this is a not the most efficient approach
    MAX = 10 ** 6 + 5

    def __init__(self):
        self.lookup = [None] * self.MAX
        

    def put(self, key: int, value: int) -> None:
        self.lookup[key] = value
        

    def get(self, key: int) -> int:
        if self.lookup[key] is None:
            return -1
        return self.lookup[key]
        

    def remove(self, key: int) -> None:
        self.lookup[key] = None
        