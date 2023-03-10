
import turtle, random
SCALE = 25 #Controls how many pixels wide each grid square is


class Game:
    '''
Purpose: 
    The Game class draws the board and calls different turtle functions
    that ensure that the turtle graphics runs at its fastest possible
Instance variables: 
    occupied: a list of lists representing all grids in the 10X20 canvas
    cv: represents the canvas object
    self.active: represents active block
Methods:
    gameloop: is to ensure to routinely create a new block in a certain time frame.
    move_left: move current active block to the left by one grid every click if it is valid to do so.
    move_right: move current active block to the right by one grid every click if it is valid to do so.
'''
    def __init__(self):       
        self.occupied = []
        for i in range (20):
                self.occupied.append([0,0,0,0,0,0,0,0,0,0])
                    
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)

        self.active = Block()
        turtle.ontimer(self.gameloop, 300) 
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        
        turtle.update()
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        if self.active.valid(0, -1,  self.occupied):
            self.active.move(0, -1)
            turtle.ontimer(self.gameloop, 300)
            turtle.update()
        else:
        # Call new active block in case invalid returns False
            for s in self.active.squares:
                # print (s.xcor(), ' ', s.ycor())
                # print ('occupied: ', self.occupied[s.ycor()][s.xcor()])
                if self.occupied[s.ycor()][s.xcor()] == 0:
                    self.occupied[s.ycor()][s.xcor()] += 1
                    self.active.move(0, 0)
            turtle.update()
            self.active = Block()
            turtle.ontimer(self.gameloop, 300) 
    
    def move_left(self):
        if self.active.valid(-1, 0, self.occupied):
            self.active.move(-1, 0)
        turtle.update()
    
    def move_right(self):
        if self.active.valid(1, 0, self.occupied):
            self.active.move(1, 0)
        turtle.update()

class Square(turtle.Turtle):
    '''
    Purpose: 
        Each square object represents one colored square in the grid.
        The Square class inherits from turtle.Turtle in order to use 'move'  method or other turtle methods.
    Instance variables: 
        x,y: represent the coordinates where the square should be created
        color: represnts the color each square should be created with


    Methods: 
        __init__ : makes calls for its base class, turtle.Turtle, to draw square objects
        '''
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.penup()
        self.goto(x,y)
        self.pendown()
        self.shape('square')
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(color)
        self.pencolor('gray')
        self.penup()
	
class Block:
    '''
    Purpose: 
        each block object represent a block, an array, which consists of 4 squares
    Instance variables: 
    Methods: 
        move : moves each square to a new location
        valid: checks if certain condition is met to validate moving squares or create new block
        __init__: creates block shape randomly based on 7 predefined shapes
        '''
    def __init__(self):
        self.squares = []
        random_block = random.randint(1,7)
        match random_block:
            case 1: # i shape
                self.squares.append(Square(3,21,'cyan'))
                self.squares.append(Square(4,21,'cyan'))
                self.squares.append(Square(5,21,'cyan'))
                self.squares.append(Square(6,21,'cyan'))
            case 2: # right L shape
                self.squares.append(Square(3,20,'cyan'))
                self.squares.append(Square(3,21,'cyan'))
                self.squares.append(Square(4,21,'cyan'))
                self.squares.append(Square(5,21,'cyan'))
            case 3: # left L shape
                self.squares.append(Square(3,21,'cyan'))
                self.squares.append(Square(4,21,'cyan'))
                self.squares.append(Square(5,20,'cyan'))
                self.squares.append(Square(5,21,'cyan'))
            case 4: # cubic shape
                self.squares.append(Square(3,20,'cyan'))
                self.squares.append(Square(3,21,'cyan'))
                self.squares.append(Square(4,20,'cyan'))
                self.squares.append(Square(4,21,'cyan'))
            case 5: # left s shape
                self.squares.append(Square(3,21,'cyan'))
                self.squares.append(Square(4,20,'cyan'))
                self.squares.append(Square(4,21,'cyan'))
                self.squares.append(Square(5,20,'cyan'))
            case 6: # right s shape
                self.squares.append(Square(3,20,'cyan'))
                self.squares.append(Square(4,20,'cyan'))
                self.squares.append(Square(4,21,'cyan'))
                self.squares.append(Square(5,21,'cyan'))
            case 7: # up side down t shape
                self.squares.append(Square(3,21,'cyan'))
                self.squares.append(Square(4,20,'cyan'))
                self.squares.append(Square(4,21,'cyan'))
                self.squares.append(Square(5,21,'cyan'))
            case _:
                return None
        
    def move(self, dx, dy):
        for s in self.squares:
            x = s.xcor() + dx
            y = s.ycor() + dy
            s.goto(x, y)
    def valid(self, dx, dy, occ):
        for s in self.squares:
            x = s.xcor() + dx
            y = s.ycor() + dy
            if x < 0 or x>9 or y < 0:
                return False
            if y <=19 and occ[y][x] == 1:
                return False
                return False
        return True
    

if __name__ == '__main__':
    Game()