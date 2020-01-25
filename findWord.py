# This program seeks to find candiate words from given letter input.

def main():
        while True:
            # Input the word length in number of characters
            try:
                wordLength = int(input('Nr letters in the word: '))
                break
            except:
                print('Input the total number of characters of the word e.g. test is 4.')

        # Each individual question 1 for each letter in the word.
        questions = {}
        for question in range(wordLength):
            # Question nr, python starts counting from 0, so add 1
            question += 1
            while True:
                try:
                    questions[question] = str(input('Input candidate letters as a whole string for character ' + str(question) + ' : ')).lower()
                    # Only accept letters as input
                    if questions[question].isalpha():
                        break
                except:
                    print('Not a valid letter.')

        AllWords = get_wordList('SwedishWordListTrim.txt')
        # The words of concern, e.g. if we are looking for a 2 characters word.
        words = get_words(AllWords, wordLength)


        # Final candidates based on matching letters
        candidates = []
        for word in words:
            score = 0 # Reset for each word
            key = 1 # Index, starting at key 1 from the dictionary.
            maxScore = 1 * len(word) # if for all the characters in the word are found in the guessed.
            for letter in word:
                if letter in questions[key]:
                    score += 1
                key += 1

            if score == maxScore:
                # If character is found within the guess set.
                candidates.append(word)

        # CMD output
        print('Possible candidates:')
        for i in candidates:
            print(' - ', i)



def get_words(AllWords, wordLength):
    candidates = []
    for word in AllWords:
        if len(word) == wordLength:
            candidates.append(word)
    return candidates

def get_wordList(filename):
    # Read in the entire wordlist in a list.
    with open(filename, 'r') as f:
        wordList = f.read().split('\n')
    return wordList



if __name__ == '__main__':
    main()
