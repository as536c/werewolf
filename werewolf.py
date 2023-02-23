from argparse import Action
from cgitb import text
import pygame
import wbutton
import wroles
import waction
import time
import threading
import socket

#background variables
BG = (0, 0, 139)
FPS = 10
HOST = '127.0.0.1'
PORT = 8888
PORT2 = 5556
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
players = 5

#player initial states
p1_state = ['alive']
p2_state = ['alive']
p3_state = ['alive']
p4_state = ['alive']
p5_state = ['alive']
self_state = ['alive', 'alive', 'alive', 'alive', 'alive']
time_state = ['night']
kill_chance = ['kill']
vote_chance = ['vote']
trick_chance = ['trick']
revive_chance = ['revive']
check_chance = ['check']

#game starts here
print('Welcome to Werewolf by Pugsitans')

#set player
#r = range(5, 11)
#while players not in r:     
#    while True:
#        try:
#            players = int(input('Please enter the number of players (min 5, max 10) : '))
#        except ValueError:
#            print('Please enter a number!')
#        else:
#            break

player_name = input("Enter name: ")

#Connecting to main server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
svrmessage = bytes(player_name, 'utf-8')
client_socket.send(svrmessage)
response = client_socket.recv(4096)
challenger_byte = response.decode("utf-8")
print("Hello, " + player_name + "! You are player", challenger_byte)
print("Waiting for other players. Please wait while the game initialize...")

# receive toggle info from server
#toggle = client_socket.recv(1024).decode()
#print(toggle)

challenger = int(challenger_byte)
#svrcommand = bytes(command, 'utf-8')

client_socket.close()
time.sleep(15)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST, PORT2))

