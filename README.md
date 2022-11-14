<h2>About program:</h2>
 Robot is searching for silver token, if he finds it he goes to it and pick it up and then
he starts searching for golden token. If he finds it, he approaches it and release next to it a silver token.
Whole procedure repeats 6 times, when the robot places all the silver tokens next to golden ones the program finishes
and a message "End of algorithm!" is shown on the screen. When robot finds a silver/golden token he adds it to a dictionary in purpose to remember, that
he made a pair with silver/golden one. In program there were used functions, for, while and if loops.

<h2>How to run it:</h2>
 In CLI we have to run a command python2 run.py assignment.py

<h2>Pseudocode:</h2>

```
Setting variable a_th to 2
Setting variable d_th to 0.4
Setting variable d_th_g to 0.5
Setting variable taken to 0	
Creating object from class Robot
for i from 0 to 6 :
	while taken is equal 0:
 		Set variable dist to 100
  		for token in R.see():
      			if token.dist is less than dist and token.info.marker_type is equal to MARKER_TOKEN_SILVER and token.info.code is not in the dictionary markers_silver:
				Set dist to token.dist
	    			Set rot_y to token.rot_y  
    		if dist is equal to 100:
			return -1, -1
    		else:
			return dist, rot_y
        	if dist is equal to -1:
			print "Searching for token"
			Set an angular velocity to 10 for 1 second
    		else if dist is less than d_th:
        		Grab the token
        		for token in R.see():
        			if (token.dist is less than d_th) and (token.info.marker_type is equal to MARKER_TOKEN_SILVER):
        				Set key in markers_silver dictionary to token.info.marker_type value
			print "Silver token grabbed"
			Set a linear velocity for -30 for 1 second
			Set an angular velocity to 9 for 6 second
			Set taken to 1
      		else if -a_th is less or equal than rot_y and rot_y is less or equal than a_th:
			print "Well aligned"
			Set a linear velocity for 30 for 0.5 second
        	else if rot_y is less than -a_th: 
			print "Move on left"
			Set an angular velocity to -2 for 0.5 second
        	else if rot_y is greater than a_th:
			print "Move on right"
			Set an angular velocity to 2 for 0.5 second
	while taken is equal to 1:
		Set dist to 100
    		for token in R.see():
        		if token.dist is less than dist and token.info.marker_type is equal to MARKER_TOKEN_GOLD and token.info.code is not in dictionary markers_gold:
            			Set dist to token.dist
	    			Set rot_y to token.rot_y
    		if dist is equal to 100:
			return -1, -1
    		else:
			return dist, rot_y
    		if dist is equal to -1: 
			print "Searching for token"
			Set an angular velocity to 15 for 1 second
    		else if dist is less than d_th_g: 
    		        Release the token
        		print "Silver token released"
        		for token in R.see():
        			if (token.dist is less than d_th_g) and (token.info.marker_type is equal to MARKER_TOKEN_GOLD):
					Set key in markers_gold dictionary to token.info.marker_type value
        		Set a linear velocity for -20 for 1 second
        		Set an angular velocity to 10 for 6 second
	    		Set taken to 0
    		else if -a_th is less or equal to rot_y and rot_y is less or equal a_th:
			print "Well aligned"
        		Set a linear velocity for 20 for 0.5 second
    		else if rot_y is less than -a_th:
        		print "Move on left"
        		Set an angular velocity to -2 for 0.5 second
    		else if rot_y is greater than a_th:
        		print "Move on right"
        		Set an angular velocity to 2 for 0.5 second
print "End of algorithm!"
```

    

<h2>Possible improvements:</h2>

 - Robot could react and move faster
 - Robot could choose more optimal way to reach tokens

