import iros_interface_cmds as ic
import serial
import socket

def initialize():
    #HOST = "169.254.103.235" # The remote host
    HOST = "192.168.1.105" # The remote host
    HOST = "169.254.187.178"
    PORT = 30000 # The same port as used by the server

    print ".......................Starting Program......................."
    print ""

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT)) # Bind to the port
    s.listen(5) # Now wait for client connection.
    c, addr = s.accept() # Establish connection with client.

    print "Connected to UR"
    print ""
   
    ser_ee = serial.Serial('/dev/ttyACM0',9600)  # open serial port
    while ser_ee.isOpen()==False:
        print "Waiting for serial"
    print ser_ee.name, ": ",ser_ee.readline()         # check which port was really used
    print "Ready"
    return c, ser_ee

c, _ = initialize()
home = {"x": 90.0, "y": -500.0, "z": 100.0, "rx": 0.0, "ry": 180.0, "rz": 0.0}

ic.safe_ur_move(c,Pose=home,CMD=4)