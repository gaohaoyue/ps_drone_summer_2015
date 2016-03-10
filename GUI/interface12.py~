#import Tkinter as tk
from Tkinter import *
import cv2
from collections import deque
import time
import Image, ImageTk
import numpy as np
import Queue
import ps_drone
import threading
import math

class Application: # This is the GUI interface class. 
	def __init__(self, master):
		self.master = master
		self.frame = Frame(self.master)
		self.frame.pack()
		self.labelface = Label(self.master, text="AR Drone 2.0",font=25)
		self.labelface.pack()
		self.button1 = Button(
			self.frame, name="button1", text="Facial Detection", fg="red", command=self.faced,
			bd=5,padx=70,pady=50,font=25)
		self.button1.pack(side=LEFT)
		self.button2 = Button(
			self.frame, name="button2", text="Manual", command=self.man,bd=5,padx=70,pady=50,font=25
			)
		self.button2.pack()
		self.button3 = Button(master=root,text ='exit', bg = 'green',command=self.quitroot,bd=5,padx=70,pady=50,font=25)
		self.button3.pack()
		self.cam = cv2.VideoCapture(0)
		self.mydrone = Ar_drone() #Create the drone instance
		self.current_page = "Main"
		#self.deter = False

	def quitroot(self):
		
		quit(self.master)
		quit(root)
		del self.mydrone
	def faced(self):  #This is the face mode GUI.
		
		
		self.button1.destroy()
		self.button2.destroy()
		self.button3.destroy()
		self.labelface.destroy()
		self.frame.destroy()

		self.topframe = Frame(self.master)
		self.topframe.pack()
		self.botframe = Frame(self.master)
		self.botframe.pack(side=BOTTOM)

		self.name = Label(self.master,text = 'face tracking',font=25)
		self.name.pack()

		self.button4 = Button(self.botframe, text="Go back",bd=5,font=25,command=self.gobackface)
		self.button4.pack()
		self.image_label = Label(master=self.master)
		self.image_label.pack()
		self.threadLock = threading.RLock()
		self.q = Queue.Queue(maxsize=100)
		self.t1=imag(self.mydrone,'t1',self.q,self.threadLock)
		self.t2=imag(self.mydrone,'t2',self.q,self.threadLock)
		#self.t4=imag(self.mydrone,'t4',self.q,self.threadLock)
		#self.t5=imag(self.mydrone,'t5',self.q,self.threadLock)
		#self.t6=imag(self.mydrone,'t6',self.q,self.threadLock)
		#self.t7=imag(self.mydrone,'t7',self.q,self.threadLock)
		self.t3=showimag(self.image_label,self.q,self.mydrone)
		self.mydrone.takeoff()
		time.sleep(1)
		self.mydrone.stop()
		self.t1.start()
		self.t2.start()
		#self.t4.start()
		#self.t5.start()
		#self.t6.start()
		#self.t7.start()
		self.t3.start()

	def gobackface(self): # Go back to main GUI from face mode
		self.mydrone.land()
		self.mydrone.reset()
		self.mydrone.printBattery()

		self.t1.delete()
		self.t2.delete()
		self.t3.delete()
		#self.t4.delete()
		#self.t5.delete()
		#self.t6.delete()
		#self.t7.delete()
		self.t1.join()
		self.t2.join()
		self.t3.join()
		#self.t4.join()
		#self.t5.join()
		#self.t6.join()
		#self.t7.join()
		cv2.destroyAllWindows()
		self.current_page = "Main"
		self.mydrone.reset()


		self.button4.destroy()
		self.name.destroy()
		self.image_label.destroy()
		self.topframe.destroy()
		self.botframe.destroy()
		#self.deter = True

		


		self.frame = Frame(self.master)
		self.frame.pack()
		self.labelface = Label(self.master, text="AR Drone 2.0",font=25)
		self.labelface.pack()		
		self.button1 = Button(
			self.frame, name="button1", text="Facial Detection", fg="red", command=self.faced,
			bd=5,padx=70,pady=50,font=25)
		self.button1.pack(side=LEFT)
		self.button2 = Button(
			self.frame, name="button2", text="Manual", command=self.man,bd=5,padx=70,pady=50,font=25
			)
		self.button2.pack()
		self.button3 = Button(self.master,text ='exit', bg = 'green',command=self.quitroot,bd=5,padx=70,pady=50,font=25)
		self.button3.pack()

		
				
		
	def man(self): # This is the manual Mode. Use up, down, left, right arrow and a, d, w, s to control the drone. When the key is pressed, the corresponding button on the GUI will turn green. Click goback button to go back to main GUI
		print "manual control"
		self.button1.destroy()
		self.button2.destroy()
		self.button3.destroy()
		self.labelface.destroy()
		self.frame.destroy()
		#Define Top and Bottom Frame for Video Display and Command Buttons
		self.current_page = "Manual"
		self.topframe = Frame(self.master)
		self.topframe.pack()
		self.botframe = Frame(self.master)
		self.botframe.pack(side=BOTTOM)
		self.name = Label(self.master,text = 'Manual Control Mode',font=25)
		self.name.pack()

		#Define the Video Display on Top Frame
		self.image_label = Label(master=self.topframe)
		self.image_label.pack()
		if (self.current_page == "Manual"):
			self.topframe.after(0, func=lambda: self.update_all())

		#Define the Command Buttons on Bottom Frame
		self.button14 = Button(self.botframe, text= "Go Back", bd=5, font=25, command=self.goback_man
			)
		self.button14.pack()
		self.button4 = Button(self.botframe, text= "Take Off", bd=5, font=25			
			)
		self.button4.pack()
		self.button5 = Button(self.botframe, text= "Stop", bd=5, font=25			
			)
		self.button5.pack()
		self.button6 = Button(self.botframe, text= "Move Left", bd=5, font=25			
			)
		self.button6.pack()
		self.button7 = Button(self.botframe, text= "Move Right", bd=5, font=25			
			)
		self.button7.pack()
		self.button8 = Button(self.botframe, text= "Move Forward", bd=5, font=25			
			)
		self.button8.pack()
		self.button9 = Button(self.botframe, text= "Move Backward", bd=5, font=25			
			)
		self.button9.pack()
		self.button10 = Button(self.botframe, text= "Move Up", bd=5, font=25			
			)
		self.button10.pack()
		self.button11 = Button(self.botframe, text= "Move Down", bd=5, font=25			
			)
		self.button11.pack()
		self.button12 = Button(self.botframe, text= "Turn Left", bd=5, font=25			
			)
		self.button12.pack()
		self.button13 = Button(self.botframe, text= "Turn Right", bd=5, font=25			
			)
		self.button13.pack()


		#Bind the button with keypress and key-release
		self.botframe.focus_set()
		self.botframe.bind("<Key>",self.guiKey)
		self.botframe.bind("<KeyRelease>",self.keyrel)

	def guiKey(self,event):	 # Key pressed binding function.
		if event.char == ' ':
			current_mode=self.button4.cget('text')
			if (current_mode == "Take Off"):
				self.button4.config(bg="green")	
				self.button4.config(text="Land")
				self.mydrone.takeoff()
			elif (current_mode == "Land" ):
				self.button4.config(bg="#d9d9d9")
				self.button4.config(text="Take Off")
				self.button5.config(bg="#d9d9d9")
				self.mydrone.land()
				self.mydrone.printBattery()

		elif event.keysym == 'Return' and self.button4.cget('text') == "Land":
			current_stop_color=self.button5.cget('bg')
			if (current_stop_color != "red"):
				self.button5.config(bg="red")	
				self.mydrone.stop()
			else:
				self.button5.config(bg="#d9d9d9")
				self.mydrone.doggyHop()

		elif event.char == 'a' and self.button4.cget('text') == "Land" and self.button5.cget('bg') !="red":
			self.button6.config(bg="green")	#Move Left
			self.mydrone.moveLeft()

		elif event.char == 'd' and self.button4.cget('text') == "Land" and self.button5.cget('bg') !="red":
			self.button7.config(bg="green")	#Move Right
			self.mydrone.moveRight()

		elif event.keysym == 'Up' and self.button4.cget('text') == "Land" and self.button5.cget('bg') !="red":
			self.button8.config(bg="green")	#Move Forward
			self.mydrone.moveForward()

		elif event.keysym == 'Down' and self.button4.cget('text') == "Land" and self.button5.cget('bg') !="red":
			self.button9.config(bg="green")	#Move Backward
			self.mydrone.moveBackward()

		elif event.char == 'w' and self.button4.cget('text') == "Land" and self.button5.cget('bg') !="red":
			self.button10.config(bg="green") #Move Up
			self.mydrone.moveUp()

		elif event.char == 's' and self.button4.cget('text') == "Land" and self.button5.cget('bg') !="red":
			self.button11.config(bg="green") #Move Down
			self.mydrone.moveDown()

		elif event.keysym == 'Left' and self.button4.cget('text') == "Land" and self.button5.cget('bg') !="red":
			self.button12.config(bg="green") #Turn Left
			self.mydrone.turnLeft()

		elif event.keysym == 'Right' and self.button4.cget('text') == "Land" and self.button5.cget('bg') !="red":
			self.button13.config(bg="green") #Turn Right
			self.mydrone.turnRight()

	def keyrel(self, event): # key release binding functions
		if event.char == 'a' and self.button4.cget('text') == "Land":
			self.button6.config(bg="#d9d9d9")
			self.mydrone.stop()
		elif event.char == 'd' and self.button4.cget('text') == "Land":
			self.button7.config(bg="#d9d9d9")
			self.mydrone.stop()
		elif event.keysym == 'Up' and self.button4.cget('text') == "Land":
			self.button8.config(bg="#d9d9d9")
			self.mydrone.stop()
		elif event.keysym == 'Down' and self.button4.cget('text') == "Land":
			self.button9.config(bg="#d9d9d9")
			self.mydrone.stop()
		elif event.char == 'w' and self.button4.cget('text') == "Land":
			self.button10.config(bg="#d9d9d9")
			self.mydrone.stop()
		elif event.char == 's' and self.button4.cget('text') == "Land":
			self.button11.config(bg="#d9d9d9")
			self.mydrone.stop()
		elif event.keysym == 'Left' and self.button4.cget('text') == "Land":
			self.button12.config(bg="#d9d9d9")
			self.mydrone.stop()
		elif event.keysym == 'Right' and self.button4.cget('text') == "Land":
			self.button13.config(bg="#d9d9d9")
			self.mydrone.stop()
		
	def goback_man(self):# Go back to main GUI from manual mode
		self.button14.destroy()
		self.button13.destroy()
		self.button12.destroy()
		self.button11.destroy()
		self.button10.destroy()
		self.button9.destroy()
		self.button8.destroy()
		self.button7.destroy()
		self.button6.destroy() 
		self.button5.destroy()
		self.button4.destroy()
		self.image_label.destroy()
		self.name.destroy()
		self.botframe.destroy()
		self.topframe.destroy()	
			

		self.frame = Frame(self.master)
		self.frame.pack()
		self.labelface = Label(self.master, text="AR Drone 2.0",font=25)
		self.labelface.pack()
		self.button1 = Button(
			self.frame, name="button1", text="Facial Detection", fg="red", command=self.faced,
			bd=5,padx=70,pady=50,font=25)
		self.button1.pack(side=LEFT)
		self.button2 = Button(
			self.frame, name="button2", text="Manual", command=self.man,bd=5,padx=70,pady=50,font=25
			)
		self.button2.pack()
		self.button3 = Button(master=root,text ='exit', bg = 'green',command=lambda: quit(root),bd=5,padx=70,pady=50,font=25)

		self.button3.pack()
		self.current_page = "Main"
		self.mydrone.reset()
		self.mydrone.printBattery()

	def update_image(self): # update video
		#_, f = self.cam.read()
		f = self.mydrone.dronevideo()
		gray_im = cv2.cvtColor(f, cv2.COLOR_BGR2RGBA)
		a = Image.fromarray(gray_im)
		b = ImageTk.PhotoImage(image=a)
		self.image_label.configure(image=b)
		self.image_label._image_cache = b  # avoid garbage collection
		self.topframe.update()

	def update_all(self): # update video
		self.update_image()
		if (self.current_page != "Main"):
			self.topframe.after(5, func=lambda: self.update_all())


	

