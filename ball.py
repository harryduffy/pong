class Ball():

    def __init__(self, x, y, color, screen_size):
        self.x = x
        self.y = y
        self.xVel = 10
        self.yVel = 10
        self.color = color
        self.screen_size = screen_size
        self.radius = 15

    def move(self, paddle_left, paddle_right):
        
        if self.check_collision(paddle_left, paddle_right):
            self.xVel *= -1

        if self.y == self.screen_size[1] or self.y == 0:
            self.yVel *= -1

        self.x += self.xVel
        self.y += self.yVel

    def check_collision(self, paddle_left, paddle_right):
        
        if (self.x == paddle_left.x + paddle_left.width) or (self.x == paddle_right.x - paddle_right.width):
            return True