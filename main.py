import cv2 as cv
import numpy as np
import os
from tkinter import *
from PIL import Image, ImageTk

# Path to images
main_path = os.path.join("BreaKHis 400X/train/malignant")
output_path = os.path.join("Preprocessed")
image_shape = (512, 512)
images_path = os.listdir(main_path)
counter = 67 

hb, hg, hr = 225, 225, 225
lb, lg, lr = 0,0,0
threshold_value = 125 

# Tkinter window setup
main = Tk()
main.geometry("1700x800")
main.title("Label Images")

counter_label = Label(text = f"{counter + 1} : {images_path[counter]}",  font = ("Sanssarif", 20, "bold") )
counter_label.pack()


def update_image():
    global counter, label, tk_output_image, hb, hg, hr, lb, lg, lr
    global contour_image, mask_rgb

    counter_label.config(text = f"{counter + 1} : {images_path[counter]}")

    image = cv.imread(os.path.join(main_path, images_path[counter]))
    orig_image = cv.resize(image, image_shape)

    # contour detection
    gray = cv.cvtColor(orig_image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, threshold_value, 255, cv.THRESH_BINARY)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contour_image = np.zeros_like(orig_image)
    cv.drawContours(contour_image, contours, -1, (255, 255, 255), 2)

    #Create a color mask based on trackbar values
    mask = np.zeros_like(orig_image)
    high = np.array([hb, hg, hr])
    low = np.array([lb, lg, lr])  
    hsv_img = cv.cvtColor(orig_image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_img, low, high)  
    mask_rgb = cv.cvtColor(mask, cv.COLOR_GRAY2BGR) 

    # # canny 
    # edges = cv.Canny(gray,50,200)
    # edges = cv.cvtColor(edges, cv.COLOR_GRAY2BGR) 

    # (H, W) = orig_image.shape[:2] 
    # blob = cv.dnn.blobFromImage(orig_image, scalefactor=1.0, size=(W, H), 
    #     swapRB=False, crop=False) 
    # net = cv.dnn.readNetFromCaffe("Week3/deploy.prototxt", "Week3/hed_pretrained_bsds.caffemodel") 
    # net.setInput(blob) 
    # hed = net.forward() 
    # hed = cv.resize(hed[0, 0], (W, H))
    
    result_mask = cv.bitwise_or(mask_rgb, contour_image)
    res = cv.bitwise_and(orig_image, orig_image, mask=mask)
    combined_result = cv.bitwise_or(result_mask, res)
    
    combined_result = cv.cvtColor(combined_result, cv.COLOR_BGR2GRAY) 
    final = cv.bitwise_and(orig_image,orig_image, mask = combined_result)

    output_image = np.hstack([orig_image, contour_image, final])

    output_pil_image = Image.fromarray(output_image)
    tk_output_image = ImageTk.PhotoImage(image=output_pil_image)

    label.config(image=tk_output_image)
    label.image = tk_output_image  


def next_image():
    global counter
    counter = (counter + 1) % len(images_path)  # Cycle through images
    update_image()
def prev_image():
    global counter
    counter = (counter - 1) % len(images_path)  # Cycle through images
    update_image()


def update_hb(val):
    global hb
    hb = int(val)
    update_image()

def update_hg(val):
    global hg
    hg = int(val)
    update_image()

def update_hr(val):
    global hr
    hr = int(val)
    update_image()

def update_lb(val):
    global lb
    lb = int(val)
    update_image()

def update_lg(val):
    global lg
    lg = int(val)
    update_image()

def update_lr(val):
    global lr
    lr = int(val)
    update_image()

def update_threshold_value(val):
    global threshold_value
    threshold_value = int(val)
    update_image()


def save_images():
    global contour_image, mask_rgb
    if not os.path.exists(output_path):
        os.makedirs(os.path.join(output_path,"boundries"))
        os.makedirs(os.path.join(output_path,"region"))
    cv.imwrite(os.path.join(output_path,"boundries", images_path[counter]), contour_image)
    cv.imwrite(os.path.join(output_path,"region", images_path[counter]), mask_rgb)
    next_image()

label = Label(main)
label.pack()
update_image()


# Settings Pannel
cv.namedWindow('Settings')

cv.createTrackbar('High Blue', 'Settings', hb, 255, update_hb)
cv.createTrackbar('High Green', 'Settings', hg, 255, update_hg)
cv.createTrackbar('High Red', 'Settings', hr, 255, update_hr)

cv.createTrackbar('Low Blue', 'Settings', lb, 255, update_lb)
cv.createTrackbar('Low Green', 'Settings', lg, 255, update_lg)
cv.createTrackbar('Low Red', 'Settings', lr, 255, update_lr)

cv.createTrackbar('Threshold', 'Settings', threshold_value, 255, update_threshold_value)



# Add buttons for navigating images
prev_button = Button(main, text="Previous", command=prev_image)
prev_button.pack(side=LEFT, padx=10)

next_button = Button(main, text="Next", command=next_image)
next_button.pack(side=RIGHT, padx=10)

save_button = Button(main, text = "Save", command= save_images) 
save_button.pack()

main.mainloop()
cv.destroyAllWindows()