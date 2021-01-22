# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# 88 ms
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            # 정렬한 값을 key로 갖고, 원래 값을 value로 갖는 딕셔너리
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())