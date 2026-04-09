class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for char in strs:
            key="".join(sorted(char))
            if key in dict:
                dict[key].append(char)
            else:
                dict[key]=[char]
        return list(dict.values())                
            




        