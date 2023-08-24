import pygame
import math

class playerBullet:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.position = (x,y)
        self.speed = 2
        self.rotation = 0
        self.scale = (10,10)
        self.image = pygame.image.load('E:/github_projects/mazeGame/assest/player_bullet.png')
        self.image = pygame.transform.scale(self.image,self.scale)
        self.sprite = self.image
        self.isDeleted = False
        self.followPos = None

    def draw(self,window):
        window.blit(self.image,(self.x,self.y))
    
    def delete(self):
        self.isDeleted = True

    def move_toward(self,object):
        x_dif = object.x - self.x
        y_dif = object.y - self.y
        dis = math.sqrt(x_dif**2+y_dif**2)
        if dis!=0:
            x_dif /= dis
            y_dif /= dis
        self.x += x_dif*self.speed
        self.y += y_dif*self.speed
    
    def move_toward_pos(self):
        x_dif = self.followPos[0] - self.x
        y_dif = self.followPos[1] - self.y
        dis = math.sqrt(x_dif**2+y_dif**2)
        if dis>0:
            nor_x = x_dif / dis
            nor_y = y_dif / dis
            self.x += nor_x*self.speed
            self.y += nor_y*self.speed
    
    def is_outside_border(self,border_x,border_y):
        if self.x < 0 or self.y < 0:
            return True
        elif self.x+5 > border_x or self.y+5 > border_y:
            return True
        else:
            return False

if __name__ == "__main__":
    print("open game.py to execute")