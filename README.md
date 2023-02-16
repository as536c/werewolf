# Werewolf project

# Install pygame to run the app, werewolf.py main app.

Werewolf is a deception party game that can currently be played by 5-10 people. The goal is simple, werewolves try to kill the villagers, while the villagers figure out who the werewolf/ves are/is and lynch them. Neutral characters are also introduced in this game where they don't side with neither villagers nor werewolves and can win the game in their own terms.

# Rules:

1. Players get their roles at the start of the game. Werewolves (if there are more than 1) will be able to tell who are their team mates while villagers don't.
2. The game starts on a night phase where werewolves can kill and villagers can utilize their abilities (if there are any).

Dev notes:
- Improve visuals (player cards, action PNG files)
- Focus polishing 5 player first before proceeding to add 6-10 players.

To test game:
1. run *server.py*, this will append random roles in *wroles.py* file, this is to make consistent roles across all players.
2. run *werewolf.py* on terminal. This can run 2 instances for now, for testing purposes but should run 5 clients.
    >> python3 werewolf.py
