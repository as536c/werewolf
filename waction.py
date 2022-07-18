import pygame
import os
import wbutton

action = '' #action to take when clicking on player cards; killing,checking,reviving
state = '' #player state; protected, concealed, deceived, dead

seedead = pygame.image.load(os.path.join('assets','seedead.png'))
shoot = pygame.image.load(os.path.join('assets','shoot.png'))
trick = pygame.image.load(os.path.join('assets','deceive.png'))
conceal = pygame.image.load(os.path.join('assets','conceal.png'))
assassinate = pygame.image.load(os.path.join('assets','assassinate.png'))
revive = pygame.image.load(os.path.join('assets','revive.png'))
check = pygame.image.load(os.path.join('assets','check.png'))
protect = pygame.image.load(os.path.join('assets','protect.png'))
kill = pygame.image.load(os.path.join('assets','kill.png'))

assvillager = pygame.image.load(os.path.join('assets','assvillager.png'))
assseer = pygame.image.load(os.path.join('assets','assseer.png'))
assmedium = pygame.image.load(os.path.join('assets','assmedium.png'))
assbodyguard = pygame.image.load(os.path.join('assets','assbodyguard.png'))
assdoctor = pygame.image.load(os.path.join('assets','assdoctor.png'))
asssheriff = pygame.image.load(os.path.join('assets','asssheriff.png'))
assfool = pygame.image.load(os.path.join('assets','assfool.png'))
asshunter = pygame.image.load(os.path.join('assets','asshunter.png'))

killbutton = wbutton.Button(220,530, kill)
assassinatebutton = wbutton.Button(220,590, assassinate)
concealbutton = wbutton.Button(220, 650, conceal)
trickbutton = wbutton.Button(220, 650, trick)
protectbutton = wbutton.Button(220,530, protect)
checkbutton = wbutton.Button(220,530, check)
revivebutton = wbutton.Button(220,530, revive)
shootbutton = wbutton.Button(220,530, shoot)
seedeadbutton = wbutton.Button(220,530, seedead)

assvillagerbutton = wbutton.Button(220, 270, assvillager)
assseerbutton = wbutton.Button(220, 332.5, assseer)
assmediumbutton = wbutton.Button(220, 395, assmedium)
assbodyguardbutton = wbutton.Button(220, 457.5, assbodyguard)
assdoctorbutton = wbutton.Button(325, 270, assdoctor)
asssheriffbutton = wbutton.Button(325, 332.5, asssheriff)
assfoolbutton = wbutton.Button(325, 395, assfool)
asshunterbutton = wbutton.Button(325, 457.5, asshunter)
