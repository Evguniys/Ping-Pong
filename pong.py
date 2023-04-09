from pygame import *

win_width = 700
win_hight = 500
window = display.set_mode((win_width,win_hight))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("234.jpg"),(win_width,win_hight))
font.init()
font2 = font.SysFont(None,36)
font3 = font.SysFont(None,100)


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

racket1=Player("racket.png",30,200,20,100,15)
racket2=Player("racket.png",win_width-30,200,20,100,15)
ball = GameSprite("tenis_ball.png",200,200,50,50,4)


speed_x = 15
speed_y = 15
point1 = 0
point2 = 0

lose1 = font3.render("Player 1 lose!",True,(255,0,0))
lose2 = font3.render("Player 2 lose!",True,(255,0,0))
poin1 = font2.render("Player 1 points:"+ str(point1),True,(255,165,0))
poin2 = font2.render("Player 2 points:"+ str(point2),True,(255,165,0))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish!= True:
        window.blit(background,(0,0))
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        ball.rect.x +=speed_x
        ball.rect.y +=speed_y
        if ball.rect.y > win_hight-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
        if ball.rect.x > win_width-50:
            point1+=1
            speed_x *= -1
            poin1 = font2.render("Player 1 points:"+ str(point1),True,(255,165,0))
        if ball.rect.x < 0:
            point2+=1
            speed_x *= -1
            poin2 = font2.render("Player 2 points:"+ str(point2),True,(255,165,0))
        if point1==5:
            finish=True
            ball.rect.x = win_width/2
            ball.rect.y = win_hight/2
            window.blit(lose2,(200,200))
        if point2==5:
            finish=True
            ball.rect.x = win_width/2
            ball.rect.y = win_hight/2
            window.blit(lose1,(200,200))
        ball.reset()
        window.blit(poin1,(10,10))
        window.blit(poin2,(500,10))
    display.update()   
    time.delay(50)         