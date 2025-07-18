import pygame

check_errors = pygame.init()
frame_size_x = 720
frame_size_y = 480
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
white = pygame.Color(255,255,255)

while True:
    ############# to fix issue on macOS with pygame quitting ##############
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #######################################################################
    game_window.fill(white)
    pygame.display.update()