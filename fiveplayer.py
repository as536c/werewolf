from argparse import Action
from cgitb import text
import pygame
import random
import wbutton
import wroles
import waction

BG = (0, 0, 139)
players = 0

def five_player():
    r = range(5, 11)
    players = 0
    while players not in r:     
        while True:
            try:
                players = int(input('Please enter the number of players (min 5, max 10) : '))
            except ValueError:
                print('Please enter a number!')
            else:
                break
            
if players == 5:
    WIDTH, HEIGHT = 640, 790
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Werewolf")

    roles = [wroles.wolf, wroles.villager, wroles.doctor, wroles.seer, wroles.wildcard]

    for n in range(1, players + 1):
        wroles.role[n] = random.choice(roles)
        roles.remove(wroles.role[n])
        if wroles.role[n] == wroles.wildcard:
            wroles.role[n] = random.choice(wroles.wildcard)

    def draw_window():
        WIN.fill(BG)
        player1 = wbutton.Button(10,530,wroles.role[1])
        player2 = wbutton.Button(10,10,wroles.role[2])
        player3 = wbutton.Button(220,10,wroles.role[3])
        player4 = wbutton.Button(430,10,wroles.role[4])
        player5 = wbutton.Button(430,530,wroles.role[5])

        if player1.draw_button(WIN):
            print('player 1')
        if player2.draw_button(WIN):
            print('player 2')
        if player3.draw_button(WIN):
            print('player 3')
        if player4.draw_button(WIN):
            print('player 4')
        if player5.draw_button(WIN):
            print('player 5')

        if wroles.role[1] in wroles.bad:
            if waction.killbutton.draw_button(WIN):
                print('kill')
            if waction.assassinatebutton.draw_button(WIN):
                print('assassinate')

            if wroles.role[1] == wroles.alpha:
                if waction.concealbutton.draw_button(WIN):
                    print('conceal')

            elif wroles.role[1] == wroles.wolfseer:
                if waction.deceivebutton.draw_button(WIN):
                    print('deceive')
        
        elif wroles.role[1] == wroles.seer:
            if waction.checkbutton.draw_button(WIN):
                print('check')

        elif wroles.role[1] == wroles.medium:
            if waction.seedeadbutton.draw_button(WIN):
                print('see dead')

        elif wroles.role[1] == wroles.bodyguard:
            if waction.protectbutton.draw_button(WIN):
                print('protect')

        elif wroles.role[1] == wroles.sheriff:
            if waction.shootbutton.draw_button(WIN):
                print('shoot')

        elif wroles.role[1] == wroles.doctor:
            if waction.revivebutton.draw_button(WIN):
                print('revive')
                