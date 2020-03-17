#mim max algorithm to solve tictactoe
#Author Vinicius Franca

#https://www.geeksforgeeks.org/python-gui-tkinter/
#http://www.codekraft.co/freecodecamp/jogo-da-velha-entendendo-o-algoritimo-minimax/
import random

class Game:
    def __init__(self, mode):
        self.state = [[]]
        self.mode = mode
        self.player = True #true for p1 and false for p3
        self.choices = []

    def start(self):
        self.state = [[-1 for i in range(0, 3)] for c in range(0, 3)]
        self.pass_turn()

    def show(self):
        for l in self.state:
            print(l)
        
        print('')

    def pass_turn(self):
        result = self.winner(self.state)
        if result[0]:
            print('*************************')
            print('The Game is over')
            print('The Winner is Player {}'.format(result[1]))
            self.show()
            print('*************************')
            return 

        if (mode == 1) & self.player:
            l = input('\n*Insira a linha 1 a 3: ')
            c = input('\n*Insira a coluna 1 a 3: ')
            self.state[l-1][c-1] = 1
        
        self.show()
        self.minmax_decision()
        
    def minmax_decision(self):
        self.generate_states(self.state, self.player, 0)
        choice = random.randint(0, len(self.choices))
        self.state = self.choices[choice]
        self.choices = []
        self.player = not self.player
        self.show()
        self.pass_turn()

    def winner(self, state):
        # result linha
        for l in state:
            found = (l[0] == l[1] == l[2]) & (l[0] != -1)
            if found: 
                return found, l[0]

        # result column
        for l in range(len(state)):
            found = (state[l][0] == state[l][1] == state[l][2]) & (state[l][0] != -1)
            if found:
                return found, state[l][0]

        # result diagonal
        found = (state[0][0] == state[1][1] == state[2][2]) & (state[0][0] != -1)
        if found:
            return found, state[0][0]
        found = (state[0][2] == state[1][1] == state[2][0]) & (state[0][2] != -1)
        if found:
            return found, state[0][2]

        # not found
        return False, -1

    def generate_states(self, state, player, height):
        value = False
        for l in range(len(state)):
            for c in range(len(state)):
                if state[l][c] == -1:
                    temp_state = state
                    temp_state[l][c] = player & 1 | 0
                    value = self.generate_states(temp_state, not player, height+1)
                    print(value)

                    # alterar
                    if player & (value==10) & height==0:
                        self.choices.append(state)
                    elif (not player) & (value==-10) & height==0:
                        self.choices.append(state) 
                    elif value==0 & height==0:
                        self.choices.append(state)
                    return value

        result = self.winner(state)
        if result[0] & result[1]==0:
            return -10
        elif result[0] & result[1]==1:
            return 10
        else:
            return 0

        

if __name__ == "__main__":

    mode = input("Choose the game mode:\n"+
        "Player vs Machine(1) or  Machine vs Machine(0)")

    game = Game(mode)
    game.start()