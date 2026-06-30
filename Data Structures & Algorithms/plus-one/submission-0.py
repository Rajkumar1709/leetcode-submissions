class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        x = str(int(s) + 1)
        temp = []
        for i in x:
            temp.append(int(i))
        return temp
