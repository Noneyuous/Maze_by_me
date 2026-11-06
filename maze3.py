from pygame import*
window = display.set_mode((700, 500))
display.set_caption('Maze')

bg = transform.scale(image.load('background.jpg'), (700, 500))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.arah = 'right'
    
    def update(self):
        if self.arah == 'right':
            self.rect.x += self.speed
        if self.arah == 'left':
            self.rect.x -= self.speed
        if self.rect.x > 615:
            self.arah = 'left'
        if self.rect.x < 470:
            self.arah = 'right'

packman = Player('hero.png', 5, 420, 4)
monster = Enemy('cyborg.png', 620, 280, 2)
final = GameSprite('treasure.png', 580, 420, 0)

dinding1 = GameSprite('image.PNG', 350, 100, 0)
dinding2 = GameSprite('image.PNG', 350, 160, 0)
dinding3 = GameSprite('image.PNG', 350, 220, 0)
dinding4 = GameSprite('image.PNG', 350, 340, 0)
dinding5 = GameSprite('image.PNG', 290, 220, 0)
dinding6 = GameSprite('image.PNG', 230, 220, 0)

clock = time.Clock()
FPS = 60 
finish = False
# Loop Game
run = True
while run:
    # Mendeteksi Event
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            run = False
    # Meletakkan Aset dan Objek
    if not finish:
        window.blit(bg, (0, 0))
        packman.reset()
        monster.reset()
        packman.update()
        monster.update()
        dinding1.reset()
        dinding2.reset()
        dinding3.reset()
        dinding4.reset()
        dinding5.reset()
        dinding6.reset()
        final.reset()
        if sprite.collide_rect(packman, monster):
            gambar_kalah = image.load('You_lose.PNG')
            window.blit(gambar_kalah, (200,100))
            finish = True
        if sprite.collide_rect(packman, final):
            gambar_menang = image.load('Cyou_win.PNG')
            window.blit(gambar_menang, (200,100))
            finish = True

    display.update()