# -*- coding: utf-8 -*-
"""File Name：     demo_client
   date：          2019/1/10"""
__author__ = 'GaoShuai'
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.113", 7777))

while True:
    cmd = input(">>:").strip()
    # if len(mgs) == 0:continue
    if cmd == "exit":
        break
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024) # 接受命令结果的长度
    # data = client.recv(1024)
    print("命令结果长度", cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size +=len(data) # 每次接受有可能小于1024， 所以必须用len判断
        # print(received_size)
        # print(data.decode())
        received_data += data
    else:
        print("cmd res receive done..", received_size)
        # bytes类型解码一下即可
        print(received_data.decode())
client.close()




