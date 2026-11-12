class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through list, break down each string into its own set, if set is already present add to list,
        anagram_list = []
        set_dict = {}
        for word in strs:
            set_s = set(strs)
            if set_s in set_dict:
                # add to list of anagrams
                # THIS IS DEF SOMETHING I CAN SOLVE
                # DICTIONARY OF SET AND LIST OF ANAGRAMS?
                # {a, c, t} : ["act"]
                pass
            else:
                set_dict[set_s] = [strs]
        
        return anagram_list