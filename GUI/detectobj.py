from Tkinter import*
import cv2
from collections import deque
import time
import Image, ImageTk




def quit_(root):
    root.destroy()

def update_image(image_label, cam):
    (readsuccessful, f) = cam.read()
    gray_im = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    a = Image.fromarray(gray_im)
    b = ImageTk.PhotoImage(image=a)
    image_label.configure(image=b)
    image_label._image_cache = b  # avoid garbage collection
    root.update()


def update_fps(fps_label):
    frame_times = fps_label._frame_times
    frame_times.rotate()
    frame_times[0] = time.time()
    sum_of_deltas = frame_times[0] - frame_times[-1]
    count_of_deltas = len(frame_times) - 1
    try:
        fps = int(float(count_of_deltas) / sum_of_deltas)
    except ZeroDivisionError:
        fps = 0
    fps_label.configure(text='FPS: {}'.format(fps))


def update_all(root, image_label, cam, fps_label):
    update_image(image_label, cam)
    update_fps(fps_label)
    root.after(20, func=lambda: update_all(root, image_label, cam, fps_label))






if __name__ == '__main__':
    root = Tk()
    root.geometry("800x600+30+30")
    topframe = Frame(root)
    topframe.pack()
    botframe = Frame(root)
    botframe.pack(side=BOTTOM)

    name = Label(root,text = 'face tracking')
    name.pack()

    image_label = Label(master=root)
    image_label.pack()
    cam = cv2.VideoCapture(0)
    fps_label = Label(master=root)
    fps_label._frame_times = deque([0]*5)  # arbitrary 5 frame average FPS
    fps_label.pack()



    button1 = Button(master=root,text ='back', bg = 'green',command=lambda: quit_(root))
    button1.pack()
    root.after(0, func=lambda: update_all(root, image_label, cam, fps_label))
    root.mainloop()

