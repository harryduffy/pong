class Paddle():

    def __init__(self, x, y, screen_size):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 125
        self.vel = 20
        self.screen_size = screen_size

    def move_up(self):
        
        if self.y > 0:
            self.y -= self.vel

    def move_down(self):

        if self.y < self.screen_size[1] - self.height:
            self.y += self.vel