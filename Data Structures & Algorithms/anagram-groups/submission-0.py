class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_dict = {}

        for i in strs:
            sort_str = ''.join(sorted(i))

            if sort_str not in key_dict:
                key_dict[sort_str]=[]
            key_dict[sort_str].append(i)

        return list(key_dict.values())
        