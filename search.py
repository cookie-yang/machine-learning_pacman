"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stateStack = util.Stack()
    stateStack.push(problem.getStartState())
    exploredList = []
    actionStack = []
    while not stateStack.isEmpty():
                tmpState = stateStack.pop()
                exploredList.append(tmpState)
                if problem.isGoalState(tmpState) == False:
                    successors = problem.getSuccessors(tmpState)
                    if len(successors) > 0:
                        actionList = actionStack.pop() if len(actionStack)>0 else []
                        for x in successors:
                            if x[0] not in exploredList:
                                stateStack.push(x[0])
                                actionStack.append(actionList+[x[1]])
                    else:
                        actionStack.pop()
                else:
                    return actionStack.pop()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    stateQueue = util.Queue()
    stateQueue.push(problem.getStartState())
    exploredList = []
    actionQueue = util.Queue()
    while not stateQueue.isEmpty():
                tmpState = stateQueue.pop()
                if tmpState not in exploredList:
                    exploredList.append(tmpState)
                    if problem.isGoalState(tmpState) == False:
                        successors = problem.getSuccessors(tmpState)
                    # print(successors)
                        if len(successors) > 0:
                            actionList = [] if actionQueue.isEmpty() else actionQueue.pop()
                        # print(actionList)
                            for x in successors:
                                    stateQueue.push(x[0])
                                    actionList.append(x[1])
                                    actionQueue.push(actionList[:])
                                    actionList.pop()
                        else:
                            actionQueue.pop()
                    else:
                        return actionQueue.pop()
                else:
                     actionQueue.pop()
           

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    stateCost_Queue = util.PriorityQueue() 
    stateCost_Queue.push((problem.getStartState(),[]),0)
    exploredList = []
    while not stateCost_Queue.isEmpty():
            item = stateCost_Queue.pop() #item includes state(x,y), actionList from root to this state, and total cost
            if item[0] not in exploredList:
                exploredList.append(item[0])
                if problem.isGoalState(item[0]) == False:
                    successors = problem.getSuccessors(item[0])
                    if len(successors) > 0:
                        for x in successors:
                                item[1].append(x[1])
                                actionList = item[1][:]
                                item[1].pop()
                                stateCost_Queue.push((x[0],actionList),problem.getCostOfActions(actionList))
                else:
                    return item[1]
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    stateCost_Queue = util.PriorityQueue()
    stateCost_Queue.push((problem.getStartState(),[]),heuristic(problem.getStartState(),problem))
    exploredList = []
    while not stateCost_Queue.isEmpty():
            # item includes state(x,y), actionList from root to this state, and
            # total cost
            item = stateCost_Queue.pop()
            if item[0] not in exploredList:
                exploredList.append((item[0]))
                if problem.isGoalState(item[0]) == False:
                    successors = problem.getSuccessors(item[0])
                    if len(successors) > 0:
                        for x in successors:
                                item[1].append(x[1])
                                actionList = item[1][:]
                                item[1].pop()
                                totalCost = problem.getCostOfActions(actionList)+heuristic(x[0],problem)
                                stateCost_Queue.push((x[0], actionList), totalCost)
                else:
                    return item[1]

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
