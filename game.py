import pygame
from sense_hat import SenseHat
from pygame.locals import *

# init hat sensor
sense = SenseHat()
sense.clear()

# init pygame library
pygame.init()
pygame.display.set_mode((640, 480))

# init colors
blue = (0, 123, 123) 
yellow = (255, 127, 0)

# player object
class Player:
    
    def __init__(self, id, color):
        self.id = id
        self.color = color
        
    def get_id(self):
        return self.id
    
    def get_color(self):
        return self.color

# init game manager
class ConnectFourGame():

  def __init__(self, xpos=0):
    # selector
    self.xpos = xpos
    # game board
    self.game_board = [
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    # players
    self.first_player = Player(1, blue)
    self.second_player = Player(2, yellow)
    self.current_player = self.first_player
    # game management
    self.running = True

  def stop(self):
    self.running = False
    print("end()")

  def get_current_player(self):
    return self.current_player

  def get_first_player(self):
    return self.first_player

  def get_second_player(self):
    return self.second_player

  def next_turn(self):
    self.current_player = (self.first_player, self.second_player)[self.current_player == self.first_player]

  def move_left(self):
    self.xpos -= 1

  def get_game_board_at(self, y, val):
    return self.game_board[y][val]

  def update_game_board(self, y_val, x_val):
    self.game_board[y_val][x_val] = self.current_player.get_id()

  def move_right(self):
    self.xpos+= 1

  def is_running(self):
    return self.running

  def get_x(self):
    return self.xpos
            
# check winning 
def check_win():
     
    # current game
    global game

    # horizontal check
    for y in [0,1,2,3,4,5,6,7]:
      for val in [0,1,2,3,4,5,6,7]:
            
        # check 
        if game.get_game_board_at(y,val) == game.get_current_player().get_id():
          count += 1
                
          if count >= 4:
            return True
                
        else:
          count = 0
                
    # vertical check
    for val in [0,1,2,3,4,5,6,7]:
      for y in [0,1,2,3,4,5,6,7]:
            
          # check 
          if game.get_game_board_at(y,val) == game.get_current_player().get_id():
            count += 1
                
            if count >= 4:
              return True
                
          else:
            count = 0
  
# on update
def update():

    # global game manager object
    global game

    current_player = game.get_current_player()
    x_val = game.get_x()

    # clear board
    sense.clear()
        
    # set the current pixel color on the first case
    sense.set_pixel(x_val, 0, current_player.get_color())
    
    # load game board saved values
    for y in [0,1,2,3,4,5,6,7]:
        for val in [0,1,2,3,4,5,6,7]:
            value = game.get_game_board_at(y, val)
            # if player 1
            if value == 1:
                sense.set_pixel(val, y, game.get_first_player().get_color())
            elif value == 2:
                sense.set_pixel(val, y, game.get_second_player().get_color())
                
# get highest y value
def get_highest_y():
  
    global game
    x_val = game.get_x()

    # for each value
    for y in [0,1,2,3,4,5,6,7]:
        if game.get_game_board_at(y, x_val) == 1 or game.get_game_board_at(y, x_val) == 2:
          return y - 1
    return 7
    
def init_game():
  
  global game
  
  print("C'est le tour du joueur ", game.get_current_player().get_id())
  sense.set_pixel(game.get_x(), 0,  game.get_current_player().get_color())
     
  # while game playing
  while game.is_running():
  
    # check key input
    for event in pygame.event.get():
          
        # on quit game event
        if event.type == QUIT:
            game.stop()
          
        # on joystick interaction
        elif event.type == KEYDOWN:
              
          # get current x selector value
          x_val = game.get_x()
  
          # get the highest value for x value
          y_val = get_highest_y()
                
          # on key interact
          if event.key == K_LEFT and x_val > 0:
            # go to left
            game.move_left()
            update()
          elif event.key == K_RIGHT and x_val < 7:
            # go to right
            game.move_right()
            update()
                    
          elif event.key == K_DOWN and y_val != -1:
            # go to down
            sense.clear()
            sense.set_pixel(x_val, y_val, game.get_current_player().get_color())
                    
            # register to list
            game.update_game_board(y_val, x_val)
                    
            # check win
            if check_win() == True:
              print("Victoire")
              sense.show_message("GG")
              game = ConnectFourGame()
              init_game()
            else:
              game.next_turn()
              update()


# init game
if __name__ == '__main__':
  game = ConnectFourGame()
  init_game()
