print("-----Game(1)-------")
import random
def word_list():
    f=open("5_letter_words.txt","r")  #your file path name, use "/" 
    return f.read().split()
    
def random_word(l):
    return random.choice(l) 
    
def is_real_word(guess,l):
    if guess in l:
        return True
    else:
        return False

def check_guess(guess,word):
    k=list(word)
    res=[]
    for i in range(len(guess)):
        if guess[i] in k and guess[i] == k[i]:
            res.append("X")
        elif guess[i] in k and guess[i] != k[i]:
            res.append("O")
        else:
            res.append("_")
        try:
            k[k.index(guess[i])]="#"
            pass
        except:
            pass    
    return "".join(res) 

def next_guess(l):

    i=input("PLEASE ENTER A GUESS:").lower()
    while(not(is_real_word(i,l))):
        print("That's not a real word!",end="\n\n")
        i=input("PLEASE ENTER A GUESS:").lower()
         
    return i  

def play():
    print("----------------------Wordle Game--------------------------")
    print("Game Description:",end="\n\n")
    print("--> You have to Guess the 5 Letter word in Six guesses by following Clues:",end="\n\n")
    print("   *  if one or more single letters in guessed word are matched and are at same position of computer generated word then it gives Clue with Letter 'X'",end="\n\n")
    print("   *  if one or more single letters in guessed word are matched and but not at same position of computer generated word then it gives Clue with Letter 'O'",end="\n\n")
    print("   *  Otherwise, it shows Letter '_'",end="\n\n\n")
    print("   *  In Between it Gives Clue by giving first letter of computer generated word",end="\n\n")
    r=random_word(word_list())
    c=1
    while(c<=6):
        n=next_guess(word_list())
        print(check_guess(n,r),end="\n\n")
       
        if r==n:
            print("YOU WON! 'THE THRONE OF WORDLE'")
            break
        else:
            c=c+1
        if c==3 or c==4 or c==5:
            print("HERE IS YOUR CLUE:")
            print("First Letter of word is:",r[0],end="\n\n")    
    else:        
        print("YOU LOST!")
        print("THE WORD WAS:",r)
play()  


