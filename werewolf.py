from argparse import Action
from cgitb import text
import pygame
import wbutton
import wroles
import waction
import time
import threading
import socket
import vote

#background variables
BG = (0, 0, 139)
FPS = 10
HOST = '127.0.0.1'
PORT = 8888
PORT2 = 5556
white = (255, 255, 255)
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
night_phase = ['first']
game_start = ['menu']
ready_chance = ['notready']
winner = ['']
wolf = 0

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

#Connecting to main server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(b'Player joined')
response = client_socket.recv(4096)
challenger_byte = response.decode("utf-8")
print("You are player", challenger_byte)
print("Waiting for other players. Please wait while the game initialize...")
# receive toggle info from server
#toggle = client_socket.recv(1024).decode()
#print(toggle)
challenger = int(challenger_byte)
client_socket.close()
time.sleep(5)

#game initiates
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST, PORT2))
rolesrcv = tcp_socket.recv(4096)
rolesplit = rolesrcv.decode('utf-8').strip(' ').split(' ',4)
r1 = 1
for r in rolesplit:
    if r == 'villager':
        wroles.role[r1] = wroles.villager
    elif r == 'doctor':
        wroles.role[r1] = wroles.doctor
    elif r == 'seer':
        wroles.role[r1] = wroles.seer
    elif r == 'hunter':
        wroles.role[r1] = wroles.hunter
    elif r == 'fool':
        wroles.role[r1] = wroles.fool
    elif r == 'wolf':
        wroles.role[r1] = wroles.wolf
        wolf = r1
    elif r == 'alpha':
        wroles.role[r1] = wroles.alpha
        wolf = r1
    elif r == 'wolftrickster':
        wroles.role[r1] = wroles.wolftrickster
        wolf = r1
    r1 += 1

