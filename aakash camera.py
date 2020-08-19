import cv2 
import time 
import cv2

# AAKASH 
# Click picture with timer
# Timer start to press SPACE
TIMER = int(10) 

# Open the camera 
cap = cv2.VideoCapture(0) 


while True: 
	
	# Read and display each frame 
	ret, img = cap.read() 
	cv2.imshow('a', img) 

	# check for the key pressed 
	k = cv2.waitKey(125)

	# set the key for the countdown 
	# to begin. Here we set SPACE 
	# if key pressed is SPACE 
	if k == ord(' '): 
		prev = time.time() 

		while TIMER >= 0: 
			ret, img = cap.read() 

			# Display countdown on each frame 
			# specify the font and draw the 
			# countdown using puttext 
			font = cv2.FONT_HERSHEY_PLAIN 
			cv2.putText(img, str(TIMER), 
						(270, 280), font, 
						7, (0, 255, 3), 
						5, cv2.LINE_AA) 
			cv2.imshow('a', img) 
			cv2.waitKey(125) 

			# current time 
			cur = time.time() 

			# Update and keep track of Countdown 
			# if time elapsed is one second 
			# than decrese the counter 
			if cur-prev >= 1: 
				prev = cur 
				TIMER = TIMER-1

		else: 
			ret, img = cap.read() 

			# Display the clicked frame for 2 
			# sec.You can increase time in 
			# waitKey also 
			cv2.imshow('a', img) 

			# time for which image displayed 
			cv2.waitKey(2000) 

			# Save the frame 
			cv2.imwrite('aakash_camera.jpg', img) 

			# HERE we can reset the Countdown timer 
			# if we want more Capture without closing 
			# the camera 

	# Press Esc to exit 
	elif k == 27: 
		break

       
                

# close the camera 
cap.release() 

# close all the opened windows 
cv2.destroyAllWindows()
