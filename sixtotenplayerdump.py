if players == 6:
    WIDTH, HEIGHT = 640, 790
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Werewolf")

    roles = [wroles.alpha, wroles.villager, wroles.bodyguard, wroles.medium, wroles.seer, wroles.wildcard]

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
        player6 = wbutton.Button(430,270,wroles.role[6])

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
        if player6.draw_button(WIN):
            print('player 6')

        if wroles.role[1] in wroles.bad:
            if waction.killbutton.draw_button(WIN):
                print('kill')
            if waction.assassinatebutton.draw_button(WIN):
                print('assassinate')

            if wroles.role[1] == wroles.alpha:
                if waction.concealbutton.draw_button(WIN):
                    print('conceal')

            elif wroles.role[1] == wroles.wolftrickster:
                if waction.trickbutton.draw_button(WIN):
                    print('trick')
        
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

if players == 7:
    WIDTH, HEIGHT = 850, 790
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Werewolf")

    roles = [wroles.alpha, wroles.villager, wroles.villager, wroles.doctor, wroles.bodyguard, wroles.seer, wroles.wildcard]

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
        player5 = wbutton.Button(640,10,wroles.role[5])
        player6 = wbutton.Button(430,530,wroles.role[6])
        player7 = wbutton.Button(640,530,wroles.role[7])

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
        if player6.draw_button(WIN):
            print('player 6')
        if player7.draw_button(WIN):
            print('player 7')

        if wroles.role[1] in wroles.bad:
            if waction.killbutton.draw_button(WIN):
                print('kill')
            if waction.assassinatebutton.draw_button(WIN):
                print('assassinate')

            if wroles.role[1] == wroles.alpha:
                if waction.concealbutton.draw_button(WIN):
                    print('conceal')

            elif wroles.role[1] == wroles.wolftrickster:
                if waction.trickbutton.draw_button(WIN):
                    print('trick')
        
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

if players == 8:
    WIDTH, HEIGHT = 850, 790
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Werewolf")

    roles = [wroles.alpha, wroles.wolftrickster, wroles.villager, wroles.medium, wroles.doctor, wroles.bodyguard, wroles.seer, wroles.wildcard]

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
        player5 = wbutton.Button(640,10,wroles.role[5])
        player6 = wbutton.Button(430,530,wroles.role[6])
        player7 = wbutton.Button(640,530,wroles.role[7])
        player8 = wbutton.Button(640,270,wroles.role[8])

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
        if player6.draw_button(WIN):
            print('player 6')
        if player7.draw_button(WIN):
            print('player 7')
        if player8.draw_button(WIN):
            print('player 8')

        if wroles.role[1] in wroles.bad:
            if waction.killbutton.draw_button(WIN):
                print('kill')
            if waction.assassinatebutton.draw_button(WIN):
                print('assassinate')

            if wroles.role[1] == wroles.alpha:
                if waction.concealbutton.draw_button(WIN):
                    print('conceal')

            elif wroles.role[1] == wroles.wolftrickster:
                if waction.trickbutton.draw_button(WIN):
                    print('trick')
        
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

if players == 9:
    WIDTH, HEIGHT = 850, 790
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Werewolf")

    roles = [wroles.alpha, wroles.wolftrickster, wroles.villager, wroles.villager, wroles.bodyguard, wroles.medium, wroles.doctor, wroles.seer, wroles.wildcard]

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
        player5 = wbutton.Button(640,10,wroles.role[5])
        player6 = wbutton.Button(430,530,wroles.role[6])
        player7 = wbutton.Button(640,530,wroles.role[7])
        player8 = wbutton.Button(640,270,wroles.role[8])
        player9 = wbutton.Button(430,270,wroles.role[9])

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
        if player6.draw_button(WIN):
            print('player 6')
        if player7.draw_button(WIN):
            print('player 7')
        if player8.draw_button(WIN):
            print('player 8')
        if player9.draw_button(WIN):
            print('player 9')

        if wroles.role[1] in wroles.bad:
            if waction.killbutton.draw_button(WIN):
                print('kill')
            if waction.assassinatebutton.draw_button(WIN):
                print('assassinate')

            if wroles.role[1] == wroles.alpha:
                if waction.concealbutton.draw_button(WIN):
                    print('conceal')

            elif wroles.role[1] == wroles.wolftrickster:
                if waction.trickbutton.draw_button(WIN):
                    print('trick')
        
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

if players == 10:
    WIDTH, HEIGHT = 850, 790
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Werewolf")

    roles = [wroles.alpha, wroles.wolftrickster, wroles.villager, wroles.villager, wroles.bodyguard, wroles.medium, wroles.doctor, wroles.seer, wroles.fool, wroles.hunter]

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
        player5 = wbutton.Button(640,10,wroles.role[5])
        player6 = wbutton.Button(430,530,wroles.role[6])
        player7 = wbutton.Button(640,530,wroles.role[7])
        player8 = wbutton.Button(640,270,wroles.role[8])
        player9 = wbutton.Button(430,270,wroles.role[9])
        player10 = wbutton.Button(10,270,wroles.role[10])

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
        if player6.draw_button(WIN):
            print('player 6')
        if player7.draw_button(WIN):
            print('player 7')
        if player8.draw_button(WIN):
            print('player 8')
        if player9.draw_button(WIN):
            print('player 9')
        if player10.draw_button(WIN):
            print('player 10')

        if wroles.role[1] in wroles.bad:
            if waction.killbutton.draw_button(WIN):
                print('kill')
            if waction.assassinatebutton.draw_button(WIN):
                print('assassinate')

            if wroles.role[1] == wroles.alpha:
                if waction.concealbutton.draw_button(WIN):
                    print('conceal')

            elif wroles.role[1] == wroles.wolftrickster:
                if waction.trickbutton.draw_button(WIN):
                    print('trick')
        
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
