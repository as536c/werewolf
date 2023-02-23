import pygame
import os

#Roles
#
#Wolves
# + any wolf can kill another villager with assassinate ONCE if correctly guessed a role, but dies if role is wrong
# + assassinate can only be used ONCE
#      (b) wolf: kills at night 
#      (u) alpha: unknown to seer; c
#      (b) wolf trickster: can reverse a role of a player each night, unknown will remain unknown: trick
#
#Villagers
#      (g) seer: can check players if good or bad
#      (g) super seer: can see roles
#      (g) silencer: can silence a chat/voice
#      (u) medium: can speak to the dead
#      (g) bodyguard: can protect/has 2 lives
#      (g) sheriff: can kill player during daytime
#      (g) doctor: can revive a player once
#      (g) villager: no power
#      (u) jailer: can jail player and restrict user powers
#      (g) priest: can splash holy water during day or night, if wolf, wolf will die. if not, priest will die.
#
#Wildcards
#
#      (u) fool: only wins if got voted out
#      (u) hunter: wins when target gets voted out
#      (u) arsonist: can put gasoline/or ignite

#killed

path = "./assets/"

dead = pygame.image.load(os.path.join(path, 'dead.png'))
invisible = pygame.image.load(os.path.join(path, 'invisible.png'))
wolf = pygame.image.load(os.path.join(path,'wolf.png'))
alpha = pygame.image.load(os.path.join(path,'alpha.png'))
wolftrickster = pygame.image.load(os.path.join(path,'wolftrickster.png'))
player_highlight = pygame.image.load(os.path.join(path,'player_highlight.png'))
villager = pygame.image.load(os.path.join(path,'villager.png'))
villager1 = pygame.image.load(os.path.join(path,'villager1.png'))
villager2 = pygame.image.load(os.path.join(path,'villager2.png'))
villager3 = pygame.image.load(os.path.join(path,'villager3.png'))
villager3clicked = pygame.image.load(os.path.join(path,'villager3clicked.png'))
villager4clicked = pygame.image.load(os.path.join(path,'villager4clicked.png'))
villager5clicked = pygame.image.load(os.path.join(path,'villager5clicked.png'))
villager6clicked = pygame.image.load(os.path.join(path,'villager6clicked.png'))
villager7clicked = pygame.image.load(os.path.join(path,'villager7clicked.png'))
villager4 = pygame.image.load(os.path.join(path,'villager4.png'))
villager5 = pygame.image.load(os.path.join(path,'villager5.png'))
villager6 = pygame.image.load(os.path.join(path,'villager6.png'))
villager7 = pygame.image.load(os.path.join(path,'villager7.png'))
seer = pygame.image.load(os.path.join(path,'seer.png'))
medium = pygame.image.load(os.path.join(path,'medium.png'))
bodyguard = pygame.image.load(os.path.join(path,'bodyguard.png'))
sheriff = pygame.image.load(os.path.join(path,'sheriff.png'))
doctor = pygame.image.load(os.path.join(path,'doctor.png'))
fool = pygame.image.load(os.path.join(path,'fool.png'))
hunter = pygame.image.load(os.path.join(path,'hunter.png'))

wildcard = [fool, hunter]
bad = [wolf, alpha, wolftrickster]
bad2 = [wolf, alpha, wolftrickster]

bad_check = [wolf, wolftrickster]
unknown_check = [fool, hunter, sheriff, alpha]
good_check = [villager, seer, medium, bodyguard, doctor]
role = {
