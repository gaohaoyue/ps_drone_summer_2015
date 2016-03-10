__author__ = 'gary'
#########
# firstVideo.py
# This program is part of the online PS-Drone-API-tutorial on www.playsheep.de/drone.
# It shows the general usage of the video-function of a Parrot AR.Drone 2.0 using the PS-Drone-API.
# The drone will stay on the ground.
# Dependencies: a POSIX OS, openCV2, PS-Drone-API 2.0 beta or higher.
# (w) J. Philipp de Graaff, www.playsheep.de, 2014
##########
# LICENCE:
#   Artistic License 2.0 as seen on http://opensource.org/licenses/artistic-license-2.0 (retrieved December 2014)
#   Visit www.playsheep.de/drone or see the PS-Drone-API-documentation for an abstract from the Artistic License 2.0.
###########

##### Suggested clean drone startup sequence #####
import time, sys
import ps_drone                                              # Import PS-Drone

drone = ps_drone.Drone()                                     # Start using drone
drone.startup()                                              # Connects to drone and starts subprocesses

drone.reset()                                                # Sets drone's status to good (LEDs turn green when red)
while (drone.getBattery()[0] == -1):      time.sleep(0.1)    # Waits until drone has done its reset
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	# Gives a battery-status
drone.useDemoMode(True)                                      # Just give me 15 basic dataset per second (is default anyway)

##### Mainprogram begin #####
drone.setConfigAllID()                                       # Go to multiconfiguration-mode
drone.sdVideo()                                              # Choose lower resolution (hdVideo() for...well, guess it)
drone.frontCam()                                             # Choose front view
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001) # Wait until it is done (after resync is done)
drone.startVideo()                                           # Start video-function
drone.showVideo()                                            # Display the video

##### And action !
print "Use <space> to toggle front- and groundcamera, any other key to stop"
IMC =    drone.VideoImageCount                               # Number of encoded videoframes
stop =   False
ground = False

while not stop:
    while drone.VideoImageCount == IMC: time.sleep(0.01)     # Wait until the next video-frame
    IMC = drone.VideoImageCount
    key = drone.getKey()                                     # Gets a pressed key
    if key==" ":
        if ground:              ground = False
        else:                   ground = True
        drone.groundVideo(ground)                            # Toggle between front- and groundcamera. Hint: options work for all videocommands
    elif key == "l":
	if drone.NavData["demo"][0][2] and not drone.NavData["demo"][0][3]:	drone.takeoff()
	else:	drone.land()
    elif key == "0":	drone.hover()
    elif key == "w":	drone.moveForward()
    elif key == "s":	drone.moveBackward()
    elif key == "a":	drone.moveLeft()
    elif key == "d":	drone.moveRight()
    elif key == "q":	drone.turnLeft()
    elif key == "e":	drone.turnRight()
    elif key == "7":	drone.turnAngle(-10,1)
    elif key == "9":	drone.turnAngle( 10,1)
    elif key == "4":	drone.turnAngle(-45,1)
    elif key == "6":	drone.turnAngle( 45,1)
    elif key == "1":	drone.turnAngle(-90,1)
    elif key == "3":	drone.turnAngle( 90,1)
    elif key == "8":	drone.moveUp()
    elif key == "2":	drone.moveDown()
    elif key == "*":	drone.doggyHop()
    elif key == "+":	drone.doggyNod()
    elif key == "-":	drone.doggyWag()
    elif key != "":		stop = True

if __name__ == "__main__":
	colour_tracker = ColourTracker()
	colour_tracker.run()
	print "the cx is: \n"
	cx = int(drone.vCapture.moment['m10']/drone.vCapture.moment['m00'])
	print cx
	#cy = int(M['m01']/M['m00'])






