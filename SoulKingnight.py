import socket

PORT = 23333

if __name__ == "__main__":
    players = ["10.6.0.3", "10.6.0.14", "10.6.0.1"]
    #上面3个IP就是代表对谁发包，现在是对3，14号发包，只有他们会搜到房间
    #要和谁玩就改谁的编号，10.6.0.这部分不要动！就改第四段数字就行
    #空的地方填10.6.0.1

    hostRecv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostRecv.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST
                        or socket.SO_REUSEADDR, 1)

    try:
        hostRecv.bind(("", PORT))
    except Exception as e:
        print("失败，重新打开此程序，如果创建了房间先退出房间")
        exit

    players = [player for player in players if player != ""]
    socks = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM) for i in players]
    print("准备完毕，可以创建房间。创建房间后切到此应用发包，其他人搜到房间后就切回去游戏")

    while True:
        for i in range(len(players)):
            hostData, hostAddr = hostRecv.recvfrom(1024)
            if len(hostData) > 0 and hostAddr[0] not in players:
                socks[i].sendto(hostData, (players[i], PORT))
                print(f"对{players[i]}发包成功")