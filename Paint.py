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

      if pygame.mouse.get_pressed(3)[0]: #Detect click on main canvas
         if curr_pos[1] > 40: #In main canvas space (+ some buffer)
            pygame.draw.circle(screen, pen_colour, pygame.mouse.get_pos(), 4)
            pygame.draw.line(screen, pen_colour, prev_pos, pygame.mouse.get_pos(), 10)
            
      prev_pos = pygame.mouse.get_pos()
      
      #Draw the toolbar at the top, after, and thus over the paint lines
      pygame.draw.rect(screen, (127,127,127), [0,0,wWidth,50])

      if 10 < curr_pos[1] < 40:                               #Detect if cursor in toolbar (specifically on the swatches Y-pos)
         #Red swatch
         if 10 < curr_pos[0] < 40:
            if pygame.mouse.get_pressed(3)[0]:                    #Detect if left-mouse-button is clicked
               pygame.draw.rect(screen, (0,0,0), [6,6,38,38], 8)    #Draw thick bound on swatch
               pen_colour = (255,0,0)                               #Change pen colour to Red
            else:
               pygame.draw.rect(screen, (0,0,0), [8,8,34,34], 4)    #Draw thin bound on swatch

         #Green swatch
         elif 50 < curr_pos[0] < 80:
            if pygame.mouse.get_pressed(3)[0]:
               pygame.draw.rect(screen, (0,0,0), [46,6,38,38], 8)
               pen_colour = (0,255,0)
            else:
               pygame.draw.rect(screen, (0,0,0), [48,8,34,34], 4)

         #Blue swatch
         elif 90 < curr_pos[0] < 120:
            if pygame.mouse.get_pressed(3)[0]:
               pygame.draw.rect(screen, (0,0,0), [86,6,38,38], 8)
               pen_colour = (0,0,255)
            else:
               pygame.draw.rect(screen, (0,0,0), [88,8,34,34], 4)
         
         #Black swatch
         elif 130 < curr_pos[0] < 160:
            if pygame.mouse.get_pressed(3)[0]:
               pygame.draw.rect(screen, (63,63,63), [126,6,38,38], 8)
               pen_colour = (0,0,0)
            else:
               pygame.draw.rect(screen, (63,63,63), [128,8,34,34], 4)
         
         #Clear button
         elif wWidth-90 < curr_pos[0] < wWidth-10:
            if pygame.mouse.get_pressed(3)[0]:
               screen.fill((255,255,255))
               pygame.draw.rect(screen, (127,127,127), [0,0,wWidth,50])
               pygame.draw.rect(screen, (255,255,255), [wWidth-94,6,88,38], 8)
            else:
               pygame.draw.rect(screen, (255,255,255), [wWidth-92,8,84,34], 4)

      #Colour swatches; click on one to change the pen to that colour
      pygame.draw.rect(screen, (255,0,0), [10, 10,30,30])
      pygame.draw.rect(screen, (0,255,0), [50, 10,30,30])
      pygame.draw.rect(screen, (0,0,255), [90, 10,30,30])
      pygame.draw.rect(screen, (0, 0, 0), [130,10,30,30])

      #Clear button: click to wipe canvas
      pygame.draw.rect(screen, (255,255,255), [wWidth-90,10,80,30], 4)
      font = pygame.font.SysFont('arialblack', 18)
      text = font.render('CLEAR', True, (255,255,255), None)
      textRect = text.get_rect()
      textRect.center = (wWidth-50, 25)
      screen.blit(text, textRect)

      #Finish the drawing for this frame
      pygame.display.flip()

if __name__ == '__main__':
   main()
