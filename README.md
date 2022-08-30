# Wordle-Solver-V2
uses an almost identical technique as my original Wordle-Solver but this code is much cleaner and easier to read

Position-based Wordle Solver -never fails for all 2000+ possible answers -average of 3.62 moves

How the Guess is Determined: -a list of list for each letter in the alphabet and each position in a five-letter word is created [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], ...] -an integer is increased by 1 for each possible answer left that has the corresponding letter in the corresponding position *the first guess 'slate' is determined by this method. since no information is known at the start of the game, the first guess is always slate. to prevent it from having the calculate this each time, an if statement is included to set the guess to 'slate' when all the possible answers are still left -if only similar answers are left, it guesses a word using the letters they don't have in common ex. for the answer: 'shall' after 'slate', the only answers left are 'scald', 'scalp', 'scaly', 'shall', 'shawl', 'small', 'snail', and 'snarl' the next guess it outputs is 'child' the feedback from this allows the solver to eliminate all words other than 'shall', getting the answer in 3 moves

User inputs feedback from the game via a 5-number String of 0s, 1s, and 2s 0s represent gray letters (not in the word) 1s represent green letters (correct letters in the correct position) 2s represent yellow letters (correct letters in the wrong position)

the only functions the user needs are in the wordle_interacts.py file 
these functions allows the user to use the solver, play this version of Wordle, and tests the solver to find it's average number of guesses and find the words it fails on
