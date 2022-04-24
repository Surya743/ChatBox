import pygame
import socket

screen = pygame.display.set_mode((1000,600))
s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
blue = (154, 245, 237)
screen.fill((blue))


clientNumber = 0

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Chatbox")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "172.16.136.216"
port = 5555
addr = (server, port)
client.connect(addr)
testlist = []



COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font("AsparagusSprouts.ttf", 32)
inputboxdata = ''

class messageboxmaker:

    def __init__(self,messno,y,message):
        self.messno = messno
        self.y = y
        self.messnoRect = ''
        self.message = message
        self.drawbox = ''
    def update(self):
        font = pygame.font.Font('AsparagusSprouts.ttf', 50)
        self.messno = font.render(self.message, True, (0, 0, 0))
        self.messnoRect = self.messno.get_rect()
        self.messnoRect.midleft = (265, self.y)
        self.drawbox = pygame.Rect(265, self.y-20, 720, 55)
        pygame.draw.rect(screen, blue, self.drawbox)
        pygame.display.update()
        screen.blit(self.messno, self.messnoRect)
        pygame.display.update()

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        
        self.txt_surface = FONT.render(text, True, self.color)
        
        self.active = False
        self.inputboxdata = ''
     
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

           
        if event.type == pygame.KEYDOWN:
            
            if self.active:
                if event.key == pygame.K_RETURN:
                    global inputboxdata
                    self.inputboxdata = self.text
                  

                    self.text = ''
                    
                    pygame.draw.rect(screen,blue,self.rect)
                elif event.key == pygame.K_BACKSPACE:
                    pygame.draw.rect(screen, blue, self.rect)
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.txt_surface = FONT.render(self.text, True, self.color)
                




    def update(self):
        # Resize the box if the text is too long.
        width = max(630, self.txt_surface.get_width()+30)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y-1))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)