if players == 5:   
    message = ['Werewolf']
    popup = ['']
    message.pop(0)
    message.append('Welcome to Werewolf! You are player ' + str(challenger))
    BGmenu = (234, 212, 252)
    # WIN = main window of game
    WIDTH, HEIGHT = 640, 790
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    #def main_menu():
    #    WIN2 = pygame.display.set_mode((WIDTH2, HEIGHT2))
    #    pygame.display.set_caption("Werewolf_menu")
    #    WIN2.fill(BG2)
    #    tcp_socket.send(b'menustart')
    #    return
    def draw_window():
        WIN.fill(BGmenu)
        pygame.display.set_caption("Werewolf - waiting room")
        if game_start[0] == 'menu' and ready_chance[0] == 'notready':
            invisible = wbutton.Button(410,510,wroles.invisible)
            logo = wbutton.Button(30,25,wroles.logo)
            if pygame.Rect(410,510,200,250).collidepoint(pygame.mouse.get_pos()):
                invisible = wbutton.Button(410,510,wroles.role[challenger])
            if invisible.draw_button(WIN):
                print('')
            if logo.draw_button(WIN):
                print('')
            if waction.readybutton.draw_button(WIN):
                pnameadd = '#' + str(challenger) + vote.player_name
                tcp_socket.send(pnameadd.encode('utf-8'))
                ready_chance[0] = 'ready'
                time.sleep(0.2)
                tcp_socket.send(b'ready')
        elif game_start[0] == 'menu' and ready_chance[0] == 'ready':
            message[0] = 'Waiting for other players . . .'
        elif game_start[0] == 'commence' and winner[0] == 'villagers':
            message[0] = 'Villagers win!'
            vote.textcolor = (0, 0, 139)
            BG = (253, 218, 13)
            WIN.fill(BG)
        elif game_start[0] == 'commence':
            pygame.display.set_caption("Werewolf")
            message[0] = 'Werewolf'
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
                player_highlight = wbutton.Button(4,524,wroles.player_highlight)
                if 'alive' in p1_state:
                    player1 = wbutton.Button(10,530,wroles.role[1])
            elif challenger == 2:
                player_highlight = wbutton.Button(4,4,wroles.player_highlight)
                if 'alive' in p2_state:
                    player2 = wbutton.Button(10,10,wroles.role[2])
            elif challenger == 3:
                player_highlight = wbutton.Button(214,4,wroles.player_highlight)
                if 'alive' in p3_state:
                    player3 = wbutton.Button(220,10,wroles.role[3])
            elif challenger == 4:
                player_highlight = wbutton.Button(424,4,wroles.player_highlight)
                if 'alive' in p4_state:
                    player4 = wbutton.Button(430,10,wroles.role[4])
            elif challenger == 5:
                player_highlight = wbutton.Button(424,524,wroles.player_highlight)
                if 'alive' in p5_state:
                    player5 = wbutton.Button(430,530,wroles.role[5])

            #options when night/day are toggled
            if time_state[0] == 'night':
                BG = (0, 0, 139)
                WIN.fill(BG)
                vote.textcolor = (255, 211, 103)
                if challenger == 1:
                    if switchtime1.draw_button(WIN):
                        tcp_socket.send(b'day')
                        popup.pop(0)
                        popup.append('Here comes the sun')
            elif time_state[0] == 'day':
                BG = (253, 218, 13)
                WIN.fill(BG)
                vote.textcolor = (0, 0, 139)
                if challenger == 1:
                    if switchtime2.draw_button(WIN):
                        tcp_socket.send(b'night')
                        popup.pop(0)
                        popup.append('Exit light')

            #draws the highlight of your card
            if player_highlight.draw_button(WIN):
                testvar = 10
                
            #hover/clicked options
            if pygame.Rect(10,530,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p1_state:
                    if challenger != 1:
                        player1 = wbutton.Button(13,533,wroles.villager3)
                        message.pop(0)
                        message.append(vote.p1)
                        if player1.draw_button(WIN):
                            player1 = wbutton.Button(16,537,wroles.villager3clicked)
            if pygame.Rect(10,10,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p2_state:
                    if challenger != 2:
                        player2 = wbutton.Button(13,13,wroles.villager4)
                        message.pop(0)
                        message.append(vote.p2)
                        if player2.draw_button(WIN):
                            player2 = wbutton.Button(16,17,wroles.villager4clicked)
            if pygame.Rect(220,10,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p3_state:
                    if challenger != 3:
                        player3 = wbutton.Button(223,13,wroles.villager5)
                        message.pop(0)
                        message.append(vote.p3)
                        if player3.draw_button(WIN):
                            player3 = wbutton.Button(226,17,wroles.villager5clicked)
            if pygame.Rect(430,10,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p4_state:
                    if challenger != 4:
                        player4 = wbutton.Button(433,13,wroles.villager6)
                        message.pop(0)
                        message.append(vote.p4)
                        if player4.draw_button(WIN):
                            player4 = wbutton.Button(436,17,wroles.villager6clicked)
            if pygame.Rect(430,530,200,250).collidepoint(pygame.mouse.get_pos()) and 'alive' in p5_state:
                    if challenger != 5:
                        player5 = wbutton.Button(433,533,wroles.villager7)
                        message.pop(0)
                        message.append(vote.p5)
                        if player5.draw_button(WIN):
                            player5 = wbutton.Button(436,537,wroles.villager7clicked)
                            
            #only show challenger skills
            if time_state[0] == 'night' and self_state[challenger-1] == 'alive':
                if wroles.role[challenger] in wroles.bad2 and kill_chance[0] == 'kill':# and night_phase[0] == 'third':
                    if waction.killbutton.draw_button(WIN):
                        popup.pop(0)
                        popup.append('Select player to kill')
                        waction.action = 'killing'
                    #if waction.assassinatebutton.draw_button(WIN):
                    #    print('assassinate')
                    #    waction.action = 'assassinating'

                    #if wroles.role[challenger] == wroles.alpha:
                    #    if waction.concealbutton.draw_button(WIN):
                    #        print('conceal')
                    #        waction.action = 'concealing'
                if wroles.role[challenger] == wroles.wolftrickster and trick_chance[0] == 'trick':# and night_phase[0] == 'first':
                    if waction.trickbutton.draw_button(WIN):
                        popup.pop(0)
                        popup.append('Select player to trick')
                        waction.action = 'tricking'
                elif wroles.role[challenger] == wroles.seer and check_chance[0] == 'check':# and night_phase[0] == 'second':
                    if waction.checkbutton.draw_button(WIN):
                        popup.pop(0)
                        popup.append('Select player to check')
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
                elif wroles.role[challenger] == wroles.doctor and revive_chance[0] == 'revive':# and night_phase[0] == 'first':
                    if waction.revivebutton.draw_button(WIN):
                        popup.pop(0)
                        popup.append('Select player to revive')
                        waction.action = 'reviving'
            elif self_state[challenger-1] == 'alive' and vote_chance[0] == 'vote':
                if waction.votebutton.draw_button(WIN):
                    popup.pop(0)
                    popup.append('Select player to vote')
                    waction.action = 'voting'

            #what happens when player1 is clicked (player1.draw_button(WIN) only returns true or false)
            if player1.draw_button(WIN):
                if waction.action == 'checking':
                    if wroles.role[1] in wroles.bad_check:
                        if 'tricked' in p1_state:
                            popup.pop(0)
                            popup.append(vote.p1 + ' is good')
                            p1_state.remove('tricked')
                            check_chance[0] = 'nocheck'
                        else:
                            popup.pop(0)
                            popup.append(vote.p1 + ' is bad')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[1] in wroles.good_check:
                        if 'tricked' in p1_state:
                            popup.pop(0)
                            popup.append(vote.p1 + ' is bad')
                            check_chance[0] = 'nocheck'
                            p1_state.remove('tricked')
                        else:
                            popup.pop(0)
                            popup.append(vote.p1 + ' is good')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[1] in wroles.unknown_check:  
                        popup.pop(0)
                        popup.append(vote.p1 + ' side is unknown')
                        check_chance[0] = 'nocheck'
                        waction.action = ''
                #if waction.action == 'protecting':
                #    if 'alive' in p1_state:
                #        popup.pop(0)
                #        popup.append('player is being protected')
                #        p1_state.append('protected')
                #        print(p1_state)
                #        waction.action = ''
                if waction.action == 'reviving':
                    if 'dead' in p1_state:
                        popup.pop(0)
                        popup.append(vote.p1 + ' revived')
                        p1_state.remove('dead')
                        p1_state.append('alive')
                        self_state[0] = 'alive'
                        revive_chance[0] = 'norevive'
                        tcp_socket.send(b'p1alive')
                    else:
                        popup.pop(0)
                        popup.append(vote.p1 + ' is still alive')
                        waction.action = ''
                #if waction.action == 'shooting':
                #    if 'alive' in p1_state:
                #        popup.pop(0)
                #        popup.append('player shot')
                #        p1_state.remove('alive')
                #        p1_state.append('dead')
                #        print(p1_state)
                #        waction.action = ''
                #if waction.action == 'seeing':
                #    if 'dead' in p1_state:
                #        popup.pop(0)
                #        popup.append('player message here')
                #        waction.action = ''
                if waction.action == 'killing':
                    if 'alive' in p1_state:
                        popup.pop(0)
                        popup.append(vote.p1 + ' killed')
                        p1_state.remove('alive')
                        p1_state.append('dead')
                        self_state[0] = 'dead'
                        tcp_socket.send(b'p1dead')
                        waction.action = ''
                        kill_chance[0] = 'nokill'
                    else:
                        popup.pop(0)
                        popup.append(vote.p1 + ' already dead')
                        waction.action = ''
                if waction.action == 'tricking':
                    if 'alive' in p1_state:
                        popup.pop(0)
                        popup.append(vote.p1 + ' tricked')
                        p1_state.append('tricked')
                        tcp_socket.send(b'p1tricked')
                        waction.action = ''
                        trick_chance[0] = 'notrick'
                    else:
                        popup.pop(0)
                        popup.append(vote.p1 + ' already dead')
                        waction.action = ''
                if waction.action == 'voting':
                    if 'alive' in p1_state:
                        popup.pop(0)
                        popup.append(vote.p1 + ' voted to be lynched')
                        tcp_socket.send(b'p1voted')
                        waction.action = ''
                        vote_chance[0] = 'novote'
                    else:
                        popup.pop(0)
                        popup.append(vote.p1 + ' already dead')
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
                #                    popup.pop(0)
                #                    popup.append('player assassinated')
                #                    p1_state.remove('alive')
                #                    p1_state.append('dead')
                #                    print(p1_state)
                #                    assassination = False
                #                else:
                #                    popup.pop(0)
                #                    popup.append('player1')  
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
                if waction.action == 'checking':
                    if wroles.role[2] in wroles.bad_check:
                        if 'tricked' in p2_state:
                            popup.pop(0)
                            popup.append(vote.p2 + ' is good')
                            check_chance[0] = 'nocheck'
                            p2_state.remove('tricked')
                        else:
                            popup.pop(0)
                            popup.append(vote.p2 + ' is bad')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[2] in wroles.good_check:
                        if 'tricked' in p2_state:
                            popup.pop(0)
                            popup.append(vote.p2 + ' is bad')
                            check_chance[0] = 'nocheck'
                            p2_state.remove('tricked')
                        else:
                            popup.pop(0)
                            popup.append(vote.p2 + ' is good')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[2] in wroles.unknown_check:  
                        popup.pop(0)
                        popup.append(vote.p2 + ' side is unknown')
                        check_chance[0] = 'nocheck'
                        waction.action = ''
                if waction.action == 'reviving':
                    if 'dead' in p2_state:
                        popup.pop(0)
                        popup.append(vote.p2 + ' revived')
                        p2_state.remove('dead')
                        p2_state.append('alive')
                        self_state[1] = 'alive'
                        revive_chance[0] = 'norevive'
                        tcp_socket.send(b'p2alive')
                    else:
                        popup.pop(0)
                        popup.append(vote.p2 + ' is still alive')
                        waction.action = ''
                if waction.action == 'killing':
                    if 'alive' in p2_state:
                        popup.pop(0)
                        popup.append(vote.p2 + ' killed')
                        p2_state.remove('alive')
                        p2_state.append('dead')
                        self_state[1] = 'dead'
                        tcp_socket.send(b'p2dead')
                        waction.action = ''
                        kill_chance[0] = 'nokill'
                    else:
                        popup.pop(0)
                        popup.append(vote.p2 + ' already dead')
                        waction.action = ''
                if waction.action == 'tricking':
                    if 'alive' in p2_state:
                        popup.pop(0)
                        popup.append(vote.p2 + ' tricked')
                        p2_state.append('tricked')
                        tcp_socket.send(b'p2tricked')
                        waction.action = ''
                        trick_chance[0] = 'notrick'
                    else:
                        popup.pop(0)
                        popup.append(vote.p2 + ' already dead')
                        waction.action = ''
                if waction.action == 'voting':
                    if 'alive' in p2_state:
                        popup.pop(0)
                        popup.append(vote.p2 + ' voted to be lynched')
                        tcp_socket.send(b'p2voted')
                        waction.action = ''
                        vote_chance[0] = 'novote'
                    else:
                        popup.pop(0)
                        popup.append(vote.p2 + ' already dead')
                        waction.action = ''

            if player3.draw_button(WIN):
                if waction.action == 'checking':
                    if wroles.role[3] in wroles.bad_check:
                        if 'tricked' in p3_state:
                            popup.pop(0)
                            popup.append(vote.p3 + ' is good')
                            check_chance[0] = 'nocheck'
                            p3_state.remove('tricked')
                        else:
                            popup.pop(0)
                            popup.append(vote.p3 + ' is bad')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[3] in wroles.good_check:
                        if 'tricked' in p3_state:
                            popup.pop(0)
                            popup.append(vote.p3 + ' is bad')
                            check_chance[0] = 'nocheck'
                            p3_state.remove('tricked')
                        else:
                            popup.pop(0)
                            popup.append(vote.p3 + ' is good')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[3] in wroles.unknown_check:  
                        popup.pop(0)
                        popup.append(vote.p3 + ' side is unknown')
                        check_chance[0] = 'nocheck'
                        waction.action = ''
                if waction.action == 'reviving':
                    if 'dead' in p3_state:
                        popup.pop(0)
                        popup.append(vote.p3 + ' revived')
                        p3_state.remove('dead')
                        p3_state.append('alive')
                        self_state[2] = 'alive'
                        revive_chance[0] = 'norevive'
                        tcp_socket.send(b'p3alive')
                    else:
                        popup.pop(0)
                        popup.append(vote.p3 + ' is still alive')
                        waction.action = ''
                if waction.action == 'killing':
                    if 'alive' in p3_state:
                        popup.pop(0)
                        popup.append(vote.p3 + ' killed')
                        p3_state.remove('alive')
                        p3_state.append('dead')
                        self_state[2] = 'dead'
                        tcp_socket.send(b'p3dead')
                        waction.action = ''
                        kill_chance[0] = 'nokill'
                    else:
                        popup.pop(0)
                        popup.append(vote.p3 + ' already dead')
                        waction.action = ''
                if waction.action == 'tricking':
                    if 'alive' in p3_state:
                        popup.pop(0)
                        popup.append(vote.p3 + ' tricked')
                        p3_state.append('tricked')
                        tcp_socket.send(b'p3tricked')
                        waction.action = ''
                        trick_chance[0] = 'notrick'
                    else:
                        popup.pop(0)
                        popup.append(vote.p3 + ' already dead')
                        waction.action = ''
                if waction.action == 'voting':
                    if 'alive' in p3_state:
                        popup.pop(0)
                        popup.append(vote.p3 + ' voted to be lynched')
                        tcp_socket.send(b'p3voted')
                        waction.action = ''
                        vote_chance[0] = 'novote'
                    else:
                        popup.pop(0)
                        popup.append(vote.p3 + ' already dead')
                        waction.action = ''

            if player4.draw_button(WIN):
                if waction.action == 'checking':
                    if wroles.role[4] in wroles.bad_check:
                        if 'tricked' in p4_state:
                            popup.pop(0)
                            popup.append(vote.p4 + ' is good')
                            check_chance[0] = 'nocheck'
                            p4_state.remove('tricked')
                        else:
                            popup.pop(0)
                            popup.append(vote.p4 + ' is bad')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[4] in wroles.good_check:
                        if 'tricked' in p4_state:
                            popup.pop(0)
                            popup.append(vote.p4 + ' is bad')
                            check_chance[0] = 'nocheck'
                            p4_state.remove('tricked')
                        else:
                            popup.pop(0)
                            popup.append(vote.p4 + ' is good')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[4] in wroles.unknown_check:  
                        popup.pop(0)
                        popup.append(vote.p4 + ' side is unknown')
                        check_chance[0] = 'nocheck'
                        waction.action = ''
                if waction.action == 'reviving':
                    if 'dead' in p4_state:
                        popup.pop(0)
                        popup.append(vote.p4 + ' revived')
                        p4_state.remove('dead')
                        p4_state.append('alive')
                        self_state[3] = 'alive'
                        revive_chance[0] = 'norevive'
                        tcp_socket.send(b'p4alive')
                    else:
                        popup.pop(0)
                        popup.append(vote.p4 + ' is still alive')
                        waction.action = ''
                if waction.action == 'killing':
                    if 'alive' in p4_state:
                        popup.pop(0)
                        popup.append(vote.p4 + ' killed')
                        p4_state.remove('alive')
                        p4_state.append('dead')
                        self_state[3] = 'dead'
                        tcp_socket.send(b'p4dead')
                        waction.action = ''
                        kill_chance[0] = 'nokill'
                    else:
                        popup.pop(0)
                        popup.append(vote.p4 + ' already dead')
                        waction.action = ''
                if waction.action == 'tricking':
                    if 'alive' in p4_state:
                        popup.pop(0)
                        popup.append(vote.p4 + ' tricked')
                        p4_state.append('tricked')
                        tcp_socket.send(b'p4tricked')
                        waction.action = ''
                        trick_chance[0] = 'notrick'
                    else:
                        popup.pop(0)
                        popup.append(vote.p4 + ' already dead')
                        waction.action = ''
                if waction.action == 'voting':
                    if 'alive' in p4_state:
                        popup.pop(0)
                        popup.append(vote.p4 + ' voted to be lynched')
                        tcp_socket.send(b'p4voted')
                        waction.action = ''
                        vote_chance[0] = 'novote'
                    else:
                        popup.pop(0)
                        popup.append(vote.p4 + ' already dead')
                        waction.action = ''

            if player5.draw_button(WIN):
                if waction.action == 'checking':
                    if wroles.role[5] in wroles.bad_check:
                        if 'tricked' in p5_state:
                            popup.pop(0)
                            popup.append(vote.p5 + ' is good')
                            check_chance[0] = 'nocheck'
                            p5_state.remove('tricked')
                        else:
                            popup.pop(0)
                            popup.append(vote.p5 + ' is bad')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[5] in wroles.good_check:
                        if 'tricked' in p5_state:
                            popup.pop(0)
                            popup.append(vote.p5 + ' is bad')
                            check_chance[0] = 'nocheck'
                            p5_state.remove('tricked')
                        else:
                            popup.pop(0)
                            popup.append(vote.p5 + ' is good')
                            check_chance[0] = 'nocheck'
                        waction.action = ''
                    elif wroles.role[5] in wroles.unknown_check:  
                        popup.pop(0)
                        popup.append(vote.p5 + ' side is unknown')
                        check_chance[0] = 'nocheck'
                        waction.action = ''
                if waction.action == 'reviving':
                    if 'dead' in p5_state:
                        popup.pop(0)
                        popup.append(vote.p5 + ' revived')
                        p5_state.remove('dead')
                        p5_state.append('alive')
                        self_state[4] = 'alive'
                        revive_chance[0] = 'norevive'
                        tcp_socket.send(b'p5alive')
                    else:
                        popup.pop(0)
                        popup.append(vote.p5 + ' is still alive')
                        waction.action = ''
                if waction.action == 'killing':
                    if 'alive' in p5_state:
                        popup.pop(0)
                        popup.append(vote.p5 + ' killed')
                        p5_state.remove('alive')
                        p5_state.append('dead')
                        self_state[4] = 'dead'
                        tcp_socket.send(b'p5dead')
                        waction.action = ''
                        kill_chance[0] = 'nokill'
                    else:
                        popup.pop(0)
                        popup.append(vote.p5 + ' already dead')
                        waction.action = ''
                if waction.action == 'tricking':
                    if 'alive' in p5_state:
                        popup.pop(0)
                        popup.append(vote.p5 + ' tricked')
                        p5_state.append('tricked')
                        tcp_socket.send(b'p5tricked')
                        waction.action = ''
                        trick_chance[0] = 'notrick'
                    else:
                        popup.pop(0)
                        popup.append(vote.p5 + ' already dead')
                        waction.action = ''
                if waction.action == 'voting':
                    if 'alive' in p5_state:
                        popup.pop(0)
                        popup.append(vote.p5 + ' voted to be lynched')
                        tcp_socket.send(b'p5voted')
                        waction.action = ''
                        vote_chance[0] = 'novote'
                    else:
                        popup.pop(0)
                        popup.append(vote.p5 + ' already dead')
                        waction.action = ''


def sync():
    time.sleep(3)
    
    while True:
        popup.pop(0)
        popup.append('')
        tcp_socket.send(b'sync')
        reply = tcp_socket.recv(512).decode('utf-8')
        print(reply)
        if '#' in reply:
            if 'endmenu' in reply:
                char = reply.replace('endmenu', '')
            if 'sync' in reply:
                char = reply.replace('sync', '')
            if 'day' in reply:
                char = reply.replace('day', '')
            if 'night' in reply:
                char = reply.replace('night', '')
            if 'p1dead' in reply:
                char = reply.replace('p1dead', '')
            if 'p2dead' in reply:
                char = reply.replace('p2dead', '')
            if 'p3dead' in reply:
                char = reply.replace('p3dead', '')
            if 'p4dead' in reply:
                char = reply.replace('p4dead', '')
            if 'p5dead' in reply:
                char = reply.replace('p5dead', '')
            if 'p1alive' in reply:
                char = reply.replace('p1alive', '')
            if 'p2alive' in reply:
                char = reply.replace('p2alive', '')
            if 'p3alive' in reply:
                char = reply.replace('p3alive', '')
            if 'p4alive' in reply:
                char = reply.replace('p4alive', '')
            if 'p5alive' in reply:
                char = reply.replace('p5alive', '')
            if 'p1tricked' in reply:
                char = reply.replace('p1tricked', '')
            if 'p2tricked' in reply:
                char = reply.replace('p2tricked', '')
            if 'p3tricked' in reply:
                char = reply.replace('p3tricked', '')
            if 'p4tricked' in reply:
                char = reply.replace('p4tricked', '')
            if 'p5tricked' in reply:
                char = reply.replace('p5tricked', '')
            if 'p1lynch' in reply:
                char = reply.replace('p1lynched', '')
            if 'p2lynch' in reply:
                char = reply.replace('p2lynched', '')
            if 'p3lynch' in reply:
                char = reply.replace('p3lynched', '')
            if 'p4lynch' in reply:
                char = reply.replace('p4lynched', '')
            if 'p5lynch' in reply:
                char = reply.replace('p5lynched', '')
            chars = char.strip('endmenu').strip('sync').strip('#').split('#')
            vote.p1 = chars[0][1:] or ''
            vote.p2 = chars[1][1:] or ''
        #    vote.p3 = chars[0][1:] or ''
        #    vote.p4 = chars[1][1:] or ''
        #    vote.p5 = chars[1][1:] or ''
        if 'endmenu' in reply:
            game_start[0] = 'commence'
        if 'p1lynch' in reply:
            if 'alive' in p1_state:
                p1_state.remove('alive')
                p1_state.append('dead')
                self_state[0] = 'dead'
                popup.pop(0)
                popup.append(vote.p1 + ' lynched')
            if str(wolf) in reply:
                winner[0] = 'villagers'
        if 'p2lynch' in reply:
            if 'alive' in p2_state:
                p2_state.remove('alive')
                p2_state.append('dead')
                self_state[1] = 'dead'
                popup.pop(0)
                popup.append(vote.p2 + ' lynched')
            if str(wolf) in reply:
                winner[0] = 'villagers'
        if 'p3lynch' in reply:
            if 'alive' in p3_state:
                p3_state.remove('alive')
                p3_state.append('dead')
                self_state[2] = 'dead'
                popup.pop(0)
                popup.append(vote.p3 + ' lynched')
            if str(wolf) in reply:
                winner[0] = 'villagers'
        if 'p4lynch' in reply:
            if 'alive' in p4_state:
                p4_state.remove('alive')
                p4_state.append('dead')
                self_state[3] = 'dead'
                popup.pop(0)
                popup.append(vote.p4 + ' lynched')
            if str(wolf) in reply:
                winner[0] = 'villagers'
        if 'p5lynch' in reply:
            if 'alive' in p5_state:
                p5_state.remove('alive')
                p5_state.append('dead')
                self_state[4] = 'dead'
                popup.pop(0)
                popup.append(vote.p5 + ' lynched')
            if str(wolf) in reply:
                winner[0] = 'villagers'
        #if 'votetie' in reply:
        #    popup.pop(0)
        #    popup.append('All players are safe... for now') 
        if 'p1tricked' in reply:
            p1_state.append('tricked')    
        if 'p2tricked' in reply:
            p2_state.append('tricked')
        if 'p3tricked' in reply:
            p3_state.append('tricked')
        if 'p4tricked' in reply:
            p4_state.append('tricked')
        if 'p5tricked' in reply:
            p5_state.append('tricked')
        if 'p1dead' in reply:
            if 'alive' in p1_state:
                p1_state.remove('alive')
                p1_state.append('dead')
                self_state[0] = 'dead'
                popup.pop(0)
                popup.append(vote.p1 + ' killed')
        if 'p2dead' in reply:
            if 'alive' in p2_state:
                p2_state.remove('alive')
                p2_state.append('dead')
                self_state[1] = 'dead'
                popup.pop(0)
                popup.append(vote.p2 + ' killed')
        if 'p3dead' in reply:
            if 'alive' in p3_state:
                p3_state.remove('alive')
                p3_state.append('dead')
                self_state[2] = 'dead'
                popup.pop(0)
                popup.append(vote.p3 + ' killed')
        if 'p4dead' in reply:
            if 'alive' in p4_state:
                p4_state.remove('alive')
                p4_state.append('dead')
                self_state[3] = 'dead'
                popup.pop(0)
                popup.append(vote.p4 + ' killed')
        if 'p5dead' in reply:
            if 'alive' in p5_state:
                p5_state.remove('alive')
                p5_state.append('dead')
                self_state[4] = 'dead'
                popup.pop(0)
                popup.append(vote.p5 + ' killed')
        if 'p1alive' in reply:
            if 'dead' in p1_state:
                p1_state.remove('dead')
                p1_state.append('alive')
                self_state[0] = 'alive'
                popup.pop(0)
                popup.append(vote.p1 + ' revived')
        if 'p2alive' in reply:
            if 'dead' in p2_state:
                p2_state.remove('dead')
                p2_state.append('alive')
                self_state[1] = 'alive'
                popup.pop(0)
                popup.append(vote.p2 + ' revived')
        if 'p3alive' in reply:
            if 'dead' in p3_state:
                p3_state.remove('dead')
                p3_state.append('alive')
                self_state[2] = 'alive'
                popup.pop(0)
                popup.append(vote.p3 + ' revived')
        if 'p4alive' in reply:
            if 'dead' in p4_state:
                p4_state.remove('dead')
                p4_state.append('alive')
                self_state[3] = 'alive'
                popup.pop(0)
                popup.append(vote.p4 + ' revived')
        if 'p5alive' in reply:
            if 'dead' in p5_state:
                p5_state.remove('dead')
                p5_state.append('alive')
                self_state[4] = 'alive'
                popup.pop(0)
                popup.append(vote.p5 + ' revived')
        if 'day' in reply:
            time_state[0] = 'day'
            kill_chance[0] = 'kill'
            trick_chance[0] = 'trick'
            check_chance[0] = 'check'
            if 'tricked' in p1_state:
                p1_state.remove('tricked')
            elif 'tricked' in p2_state:
                p2_state.remove('tricked')
            elif 'tricked' in p3_state:
                p3_state.remove('tricked')
            elif 'tricked' in p4_state:
                p4_state.remove('tricked')
            elif 'tricked' in p5_state:
                p5_state.remove('tricked')
        if 'night' in reply:
            time_state[0] = 'night'
            vote_chance[0] = 'vote'
            tcp_socket.send(b'votestart')
#        if 'night2' in reply:
#           night_phase[0] = 'second'
#        if 'night3' in reply:
#            night_phase[0] = 'third'
        time.sleep(3)

#def menu():
#    run = True
#    main_menu()
#    while run:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                run = False
#        pygame.display.flip()
#    pygame.quit()

def main():
    pygame.init()
    import vote
    clock = pygame.time.Clock()
    base_font = pygame.font.Font(None, 32)
    input_rect = pygame.Rect(vote.rectx, vote.recty, vote.recta, vote.rectb)
    color_active = pygame.Color(165,3,192)
    color_passive = pygame.Color(123,2,144)
    color = color_passive
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    vote.active = True
                else:
                    vote.active = False
    
            if color == color_active and event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN: 
                    ready_chance[0] = 'ready'
                    pnameadd = '#' + str(challenger) + vote.player_name
                    tcp_socket.send(pnameadd.encode('utf-8'))
                    time.sleep(0.5)
                    tcp_socket.send(b'ready')

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    vote.player_name = vote.player_name[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    vote.player_name += event.unicode
        
        if vote.active:
            color = color_active
        else:
            color = color_passive
        draw_window()
        font = pygame.font.Font('freesansbold.ttf', 28)
        fontpop = pygame.font.Font('freesansbold.ttf', 23)
        if ready_chance[0] == 'notready':
            text_surface = base_font.render(vote.player_name, True, (255, 255, 255))
            pygame.draw.rect(WIN, color, input_rect)
            WIN.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, text_surface.get_width()+5)
            enter = font.render('Enter name: ', True, vote.textcolor)
            entername = enter.get_rect()
            entername.center = (155,447)
            WIN.blit(enter, entername)
        text = font.render(message[0], True, vote.textcolor)
        textpop = fontpop.render(popup[0], True, vote.textcolor)
        textRect = text.get_rect()
        textpopRect = textpop.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        textpopRect.center = (WIDTH // 2, HEIGHT // 1.8)
        WIN.blit(text, textRect)
        WIN.blit(textpop, textpopRect)
        pygame.display.update()
    client_socket.close()
    pygame.quit()

syncwerewolf = threading.Thread(name='background', target=sync)
mainwerewolf = threading.Thread(name='foreground', target=main)
#menuwerewolf = threading.Thread(name='menuground', target=menu)

if __name__ == "__main__":
    syncwerewolf.start()
    main()