from tkinter import *
import tkinter.messagebox
from Domain import Board


class GUI:
    
    def __init__(self, game):
        self.game = game
        
        self.app = Tk()
        self.app.title('Connect Four')
        self.app.geometry('600x600')
        
        self.game_over = False
        
        self.buttons = {}
        self.table = [[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7]
        self.message = {1:'You lost', -1:'You won', 0:"It's a tie"}
        
        for column in range(0,7):
            handler = lambda column=column: self.move(column) 
            button = Button(self.app, text=column+1, command=handler, width=10, height=5)
            button.grid(row=0, column=column)
            self.buttons[column] = button 
            
        for line in range(0,6):
            for column in range(0,7):
                label = Label(self.app, width=10, height=5, bg="white", relief='groove')
                label.grid(row=line+1, column=column)
                self.table[line][column] = label
        
        
        self.reset_button = Button(self.app, text='Reset', command=self.reset_game)
        self.reset_button.grid(row=8, column=3)
                
                
    def reset_game(self):
        self.game.reset()
        for line in range(6):
            for column in range(7):
                self.table[line][column].configure(bg='white')
                

    def update(self, line,column, color):
        self.table[line][column].configure(bg=color)
                
        
    def move(self, column):
        try:
            line = self.game.get_open_spot(column)
            self.update(line,column, 'red')
            self.game.player_move(column)
        except Exception:
            tkinter.messagebox.showinfo('Error', 'Column is full') 
               
        self.game_over, self.result = self.game.check_game_over()
        if self.game_over == True:
            tkinter.messagebox.showinfo("Game Over", self.message[self.result])
            
        else:
            self.computer_move()
            
    def computer_move(self):
        column = self.game.get_computer_move()
        line = self.game.get_open_spot(column)
        self.update(line,column, 'black') 
        self.game.computer_move(column)
        
        self.game_over, self.result = self.game.check_game_over()
        if self.game_over == True:
            tkinter.messagebox.showinfo("Game Over", self.message[self.result])
            
    
    def start(self):
        self.app.mainloop()    
        