import random
words_list=[]
with open("datasets/five_let_words.txt","r") as f:
    for line in f:
        words_list.append(line.strip())
print("="*50)
print(f"{'Welcome to Wordle!':^50}")
print("="*50)

sec_word = random.choice(words_list).lower().strip()

attempts=6
win=0

def check_word(user_word_dict,sec_word_dict):
    feed_list=["Gray"]*5
    for i,(letter,trfa) in user_word_dict.items():
        if (letter == sec_word_dict[i][0]):
            feed_list[i]="Green"
            sec_word_dict[i][1]=1
    

    for i,(letter,trfa) in user_word_dict.items():
            for idx,(let_sec,trfa_sec) in sec_word_dict.items():
                if feed_list[i]!="Green":
                    # print(feed_list,sec_word_dict,let_sec)
                    if (letter==let_sec) and trfa_sec==0:
                            sec_word_dict[idx][1]=1
                            feed_list[i]="Yellow"
                            break


    return feed_list


while attempts>0:
    user_word=input("Enter a 5 letter word: ").lower()
    
    user_word_dict = {i: [ch, 0] for i, ch in enumerate(user_word)}
    sec_word_dict = {i: [ch, 0] for i, ch in enumerate(sec_word)}
    # print(user_word_dict)
    # print(sec_word_dict)
    if len(user_word)!=5:
        print("Please enter a valid 5 letter word")
        print("-"*50)
        continue
    else:
        if user_word==sec_word:
            print("="*50)
            print("Congratulations! You guessed the word correctly.")
            print("="*50)
            win=1
            break
        else:
            feedb=check_word(user_word_dict,sec_word_dict)
            print("Wrong Guess!")
            print("Feedback:")
            for i in range(5):
                 print(f"{user_word[i]}:{feedb[i]}",end=" ")
            attempts-=1
            print(f"\nYou have {attempts} attempts left.")

    print("-"*50)

if win==0:
        print(f"Sorry, you've used all your attempts.\nThe correct word was '{sec_word}'.")
        print("="*50)
