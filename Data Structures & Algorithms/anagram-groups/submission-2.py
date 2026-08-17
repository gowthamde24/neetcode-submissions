class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hashmap = {}

        for i in strs:
            sort_strs = ''.join(sorted(i))

            if sort_strs not in hashmap:
                hashmap[sort_strs]=[]
            hashmap[sort_strs].append(i)
        return list(hashmap.values())

        
        