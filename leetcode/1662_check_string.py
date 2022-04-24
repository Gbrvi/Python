# def check(word1, word2):
#     return ''.join(word1) == ''.join(word2)



# print(check(['a', 'cb'], ['ab', 'c']))

# class Solution:
#     def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
#         for c1, c2 in zip(self.generate(word1), self.generate(word2)):
#             if c1 != c2:
#                 return False
#         return True

#     def generate(self, wordlist: list[str]):
#         for word in wordlist:
#             for char in word:
#                 yield char
#         yield None

# a = Solution()

# print(a.arrayStringsAreEqual(['ab', 'c'], ["a", "bc", "d", "efg"]))


def checador(l1: list[str], l2: list[str]):
    for c1, c2 in zip(gerador(l1), gerador(l2)):
        if c1 != c2:
            return False
    return True


def gerador(wordlist): 
    for word in wordlist:
        for caractere in word:
            yield caractere
    yield None
        

print(checador(['ab', 'c'], ["a", "bc"]))
