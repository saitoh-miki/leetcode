# %% [706. Design HashMap](https://leetcode.com/problems/design-hashmap/)
class MyHashMap(dict):
    def put(self, key: int, value: int) -> None:
        self[key] = value

    def get(self, key: int) -> int:
        return dict.get(self, key, -1)

    def remove(self, key: int) -> None:
        if key in self:
            del self[key]
