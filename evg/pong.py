from pygame import *

win_width = 700
win_hight = 500
window = display.set_mode((win_width,win_hight))
display.set_caption("Ping-Pong")


run = True
finish = False




class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    # метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y<win_hight-80:
            self.rect.y +=self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y<win_hight-80:
            self.rect.y +=self.speed

racket1=Player("racket.png",30,200,10,50,10)
racket2=Player("racket.png",win_width-30,200,10,50,10)
ball = GameSprite("tenis_ball.png",200,200,50,50,4)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish!= True:
        window.fill((150,100,175))
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()   
    time.delay(50)         