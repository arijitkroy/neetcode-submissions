class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            srt = ''.join(sorted(s))
            out[srt].append(s)
        return list(out.values())