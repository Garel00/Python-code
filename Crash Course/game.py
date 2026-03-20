import sys
import pygame

def run_pygame():
    #Initialize game and create an screen object
    pygame.init()
    screen = pygame.display.set.mode((1200,800))
    pygame.display.ser_caption("Alien Invasion")

    #Start the main loop
    while True:

        #Watch for input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Make the ost recently draw screen visible
        pygame.display.flip()
run_game()