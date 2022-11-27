#Application with basic canvas and ability to draw on it in multiple colours, as well as some other features like clearing the canvas.

import pygame

#Width and Height of the window
wWidth = 1000
wHeight = 800

def main():
   #Create the window with initialized width and height, and title it
   pygame.init()
   screen = pygame.display.set_mode([wWidth, wHeight])
   pygame.display.set_caption("Python Paint")

   done = False
   clock = pygame.time.Clock()
   screen.fill((255,255,255))
   prev_pos = (0,0)
   pen_colour = (0,0,0)
   while not done:
      clock.tick(200) #Frames per second
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            done = True

      curr_pos = pygame.mouse.get_pos()
      if pygame.mouse.get_pressed(3)[0]: #Detect clicks on colour swatches
         if 10 < curr_pos[0] < 40 and 10 < curr_pos[1] < 40:
            pen_colour = (255,0,0)
         elif 50 < curr_pos[0] < 80 and 10 < curr_pos[1] < 40:
            pen_colour = (0,255,0)
         elif 90 < curr_pos[0] < 120 and 10 < curr_pos[1] < 40:
            pen_colour = (0,0,255)
         elif wWidth-40 < curr_pos[0] < wWidth-10 and 10 < curr_pos[1] < 40:
            screen.fill((255,255,255))
         else:
            pygame.draw.circle(screen, pen_colour, pygame.mouse.get_pos(), 4)
            pygame.draw.line(screen, pen_colour, prev_pos, pygame.mouse.get_pos(), 10)
      prev_pos = pygame.mouse.get_pos()
      
      #Draw the toolbar at the top, after, and thus over the paint lines
      pygame.draw.rect(screen, (127,127,127), [0,0,wWidth,50])

      #Colour swatches; click on one to change the pen to that colour
      pygame.draw.rect(screen, (255,0,0), [10,10,30,30])
      pygame.draw.rect(screen, (0,255,0), [50,10,30,30])
      pygame.draw.rect(screen, (0,0,255), [90,10,30,30])
      pygame.draw.rect(screen, (255,255,255), [wWidth-40,10,30,30], 4)

      #Finish the drawing for this frame
      pygame.display.flip()

if __name__ == '__main__':
   main()