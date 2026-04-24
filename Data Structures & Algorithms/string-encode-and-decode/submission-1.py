class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(s)
            res.append('\0')
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        return s.split("\0")[0:-1]
