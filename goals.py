def setGoals():
    goal = input('What is your goal? ')
    goal_file = open(goal + '.txt', 'w+')

    getInput(goal_file, 'specific subgoal')
    getInput(goal_file, 'measure of success')
    getInput(goal_file, 'way of making sure this is achievable')
    getInput(goal_file, 'way of making sure this is realistic')
    getInput(goal_file, 'timeline for this goal')

def getInput(goal_file, goal_string):
    while True:
        subgoal = input('What is your ' + goal_string + ' (Enter \'n\' to exit)? ')
        if(subgoal == 'n'):
            break
        goal_file.write('My ' + goal_string + ' is ' + subgoal + '\n')
