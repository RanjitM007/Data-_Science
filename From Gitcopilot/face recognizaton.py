
    // creating a function that collect the image and save in a folder
    // and return the path of the folder        
    // function name: get_image_path
    // return: string
    // parameters: string
    // description: get the path of the folder where the image will be saved
    //
    //     

    import cv2
    import numpy as np

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return 0

        
//crating function  for image traing 



import cv2
import numpy as np

img = cv2.imread('/home/saujanya/OCR/practice/test_images/lion.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

//creating a function to load a image folder and return a list of images
//this function is called in main
//the function is called in the main function   
def load_images(path):
    //creating an empty list
    images = []
    //using the os module to get the file names in the folder
    //the os.listdir function returns a list of file names
    for file_name in os.listdir(path):
        //creating a variable called image
        image = pygame.image.load(path + "/" + file_name)
        //appending the image to the list
        images.append(image)
    return images


//creating a function to load a sound folder and return a list of sounds
//this function is called in main
//the function is called in the main function
def load_sounds(path):
    //creating an empty list
    sounds = []
    //using the os module to get the file names in the folder
    //the os.listdir function returns a list of file names
    for file_name in os.listdir(path):
        //creating a variable called sound
        sound = pygame.mixer.Sound(path + "/" + file_name)
        //appending the sound to the list
        sounds.append(sound)
    return sounds


//creating a function to load a font folder and return a list of fonts
//this function is called in main
//the function is called in the main function
def load_fonts(path):
    //creating an empty list
    fonts = []
    //using the os module to get the file names in the folder
    //the os.listdir function returns a list of file names
    for file_name in os.listdir(path):
        //creating a variable called font
        font = pygame.font.Font(path + "/" + file_name, 30)
        //appending the font to the list
        fonts.append(font)
        