class Ar_drone: # This class contains all the command for the drone. It interacts between the computer and the drone.
	def __init__(self):
		self.drone = ps_drone.Drone()                                     # Start using drone
		self.drone.startup()                                              # Connects to drone and starts subprocesses
		self.drone.reset()                                                # Sets drone's status to good (LEDs turn green when red)
		while (self.drone.getBattery()[0] == -1):      time.sleep(0.1)    # Waits until drone has done its reset
		print "Battery: "+str(self.drone.getBattery()[0])+"%  "+str(self.drone.getBattery()[1])	# Gives a battery-status
		self.drone.useDemoMode(True)                                      # Just give me 15 basic dataset per second (is default anyway)
		##### Mainprogram begin #####
		self.drone.setConfigAllID()                                       # Go to multiconfiguration-mode
		self.drone.fastVideo()                                              # Choose lower resolution (hdVideo() for...well, guess it)
		#self.drone.sdVideo()
		self.drone.frontCam()                                             # Choose front view
		self.CDC = self.drone.ConfigDataCount
		while self.CDC == self.drone.ConfigDataCount:       time.sleep(0.0001) # Wait until it is done (after resync is done)
		self.drone.startVideo()                                           # Start video-function
		#drone.midVideo()
		#drone.showVideo()                                                # Display the video
		self.IMC = self.drone.VideoImageCount                             # Number of encoded videoframes
	def printBattery(self):
		print "Battery: "+str(self.drone.getBattery()[0])+"%  "+str(self.drone.getBattery()[1])	# Gives a battery-status
	def dronevideo(self):
		while self.drone.VideoImageCount == self.IMC: time.sleep(0.01)     # Wait until the next video-frame		
		self.IMC =    self.drone.VideoImageCount                               # Number of encoded videoframes
		self.image = self.drone.VideoImage
		return self.image
	def takeoff(self):
		self.drone.takeoff()
	def land(self):
		self.drone.land()
	def stop(self):
		self.drone.hover()
		print "The Drone STOP"
	def doggyHop(self):
		self.drone.doggyHop()
	def moveLeft(self):
		self.drone.move(-0.1,0.0,0.0,0.0)
		
		print "a --- Move left"
	def moveRight(self):
		self.drone.move(0.1,0.0,0.0,0.0)
		
		print "d --- Move Right"
	def moveForward(self):
		self.drone.move(0.0,0.1,0.0,0.0)
		print "Up --- Move Forward"
	def moveBackward(self):
		self.drone.move(0.0,-0.1,0.0,0.0)
		print "Down --- Move Backward"
	def moveUp(self):
		self.drone.move(0.0,0.0,0.5,0.0)
		
		print "w --- Move Up"
	def moveDown(self):
		self.drone.move(0.0,0.0,-0.5,0.0)
		
		print "s --- Move Down"
	def turnLeft(self):
		self.drone.move(0.0,0.0,0.0,-0.55)
		time.sleep(0.4)
		self.drone.stop()
		print "Left --- Turn left"
	def turnRight(self):
		self.drone.move(0.0,0.0,0.0,0.15)
		time.sleep(0.4)
		self.drone.stop()
		print "Right --- Turn right"
	def reset(self):
		self.drone.reset() 
	def __del__(self):
		 
		print "mydrone has been deleted"
		

