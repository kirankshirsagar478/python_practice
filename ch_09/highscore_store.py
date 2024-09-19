import random

def game():
    print("You are playing the game")
    score = random.randint(1,100)
    with open("C:\\Users\\kiran\\OneDrive\\Desktop\\python new\\ch_09\\highscore.txt") as f:
        highscore = f.read()
        if (highscore !=""):
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"Your Score ={score}")
    if (score>highscore):
        with open("C:\\Users\\kiran\\OneDrive\\Desktop\\python new\\ch_09\\highscore.txt", "w") as f:
            f.write(str(score))
        return score
game()
