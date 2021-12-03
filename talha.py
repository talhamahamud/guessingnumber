from mahamud import words
import random
# import string
def get_word():
    word=random.choice(words)
    return word.upper()
def play(word):
    word_completion='_'*len(word)
    guessed_letter=[]
    guessed_word=[]
    guessed=False
    tries=6
    print ('play hangman')
    print (f'you have {tries} only.')
    print (word_completion)
    print ("\n")
    while not guessed and tries>0:
        guess = input("pls input a letter or word: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letter:
                print ('you have already guessed that letter')
            elif guess not in word:
                print("you enter a wrong letter")
                tries-=1
                guessed_letter.append(guess)
            else:
                print(f'good job {guess} in the word')
                guessed_letter.append(guess)
                word_as_list=list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion= "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_word:
                print("you have already enter this word")
            elif guess not in guessed_word:
                print("you enter a wrong word")
                tries-=1
                guessed_word.append(guess)
            else:
                guessed=True
                word_completion=word
        else:
            print("Sorry! you don't enter a valid word")
        print(word_completion)
    if guessed:
        print("Congrates, you got the word")
    else:
        print("Sorry, you lose the game.")
        print(f"The word is {word}")

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()