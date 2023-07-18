
# programa sacado de curso Python Programming & Cybersec - UDEMY

import os

for x in range(60, 80):
    host = '192.168.1.' + str(x)
    ping_test = os.system("ping -c 1 " + host + " > /dev/null") # os.system() to run commands
    if ping_test == 0:
        print(f"ping al {host} es exitoso")
    else:
        print(f"No hay conexion al {host}")
