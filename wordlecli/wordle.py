from datetime import date
from wordlecli.words import target_words, valid_words
from rich.console import Console
import pyperclip
# Instantiating this since it'll probably be needed by multiple functions
console = Console()

def get_wordle_num():

    '''
    get_wordle_num() -> int

    returns the wordle # for the day
    '''

    original_date = date(2021, 6, 19)
    today_date = date.today()

    return abs(original_date - today_date).days

def get_wordle(num):

    '''
    get_wordle(num) -> string

    return the wordle for a given #

    :param num - wordle # to access
    '''
    return target_words[num]

def check_valid_word(word):

    '''
    check_valid_word(word) -> bool

    checks if the word is valid based on the two list of words and it's length

    :param word - any string 
    '''
    
    word = word.lower()

    return ((word in target_words) or (word in valid_words)) and (len(word) == 5)
   
def generate_frequency(word):
    
    '''
    generate_frequency(word) -> dictionary

    returns a dictionary with letters as the key and their frequency as the value

    :param word - any string
    '''


    word = word.lower()
    freq = {}
  
    for keys in word:
        freq[keys] = freq.get(keys, 0) + 1

    return freq

def compare_words(guess, target):

    '''
    compare_words(guess, target) -> color-formatted string

    returns a string in the classic wordle style of green, yellow, and grey
    based on a comparison of the two strings

    :param guess - word guessed by the user
    :param target - word to compare to
    '''

    text = ""
    guess = guess.lower()
    target_freq = generate_frequency(target)

    if guess == target:
        text =  f"[green]{guess.upper()}[/green]"
    else:
        for i in range(len(guess)):
            
            if guess[i] == target[i]:
                
                text += f"[green]{guess[i].upper()}[/green]"
                target_freq[guess[i]] -= 1
            
            elif (guess[i] != target[i]) and (guess[i] in target):
                
                if target_freq[guess[i]] > 0:
                    text += f"[yellow]{guess[i].upper()}[/yellow]"
                    target_freq[guess[i]] -= 1
                else:
                    text += f"[bright_black]{guess[i].upper()}[/bright_black]"

            else:
                text += f"[bright_black]{guess[i].upper()}[/bright_black]"
    
    return text

def generate_share(guess, target):
    
    '''
    compare_words(guess, target) -> string with emojis

    returns a emoji string in the classic wordle style of green, yellow, and grey
    based on a comparison of the two strings

    :param guess - word guessed by the user
    :param target - word to compare to

    NOTE: this is very similar to compare_words and I know that I could just combine the two
    '''
    
    text = ""
    guess = guess.lower()
    target_freq = generate_frequency(target)

    if guess == target:
        text =  "\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9"
    else:
        for i in range(len(guess)):
            
            if guess[i] == target[i]:
                
                text += "\U0001F7E9"
                target_freq[guess[i]] -= 1
            
            elif (guess[i] != target[i]) and (guess[i] in target):
                
                if target_freq[guess[i]] > 0:
                    text += "\U0001F7E8"
                    target_freq[guess[i]] -= 1
                else:
                    text += "\U0001F7EB"

            else:
                text += "\U0001F7EB"
    
    return text

def copy_share(num, share_list):
    
    clean_list = [shr.replace('\U0001F7EB', '\u2B1B') for shr in share_list]

    share_str = f"Wordle {num} {len(clean_list)}/6\n\n"

    for shareable in clean_list:
        share_str += f"{shareable}\n"
    
    pyperclip.copy(share_str.removesuffix('\n'))

def print_result(num, guesses, share_list, win_status):


    '''
    print_result(num, guesses, share_list, win_status) -> None

    prints out an end-of-game message and also prints out the wordle shareable emojis

    :param num - wordle #
    :param guesses - a list of all the guesses
    :param share_list - a list of all the share strings
    :param win_status - the status of the game 
    '''

    if win_status:
        console.print(f"[green]Congratulations!![/green]", style="bold", justify="center")
        print()

        print(f"Wordle {num} {len(guesses)}/6\n")
        for shareable in share_list:
            console.print(shareable)
    else:
        console.print(f"[green]Good luck next time!![/green]", style="bold", justify="center")
        print()

        print(f"Wordle {num} {len(guesses)}/6\n")
        for shareable in share_list:
            console.print(shareable)

def main(target_num = get_wordle_num()):
    
    '''
    main(target_num) -> None

    The main wordle game 

    :param target_num - wordle # the user wants to play, the current day's wordle by default
    '''
   
    # Not letting the user play ahead
    if int(target_num) > get_wordle_num():
        target_num = get_wordle_num()

    target_word = get_wordle(int(target_num))
   
    console.print(f"[pink1]Welcome to wordle! You know how to play :)[/pink1]", style="bold", justify="center")   
    print()

    turn_count = 1
    win = False
    
    guess_list = []
    wordle_share = []

    while turn_count <= 6 and not(win):    
        guess_word = console.input(f"[blue]Please enter a word:[/blue] ").lower()

        if check_valid_word(guess_word):

            guess_list.append(compare_words(guess_word, target_word))
            wordle_share.append(generate_share(guess_word, target_word))

            if guess_word == target_word:
                win = True
            
            print()
            for word in guess_list:
                console.print(f"{word} [{guess_list.index(word) + 1}/6]", justify="center")
            print()

            turn_count += 1
        else:
            console.print(f"[red]Not a valid word![/red]", style="bold", justify="center")

    print_result(target_num, guess_list, wordle_share, win)
    copy_share(target_num, wordle_share)
