import random
COLORS = {"black":"#000000", "white":"#FFFFFF",
            "red":"#FF0000", "green":"#00FF00",
            "blue":"#0000FF", "yellow":"#FFFF00",
            "orange":"#FFA500", "hendrixorange":"#F58025",
            "purple":"#9B30FF", "darkgray": "#A9A9A9"}

class Snake:
    def __init__(self, x , y , width, height, velx, vely, color, interface):
        self.width = width
        self.height = height
        self.x = x 
        self.y = y 
        self.color = color
        self.velx = velx
        self.vely = vely
        self.interface = interface
        
    def update(self):
        self.draw()
        self.boundary()
        
    def draw(self):
        fill(self.color)
        rect(self.x - 10, self.y - 10, 20, 20)
        
    def boundary(self):
        self.y += self.vely
        self.x += self.velx
        if self.x >= 1690 or self.x <= 120:
            self.velx *= -1
            self.interface.score_reduced()
        elif self.y >= 780 or self.y <= 160:
            self.vely *= -1
            self.interface.score_reduced()
        
    def move(self):
        self.turn()
        
    def turn(self):
         if keyPressed and key == "u":
            self.velx = 0
            self.vely = -1
            
         if keyPressed and key == "d":
            self.velx = 0
            self.vely = 1
            
         if keyPressed and key == "r":
            self.vely = 0
            self.velx = -1
            
         if keyPressed and key == "l":
            self.vely = 0
            self.velx = 1
        
    def colided(self, other):
        d = sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        if d < 20:
            return True
        else:
            return False
            
    def move_food(self):
        x, y = random_locations()
        self.x = x
        self.y = y

class snake_cells:
    def __init__(self, food, interface):
        x, y = random_locations()
        initial_snake = Snake(x, y, 20, 20, 0, 0, COLORS["blue"], interface)
        self.cells = [initial_snake]
        self.food = food
        self.interface = interface
        
    def add_head(self, other):
        self.cells.insert(0, other)
        
    def drop_tail(self):
        self.cells.pop()
    
    def draw(self):
        for i in self.cells:
            i.draw()
            
    def update(self):
        self.cells[0].move()
        self.draw()
        if self.cells[0].velx != 0 or self.cells[0].vely != 0:
            self.call_move()
            self.cells[0].boundary()
            if self.cells[0].colided(self.food)== True:
                self.cells.append(self.create_Snake_object(self.cells[0].x, self.cells[0].y - 20))
                self.food.move_food()
                self.interface.score_added()
                
    def create_Snake_object(self, x, y):
        new_snake_object = Snake(x, y, 20, 20, self.cells[0].velx, self.cells[0].vely, COLORS["blue"], self.interface)
        return new_snake_object
    
    def move_cells(self):
        if self.cells[0].vely < 0:
            new_cell = self.create_Snake_object(self.cells[0].x, self.cells[0].y - 20)
            return new_cell
        
        elif self.cells[0].vely > 0:
            new_cell = self.create_Snake_object(self.cells[0].x, self.cells[0].y + 20)
            return new_cell
        
        elif self.cells[0].velx < 0:
            new_cell = self.create_Snake_object(self.cells[0].x - 20, self.cells[0].y)
            return new_cell
        
        elif self.cells[0].velx > 0:
            new_cell = self.create_Snake_object(self.cells[0].x + 20, self.cells[0].y)
            return new_cell
                
    def call_move(self):
        self.add_head(self.move_cells())
        self.drop_tail()
        
    def destroy_snake(self):
        for i in range(len(self.cells), 1, -1):
            self.cells.pop()    
    
