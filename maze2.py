from pygame import *
'''Kelas wajib'''




#kelas induk untuk sprite
class GameSprite(sprite.Sprite):
   #konstruktor kelas
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # setiap sprite harus menyimpan properti image - gambar
       self.image = transform.scale(image.load(player_image), (80, 80))
       self.speed = player_speed
       # setiap sprite harus menyimpan properti rect - persegi panjang di mana sprite tersebut dituliskan
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

#kelas penerus untuk sprite musuh (bergerak sendiri)
class Enemy(GameSprite):
   direction = "left"
   def update(self):
       if self.rect.x <= 470:
           self.direction = "right"
       if self.rect.x >= win_width - 85:
           self.direction = "left"
       if self.direction == "left":
           self.rect.x -= self.speed
       else:
           self.rect.x += self.speed


#adegan permainan
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))


#karakter permainan
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

game = True
finish = False
clock = time.Clock()
FPS = 60

#musik
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

    display.update()
    clock.tick(FPS)