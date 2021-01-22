# 819. Most Common Word
# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

# 1. Using defaultdict (36 ms)
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                if word not in banned]
        
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
        
        return max(counts, key=lambda x: counts[x])
        # return max(counts, key=counts.get)
"""

# 2. Using object of Counter (40 ms)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                if word not in banned]
        
        counts = collections.Counter(words)
        
        return counts.most_common(1)[0][0]
