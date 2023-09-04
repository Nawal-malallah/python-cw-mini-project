# write your code here
def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20
    else:
        print("no choose indoor or outdoor")

def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100
    elif racket_brand == "Nox":
        return 140
    elif racket_brand == "Siux":
        return 200
    else:
        print("choose one bullpadel or nox or siux")

def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5
    else:
        print("our services offer boxes of 1 or 2 or 3 choose onw of these")

def padel_game_cost():
    Court = input("please select a court type indoor or outdoor   ")
    brand = input("select a racket brand of Bullpadle, Nox , Siux   ")
    balls = int(input("select a number of boxes 1, 2, 3  ")) 
    result = padel_court_cost(Court) + rackets_cost(brand) + padel_balls_cost(balls)
    return result

print(padel_game_cost())
