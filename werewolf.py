from argparse import Action
from cgitb import text
import pygame
import wbutton
import wroles
import waction
import time
import threading

BG = (0, 0, 139)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
FPS = 5

p1_state = ['alive']
p2_state = ['alive']
p3_state = ['alive']
p4_state = ['alive']
p5_state = ['alive']

time_state = ['night']

r = range(5, 11)
players = 0

print('Welcome to Werewolf by Pugsitans')

#set player
#while players not in r:     
#    while True:
#        try:
#            players = int(input('Please enter the number of players (min 5, max 10) : '))
#        except ValueError:
#            print('Please enter a number!')
#        else:
#            break

players = 5

import socket

HOST = '127.0.0.1'
PORT = 5555
PORT2 = 5556

#command = 'hello'
player_name = input("Enter name: ")
#TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET = telling it that we're creating an ipv4 socket
    # SOCK_STREAM = open a socket that is a streaming socket(tcp socket)
    # both are just constants in socket module that is imported in line 1
    # numeric equivalents 
client_socket.connect((HOST, PORT))
    # initiates the tcp handshake, we should be able to connect
    # to a remote server if the server is ready and is able to complete the
    # handshake.
svrmessage = bytes(player_name, 'utf-8')
    # b = bytes string
#print("Player name:", message.decode("utf-8"))
client_socket.send(svrmessage)
    # used to transmit data from one host to another
    # send is used because the data is small
    # sendall will be used to guarantee that all message is sent for bigger files
response = client_socket.recv(4096)
    # used to confirm the message has been received, can act as
    # a blocker because it will be stale if no response is being
    # received
#print("Received:", response.decode("utf-8"))
challenger_byte = response.decode("utf-8")
print("Hello, " + player_name + "! You are player", challenger_byte)
print("Waiting for other players. Please wait while the game initialize...")

# receive toggle info from server
#toggle = client_socket.recv(1024).decode()
#print(toggle)

challenger = int(challenger_byte)
#svrcommand = bytes(command, 'utf-8')

client_socket.close()
time.sleep(8)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST, PORT2))

