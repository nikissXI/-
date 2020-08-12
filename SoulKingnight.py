import socket

PORT = 23333

def send():
    players = ["10.6.0.3", "10.6.0.16", ""]
    #上面3个IP就是代表对谁发包，现在是对10.6.0.3，10.6.0.16发包，只有他们会搜到房间
    #要和谁玩就填谁的虚拟局域网IP地址
    #没有的就直接空着或者直接写网关地址
    players = [player for player in players if player != ""]
    socks = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM) for i in players]
    print("准备完毕，可以创建房间。创建房间后切到此应用发包，其他人搜到房间后就切回去游戏")

    while True:
        for i in range(len(players)):
            hostData, hostAddr = hostRecv.recvfrom(1024)
            if len(hostData) > 0 and hostAddr[0] not in players:
                socks[i].sendto(hostData, (players[i], PORT))
                print(f"对{players[i]}发包成功")

if __name__ == "__main__":
    hostRecv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostRecv.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST
                        or socket.SO_REUSEADDR, 1)

    try:
        hostRecv.bind(("", PORT))
        send()
    except Exception as e:
        print("错误，重新打开Python3IDE")
