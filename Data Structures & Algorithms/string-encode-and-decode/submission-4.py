class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, words = [], []
        for s in strs:
            sizes.append(f"{len(s)}")
            sizes.append(',')

        sizes.append('#')
        for s in strs:
            sizes.append(s)
        return "".join(sizes)

    def decode(self, s: str) -> List[str]:
        delim = s.find('#')
        if delim == -1:
            return []
        header = s[:delim]
        sizes = [int(x) for x in header.split(',') if x != '']
        out = []
        i = delim + 1
        for size in sizes:
            out.append(s[i : i + size])
            i += size
        return out