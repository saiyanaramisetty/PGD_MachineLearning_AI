from gym import spaces
import numpy as np
import random
from itertools import groupby
from itertools import product



class TicTacToe():

    def __init__(self):
        """initialising the board"""
        
        # initialise state as an array
        self.state = [np.nan for _ in range(9)]  # initialises the board position, can initialise to an array or matrix
        # all possible numbers
        self.all_possible_numbers = [i for i in range(1, len(self.state) + 1)] # , can initialise to an array or matrix
        
        self.reset()


    def is_winning(self, curr_state):
        """Takes state as an input and returns whether any row, column or diagonal has winning sum
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        Output = False"""
        
        rowIndexes = [(0,1,2), (3,4,5), (6,7,8)]
        colIndexes = [(0,3,6), (1,4,7), (2,5,8)]
        diagonalIndexes = [(0,4,8), (2,4,6)]
        
        # Row check - If sum of the rows is equal to 15
        if(self.get_count(rowIndexes, curr_state)):
            return True
        
        # Column check - If sum of the columns is equal to 15
        if(self.get_count(colIndexes, curr_state)):
            return True
        
        # Diagonal check - If sum of the diagonals is equal to 15
        if(self.get_count(diagonalIndexes, curr_state)):
            return True
            
        return False
    
    
    
    def get_count(self, indexesList, values):
        """Takes indexes values to add up the values to check if the total is equal to 15"""
        for i in range(0, len(indexesList)):
            x, y, z = indexesList[i]
            if(not np.isnan(values[x]) and not np.isnan(values[y]) and not np.isnan(values[z])):
                if(values[x] + values[y] + values[z]):
                    return True
        
     

    def is_terminal(self, curr_state):
        # Terminal state could be winning state or when the board is filled up
        if self.is_winning(curr_state) == True:
            return True, 'Win'

        elif len(self.allowed_positions(curr_state)) ==0:
            return True, 'Tie'

        else:
            return False, 'Resume'



    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]


    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""
        used_values = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 !=0]
        env_values = [val for val in self.all_possible_numbers if val not in used_values and val % 2 ==0]
        return (agent_values, env_values)


    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions, i.e, all combinations of allowed positions and allowed values"""

        agent_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0])
        env_actions = product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1])
        return (agent_actions, env_actions)




    def state_transition(self, curr_state, curr_action):
        
        """Takes current state and action and returns the board position just after agent's move.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]
        """
        
        curr_state[curr_action[0]] = curr_action[1]
        return curr_state


    def step(self, curr_state, curr_action):
        
        
        """Takes current state and action and returns the next state, reward and whether the state is terminal. Hint: First, check the board position after
        agent's move, whether the game is won/loss/tied. Then incorporate environment's move and again check the board status.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [7, 9] or [position, value]
        Output = ([1, 2, 3, 4, nan, nan, nan, 9, nan], -1, False)"""
        
        is_terminal_finalState = False
        
        newCurrentState = self.state_transition(curr_state, curr_action)
        
        is_terminal_finalState, is_terminal_status = self.is_terminal(newCurrentState)
        
        if is_terminal_finalState == True:
            if is_terminal_status == "Win":
                # Agent Wins the game
                reward = 10
            else:
                # More steps to play
                reward = 0
        else:
            allowedPosition = random.choice(self.allowed_positions(newCurrentState))
            allowedValue = random.choice(self.allowed_values(newCurrentState)[1])
            newCurrentState[allowedPosition] = allowedValue
            
            is_terminal_finalState, is_terminal_status = self.is_terminal(newCurrentState)
            if is_terminal_finalState == True:
                if is_terminal_status == "Win":
                    # Environment Wins the game
                    reward = -10
                else:
                    # More steps to play
                    reward = 0
            else:
                # Deducting reward for using more steps
                reward = -1
                
        return newCurrentState, reward, is_terminal_finalState

    def reset(self):
        return self.state
