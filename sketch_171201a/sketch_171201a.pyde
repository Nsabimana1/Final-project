add_library("sound")

counter = 0
img = None
x = 0
hs = None
justPressed = False

class HoverableSquare:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y
        
    def draw(self):
        if self.x <= mouseX <= self.x + self.size and self.y <= mouseY <= self.y + self.size:
            fill(255, 0, 255)
        else:
            fill(0, 255, 0)
        rect(self.x, self.y, self.size, self.size)
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

def setup():
    global img, sf, hs
    size(640, 480)
    frameRate(120)
    img = loadImage("mandolin.jpg")
    sf = SoundFile(this,"Kurzweil-K2000-Grand-Strings-C3.wav")
    hs = HoverableSquare(200, 400, 50)
    
def draw():
    global counter, x, img, justPressed
    background("#FFFFFF")
    counter += 1
    courier = createFont("Courier", 32)
    textFont(courier)
    fill(255, 0, 0)
    text("Hello " + str(counter), 100, 75)
    
    text("Object", x, 200)
    x += 1
    
    image(img, 0, 0, 100, 100)
    
    hs.draw()
    
    if justPressed:
        if key == 'w':
            hs.move(0, -1)
        elif key == 'a':
            hs.move(-1, 0)
        elif key == 's':
            hs.move(0, 1)
        elif key == 'd':
            hs.move(1, 0)
        justPressed = False
        
def keyPressed():
    global justPressed
    justPressed = True
    
def mouseClicked():
    # Play sound when mouse clicked on canvas.
    sf.play()
    
    