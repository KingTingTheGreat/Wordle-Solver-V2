import time
from wordle_functions import *
from wordlegame import wordlegame
from wordlesolver import wordlesolver

def findAverage():
    """ finds the average number of moves for the wordlesolver to solve Wordle """
    start = time.time()
    total_num_guesses = 0
    num_answers_tried = 0
    fails = []
    for answer in getAllAnswers():
        num_answers_tried += 1

        x = wordlegame(answer)
        if x.game_loop_solver() == None:
            fails += [answer]
        total_num_guesses += x.move_num

    average = total_num_guesses / num_answers_tried
    print("average number of moves:", str(average))
    print("failed words: ")
    print(fails)
    end = time.time()
    print(end - start)


def useSolver():
    """ a function that allows a user to easily interact with a wordlesolver """
    solver = wordlesolver()
    while True:
        guess = solver.bestGuess()
        print("current guess:", guess)
        feedback = solver.getFeedback()
        solver.processFeedback(guess, feedback)
        if feedback == '11111':
            break

            
def playGame():
    """ allows the user to play this version of Wordle """
    game = wordlegame(None)
    game.game_loop_player()

    
# useSolver()
# playGame()
findAverage()
