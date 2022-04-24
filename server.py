import socket
from _thread import *

server = "172.16.136.216"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(10000)
print("Waiting for a connection, Server Started")


def read_pos(str1,player):

    str1 = str1.split(",")

    if str1[0] == "message":
        global message
        message = str1[1]

    elif str1[0] == "name":
        playernames.append(str1[1]+","+str(player))

    return " "


def make_pos(list1):
    global message
    playnamesstring = ""
    for i in range(0,len(playernames)):
        temp = playernames[i].split(",")
        playnamesstring = playnamesstring + temp[0] + ","
    return str(list1) + "," + message + "," + playnamesstring


playernames = []
sentplayernames = []
message = ""
attendancelist = ["A","A","A","A","A","A"]

def threaded_client(conn, player):

    while True:
        try:
            global currentPlayer
            try:
                data = read_pos(conn.recv(4096*100).decode(),player)
            except ValueError:

                currentPlayer = currentPlayer - 1
                try:
                    for i in range(0,len(playernames)):
                        if str(player) in playernames[i]:
                            playernames.remove(playernames[i])
                except:
                    pass
                break

            if not data:
                print("Disconnected")
                try:
                    for i in range(0, len(playernames)):
                        if str(player) in playernames[i]:
                            playernames.remove(playernames[i])
                except:
                    pass
                break

            conn.sendall(str.encode(make_pos(data)))

            print(playernames)
        except socket.error:
            print(socket.error)
            break

    print("Lost connection")
    attendancelist[currentPlayer] = "A"

    try:
        for i in range(0, len(playernames)):
            if str(player) in playernames[i]:
                playernames.remove(playernames[i])
    except:
        pass
    print(playernames)
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()

    #print("Connected to:", addr)
    for i in range(0, len(attendancelist)):
        if attendancelist[i] == "A":
            currentPlayer = i
            attendancelist[i] = "P"
            break
    start_new_thread(threaded_client, (conn, currentPlayer))