if players == 5:   
    message = ['Werewolf']
    WIDTH, HEIGHT = 640, 790
    # WIN = main window of game
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Werewolf")

    #for n in range(1, players + 1):
    #    wroles.role[n] = random.choice(roles)
    #    roles.remove(wroles.role[n])
    #    if wroles.role[n] == wroles.bad:
    #        wroles.role[n] = random.choice(wroles.bad)
    #        wroles.bad.remove(wroles.role[n])
    #    if wroles.role[n] == wroles.wildcard:
    #        wroles.role[n] = random.choice(wroles.wildcard)

    def draw_window():
        #turns all player card to random villagers
        if 'dead' in p1_state:
            player1 = wbutton.Button(10,530,wroles.dead)
        else:
            player1 = wbutton.Button(10,530,wroles.villager3)
        if 'dead' in p2_state:
            player2 = wbutton.Button(10,10,wroles.dead)
        else:
            player2 = wbutton.Button(10,10,wroles.villager4)
        if 'dead' in p3_state:
            player3 = wbutton.Button(220,10,wroles.dead)
        else:    
            player3 = wbutton.Button(220,10,wroles.villager5)
        if 'dead' in p4_state:
            player4 = wbutton.Button(430,10,wroles.dead)
        else:
            player4 = wbutton.Button(430,10,wroles.villager6)
        if 'dead' in p5_state:
            player5 = wbutton.Button(430,530,wroles.dead)
        else:
            player5 = wbutton.Button(430,530,wroles.villager7)
        switchtime1 = wbutton.Button(220,680,waction.day)
        switchtime2 = wbutton.Button(220,730,waction.night)

        # only player card will be visible
        if challenger == 1:
            player_highlight = wbutton.Button(10,530,wroles.player_highlight)
            if 'alive' in p1_state:
                player1 = wbutton.Button(10,530,wroles.role[1])
        elif challenger == 2:
            player_highlight = wbutton.Button(10,10,wroles.player_highlight)
            if 'alive' in p2_state:
                player2 = wbutton.Button(10,10,wroles.role[2])
        elif challenger == 3:
            player_highlight = wbutton.Button(220,10,wroles.player_highlight)
            if 'alive' in p3_state:
                player3 = wbutton.Button(220,10,wroles.role[3])
        elif challenger == 4 and 'alive' in p4_state:
            player_highlight = wbutton.Button(430,10,wroles.player_highlight)
            if 'alive' in p4_state:
                player4 = wbutton.Button(430,10,wroles.role[4])
        elif challenger == 5 and 'alive' in p5_state:
            player_highlight = wbutton.Button(430,530,wroles.player_highlight)
            if 'alive' in p5_state:
                player5 = wbutton.Button(430,530,wroles.role[5])

        #options when night/day are toggled
        if time_state[0] == 'night':
            BG = (0, 0, 139)
            WIN.fill(BG)
            if challenger == 1:
                if switchtime1.draw_button(WIN):
                    tcp_socket.send(b'day')
        elif time_state[0] == 'day':
            BG = (255, 255, 51)
            WIN.fill(BG)
            if challenger == 1:
                if switchtime2.draw_button(WIN):
                    tcp_socket.send(b'night')

        #only show challenger skills
        if time_state[0] == 'night' and self_state[challenger-1] == 'alive':
            if wroles.role[challenger] in wroles.bad2 and kill_chance[0] == 'kill':
                if waction.killbutton.draw_button(WIN):
                    message.pop(0)
                    message.append('Select player to kill')
                    waction.action = 'killing'
                #if waction.assassinatebutton.draw_button(WIN):
                #    print('assassinate')
                #    waction.action = 'assassinating'

                #if wroles.role[challenger] == wroles.alpha:
                #    if waction.concealbutton.draw_button(WIN):
                #        print('conceal')
                #        waction.action = 'concealing'
                if wroles.role[challenger] == wroles.wolftrickster and trick_chance[0] == 'trick':
                    if waction.trickbutton.draw_button(WIN):
                        message.pop(0)
                        message.append('Select player to trick')
                        waction.action = 'tricking'
            elif wroles.role[challenger] == wroles.seer and check_chance[0] == 'check':
                if waction.checkbutton.draw_button(WIN):
                    message.pop(0)
                    message.append('Select player to check')
                    waction.action = 'checking'
            #elif wroles.role[challenger] == wroles.medium:
            #    if waction.seedeadbutton.draw_button(WIN):
            #        print('see dead')
            #        waction.action = 'seeing'
            #elif wroles.role[challenger] == wroles.bodyguard:
            #    if waction.protectbutton.draw_button(WIN):
            #        print('protect')
            #        waction.action = 'protecting'
            #elif wroles.role[challenger] == wroles.sheriff:
            #    if waction.shootbutton.draw_button(WIN):
            #        print('shoot')
            #        waction.action = 'shooting'
            elif wroles.role[challenger] == wroles.doctor and revive_chance[0] == 'revive':
                if waction.revivebutton.draw_button(WIN):
                    message.pop(0)
                    message.append('Select player to revive')
                    waction.action = 'reviving'
        elif self_state[challenger-1] == 'alive' and vote_chance[0] == 'vote':
            if waction.votebutton.draw_button(WIN):
                message.pop(0)
                message.append('Select player to vote')
                waction.action = 'voting'
        
        #draws the highlight of your card
        if player_highlight.draw_button(WIN):
            testvar = 10
            
        #hover/clicked options
        if pygame.Rect(10,530,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p1_state:
                if challenger != 1:
                    player1 = wbutton.Button(13,533,wroles.villager3)
                    if player1.draw_button(WIN):
                        player1 = wbutton.Button(16,537,wroles.villager3clicked)
        if pygame.Rect(10,10,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p2_state:
                if challenger != 2:
                    player2 = wbutton.Button(13,13,wroles.villager4)
                    if player2.draw_button(WIN):
                        player2 = wbutton.Button(16,17,wroles.villager4clicked)
        if pygame.Rect(220,10,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p3_state:
                if challenger != 3:
                    player3 = wbutton.Button(223,13,wroles.villager5)
                    if player3.draw_button(WIN):
                        player3 = wbutton.Button(226,17,wroles.villager5clicked)
        if pygame.Rect(430,10,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p4_state:
                if challenger != 4:
                    player4 = wbutton.Button(433,13,wroles.villager6)
                    if player4.draw_button(WIN):
                        player4 = wbutton.Button(436,17,wroles.villager6clicked)
        if pygame.Rect(430,530,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p5_state:
                if challenger != 5:
                    player5 = wbutton.Button(433,533,wroles.villager7)
                    if player5.draw_button(WIN):
                        player5 = wbutton.Button(436,537,wroles.villager7clicked)

        #what happens when player1 is clicked (player1.draw_button(WIN) only returns true or false)
        if player1.draw_button(WIN):
            message.pop(0)
            message.append('Player 1')
            if waction.action == 'checking':
                if wroles.role[1] in wroles.bad_check:
                    if 'tricked' in p1_state:
                        message.pop(0)
                        message.append('Player 1 is good')
                        p1_state.remove('tricked')
                        check_chance[0] = 'nocheck'
                    else:
                        message.pop(0)
                        message.append('Player 1 is bad')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[1] in wroles.good_check:
                    if 'tricked' in p1_state:
                        message.pop(0)
                        message.append('Player 1 is bad')
                        check_chance[0] = 'nocheck'
                        p1_state.remove('tricked')
                    else:
                        message.pop(0)
                        message.append('Player 1 is good')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[1] in wroles.unknown_check:  
                    message.pop(0)
                    message.append('Player 1 side is unknown')
                    check_chance[0] = 'nocheck'
                    waction.action = ''
            #if waction.action == 'protecting':
            #    if 'alive' in p1_state:
            #        message.pop(0)
            #        message.append('player is being protected')
            #        p1_state.append('protected')
            #        print(p1_state)
            #        waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p1_state:
                    message.pop(0)
                    message.append('Player 1 revived')
                    p1_state.remove('dead')
                    p1_state.append('alive')
                    self_state[0] = 'alive'
                    revive_chance[0] = 'norevive'
                    tcp_socket.send(b'p1alive')
                else:
                    message.pop(0)
                    message.append('Player 1 is still alive')
                    waction.action = ''
            #if waction.action == 'shooting':
            #    if 'alive' in p1_state:
            #        message.pop(0)
            #        message.append('player shot')
            #        p1_state.remove('alive')
            #        p1_state.append('dead')
            #        print(p1_state)
            #        waction.action = ''
            #if waction.action == 'seeing':
            #    if 'dead' in p1_state:
            #        message.pop(0)
            #        message.append('player message here')
            #        waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p1_state:
                    message.pop(0)
                    message.append('Player 1 killed')
                    p1_state.remove('alive')
                    p1_state.append('dead')
                    self_state[0] = 'dead'
                    tcp_socket.send(b'p1dead')
                    waction.action = ''
                    kill_chance[0] = 'nokill'
                else:
                    message.pop(0)
                    message.append('Player 1 already dead')
                    waction.action = ''
            if waction.action == 'tricking':
                if 'alive' in p1_state:
                    message.pop(0)
                    message.append('Player 1 tricked')
                    p1_state.append('tricked')
                    tcp_socket.send(b'p1tricked')
                    waction.action = ''
                    trick_chance[0] = 'notrick'
                else:
                    message.pop(0)
                    message.append('Player 1 already dead')
                    waction.action = ''
            if waction.action == 'voting':
                if 'alive' in p1_state:
                    message.pop(0)
                    message.append('Player 1 voted to be lynched')
                    tcp_socket.send(b'p1voted')
                    waction.action = ''
                    vote_chance[0] = 'novote'
                else:
                    message.pop(0)
                    message.append('Player 1 already dead')
                    waction.action = ''

            #assassinate (TO BE IMPLEMENTED, TOO COMPLEX FOR MULTIPLAYER)        
            #if waction.action == 'assassinating':
            #    if 'alive' in p1_state:
            #        assassination = True
            #        clock = pygame.time.Clock()
            #        while assassination:
            #            clock.tick(FPS)
            #            for event in pygame.event.get():
            #                if event.type == pygame.QUIT:
            #                    assassination = False
            #            if waction.assvillagerbutton.draw_button(WIN):
            #                if wroles.role[1] == wroles.villager:
            #                    message.pop(0)
            #                    message.append('player assassinated')
            #                    p1_state.remove('alive')
            #                    p1_state.append('dead')
            #                    print(p1_state)
            #                    assassination = False
            #                else:
            #                    message.pop(0)
            #                    message.append('player1')  
            #                    assassination = False         
            #            if waction.assseerbutton.draw_button(WIN):
            #                if wroles.role[1] == wroles.seer:
            #                    print('player assassinated')
            #                    p1_state.remove('alive')
            #                    p1_state.append('dead')
            #                    print(p1_state)
            #                    assassination = False
            #                else:
            #                    print('wrong guess! you are ded')
            #                    assassination = False
            #            if waction.assmediumbutton.draw_button(WIN):
            #                if wroles.role[1] == wroles.medium:
            #                    print('player assassinated')
            #                    p1_state.remove('alive')
            #                    p1_state.append('dead')
            #                    print(p1_state)
            #                    assassination = False
            #                else:
            #                    print('wrong guess! you are ded')
            #                    assassination = False
            #            if waction.assbodyguardbutton.draw_button(WIN):
            #                if wroles.role[1] == wroles.bodyguard:
            #                    print('player assassinated')
            #                    p1_state.remove('alive')
            #                    p1_state.append('dead')
            #                    print(p1_state)
            #                    assassination = False
            #                else:
            #                    print('wrong guess! you are ded')
            #                    assassination = False
            #            if waction.assdoctorbutton.draw_button(WIN):
            #                if wroles.role[1] == wroles.doctor:
            #                    print('player assassinated')
            #                    p1_state.remove('alive')
            #                    p1_state.append('dead')
            #                    print(p1_state)
            #                    assassination = False
            #                else:
            #                    print('wrong guess! you are ded')
            #                    assassination = False
            #            if waction.asssheriffbutton.draw_button(WIN):
            #                if wroles.role[1] == wroles.sheriff:
            #                    print('player assassinated')
            #                    p1_state.remove('alive')
            #                    p1_state.append('dead')
            #                    print(p1_state)
            #                    assassination = False
            #                else:
            #                    print('wrong guess! you are ded')
            #                    assassination = False
            #            if waction.assfoolbutton.draw_button(WIN):
            #                if wroles.role[1] == wroles.fool:
            #                    print('player assassinated')
            #                    p1_state.remove('alive')
            #                    p1_state.append('dead')
            #                    print(p1_state)
            #                    assassination = False
            #                else:
            #                    print('wrong guess! you are ded')
            #                    assassination = False
            #            if waction.asshunterbutton.draw_button(WIN):
            #                if wroles.role[1] == wroles.hunter:
            #                    print('player assassinated')
            #                    p1_state.remove('alive')
            #                    p1_state.append('dead')
            #                    print(p1_state)
            #                    assassination = False
            #                else:
            #                    print('wrong guess! you are ded')
            #                    assassination = False
            #            pygame.display.update()
            #        waction.action = ''
            #    
            #   else:
            #        print('player is already dead!')

        if player2.draw_button(WIN):
            message.pop(0)
            message.append('Player 2')
            if waction.action == 'checking':
                if wroles.role[2] in wroles.bad_check:
                    if 'tricked' in p2_state:
                        message.pop(0)
                        message.append('Player 2 is good')
                        check_chance[0] = 'nocheck'
                        p2_state.remove('tricked')
                    else:
                        message.pop(0)
                        message.append('Player 2 is bad')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[2] in wroles.good_check:
                    if 'tricked' in p2_state:
                        message.pop(0)
                        message.append('Player 2 is bad')
                        check_chance[0] = 'nocheck'
                        p2_state.remove('tricked')
                    else:
                        message.pop(0)
                        message.append('Player 2 is good')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[2] in wroles.unknown_check:  
                    message.pop(0)
                    message.append('Player 2 side is unknown')
                    check_chance[0] = 'nocheck'
                    waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p2_state:
                    message.pop(0)
                    message.append('Player 2 revived')
                    p2_state.remove('dead')
                    p2_state.append('alive')
                    self_state[1] = 'alive'
                    revive_chance[0] = 'norevive'
                    tcp_socket.send(b'p2alive')
                else:
                    message.pop(0)
                    message.append('Player 2 is still alive')
                    waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p2_state:
                    message.pop(0)
                    message.append('Player 2 killed')
                    p2_state.remove('alive')
                    p2_state.append('dead')
                    self_state[1] = 'dead'
                    tcp_socket.send(b'p2dead')
                    waction.action = ''
                    kill_chance[0] = 'nokill'
                else:
                    message.pop(0)
                    message.append('Player 2 already dead')
                    waction.action = ''
            if waction.action == 'tricking':
                if 'alive' in p2_state:
                    message.pop(0)
                    message.append('Player 2 tricked')
                    p2_state.append('tricked')
                    tcp_socket.send(b'p2tricked')
                    waction.action = ''
                    trick_chance[0] = 'notrick'
                else:
                    message.pop(0)
                    message.append('Player 2 already dead')
                    waction.action = ''
            if waction.action == 'voting':
                if 'alive' in p2_state:
                    message.pop(0)
                    message.append('Player 2 voted to be lynched')
                    tcp_socket.send(b'p2voted')
                    waction.action = ''
                    vote_chance[0] = 'novote'
                else:
                    message.pop(0)
                    message.append('Player 2 already dead')
                    waction.action = ''

        if player3.draw_button(WIN):
            message.pop(0)
            message.append('Player 3')
            if waction.action == 'checking':
                if wroles.role[3] in wroles.bad_check:
                    if 'tricked' in p3_state:
                        message.pop(0)
                        message.append('Player 3 is good')
                        check_chance[0] = 'nocheck'
                        p3_state.remove('tricked')
                    else:
                        message.pop(0)
                        message.append('Player 3 is bad')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[3] in wroles.good_check:
                    if 'tricked' in p3_state:
                        message.pop(0)
                        message.append('Player 3 is bad')
                        check_chance[0] = 'nocheck'
                        p3_state.remove('tricked')
                    else:
                        message.pop(0)
                        message.append('Player 3 is good')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[3] in wroles.unknown_check:  
                    message.pop(0)
                    message.append('Player 3 side is unknown')
                    check_chance[0] = 'nocheck'
                    waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p3_state:
                    message.pop(0)
                    message.append('Player 3 revived')
                    p3_state.remove('dead')
                    p3_state.append('alive')
                    self_state[2] = 'alive'
                    revive_chance[0] = 'norevive'
                    tcp_socket.send(b'p3alive')
                else:
                    message.pop(0)
                    message.append('Player 3 is still alive')
                    waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p3_state:
                    message.pop(0)
                    message.append('Player 3 killed')
                    p3_state.remove('alive')
                    p3_state.append('dead')
                    self_state[2] = 'dead'
                    tcp_socket.send(b'p3dead')
                    waction.action = ''
                    kill_chance[0] = 'nokill'
                else:
                    message.pop(0)
                    message.append('Player 3 already dead')
                    waction.action = ''
            if waction.action == 'tricking':
                if 'alive' in p3_state:
                    message.pop(0)
                    message.append('Player 3 tricked')
                    p3_state.append('tricked')
                    tcp_socket.send(b'p3tricked')
                    waction.action = ''
                    trick_chance[0] = 'notrick'
                else:
                    message.pop(0)
                    message.append('Player 3 already dead')
                    waction.action = ''
            if waction.action == 'voting':
                if 'alive' in p3_state:
                    message.pop(0)
                    message.append('Player 3 voted to be lynched')
                    tcp_socket.send(b'p3voted')
                    waction.action = ''
                    vote_chance[0] = 'novote'
                else:
                    message.pop(0)
                    message.append('Player 3 already dead')
                    waction.action = ''

        if player4.draw_button(WIN):
            message.pop(0)
            message.append('Player 4')
            if waction.action == 'checking':
                if wroles.role[4] in wroles.bad_check:
                    if 'tricked' in p4_state:
                        message.pop(0)
                        message.append('Player 4 is good')
                        check_chance[0] = 'nocheck'
                        p4_state.remove('tricked')
                    else:
                        message.pop(0)
                        message.append('Player 4 is bad')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[4] in wroles.good_check:
                    if 'tricked' in p4_state:
                        message.pop(0)
                        message.append('Player 4 is bad')
                        check_chance[0] = 'nocheck'
                        p4_state.remove('tricked')
                    else:
                        message.pop(0)
                        message.append('Player 4 is good')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[4] in wroles.unknown_check:  
                    message.pop(0)
                    message.append('Player 4 side is unknown')
                    check_chance[0] = 'nocheck'
                    waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p4_state:
                    message.pop(0)
                    message.append('Player 4 revived')
                    p4_state.remove('dead')
                    p4_state.append('alive')
                    self_state[3] = 'alive'
                    revive_chance[0] = 'norevive'
                    tcp_socket.send(b'p4alive')
                else:
                    message.pop(0)
                    message.append('Player 4 is still alive')
                    waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p4_state:
                    message.pop(0)
                    message.append('Player 4 killed')
                    p4_state.remove('alive')
                    p4_state.append('dead')
                    self_state[3] = 'dead'
                    tcp_socket.send(b'p4dead')
                    waction.action = ''
                    kill_chance[0] = 'nokill'
                else:
                    message.pop(0)
                    message.append('Player 4 already dead')
                    waction.action = ''
            if waction.action == 'tricking':
                if 'alive' in p4_state:
                    message.pop(0)
                    message.append('Player 4 tricked')
                    p4_state.append('tricked')
                    tcp_socket.send(b'p4tricked')
                    waction.action = ''
                    trick_chance[0] = 'notrick'
                else:
                    message.pop(0)
                    message.append('Player 4 already dead')
                    waction.action = ''
            if waction.action == 'voting':
                if 'alive' in p4_state:
                    message.pop(0)
                    message.append('Player 4 voted to be lynched')
                    tcp_socket.send(b'p4voted')
                    waction.action = ''
                    vote_chance[0] = 'novote'
                else:
                    message.pop(0)
                    message.append('Player 4 already dead')
                    waction.action = ''

        if player5.draw_button(WIN):
            message.pop(0)
            message.append('Player 5')
            if waction.action == 'checking':
                if wroles.role[5] in wroles.bad_check:
                    if 'tricked' in p5_state:
                        message.pop(0)
                        message.append('Player 5 is good')
                        check_chance[0] = 'nocheck'
                        p5_state.remove('tricked')
                    else:
                        message.pop(0)
                        message.append('Player 5 is bad')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[5] in wroles.good_check:
                    if 'tricked' in p5_state:
                        message.pop(0)
                        message.append('Player 5 is bad')
                        check_chance[0] = 'nocheck'
                        p5_state.remove('tricked')
                    else:
                        message.pop(0)
                        message.append('Player 5 is good')
                        check_chance[0] = 'nocheck'
                    waction.action = ''
                elif wroles.role[5] in wroles.unknown_check:  
                    message.pop(0)
                    message.append('Player 5 side is unknown')
                    check_chance[0] = 'nocheck'
                    waction.action = ''
            if waction.action == 'reviving':
                if 'dead' in p5_state:
                    message.pop(0)
                    message.append('Player 5 revived')
                    p5_state.remove('dead')
                    p5_state.append('alive')
                    self_state[4] = 'alive'
                    revive_chance[0] = 'norevive'
                    tcp_socket.send(b'p5alive')
                else:
                    message.pop(0)
                    message.append('Player 5 is still alive')
                    waction.action = ''
            if waction.action == 'killing':
                if 'alive' in p5_state:
                    message.pop(0)
                    message.append('Player 5 killed')
                    p5_state.remove('alive')
                    p5_state.append('dead')
                    self_state[4] = 'dead'
                    tcp_socket.send(b'p5dead')
                    waction.action = ''
                    kill_chance[0] = 'nokill'
                else:
                    message.pop(0)
                    message.append('Player 5 already dead')
                    waction.action = ''
            if waction.action == 'tricking':
                if 'alive' in p5_state:
                    message.pop(0)
                    message.append('Player 5 tricked')
                    p5_state.append('tricked')
                    tcp_socket.send(b'p5tricked')
                    waction.action = ''
                    trick_chance[0] = 'notrick'
                else:
                    message.pop(0)
                    message.append('Player 5 already dead')
                    waction.action = ''
            if waction.action == 'voting':
                if 'alive' in p5_state:
                    message.pop(0)
                    message.append('Player 5 voted to be lynched')
                    tcp_socket.send(b'p5voted')
                    waction.action = ''
                    vote_chance[0] = 'novote'
                else:
                    message.pop(0)
                    message.append('Player 5 already dead')
                    waction.action = ''

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
    time.sleep(3)
    
    while True:
        tcp_socket.send(b'sync')
        reply = tcp_socket.recv(512).decode('utf-8')
        print(reply)
        if 'p1dead' in reply:
            if 'alive' in p1_state:
                p1_state.remove('alive')
                p1_state.append('dead')
                self_state[0] = 'dead'
        if 'p2dead' in reply:
            if 'alive' in p2_state:
                p2_state.remove('alive')
                p2_state.append('dead')
                self_state[1] = 'dead'
        if 'p3dead' in reply:
            if 'alive' in p3_state:
                p3_state.remove('alive')
                p3_state.append('dead')
                self_state[2] = 'dead'
        if 'p4dead' in reply:
            if 'alive' in p4_state:
                p4_state.remove('alive')
                p4_state.append('dead')
                self_state[3] = 'dead'
        if 'p5dead' in reply:
            if 'alive' in p5_state:
                p5_state.remove('alive')
                p5_state.append('dead')
                self_state[4] = 'dead'
        if 'p1alive' in reply:
            if 'dead' in p1_state:
                p1_state.remove('dead')
                p1_state.append('alive')
                self_state[0] = 'alive'
        if 'p2alive' in reply:
            if 'dead' in p2_state:
                p2_state.remove('dead')
                p2_state.append('alive')
                self_state[1] = 'alive'
        if 'p3alive' in reply:
            if 'dead' in p3_state:
                p3_state.remove('dead')
                p3_state.append('alive')
                self_state[2] = 'alive'
        if 'p4alive' in reply:
            if 'dead' in p4_state:
                p4_state.remove('dead')
                p4_state.append('alive')
                self_state[3] = 'alive'
        if 'p5alive' in reply:
            if 'dead' in p5_state:
                p5_state.remove('dead')
                p5_state.append('alive')
                self_state[4] = 'alive'
        if 'day' in reply:
            time_state[0] = 'day'
            kill_chance[0] = 'kill'
            trick_chance[0] = 'trick'
            check_chance[0] = 'check'
        if 'night' in reply:
            time_state[0] = 'night'
            vote_chance[0] = 'vote'
            tcp_socket.send(b'votestart')
        time.sleep(3)

syncwerewolf = threading.Thread(name='background', target=sync)
mainwerewolf = threading.Thread(name='foreground', target=main)

if __name__ == "__main__":
    syncwerewolf.start()
    main()