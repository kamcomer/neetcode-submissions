class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{s}\0"
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("\0")[0:-1]
