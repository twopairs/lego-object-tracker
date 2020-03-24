import paramiko
import sys
import time
import shutil

while True:
    host = "192.168.1.6"
    port = 22
    transport = paramiko.Transport((host, port))

    username = "pi"                #hard-coded
    password = "raspberry"                #hard-coded
    transport.connect(username = username, password = password)

    sftp = paramiko.SFTPClient.from_transport(transport)
    path = '/home/pi/image.jpg'   #hard-coded
    localpath = './image.jpg'
    sftp.get(path, localpath)
    sftp.close()
    transport.close()

    time.sleep(5)



