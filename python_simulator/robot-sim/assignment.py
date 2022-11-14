#importing libraries
from __future__ import print_function
import time
from sr.robot import *
a_th = 2.0 #threshold for the control of the linear distance
d_th = 0.4 #threshold for the control of the orientation
d_th_g = 0.5 #threshold for the control of the orientation
taken = 0 #variable that indicates if silver token is taken by robot
markers_silver = {} #dictionary for silver tokens, that are placed next to golden tokens
markers_gold = {} #dictionary for golden tokens, that are placed next to golden tokens

#function for setting a linear velocity
#args: speed (int): the speed of the wheels, seconds (int): the time interval
def drive(speed, seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
#function for setting an angular velocity
#args: speed (int): the speed of the wheels, seconds (int): the time interval
def turn(speed, seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
#function to find the closest silver token
#returns: dist (float): distance of the closest silver token (-1 if no silver token is detected), rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)    
def find_silver_token():
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and token.info.code not in markers_silver:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
	return dist, rot_y
	
#function to find the closest golden token   	
#returns: dist (float): distance of the closest golden token (-1 if no golden token is detected), rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
def find_golden_token():
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and token.info.code not in markers_gold:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
	return dist, rot_y

#function to lead robot to the golden token and put a silver token next to golden one 	
def go_to_gold():
	global taken
	while(taken==1):
		dist, rot_y = find_golden_token()
    		if dist==-1: # if no token is detected, we make the robot turn 
			print("Searching for token")
			turn(15, 1)
    		elif dist <d_th_g: # if we are close to the token, we release it.
    		        R.release() #release the token
        		print("Silver token released")
        		for token in R.see():
        			if (token.dist <d_th_g) and (token.info.marker_type is MARKER_TOKEN_GOLD):
        				markers_gold[token.info.code] = token.info.marker_type
        		drive(-20,1)
        		turn(10, 6)
	    		taken = 0
    		elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
			print("Well aligned")
        		drive(20, 0.5)
    		elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        		print("Move on left")
        		turn(-2, 0.5)
    		elif rot_y > a_th:
        		print("Move on right")
        		turn(2, 0.5)
        		
#function to lead robot to the silver token and grab it      
def go_to_silver():
	global taken
	while(taken==0):
		dist, rot_y = find_silver_token()
        	if dist==-1: # if no token is detected, we make the robot turn 
			print("Searching for token")
			turn(10, 1)
    		elif dist <d_th: # if we are close to the token, we grab it.
        		R.grab()# grab the token
        		for token in R.see():
        			if (token.dist <d_th) and (token.info.marker_type is MARKER_TOKEN_SILVER):
        				markers_silver[token.info.code] = token.info.marker_type
			print("Silver token grabbed")
			drive(-30,1)
			turn(9, 6)
			taken = 1
    		elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
			print("Well aligned")
			drive(30, 0.5)
        	elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
			print("Move on left")
			turn(-2, 0.5)
        	elif rot_y > a_th:
			print("Move on right")
			turn(2, 0.5)
#main			
R = Robot()
for i in range (0, 6):
	go_to_silver()
	go_to_gold()
print("End of algorithm!")