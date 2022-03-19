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

    text = ["", "", "", "", ""]
    guess = guess.lower()
    target_freq = generate_frequency(target)

    if guess == target:
        text = [f"[green]{word.upper()}[/green]" for word in guess]
    else:

        for i in range(len(guess)):
            
            if guess[i] == target[i]:
                
                text[i] = f"[green]{guess[i].upper()}[/green]"
                target_freq[guess[i]] -= 1
       
        for i in range(len(guess)):
            if (guess[i] != target[i]) and (guess[i] in target):
                
                if target_freq[guess[i]] > 0:
                    text[i] = f"[yellow]{guess[i].upper()}[/yellow]"
                    target_freq[guess[i]] -= 1
                else:
                    text[i] = f"[bright_black]{guess[i].upper()}[/bright_black]"

            elif guess[i] not in target:
                text[i] = f"[bright_black]{guess[i].upper()}[/bright_black]"
    
    return ''.join(text)

def update_keyboard(guess, target, row1, row2, row3):

    '''
    update_keyboard(guess, target, row1, row2, row3) -> None

    updates the keyboard dict for each row of the keyboard

    :param guess - word guessed by the user
    :param target - word to compare to        
    :param row1 - keyboard row 1 (dict)
    :param row2 - keyboard row 2 (dict)
    :param row3 - keyboard row 3 (dict)
    '''

    word_row1 = "qwertyuiop"
    word_row2 = "asdfghjkl"

    guess = guess.lower()
    target_freq = generate_frequency(target)

    if guess == target:
        
        for word in guess:
            if word in word_row1:
                row1[word] = "green"
            elif word in word_row2:
                row2[word] = "green"
            else:
                row3[word] = "green"
    else:

        for i in range(len(guess)):
            
            if guess[i] == target[i]:
                
                if guess[i] in word_row1:
                    row1[guess[i]] = "green"
                elif guess[i] in word_row2:
                    row2[guess[i]] = "green"
                else:
                    row3[guess[i]] = "green"
            
                target_freq[guess[i]] -= 1
       
        for i in range(len(guess)):
            if (guess[i] != target[i]) and (guess[i] in target):
                
                if target_freq[guess[i]] > 0:
                    if guess[i] in word_row1:
                        row1[guess[i]] = "yellow"
                    elif guess[i] in word_row2:
                        row2[guess[i]] = "yellow"
                    else:
                        row3[guess[i]] = "yellow"

                    target_freq[guess[i]] -= 1
                else:
                    if guess[i] in word_row1:
                        row1[guess[i]] = "bright_black"
                    elif guess[i] in word_row2:
                        row2[guess[i]] = "bright_black"
                    else:
                        row3[guess[i]] = "bright_black"

            elif guess[i] not in target:
                if guess[i] in word_row1:
                    row1[guess[i]] = "bright_black"
                elif guess[i] in word_row2:
                    row2[guess[i]] = "bright_black"
                else:
                    row3[guess[i]] = "bright_black"

def print_keyboard(row1, row2, row3):

    '''
    print_keyboard(row1, row2, row3) -> None

    prints out the keyboard in it's current state

    :param row1 - keyboard row 1 (dict)
    :param row2 - keyboard row 2 (dict)
    :param row3 - keyboard row 3 (dict)
    '''

    text1 = [f"[{v}]{k.upper()}[/{v}]" for (k,v) in row1.items()]
    text2 = [f"[{v}]{k.upper()}[/{v}]" for (k,v) in row2.items()]
    text3 = [f"[{v}]{k.upper()}[/{v}]" for (k,v) in row3.items()]
    
    console.print(" ".join(text1), style="bold", justify="center")
    console.print(" ".join(text2), style="bold", justify="center")
    console.print(" ".join(text3), style="bold", justify="center")

def generate_share(guess, target):
    
    '''
    generate_share(guess, target) -> string with emojis

    returns a emoji string in the classic wordle style of green, yellow, and grey
    based on a comparison of the two strings

    :param guess - word guessed by the user
    :param target - word to compare to

    NOTE: this is very similar to compare_words and I know that I could just combine the two
    '''
    
    text = ["", "", "", "", ""]
    guess = guess.lower()
    target_freq = generate_frequency(target)

    if guess == target:
        text =  ["\U0001F7E9", "\U0001F7E9", "\U0001F7E9", "\U0001F7E9", "\U0001F7E9"]
    else:
        for i in range(len(guess)):
            
            if guess[i] == target[i]:
                text[i] = "\U0001F7E9"
                target_freq[guess[i]] -= 1

        for i in range(len(guess)):
            if (guess[i] != target[i]) and (guess[i] in target):
                
                if target_freq[guess[i]] > 0:
                    text[i] = "\U0001F7E8"
                    target_freq[guess[i]] -= 1
                else:
                    text[i] = "\U0001F7EB"

            elif guess[i] not in target:
                text[i] = "\U0001F7EB"
    
    return ''.join(text)

def copy_share(num, share_list):

    '''
    copy_share(num, share_list) -> None

    copies the wordle share to the clipboard

    :param num - the worlde number to share result for
    :param share_list - the list of "share strings" generated by generate_share
    '''
    
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

def main(target_num = get_wordle_num(), easy=True):
    
    '''
    main(target_num, easy) -> None

    The main wordle game 

    :param target_num - wordle # the user wants to play, the current day's wordle by default
    :param easy = toggle between easy mode and hard mode
    '''
   
    # Not letting the user play ahead
    if int(target_num) > get_wordle_num():
        target_num = get_wordle_num()

    target_word = get_wordle(int(target_num))
   
    # Making the keyboard dicts to be modified later
    text_row1 = {"q":"white", "w":"white", "e":"white", "r":"white", "t":"white", "y":"white", "u":"white", "i":"white", "o":"white", "p":"white"}
    text_row2 = {"a":"white", "s":"white", "d":"white", "f":"white", "g":"white", "h":"white", "j":"white", "k":"white", "l":"white"}
    text_row3 = {"z":"white", "x":"white", "c":"white", "v":"white", "b":"white", "n":"white", "m":"white"}
   
    console.print(f"[pink1]Welcome to wordle! You know how to play :)[/pink1]", style="bold", justify="center")   
    print()

    turn_count = 1
    win = False
    first_try = True
    
    guess_list = []
    wordle_share = []

    while turn_count <= 6 and not(win):
        if first_try and easy:
            print_keyboard(text_row1, text_row2, text_row3)
            first_try = False

        guess_word = console.input(f"[blue]Please enter a word:[/blue] ").lower()

        if check_valid_word(guess_word):

            guess_list.append(compare_words(guess_word, target_word))
            update_keyboard(guess_word, target_word, text_row1, text_row2, text_row3)
            wordle_share.append(generate_share(guess_word, target_word))

            if guess_word == target_word:
                win = True
            
            print()
            for word in guess_list:
                console.print(f"{word} [{guess_list.index(word) + 1}/6]", justify="center")
            print()
            if easy and not(win):
                print_keyboard(text_row1, text_row2, text_row3)
                print()

            turn_count += 1
        else:
            console.print(f"[red]Not a valid word![/red]", style="bold", justify="center")
            print()
            if easy and not(win):
                print_keyboard(text_row1, text_row2, text_row3)
                print()

    print_result(target_num, guess_list, wordle_share, win)
    copy_share(target_num, wordle_share)