if players == 5:
    message = ['hehe']
    WIDTH, HEIGHT = 640, 790
    # WIN = main window of game
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Werewolf")
    #roles = [wroles.bad, wroles.villager, wroles.doctor, wroles.seer, wroles.wildcard]

    #for n in range(1, players + 1):
    #    wroles.role[n] = random.choice(roles)
    #    roles.remove(wroles.role[n])
    #    if wroles.role[n] == wroles.bad:
    #        wroles.role[n] = random.choice(wroles.bad)
    #        wroles.bad.remove(wroles.role[n])
    #    if wroles.role[n] == wroles.wildcard:
    #        wroles.role[n] = random.choice(wroles.wildcard)
    
    def draw_window():
        
        #turns all player card to invisible
        if 'dead' in p1_state:
            player1 = wbutton.Button(10,530,wroles.dead)
        else:
            player1 = wbutton.Button(10,530,wroles.invisible)
        if 'dead' in p2_state:
            player2 = wbutton.Button(10,10,wroles.dead)
        else:
            player2 = wbutton.Button(10,10,wroles.invisible)
        if 'dead' in p3_state:
            player3 = wbutton.Button(220,10,wroles.dead)
        else:    
            player3 = wbutton.Button(220,10,wroles.invisible)
        if 'dead' in p4_state:
            player4 = wbutton.Button(430,10,wroles.dead)
        else:
            player4 = wbutton.Button(430,10,wroles.invisible)
        if 'dead' in p5_state:
            player5 = wbutton.Button(430,530,wroles.dead)
        else:
            player5 = wbutton.Button(430,530,wroles.invisible)  
        switchtime1 = wbutton.Button(220,680,waction.shoot)
        switchtime2 = wbutton.Button(220,730,waction.trick)

        #player1 = wbutton.Button(10,530,wroles.role[1])
        #player2 = wbutton.Button(10,10,wroles.role[2])
        #player3 = wbutton.Button(220,10,wroles.role[3])
        #player4 = wbutton.Button(430,10,wroles.role[4])
        #player5 = wbutton.Button(430,530,wroles.role[5])
        #switchtime1 = wbutton.Button(220,680,waction.shoot)
        #switchtime2 = wbutton.Button(220,730,waction.trick)

        # only player card will be visible
        if challenger == 1 and 'alive' in p1_state:
            player1 = wbutton.Button(10,530,wroles.role[1])
        elif challenger == 2 and 'alive' in p2_state:
            player2 = wbutton.Button(10,10,wroles.role[2])
        elif challenger == 3 and 'alive' in p3_state:
            player3 = wbutton.Button(220,10,wroles.role[3])
        elif challenger == 4 and 'alive' in p4_state:
            player4 = wbutton.Button(430,10,wroles.role[4])
        elif challenger == 5 and 'alive' in p5_state:
            player5 = wbutton.Button(430,530,wroles.role[5])

        #switch day/night toggle
        #if challenger == 0: (to be developed, admin mode to toggle night day)
        if time_state[0] == 'night':
            BG = (0, 0, 139)
            WIN.fill(BG)
            if switchtime1.draw_button(WIN):
                print('click')
                time_state[0] = 'day'
                print(time_state)
        elif time_state[0] == 'day':
            BG = (255, 255, 51)
            WIN.fill(BG)
            if switchtime2.draw_button(WIN):
                print('click')
                time_state[0] = 'night'
                print(time_state)

        # update to only show challenger skills, not the first player's skills
        if time_state[0] == 'night':
            if wroles.role[challenger] in wroles.bad2:
                if waction.killbutton.draw_button(WIN):
                    print('kill')
                    waction.action = 'killing'
                #if waction.assassinatebutton.draw_button(WIN):
                #    print('assassinate')
                #    waction.action = 'assassinating'

                if wroles.role[challenger] == wroles.alpha:
                    if waction.concealbutton.draw_button(WIN):
                        print('conceal')
                        waction.action = 'concealing'

                elif wroles.role[challenger] == wroles.wolftrickster:
                    if waction.trickbutton.draw_button(WIN):
                        print('trick')
                        waction.action = 'tricking'
            
            elif wroles.role[challenger] == wroles.seer:
                if waction.checkbutton.draw_button(WIN):
                    print('check')
                    waction.action = 'checking'

            elif wroles.role[challenger] == wroles.medium:
                if waction.seedeadbutton.draw_button(WIN):
                    print('see dead')
                    waction.action = 'seeing'

            elif wroles.role[challenger] == wroles.bodyguard:
                if waction.protectbutton.draw_button(WIN):
                    print('protect')
                    waction.action = 'protecting'

            elif wroles.role[challenger] == wroles.sheriff:
                if waction.shootbutton.draw_button(WIN):
                    print('shoot')
                    waction.action = 'shooting'

            elif wroles.role[challenger] == wroles.doctor:
                if waction.revivebutton.draw_button(WIN):
                    print('revive')
                    waction.action = 'reviving'

        if player1.draw_button(WIN):
            tcp_socket.send(b'hello')
            reply = tcp_socket.recv(512).decode('utf-8')
            if reply == 'hello':
                time_state[0] = 'day'
            message.pop(0)
            message.append('player1')
            if waction.action == 'checking':
                if wroles.role[1] in wroles.bad_check:
                    if 'tricked' in p1_state:
                        message.pop(0)
                        message.append('player is good')
                    else:
                        message.pop(0)
                        message.append('player is bad')
                    waction.action = ''
                elif wroles.role[1] in wroles.good_check:
                    if 'tricked' in p1_state:
                        message.pop(0)
                        message.append('player is bad')
                    else:
                        message.pop(0)
                        message.append('player is good')
                    waction.action = ''
                elif wroles.role[1] in wroles.unknown_check:  
                    message.pop(0)
                    message.append('player side is unknown')
                    waction.action = ''
            if waction.action == 'protecting':
                if 'alive' in p1_state:
                    message.pop(0)
                    message.append('player is being protected')
                    p1_state.append('protected')
                    print(p1_state)
                    waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p1_state:
                    message.pop(0)
                    message.append('player revived')
                    p1_state.remove('dead')
                    p1_state.append('alive')
                    print(p1_state)
                else:
                    message.pop(0)
                    message.append('player is still alive')
            if waction.action == 'shooting':
                if 'alive' in p1_state:
                    message.pop(0)
                    message.append('player shot')
                    p1_state.remove('alive')
                    p1_state.append('dead')
                    print(p1_state)
                    waction.action = ''
            if waction.action == 'seeing':
                if 'dead' in p1_state:
                    message.pop(0)
                    message.append('player message here')
                    waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p1_state:
                    message.pop(0)
                    message.append('player killed')
                    p1_state.remove('alive')
                    p1_state.append('dead')
                    print(p1_state)
                    waction.action = ''
                else:
                    message.pop(0)
                    message.append('cannot kill dead player')
            if waction.action == 'tricking':
                if 'alive' in p1_state:
                    message.pop(0)
                    message.append('player tricked')
                    p1_state.append('tricked')
                    waction.action = ''
            if waction.action == 'assassinating':
                if 'alive' in p1_state:
                    assassination = True
                    clock = pygame.time.Clock()
                    while assassination:
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                assassination = False
                        if waction.assvillagerbutton.draw_button(WIN):
                            if wroles.role[1] == wroles.villager:
                                message.pop(0)
                                message.append('player assassinated')
                                p1_state.remove('alive')
                                p1_state.append('dead')
                                print(p1_state)
                                assassination = False
                            else:
                                message.pop(0)
                                message.append('player1')  
                                assassination = False         
                        if waction.assseerbutton.draw_button(WIN):
                            if wroles.role[1] == wroles.seer:
                                print('player assassinated')
                                p1_state.remove('alive')
                                p1_state.append('dead')
                                print(p1_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assmediumbutton.draw_button(WIN):
                            if wroles.role[1] == wroles.medium:
                                print('player assassinated')
                                p1_state.remove('alive')
                                p1_state.append('dead')
                                print(p1_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assbodyguardbutton.draw_button(WIN):
                            if wroles.role[1] == wroles.bodyguard:
                                print('player assassinated')
                                p1_state.remove('alive')
                                p1_state.append('dead')
                                print(p1_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assdoctorbutton.draw_button(WIN):
                            if wroles.role[1] == wroles.doctor:
                                print('player assassinated')
                                p1_state.remove('alive')
                                p1_state.append('dead')
                                print(p1_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asssheriffbutton.draw_button(WIN):
                            if wroles.role[1] == wroles.sheriff:
                                print('player assassinated')
                                p1_state.remove('alive')
                                p1_state.append('dead')
                                print(p1_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assfoolbutton.draw_button(WIN):
                            if wroles.role[1] == wroles.fool:
                                print('player assassinated')
                                p1_state.remove('alive')
                                p1_state.append('dead')
                                print(p1_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asshunterbutton.draw_button(WIN):
                            if wroles.role[1] == wroles.hunter:
                                print('player assassinated')
                                p1_state.remove('alive')
                                p1_state.append('dead')
                                print(p1_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        pygame.display.update()
                    waction.action = ''

                else:
                    print('player is already dead!')

        if player2.draw_button(WIN):
            print('player 2')
            if waction.action == 'checking':
                if wroles.role[2] in wroles.bad_check:
                    if 'tricked' in p2_state:
                        print('player is good')
                    else:
                        print('player is bad')
                    waction.action = ''
                elif wroles.role[2] in wroles.good_check:
                    if 'tricked' in p2_state:
                        print('player is bad')
                    else:
                        print('player is good')
                    waction.action = ''
                elif wroles.role[2] in wroles.unknown_check:  
                    print('player side is unknown')
                    waction.action = ''
            if waction.action == 'protecting':
                if 'alive' in p2_state:
                    print('player is being protected')
                    p2_state.append('protected')
                    print(p2_state)
                    waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p2_state:
                    print('player is revived')
                    p2_state.remove('dead')
                    p2_state.append('alive')
                    print(p2_state)
                else:
                    print('player is still alive!')
            if waction.action == 'shooting':
                if 'alive' in p2_state:
                    print('player is shot')
                    p2_state.remove('alive')
                    p2_state.append('dead')
                    print(p2_state)
                    waction.action = ''
            if waction.action == 'seeing':
                if 'dead' in p2_state:
                    print('message from dead: "enter message here"')
                    waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p2_state:
                    print('player is killed')
                    p2_state.remove('alive')
                    p2_state.append('dead')
                    print(p2_state)
                    waction.action = ''
                else:
                    print('player is already dead')
                    waction.action = ''
            if waction.action == 'tricking':
                if 'alive' in p2_state:
                    print('player is tricked')
                    p2_state.append('tricked')
                    waction.action = ''
            if waction.action == 'assassinating':
                if 'alive' in p2_state:
                    assassination = True
                    clock = pygame.time.Clock()
                    while assassination:
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                assassination = False
                        if waction.assvillagerbutton.draw_button(WIN):
                            if wroles.role[2] == wroles.villager:
                                print('player assassinated')
                                p2_state.remove('alive')
                                p2_state.append('dead')
                                print(p2_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')   
                                assassination = False         
                        if waction.assseerbutton.draw_button(WIN):
                            if wroles.role[2] == wroles.seer:
                                print('player assassinated')
                                p2_state.remove('alive')
                                p2_state.append('dead')
                                print(p2_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assmediumbutton.draw_button(WIN):
                            if wroles.role[2] == wroles.medium:
                                print('player assassinated')
                                p2_state.remove('alive')
                                p2_state.append('dead')
                                print(p2_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assbodyguardbutton.draw_button(WIN):
                            if wroles.role[2] == wroles.bodyguard:
                                print('player assassinated')
                                p2_state.remove('alive')
                                p2_state.append('dead')
                                print(p2_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assdoctorbutton.draw_button(WIN):
                            if wroles.role[2] == wroles.doctor:
                                print('player assassinated')
                                p2_state.remove('alive')
                                p2_state.append('dead')
                                print(p2_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asssheriffbutton.draw_button(WIN):
                            if wroles.role[2] == wroles.sheriff:
                                print('player assassinated')
                                p2_state.remove('alive')
                                p2_state.append('dead')
                                print(p2_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assfoolbutton.draw_button(WIN):
                            if wroles.role[2] == wroles.fool:
                                print('player assassinated')
                                p2_state.remove('alive')
                                p2_state.append('dead')
                                print(p2_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asshunterbutton.draw_button(WIN):
                            if wroles.role[2] == wroles.hunter:
                                print('player assassinated')
                                p2_state.remove('alive')
                                p2_state.append('dead')
                                print(p2_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        pygame.display.update()
                    waction.action = ''

                else:
                    print('player is already dead!')

        if player3.draw_button(WIN):
            print('player 3')
            if waction.action == 'checking':
                if wroles.role[3] in wroles.bad_check:
                    if 'tricked' in p3_state:
                        print('player is good')
                    else:
                        print('player is bad')
                    waction.action = ''
                elif wroles.role[3] in wroles.good_check:
                    if 'tricked' in p3_state:
                        print('player is bad')
                    else:
                        print('player is good')
                    waction.action = ''
                elif wroles.role[3] in wroles.unknown_check:  
                    print('player side is unknown')
                    waction.action = ''
            if waction.action == 'protecting':
                if 'alive' in p3_state:
                    print('player is being protected')
                    p3_state.append('protected')
                    print(p3_state)
                    waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p3_state:
                    print('player is revived')
                    p3_state.remove('dead')
                    p3_state.append('alive')
                    print(p3_state)
                else:
                    print('player is still alive!')
            if waction.action == 'shooting':
                if 'alive' in p3_state:
                    print('player is shot')
                    p3_state.remove('alive')
                    p3_state.append('dead')
                    print(p3_state)
                    waction.action = ''
            if waction.action == 'seeing':
                if 'dead' in p3_state:
                    print('message from dead: "enter message here"')
                    waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p3_state:
                    print('player is killed')
                    p3_state.remove('alive')
                    p3_state.append('dead')
                    print(p3_state)
                    waction.action = ''
                else:
                    print('player is already dead!')
            if waction.action == 'tricking':
                if 'alive' in p3_state:
                    print('player is tricked')
                    p3_state.append('tricked')
                    waction.action = ''
            if waction.action == 'assassinating':
                if 'alive' in p3_state:
                    assassination = True
                    clock = pygame.time.Clock()
                    while assassination:
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                assassination = False
                        if waction.assvillagerbutton.draw_button(WIN):
                            if wroles.role[3] == wroles.villager:
                                print('player assassinated')
                                p3_state.remove('alive')
                                p3_state.append('dead')
                                print(p3_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')   
                                assassination = False         
                        if waction.assseerbutton.draw_button(WIN):
                            if wroles.role[3] == wroles.seer:
                                print('player assassinated')
                                p3_state.remove('alive')
                                p3_state.append('dead')
                                print(p3_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assmediumbutton.draw_button(WIN):
                            if wroles.role[3] == wroles.medium:
                                print('player assassinated')
                                p3_state.remove('alive')
                                p3_state.append('dead')
                                print(p3_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assbodyguardbutton.draw_button(WIN):
                            if wroles.role[3] == wroles.bodyguard:
                                print('player assassinated')
                                p3_state.remove('alive')
                                p3_state.append('dead')
                                print(p3_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assdoctorbutton.draw_button(WIN):
                            if wroles.role[3] == wroles.doctor:
                                print('player assassinated')
                                p3_state.remove('alive')
                                p3_state.append('dead')
                                print(p3_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asssheriffbutton.draw_button(WIN):
                            if wroles.role[3] == wroles.sheriff:
                                print('player assassinated')
                                p3_state.remove('alive')
                                p3_state.append('dead')
                                print(p3_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assfoolbutton.draw_button(WIN):
                            if wroles.role[3] == wroles.fool:
                                print('player assassinated')
                                p3_state.remove('alive')
                                p3_state.append('dead')
                                print(p3_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asshunterbutton.draw_button(WIN):
                            if wroles.role[3] == wroles.hunter:
                                print('player assassinated')
                                p3_state.remove('alive')
                                p3_state.append('dead')
                                print(p3_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        pygame.display.update()
                    waction.action = ''

                else:
                    print('player is already dead!')

        if player4.draw_button(WIN):
            print('player 4')
            if waction.action == 'checking':
                if wroles.role[4] in wroles.bad_check:
                    if 'tricked' in p4_state:
                        print('player is good')
                    else:
                        print('player is bad')
                    waction.action = ''
                elif wroles.role[4] in wroles.good_check:
                    if 'tricked' in p4_state:
                        print('player is bad')
                    else:
                        print('player is good')
                    waction.action = ''
                elif wroles.role[4] in wroles.unknown_check:  
                    print('player side is unknown')
                    waction.action = ''
            if waction.action == 'protecting':
                if 'alive' in p4_state:
                    print('player is being protected')
                    p4_state.append('protected')
                    print(p4_state)
                    waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p4_state:
                    print('player is revived')
                    p4_state.remove('dead')
                    p4_state.append('alive')
                    print(p4_state)
                else:
                    print('player is still alive!')
            if waction.action == 'shooting':
                if 'alive' in p4_state:
                    print('player is shot')
                    p4_state.remove('alive')
                    p4_state.append('dead')
                    print(p4_state)
                    waction.action = ''
            if waction.action == 'seeing':
                if 'dead' in p4_state:
                    print('message from dead: "enter message here"')
                    waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p4_state:
                    print('player is killed')
                    p4_state.remove('alive')
                    p4_state.append('dead')
                    print(p4_state)
                    waction.action = ''
                else:
                    print('player is already dead!')
            if waction.action == 'tricking':
                if 'alive' in p4_state:
                    print('player is tricked')
                    p4_state.append('tricked')
                    waction.action = ''
            if waction.action == 'assassinating':
                if 'alive' in p4_state:
                    assassination = True
                    clock = pygame.time.Clock()
                    while assassination:
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                assassination = False
                        if waction.assvillagerbutton.draw_button(WIN):
                            if wroles.role[4] == wroles.villager:
                                print('player assassinated')
                                p4_state.remove('alive')
                                p4_state.append('dead')
                                print(p4_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')   
                                assassination = False         
                        if waction.assseerbutton.draw_button(WIN):
                            if wroles.role[4] == wroles.seer:
                                print('player assassinated')
                                p4_state.remove('alive')
                                p4_state.append('dead')
                                print(p4_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assmediumbutton.draw_button(WIN):
                            if wroles.role[4] == wroles.medium:
                                print('player assassinated')
                                p4_state.remove('alive')
                                p4_state.append('dead')
                                print(p4_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assbodyguardbutton.draw_button(WIN):
                            if wroles.role[4] == wroles.bodyguard:
                                print('player assassinated')
                                p4_state.remove('alive')
                                p4_state.append('dead')
                                print(p4_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assdoctorbutton.draw_button(WIN):
                            if wroles.role[4] == wroles.doctor:
                                print('player assassinated')
                                p4_state.remove('alive')
                                p4_state.append('dead')
                                print(p4_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asssheriffbutton.draw_button(WIN):
                            if wroles.role[4] == wroles.sheriff:
                                print('player assassinated')
                                p4_state.remove('alive')
                                p4_state.append('dead')
                                print(p4_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assfoolbutton.draw_button(WIN):
                            if wroles.role[4] == wroles.fool:
                                print('player assassinated')
                                p4_state.remove('alive')
                                p4_state.append('dead')
                                print(p4_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asshunterbutton.draw_button(WIN):
                            if wroles.role[4] == wroles.hunter:
                                print('player assassinated')
                                p4_state.remove('alive')
                                p4_state.append('dead')
                                print(p4_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        pygame.display.update()
                    waction.action = ''

                else:
                    print('player is already dead!')

        if player5.draw_button(WIN):
            print('player 5')
            if waction.action == 'checking':
                if wroles.role[5] in wroles.bad_check:
                    if 'tricked' in p5_state:
                        print('player is good')
                    else:
                        print('player is bad')
                    waction.action = ''
                elif wroles.role[5] in wroles.good_check:
                    if 'tricked' in p5_state:
                        print('player is bad')
                    else:
                        print('player is good')
                    waction.action = ''
                elif wroles.role[5] in wroles.unknown_check:  
                    print('player side is unknown')
                    waction.action = ''
            if waction.action == 'protecting':
                if 'alive' in p5_state:
                    print('player is being protected')
                    p5_state.append('protected')
                    print(p5_state)
                    waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p5_state:
                    print('player is revived')
                    p5_state.remove('dead')
                    p5_state.append('alive')
                    print(p5_state)
                else:
                    print('player is still alive!')
            if waction.action == 'shooting':
                if 'alive' in p5_state:
                    print('player is shot')
                    p5_state.remove('alive')
                    p5_state.append('dead')
                    print(p5_state)
                    waction.action = ''
            if waction.action == 'seeing':
                if 'dead' in p5_state:
                    print('message from dead: "enter message here"')
                    waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p5_state:
                    print('player is killed')
                    p5_state.remove('alive')
                    p5_state.append('dead')
                    print(p5_state)
                    waction.action = ''
                else:
                    print('player is already dead!')
            if waction.action == 'tricking':
                if 'alive' in p5_state:
                    print('player is tricked')
                    p5_state.append('tricked')
                    waction.action = ''
            if waction.action == 'assassinating':
                if 'alive' in p5_state:
                    assassination = True
                    clock = pygame.time.Clock()
                    while assassination:
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                assassination = False
                        if waction.assvillagerbutton.draw_button(WIN):
                            if wroles.role[5] == wroles.villager:
                                print('player assassinated')
                                p5_state.remove('alive')
                                p5_state.append('dead')
                                print(p5_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')   
                                assassination = False         
                        if waction.assseerbutton.draw_button(WIN):
                            if wroles.role[5] == wroles.seer:
                                print('player assassinated')
                                p5_state.remove('alive')
                                p5_state.append('dead')
                                print(p5_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assmediumbutton.draw_button(WIN):
                            if wroles.role[5] == wroles.medium:
                                print('player assassinated')
                                p5_state.remove('alive')
                                p5_state.append('dead')
                                print(p5_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assbodyguardbutton.draw_button(WIN):
                            if wroles.role[5] == wroles.bodyguard:
                                print('player assassinated')
                                p5_state.remove('alive')
                                p5_state.append('dead')
                                print(p5_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assdoctorbutton.draw_button(WIN):
                            if wroles.role[5] == wroles.doctor:
                                print('player assassinated')
                                p5_state.remove('alive')
                                p5_state.append('dead')
                                print(p5_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asssheriffbutton.draw_button(WIN):
                            if wroles.role[5] == wroles.sheriff:
                                print('player assassinated')
                                p5_state.remove('alive')
                                p5_state.append('dead')
                                print(p5_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.assfoolbutton.draw_button(WIN):
                            if wroles.role[5] == wroles.fool:
                                print('player assassinated')
                                p5_state.remove('alive')
                                p5_state.append('dead')
                                print(p5_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        if waction.asshunterbutton.draw_button(WIN):
                            if wroles.role[5] == wroles.hunter:
                                print('player assassinated')
                                p5_state.remove('alive')
                                p5_state.append('dead')
                                print(p5_state)
                                assassination = False
                            else:
                                print('wrong guess! you are ded')
                                assassination = False
                        pygame.display.update()
                    waction.action = ''

                else:
                    print('player is already dead!')

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
        pygame.init()
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render(message[0], True, green, blue)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        WIN.blit(text, textRect)
        pygame.display.update()
    client_socket.close()
    pygame.quit()

def sync():
    time.sleep(5)
    while True:
        tcp_socket.send(b'sync')
        reply = tcp_socket.recv(512).decode('utf-8')
        print(reply)
        time.sleep(5)

syncwerewolf = threading.Thread(name='background', target=sync)
mainwerewolf = threading.Thread(name='foreground', target=main)

if __name__ == "__main__":
    syncwerewolf.start()
    main()
