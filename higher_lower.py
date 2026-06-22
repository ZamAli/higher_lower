import random
from game_data import data
from art import logo, vs

def answer(A, B):
    if A['follower_count'] > B['follower_count']:
        res = A['name']
    else:
        res = B['name']
    return res

def continue_play(opponentB):
    opponentA = opponentB
    print (f"A: {opponentA['name']}, a {opponentA['description']}, from {opponentA['country']}")
    opponentB = random.choice(data)
    while opponentA == opponentB:
        opponentB = random.choice(data)
    print (vs)
    print (f"B: {opponentB['name']}, a {opponentB['description']}, from {opponentB['country']}")
    result = answer(opponentA, opponentB)
    return opponentA, opponentB, result


def play():
    opponentA = random.choice(data)
    print (logo)
    print(f"A: {opponentA['name']}, a {opponentA['description']}, from {opponentA['country']}")
    opponentB = random.choice(data)
    while opponentA == opponentB:
        opponentB = random.choice(data)
    print (vs)
    print(f"B: {opponentB['name']}, a {opponentB['description']}, from {opponentB['country']}")
    game_over = True
    score = 0
    result = answer(opponentA, opponentB)
    while game_over:
        user_input = input("who has more followers? A or B?: ")
        if user_input == 'A' and result == opponentA['name']:
            score +=1
            print (f"correct answer, your score is {score}")
            opponentA, opponentB, result = continue_play(opponentB)
        elif user_input == 'B' and result == opponentB['name']:
            score += 1
            print(f"correct answer, your score is {score}")
            opponentA, opponentB, result = continue_play(opponentB)
        else:
            print(f"wrong answer, your score is {score}")
            game_over = False


play()