class imag(threading.Thread): #The image class will read frame from camera and detect red obeject. After that, it will draw a red box around the red object. Then, it will send the frame into a queue to display.
	def  __init__(self,mydrone,name,q,threadLock):
		threading.Thread.__init__(self)
		self.q = q
		self.threadLock = threadLock
		self.mydrone = mydrone
		self.scale_down = 4
		self.name = name
		self.true = True
		self.f = open('sb','w')

	def run(self):
		while (self.true == True):
			#print "Enter while, %s\n"%self.name
			self.threadLock.acquire()
			#print "Get the Image, %s\n"%self.name
			self.image = self.mydrone.dronevideo()
			self.threadLock.release()

			self.orig_img = self.image
			self.img = cv2.GaussianBlur(self.orig_img, (5,5), 0)
			self.img = cv2.cvtColor(self.orig_img, cv2.COLOR_BGR2HSV)
			self.img = cv2.resize(self.img, (len(self.orig_img[0]) / self.scale_down, len(self.orig_img) / self.scale_down))
			self.red_lower = np.array([0, 120, 0],np.uint8)
			self.red_upper = np.array([3, 255, 255],np.uint8)
			self.red_binary = cv2.inRange(self.img, self.red_lower, self.red_upper)
			self.dilation = np.ones((15, 15), "uint8")
			self.red_binary = cv2.dilate(self.red_binary, self.dilation)
			self.image, self.contours, self.hierarchy = cv2.findContours(self.red_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
			self.max_area = 0
			self.largest_contour = None
			for self.idx, self.contour in enumerate(self.contours):
				self.area = cv2.contourArea(self.contour)
				if self.area > self.max_area:
					self.max_area = self.area
					self.largest_contour = self.contour
			if self.largest_contour == None:
				self.q.put([self.orig_img, [], -1])

			if not self.largest_contour == None:
				perimeter = cv2.arcLength(self.largest_contour,True)
				#print "perimeter", perimeter
				#self.f.write(str(perimeter))
				#self.f.write("\n")
				self.moment = cv2.moments(self.largest_contour)
				if self.moment["m00"] > 1000 / self.scale_down:
					self.rect = cv2.minAreaRect(self.largest_contour)
					self.rect = ((self.rect[0][0] * self.scale_down, self.rect[0][1] * self.scale_down), (self.rect[1][0] * self.scale_down, self.rect[1][1] * self.scale_down), self.rect[2])
					self.box = cv2.boxPoints(self.rect)
					self.box = np.int0(self.box)
					self.q.put([self.orig_img, self.box,perimeter])
					
					#print "Putting pic in the Queue"

	def delete(self):
		self.true = False		 
		print "Image has been deleted", self.name

class showimag(threading.Thread):#This showimage class will get frame from the queue and display it. It will also determine which command to send to the drone.

	def  __init__(self,image_label,q,mydrone):
		threading.Thread.__init__(self)
		self.image_label = image_label
		self.q = q
		self.mydrone = mydrone
		self.tag =0
		self.tagold = 0
		self.bxold=0
		self.byold = 0
		self.center_d = 0
		self.true = True
		self.num = 0
		self.time = time.ctime()
		self.i=0
		self.j=0
		self.w=0
		#print "The initial time is: ",self.time

	def run(self):
		#cv2.namedWindow("ColourTrackerWindow", cv2.WINDOW_NORMAL)
		while self.true == True:
			if self.q.empty() is False:
				items = self.q.get()
				self.q.task_done()
				item1 = items[0]
				item2 = items[1]
				perimeter = items[2]
				if len(item2) != 0:
					cv2.drawContours(item1, [item2], 0, (0, 0, 255), 2)

					#Calculate the box center and image center
					box = item2
					cbox = (box[0]+box[1]+box[2]+box[3])/4
					bx = cbox[0]
					by = cbox[1]
					ix = len(item1[0])/2
					iy = len(item1)/2
					length = len(item1)   #iy
					width = len(item1[0])   #ix
					self.center_d = math.sqrt( math.pow(bx-self.bxold, 2) + math.pow(by-self.byold, 2))


					# Adjust the drone to follow the red square------------------------
					self.num+=1
					if self.num == 8:
						print "Sending command"
						self.bxold = bx
						self.byold = by
						if by <= length/3:
							if bx <= width/3:
								self.tag = 1
								if self.center_d <length/3:
									#print 'tag and tagold :',self.tag, self.tagold
									while (self.i!=8):
										self.mydrone.moveUp()
										self.i+=1
									while (self.j!=1):
										#self.mydrone.moveLeft()
										self.mydrone.turnLeft()
										self.j+=1
									self.tagold = 1
								print "Enter tag 1"

							elif bx >= width/3 and bx < 2*width/3:
								self.tag = 2
								if self.center_d <length/3:
									while (self.i!=8):
										self.mydrone.moveUp()
										self.i+=1
									self.tagold = 2
								print "Enter tag 2"

							else:
								self.tag = 3
								if self.center_d <length/3:
									while (self.i!=8):
										self.mydrone.moveUp()
										self.i+=1
									while (self.j!=1):
										#self.mydrone.moveRight()
										self.mydrone.turnRight()
										self.j+=1
									self.tagold = 3
								print "Enter tag 3"


						elif by < 2*length/3 and by > length/3:
							if bx < width/3:
								self.tag = 4
								if self.center_d <length/3:
									while (self.j!=1):
										self.mydrone.turnLeft()
										self.j+=1
									self.tagold = 4
								print "Enter tag 4"

							elif bx > 2*width/3 and bx < width:
								self.tag = 6
								if self.center_d <length/3:
									while (self.j!=1):
										#self.mydrone.moveRight()
										self.mydrone.turnRight()
										self.j+=1
									self.tagold = 6
								print "Enter tag 6"

							else:
								self.tagold = 5
								print "Enter tag 5 ------Center!"
								if self.tag != self.tagold:
									self.mydrone.stop()
									self.tagold = 5


						elif by > 2*length/3 and by < length:
							if bx < width/3:
								self.tag = 7
								if self.center_d <length/3:
									while (self.i!=8):
										self.mydrone.moveDown()
										self.i+=1
									while (self.j!=1):
										#self.mydrone.moveLeft()
										self.mydrone.turnLeft()
										self.j+=1
									self.tagold = 7
								print "Enter tag 7"

							elif bx > width/3 and bx < 2*width/3:
								self.tag = 8
								if self.center_d <length/3:
									while (self.i!=8):
										self.mydrone.moveDown()
										self.i+=1
									self.tagold = 8
								print "Enter tag 8"

							elif bx > 2*width/3 and bx < width:
								self.tag = 9
								if self.center_d <length/3:
									while (self.i!=8):
										self.mydrone.moveDown()
										self.i+=1
									while (self.j!=1):
										#self.mydrone.moveRight()
										self.mydrone.turnRight()
										self.j+=1
									self.tagold = 9
								print "Enter tag 9"

						if perimeter<180 and perimeter >140:
							self.mydrone.stop()

						elif perimeter > 180:
							while(self.w != 4):
								self.mydrone.moveBackward()
								self.w +=1
						elif perimeter < 140:
							while(self.w != 4):
								self.mydrone.moveForward()
								self.w +=1


						else:
							pass
					    #------------------------------------------------------------------'''
						self.num=0
						self.i=0
						self.j=0
						self.w=0
						print "no enter ifelse"

				else:
					self.mydrone.stop()
					print "item2: ", item2
				item3 = cv2.cvtColor(item1, cv2.COLOR_BGR2RGBA)
				a = Image.fromarray(item3)
				b = ImageTk.PhotoImage(image=a)
				self.image_label.configure(image=b)
				self.image_label._image_cache = b  # avoid garbage collection


	
				
				
	def delete(self):
		self.true = False		 
		print "ShowImage has been deleted"
	
	
if __name__ == '__main__':		
	root = Tk()
	root.geometry("800x600+30+30")
	app = Application(root)
	root.mainloop()

#-------------------Garbage

'''if (bx-ix)<-10 and (by-iy)<-10:  #left upper , move up and turn right, tag = #1
							self.tag = 1
							if self.tag != self.tagold:
								print 'tag and tagold 1:',self.tag, self.tagold
								while (self.i!=8):
									self.mydrone.moveUp()
									self.i+=1
								while (self.j!=4):
									self.mydrone.moveLeft()
									self.j+=1
								self.tagold = 1
							print "Enter if"
						elif (bx-ix)<-10 and (by-iy)>10: #left lower, move down and turn right, tag = #2
							self.tag = 2
							if self.tag != self.tagold:
								print 'tag and tagold 2:',self.tag, self.tagold
								while (self.i!=8):
									self.mydrone.moveDown()
									self.i+=1
								while (self.j!=4):
									self.mydrone.moveLeft()
									self.j+=1
								self.tagold = 2
							print "Enter if"
						elif (bx-ix)>10 and (by-iy)<-10:  #right upper, move up and turn left, #3
							self.tag = 3
							if self.tag != self.tagold:
								print 'tag and tagold 3:',self.tag, self.tagold
								while (self.i!=8):
									self.mydrone.moveUp()
									self.i+=1
								while (self.j!=4):
									self.mydrone.moveRight()
									self.j+=1
								self.tagold = 3
							print "Enter if"
						elif (bx-ix)>10 and (by-iy)>10: #right lower, move down and turn left, #4
							self.tag = 4
							if self.tag != self.tagold:
								print 'tag and tagold 4:',self.tag, self.tagold
								while (self.i!=8):
									self.mydrone.moveDown()
									self.i+=1
								while (self.j!=4):
									self.mydrone.moveRight()
									self.j+=1
								self.tagold = 4
							print "Enter if"

						else:
							self.mydrone.stop()
							print "send_STOP"    '''


#self.tag != self.tagold and
