import json


class ParagraphStats:
    def __init__(self, paragraph):
        self.paragraph = paragraph

    def count_vowels(self):
        vowels = set('aeiouAEIOU')
        return sum(c in vowels for c in self.paragraph)

    def count_consonants(self):
        return sum(c.isalpha() and c not in 'aeiouAEIOU' for c in self.paragraph)

    def count_words(self):
        return len(self.paragraph.split())

    def count_sentences(self):
        return len(self.paragraph.split('.'))

    def count_digits(self):
        return sum(c.isdigit() for c in self.paragraph)

    def count_symbols(self):
        symbols = set('!@#$%^&*()_+-=[]{};:\'",.<>?/\\|`~')
        return sum(c in symbols for c in self.paragraph)

    def word_frequency(self):
        words = self.paragraph.split()
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        return frequency

    def count_palindromes(self):
        words = self.paragraph.split()
        return sum(word == word[::-1] for word in words)

    def count_anagrams(self):
        words = self.paragraph.split()
        anagram_set = set()
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if sorted(words[i]) == sorted(words[j]):
                    anagram_set.add((words[i], words[j]))
        return len(anagram_set)

    def paragraph_stats(self):
        stats = {}
        stats['vowels'] = self.count_vowels()
        stats['consonants'] = self.count_consonants()
        stats['words'] = self.count_words()
        stats['sentences'] = self.count_sentences()
        stats['digits'] = self.count_digits()
        stats['symbols'] = self.count_symbols()
        stats['frequency'] = self.word_frequency()
        stats['palindrome'] = self.count_palindromes()
        stats['anagrams'] = self.count_anagrams()
        return stats

paragraph = "There is no strife, no prejudice, no national conflict in outer space as yet. Its hazards are hostile to us all. Its conquest deserves the best of all mankind, and its opportunity for peaceful cooperation many never come again. But why, some say, the moon? Why choose this as our goal? And they may well ask why climb the highest mountain? Why, 35 years ago, fly the Atlantic? Why does Rice play Texas? We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organise and measure the best of our energies and skills, because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win, and the others, too. -- John F Kennedy"
stats = ParagraphStats(paragraph).paragraph_stats()
print(json.dumps(stats,indent=4))
