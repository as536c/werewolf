import socket
import sys
import random

#this will append roles in wroles.py file upon server startup. this is to ensure that there will be similar roles across players
wildcard = ['fool', 'hunter']
bad = ['wolf', 'alpha', 'wolftrickster']
roles = ['bad', 'villager', 'doctor', 'seer', 'wildcard']

for n in range(1, 6):
    if n != 5:
        role = random.choice(roles)
        roles.remove(role)
        if role == 'bad':
            role = random.choice(bad)
            bad.remove(role)
            with open("wroles.py", "a") as f:
                f.write(" " + str(n) + ": " + role + ",\n")
        elif role == 'wildcard':
            role = random.choice(wildcard)
            wildcard.remove(role)
            with open("wroles.py", "a") as f:
                f.write(" " + str(n) + ": " + role + ",\n")
        else:
            with open("wroles.py", "a") as f:
                f.write(" " + str(n) + ": " + role + ",\n")     # 1: villager,
    else:
        role = random.choice(roles)
        roles.remove(role)
        if role == 'bad':
            role = random.choice(bad)
            bad.remove(role)
            with open("wroles.py", "a") as f:
                f.write(" " + str(n) + ": " + role + "\n}")
        elif role == 'wildcard':
            role = random.choice(wildcard)
            wildcard.remove(role)
            with open("wroles.py", "a") as f:
                f.write(" " + str(n) + ": " + role + "\n}")
        else:
            with open("wroles.py", "a") as f:
                f.write(" " + str(n) + ": " + role + "\n}") 

#server states
p1_state = ['alive']
p2_state = ['alive']
p3_state = ['alive']
p4_state = ['alive']
p5_state = ['alive']

HOST = '127.0.0.1'
PORT = 5555
clients = {}

#TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f'[*] Listening on {HOST}:{PORT}')
challenger = 1
#connects players
while challenger < 3:
    try:
        client_socket, address = server_socket.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        clients[address] = client_socket
        request = client_socket.recv(512)
        print(f'[*] Received: {request.decode("utf-8")}')
        x = request.decode("utf-8")
        chal_str = str(challenger)
        chal_bytes = chal_str.encode()
        client_socket.send(chal_bytes)
        challenger += 1
        print("Player name:", x)    
        client_socket.close()
    except KeyboardInterrupt or ConnectionResetError or BrokenPipeError:
        print('\nClosing Server Socket...')
        #remove appended roles in wroles.py, for a fresh start
        with open("wroles.py", 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[:-6])
        server_socket.close()
        sys.exit()
#after players connect, this segment should be server constantly accepting commands from client. (not working)     
server_socket.close()
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT))
print('bound')
try:
    while True:
        data, client = udp_socket.recvfrom (1024)
        com = data.decode("utf-8")
        print(com) 
        udp_socket.sendto(b'from server', client)
except KeyboardInterrupt or ConnectionResetError or BrokenPipeError or OSError:
    print('\nClosing Server Socket...')
    #remove appended roles in wroles.py, for a fresh start
    with open("wroles.py", 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[:-6])
    udp_socket.close()
    sys.exit()
    #send toggle info to clients
    #while True:
    #    ClientMsg = input(' -> ')
    #    client_socket.send(ClientMsg.encode())
    #    client_socket.close()
    

    #server needs to update (send heartbeat every game event) the following in the clients:
    # > players states (alive/dead/tricked/protected,etc)
    # > night/day
    # > 