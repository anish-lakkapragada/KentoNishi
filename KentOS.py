import pygame
pygame.init()

BLACK = (0, 0, 0)
DARK_GRAY = (64, 64, 64)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
WHITE = (255, 255, 255)

FONT = pygame.font.SysFont("ubuntu", 24)
IMGS = {
    "original": pygame.image.load("images/original.jpg"),
    "face": pygame.image.load("images/face.jpg"),
    "noface": pygame.image.load("images/noface.jpg"),
}
CLOCK = pygame.time.Clock()


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def boot(surface):
    progress = 0

    while True:
        CLOCK.tick(60)
        pygame.display.update()
        events()

        surface.fill(WHITE)
        pygame.draw.rect(surface, LIGHT_GRAY, (540, 620, progress*200, 20))
        pygame.draw.rect(surface, GRAY, (540, 620, 200, 20), 2)

        img = IMGS["original"] if (int(progress*10) % 2) == 1 else IMGS["noface"]
        surface.blit(img, (640-img.get_width()//2, 120))

        text = FONT.render("KentOS is booting...", 1, BLACK)
        surface.blit(text, (640-text.get_width()//2, 40))

        progress += 0.003
        if progress > 1:
            break


def main():
    pygame.display.set_caption("KentOS")
    surface = pygame.display.set_mode((1280, 720))
    surface.fill(WHITE)

    boot(surface)


main()
