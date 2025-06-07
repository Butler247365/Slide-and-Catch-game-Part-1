import pygame, simpleGE, random

class Ball (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Ball2.jpg")
        self.setSize(25,25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        
class Basketball(simpleGE.Sprite):
    def __init__(self, scene): 
        super().__init__(scene)
        self.setImage("hoop1.jpg")
        self.setSize(50, 50) 
        self.position = (320, 400) 
        self.moveSpeed = 5

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT): 
            self.x += self.moveSpeed
    

class Game(simpleGE.Scene):
    def __init__(self): 
        super().__init__() 
        self.setImage("court2.jpg")
        
        self.sndBall = simpleGE.Sound("swish.wav")
        self.numBalls = 10

        self.basketball = Basketball(self)
        
        self.balls= []
        for i in range(self.numBalls):
            self.balls.append(Ball(self))
            
        self.sprites = [self.basketball,
                        self.balls]
        
    def process(self):
        for ball in self.balls:
            if ball.collidesWith(self.basketball):
               ball.reset()
               self.sndBall.play()
               
def main(): 
    game = Game() 
    game.start()

if __name__ == "__main__":
    main()