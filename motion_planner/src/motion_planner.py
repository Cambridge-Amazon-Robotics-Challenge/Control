
import iros_interface_cmds as ic
import iros_waypoints as iw
import serial
import socket
import math

class MotionPlanner():

    def __init__(self, h_pick, host, port):
        self.h_pick = h_pick 
        # the hight relative to the object to move to first before starting to pick
        
        self._connect_to_ur5(host, port) 
        # host: The remote host
        # port: The same port as used by the server

    def _connect_to_ur5(self, host, port):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port)) # Bind to the port
        sock.listen(5) # Now wait for client connection.
        self.conn, addr = sock.accept() # Establish connection with client.


    def move_to_grabbing_points(self, x1, y1, x2, y2, depth):

        prep_pose = [(x1+x2)/2, (y1+y2)/2, depth-self.h_pick]
        self._move_end_to_position(prep_pose)

        angle = math.degrees(math.atan((y1-y2)/(x1-x2)))
        self._move_grabber_to_angle(angle)

        pick_pose = prep_pose
        pick_pose[2] += self.h_pick
        self._move_end_to_position(pick_pose)

    def move_to_home(self):
        ic.safe_ur_move(self.conn, iw.home, 4)

    def _pose_from_array(self, arr):
        assert(len(arr) == 6)

        pose = {}
        pose['x'] = arr[0]
        pose['y'] = arr[1]
        pose['z'] = arr[2]
        pose['rx'] = arr[3]
        pose['ry'] = arr[4]
        pose['rz'] = arr[5]

        return pose

    def _get_neutral_axis_angle(self):
        return list((iw.home['rx'], iw.home['ry'], iw.home['rz']))


    def _move_end_to_position(self, position):
        
        pose_arr = [0]*6
        pose_arr[:3] = list(position)
        pose_arr[3:] = self._get_neutral_axis_angle()
        pose = self._pose_from_array(pose_arr)
        
        ic.safe_ur_move(self.conn,Pose=pose,CMD=4)


    def _move_grabber_to_angle(self, angle): # assume pointing straight down

        joint_pos = ic.get_ur_position(self.conn, 3)
        joint_pos[5] -= angle   # rotate end joint by angle
        ic.safe_ur_move(self.conn,Pose=joint_pos,CMD=2)
