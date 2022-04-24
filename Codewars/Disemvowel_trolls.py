from string import ascii_letters

def disemvowel(word):
    vowel = 'aAeEiIoOuU'
    word_ = [x for x in word if x not in vowel]
    return ''.join(word_)


print(disemvowel('This website is for losers LOL!'))