class Interface:
    def __init__(self, central_background):
        self.central_backg = central_background 
        self.level = None
        self.speed = 10
        self.level_selected = False
        self.game_quited = True
        self.score = 5
        self.check_hover_active = True
           
    def draw_header(self):
        fill(COLORS["hendrixorange"])
        rect(2, 2, 1796, 100)
        fill(COLORS["black"])
        line(590, 2, 590, 90)
        fill(COLORS["black"])
        line(1190, 2, 1190, 90)
        line(1490, 2, 1490, 90)
        fill(COLORS["black"])
        line(602, 31, 800, 31)
        line(602, 32, 800, 32)
        Algerian = createFont("Algerian", 45)
        textFont(Algerian)
        text('Scores :', 1500, 70)
        fill(COLORS["white"])
        text(str(self.score), 1700, 70)
        fill(COLORS["black"])
        line(1212, 30, 1472, 30)
        line(1212, 32, 1472, 32)
        Algerian = createFont("Algerian", 32)
        textFont(Algerian)
        fill(COLORS["black"])
        text(str(self.level), 1212, 70)
        # Central frame
        fill(self.central_backg)
        rect(100, 150, 1600, 650)
    
    def draw_margin(self):
        fill(COLORS["black"])
        line(2, 2, 1798, 2)
        line(2, 2, 2, 898)
        line(1798, 2, 1798, 898)
        line(2, 898, 1798, 898)
        
    def draw_footer_line(self):
        fill(COLORS["red"])
        line(3, 860, 1797, 860)
        
    def play_game(self):
        if mousePressed and self.check_hover() == True:
            self.level_selected = True
            self.game_quited = False
            self.central_backg = COLORS["black"]
            self.chek_hover_active = False    
            
    def replay_game(self):
        if (keyPressed and key == "q") or (keyPressed and key == "p"):
            self.score = 5
            self.central_backg = COLORS["darkgray"]
            self.level_selected = False
 
    def game_stoped(self):   
        if self.score == 0:     
            self.level_selected = False
            self.display_failing_message()
            self.display_replay_or_close_game()
            
        elif self.score == 100:
            self.level_selected = False
            self.display_wining_message()
            self.display_replay_or_close_game()

    def display_wining_message(self):
        fill(COLORS["white"])
        courier = createFont("Courier", 40)
        textFont(courier)
        text('Congratulations!!!! You won the game with ' + str(self.score) + ' Scores' , 300, 450)
        
    def display_failing_message(self):
        fill(COLORS["white"])
        courier = createFont("Courier", 40)
        textFont(courier)
        text('Sorry!!! You lost the game with ' + str(self.score) + ' Scores' , 400, 450)
        
    def display_replay_or_close_game(self):
        fill(COLORS["white"])
        courier = createFont("Courier", 20)
        textFont(courier)
        text('Press "P" button to replay the game ', 400, 500)
        text('Click on the upper right coner close button to close the game window ', 400, 520)
        
    def check_hover(self):
        if self.check_hover_active: 
            if (700 <= mouseX <= 940) and (360 <= mouseY <= 380): 
                line(700, 380, 940, 380)
                line(700, 382, 940, 382)
                if self.level_selected and self.game_quited == False:
                    self.level = "Low"
                    self.speed = 10
                return True
            elif (700 <= mouseX <= 980) and (380 <= mouseY <= 420):
                line(700, 410, 980, 410)
                line(700, 412, 980, 412)
                if self.level_selected and self.game_quited == False:
                    self.level = "Medium"
                    self.speed = 20
                return True
            elif (700 <= mouseX <= 960) and (420 <= mouseY <= 460):
                line(700, 440, 950, 440)
                line(700, 442, 950, 442)
                if self.level_selected and self.game_quited == False:
                    self.level = "High"
                    self.speed = 40
                return True
            else:
                return False
        
    def score_added(self):
        self.score += 5
            
    def score_reduced(self):
        self.score -= 5    

def header_content(interface):
    Algerian = createFont("Algerian", 32)
    textFont(Algerian)
    fill(COLORS["black"])
    text("Game Rules", 602, 30)
    Algerian = createFont("Algerian", 20)
    textFont(Algerian)
    text('Press "U" for Up', 602, 60)
    text('Press "D" for Down', 602, 90)
    text('Press "R" for Right', 870, 60)
    text('Press "L" for Left', 870, 90)
    #selected_level part
    Algerian = createFont("Algerian", 32)
    textFont(Algerian)
    fill(COLORS["black"])
    text("Selected Level", 1212, 30)
    text('Press "Q" button to quit!', 600, 850)
    
def footer_content(interface):
    interface.draw_footer_line()
    interface.draw_margin()
    courier = createFont("Courier", 20)
    textFont(courier)
    fill(COLORS["black"])
    text("All rights are reserved| Innocent Nsabimana| Hendrix College CS 150 ", 400, 890)
    
def body_content(interface):
    fill(COLORS["black"])
    Algerian = createFont("Algerian", 50)
    textFont(Algerian)
    text('Select Level', 700, 350)
    Algerian = createFont("Algerian", 30)
    textFont(Algerian)
    text('1.  Low Level', 700, 380)
    text('2.  Medium Level', 700, 410)
    text('3.  High Level', 700, 440) 
    
def random_locations():
    x = random.randint(140, 1570)
    y = random.randint(180, 620)
    return x, y

def restart_game():
    if interface.level_selected == False:
        body_content(interface)
        interface.check_hover_active = True
        x, y = random_locations()
        snake_with_cells.cells[0].x = x
        snake_with_cells.cells[0].y = y
        snake_with_cells.cells[0].velx = 0
        snake_with_cells.cells[0].vely = 0
        snake_with_cells.destroy_snake()
        x, y = random_locations()
        snake_with_cells.food.x = x
        snake_with_cells.food.y = y
    else:
        interface.check_hover_active = False

list_of_components = []
interface = None
img = None
snake_with_cells = None

def setup():
    size(1800, 900)
    global interface, img, snake_with_cells
    interface = Interface(COLORS["darkgray"])
    img = loadImage("snake.jpg")
    x, y = random_locations()
    food = Snake(x, y , 20, 20, 0, 0, COLORS["red"], interface)
    list_of_components.append(food)
    snake_with_cells = snake_cells(food, interface)
    list_of_components.append(snake_with_cells)
    frameRate(int(interface.speed))
    
def draw():
    global img, snake_with_cells
    background(COLORS["darkgray"])
    interface.draw_header()
    interface.check_hover()
    image(img, 2, 2, 400, 100)
    header_content(interface)
    restart_game() 
    footer_content(interface)
    frameRate(int(interface.speed))
    interface.play_game()
    interface.replay_game()
    interface.game_stoped()
    if interface.level_selected == True:
        for component in list_of_components:
            component.update()

    
    


    