# -*- coding: utf-8 -*-
"""File Name：     demo
   date：          2019/1/10"""
import os

__author__ = 'GaoShuai'
# 服务器
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 7777))
server.listen(5)
while True:
    conn, addr = server.accept() # 阻塞

    while True:
        print("new conn", addr)
        data = conn.recv(1024) # 不超过8192
        # 默认是阻塞的
        if not data:
            print("客户端已断开")
            break # 客户端已断开， conn, recv收到的就都是空数据
        # decode()
        print("执行指令:",data.decode())
        # 需要在打开指令后  将bytes 转换了一下decode()
        cmd_res = os.popen(data.decode()).read() # 接受字符串 执行结果也是字符串
        print("before send", len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output.."
        #  大小  中文字符占3个字节
        conn.send( str(len(cmd_res.encode())).encode("utf-8")  )  # 先发大小 给客户端
        conn.send(cmd_res.encode("utf-8"))
        print("send done")

server.close()