def main():
    def eventchecker():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()
        for box in input_boxes:
            box.draw(screen)

        pygame.display.update()
    run = True

    font = pygame.font.Font('AsparagusSprouts.ttf', 55)
    font2 = pygame.font.Font('AsparagusSprouts.ttf', 45)
    text = font.render('Chatbox!', True, (0, 0, 0))
    text2 = font.render('Client Name:', True, (0, 0, 0))
    text3 = font2.render('The maximum length for the client name is 11 characters', True, (0, 0, 0))
    


    # create a rectangular object for the
    # text surface object
    text3Rect = text3.get_rect()
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    
    


    # set the center of the rectangular object.
    text2Rect.center = (150, 300)
    textRect.center = (500, 100)
    text3Rect.midleft = (50,450)


    input_box1 = InputBox(280, 285, 50, 30)
    input_boxes = [input_box1]

    while run:
        clock = pygame.time.Clock()
        clock.tick(50)
        screen.fill((blue))

        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        screen.blit(text3, text3Rect)

        eventchecker()
        if input_box1.inputboxdata:
            playername = input_box1.inputboxdata
            client.send(str.encode("name," + playername))
            break

    screen.fill((blue))



    input_box1 = InputBox(260, 540, 500,50)
    rect = pygame.Rect(10,10,240,580)
    rect2 = pygame.Rect(260,10,730,520)
   

    pygame.draw.rect(screen,(0,0,0),rect2,2)
    pygame.draw.rect(screen, (0,0,0), rect,2)
   
    messno1 = messageboxmaker(1,480,"")
    messno1.update()

    messno2 = messageboxmaker(2,420,"")
    messno2.update()

    messno3 = messageboxmaker(3,360,"")
    messno3.update()

    messno4 = messageboxmaker(4,300,"")
    messno4.update()

    messno5 = messageboxmaker(5,240,"")
    messno5.update()

    messno6 = messageboxmaker(6,180,"")
    messno6.update()

    messno7 = messageboxmaker(7,120,"")
    messno7.update()

    messno8 = messageboxmaker(8,60,"")
    messno8.update()



    def playernamesarranger(finallist):


        player1 = font.render("", True, (0, 0, 0))
        player2 = font.render("", True, (0, 0, 0))
        player3 = font.render("", True, (0, 0, 0))
        player4 = font.render("", True, (0, 0, 0))
        player5 = font.render("", True, (0, 0, 0))
        player6 = font.render("", True, (0, 0, 0))

        if len(finallist) == 1:
            player1 = font.render(finallist[0], True, (0, 0, 0))

        if len(finallist) == 2:
            player1 = font.render(finallist[0], True, (0, 0, 0))
            player2 = font.render(finallist[1], True, (0, 0, 0))

        if len(finallist) == 3:
            player1 = font.render(finallist[0], True, (0, 0, 0))
            player2 = font.render(finallist[1], True, (0, 0, 0))
            player3 = font.render(finallist[2], True, (0, 0, 0))

        if len(finallist) == 4:
            player1 = font.render(finallist[0], True, (0, 0, 0))
            player2 = font.render(finallist[1], True, (0, 0, 0))
            player3 = font.render(finallist[2], True, (0, 0, 0))
            player4 = font.render(finallist[3], True, (0, 0, 0))

        if len(finallist) == 5:
            player1 = font.render(finallist[0], True, (0, 0, 0))
            player2 = font.render(finallist[1], True, (0, 0, 0))
            player3 = font.render(finallist[2], True, (0, 0, 0))
            player4 = font.render(finallist[3], True, (0, 0, 0))
            player5 = font.render(finallist[4], True, (0, 0, 0))

        if len(finallist) == 6:
            player1 = font.render(finallist[0], True, (0, 0, 0))
            player2 = font.render(finallist[1], True, (0, 0, 0))
            player3 = font.render(finallist[2], True, (0, 0, 0))
            player4 = font.render(finallist[3], True, (0, 0, 0))
            player5 = font.render(finallist[4], True, (0, 0, 0))
            player6 = font.render(finallist[5], True, (0, 0, 0))


        player1Rect = player1.get_rect()
        player2Rect = player2.get_rect()
        player3Rect = player3.get_rect()
        player4Rect = player4.get_rect()
        player5Rect = player5.get_rect()
        player6Rect = player6.get_rect()


        player1Rect.midleft = (15, 35)
        player2Rect.midleft = (15, 95)
        player3Rect.midleft = (15, 155)
        player4Rect.midleft = (15, 215)
        player5Rect.midleft = (15, 275)
        player6Rect.midleft = (15, 335)

        drawbox1 = pygame.Rect(15, 15, 225, 60)
        pygame.draw.rect(screen, blue, drawbox1)
        drawbox2 = pygame.Rect(15, 75, 225, 60)
        pygame.draw.rect(screen, blue, drawbox2)
        drawbox3 = pygame.Rect(15, 135, 225, 60)
        pygame.draw.rect(screen, blue, drawbox3)
        drawbox4 = pygame.Rect(15, 195, 225, 60)
        pygame.draw.rect(screen, blue, drawbox4)
        drawbox5 = pygame.Rect(15, 255, 225, 60)
        pygame.draw.rect(screen, blue, drawbox5)
        drawbox6 = pygame.Rect(15, 315, 225, 60)
        pygame.draw.rect(screen, blue, drawbox6)



        screen.blit(player1, player1Rect)
        screen.blit(player2, player2Rect)
        screen.blit(player3, player3Rect)
        screen.blit(player4, player4Rect)
        screen.blit(player5, player5Rect)
        screen.blit(player6, player6Rect)

        pygame.display.update()

    input_boxes = [input_box1]

    
    b = ''

    
    def messagearranger(newmessage):
        messno8.message = messno7.message       
        
        messno7.message = messno6.message        
        
        messno6.message = messno5.message

        messno5.message = messno4.message

        messno4.message = messno3.message

        messno3.message = messno2.message

        messno2.message = messno1.message

        messno1.message = newmessage
        
        messno1.update()
        messno2.update()
        messno3.update()
        messno4.update()
        messno5.update()
        messno6.update()
        messno7.update()
        messno8.update()

    while run:

        clock = pygame.time.Clock()
        clock.tick(20)
        client.send(str.encode(" "))

        recv_data = client.recv(2048).decode()
        recv_data = recv_data.split(",")
        
        ##(recv_data)
        a = recv_data[1]
        playernamesstring = recv_data[2:-1]
        if " " in playernamesstring:
            indexno = playernamesstring.index(" ")
            playernamesstring = playernamesstring[:indexno]
        playernamesarranger(playernamesstring)
        font = pygame.font.Font("AsparagusSprouts.ttf", 60)

        if a ==b:
            pass

        else:
            messagearranger(a)

    
        b = a

        eventchecker()

        if input_box1.inputboxdata:

            message = input_box1.inputboxdata
            
            client.send(str.encode("message," + playername + ":" + message))
                       
            input_box1.inputboxdata = False

main()
