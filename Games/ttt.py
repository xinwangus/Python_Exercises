'''
Implement Game Tic-Tac-Toe
'''

class ttt:
    '''
    0: not played.
    1: Played as "X".
    -1: Played as "O".
    '''
    __two_d_array__ = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    __played__ = 0
    __current__ = 0
        
    def show_board(self):
        print("Current Board:")
        for row in range(len(self.__two_d_array__)):
            for col in range(len(self.__two_d_array__[row])):
                if self.__two_d_array__[row][col] == 0:
                    s = ' - '
                elif self.__two_d_array__[row][col] == -1:
                    s = ' O '
                elif self.__two_d_array__[row][col] == 1:
                    s = ' X '
                print(s, end='')
            print() # new line

    def check_winner(self):
        length = len(self.__two_d_array__)      
        # check row
        for r in range(length):
            if sum(self.__two_d_array__[r]) == 3 or \
               sum(self.__two_d_array__[r]) == -3:
                return True       
        # check colume
        for c in range(length):
            col_sum = 0
            for r in range(length):
                col_sum += self.__two_d_array__[r][c]
            if col_sum == 3 or \
               col_sum == -3:
                return True
        #check diag 1
        diag_sum = 0
        for r in range(length):
            diag_sum += self.__two_d_array__[r][r]
            if diag_sum == 3 or \
               diag_sum == -3:
                return True
        #check diag 2
        diag_sum = 0
        for r in range(length):
            diag_sum += self.__two_d_array__[r][length-r-1]
            if diag_sum == 3 or \
               diag_sum == -3:
                return True
        return False
          
    def play(self):
        while (self.__played__ < 9):
            if self.__current__ == 0:
                print("\nPlayer One to Play:")
            elif self.__current__ == 1:
                print("\nPlayer Two to Play:")
            self.show_board()
            r = -1
            c = -1
            while True:
                r_str = input("Position row 0-2: ")
                r = int(r_str)
                if r >= 0 and r <= 2:
                    break        
            while True:
                c_str = input("Position column 0-2: ")
                c = int(c_str)
                if c >= 0 and c <= 2:
                    break
            if self.__two_d_array__[r][c] != 0:
                print("This position already Played!")
                continue
            
            if self.__current__ == 0:
                self.__two_d_array__[r][c] = 1                   
            else:
                self.__two_d_array__[r][c] = -1
            self.__played__ += 1
            if (self.check_winner()):
                print("\nWon!")
                self.show_board()
                return True
            else:
                self.__current__ = (self.__current__ + 1) % 2
        print("\nNobody won!")
        self.show_board()
        return False
                          

if __name__ == '__main__':
    game = ttt()
    game.play()
        
            
