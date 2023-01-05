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
invisible = pygame.image.load(os.path.join('assets','invisible.png'))
wolf = pygame.image.load(os.path.join('assets','wolf.png'))
alpha = pygame.image.load(os.path.join('assets','alpha.png'))
wolftrickster = pygame.image.load(os.path.join('assets','wolftrickster.png'))
villager = pygame.image.load(os.path.join('assets','villager.png'))
seer = pygame.image.load(os.path.join('assets','seer.png'))
medium = pygame.image.load(os.path.join('assets','medium.png'))
bodyguard = pygame.image.load(os.path.join('assets','bodyguard.png'))
sheriff = pygame.image.load(os.path.join('assets','sheriff.png'))
doctor = pygame.image.load(os.path.join('assets','doctor.png'))
fool = pygame.image.load(os.path.join('assets','fool.png'))
hunter = pygame.image.load(os.path.join('assets','hunter.png'))

wildcard = [fool, hunter]
bad = [wolf, alpha, wolftrickster]
bad2 = [wolf, alpha, wolftrickster]

bad_check = [wolf, wolftrickster]
unknown_check = [fool, hunter, sheriff, alpha]
good_check = [villager, seer, medium, bodyguard, doctor]

role = {
 1: villager,
 2: villager,
 3: villager,
 4: villager,
 5: villager,
 6: villager,
 7: villager,
 8: villager,
 9: villager,
 10: villager
}