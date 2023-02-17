import socket
import sys
import random
import threading
import time

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
PORT2 = 5556
clients = {}
challenger = 1

#TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f'[*] Listening on {HOST}:{PORT}')
#connects players
while challenger < 3:
    try:
        client_socket, address = server_socket.accept()
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
    clients[address] = client_socket
    print(f'[*] Accepted connection from {address[0]}:{address[1]}')   
    request = client_socket.recv(1024)
    chal_str = str(challenger)
    chal_bytes = chal_str.encode()
    challenger += 1
    client_socket.send(chal_bytes)
    x = request.decode("utf-8")
    print("Player name:", x)  
    client_socket.close()

server_socket.close()
print('Initializing...')
time.sleep(5)

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((HOST, PORT2))
tcp_socket.listen(5)
print('[*] Game initiated. Press Ctrl-C to Exit')

def handle_client(tcp_socket):
    with tcp_socket as sock:
        while True:
            com = sock.recv(1024)
            if com.decode('utf-8') == 'sync':
                sock.send(com)
                print('sync')
            else:
                for c in clients.keys():
                    sock.sendto(com, c)
                    print('sent to', c)    
                    time.sleep(1)

while True:
    try:
        client, tcp_address = tcp_socket.accept()        
    except KeyboardInterrupt:                        
        print("\nClosing Server Socket...")
        #remove appended roles in wroles.py, for a fresh start
        with open("wroles.py", 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[:-6])
        tcp_socket.close()
        sys.exit()
    
    print(f'[*] Accepted connection from {address[0]}:{address[1]}')
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()



#after players connect, this segment should be server constantly accepting commands from client. (not working)     
#server_socket.close()
#udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#udp_socket.bind((HOST, PORT))
#udp_clients = {}
#print('bound')
#try:
#    while True:
#        data, udp_client = udp_socket.recvfrom (1024)
#        udp_clients[udp_client] = udp_socket
#        com = data.decode("utf-8")
#        print(com)
#        for client in clients.keys():
#            time.sleep(2)
#            udp_socket.sendto(b'from server', client)
#            print('sent to', client)
##except KeyboardInterrupt or ConnectionResetError or BrokenPipeError or OSError:
 #   print('\nClosing Server Socket...')
    #remove appended roles in wroles.py, for a fresh start
#    with open("wroles.py", 'r+') as fp:
#        lines = fp.readlines()
#        fp.seek(0)
#        fp.truncate()
#        fp.writelines(lines[:-6])
#    udp_socket.close()
#    sys.exit()



    #send toggle info to clients
    #while True:
    #    ClientMsg = input(' -> ')
    #    client_socket.send(ClientMsg.encode())
    #    client_socket.close()
    

    #server needs to update (send heartbeat every game event) the following in the clients:
    # > players states (alive/dead/tricked/protected,etc)
    # > night/day
    # > 