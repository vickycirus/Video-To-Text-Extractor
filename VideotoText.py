import cv2
import pytesseract
import os
try:
    from PIL import Image
except ImportError:
    import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'   
#give the path of the video 
cam = cv2.VideoCapture(r'C:\Users\Vikram\Desktop\javaweek9\week9\src\collec\bheeshma.mp4')
currentframe = 0
d={}
while(True):
    ret,frame = cam.read()
  
    if ret:
        name = r'C:\Users\Vikram\Desktop\javaweek9\week9\src\collec\Frame(' + str(currentframe) + ').jpg'
        
        cv2.imwrite(name, frame)
        k=pytesseract.image_to_string(Image.open(name))
        if k not in d.keys():
            print(k)
            d[k]=1
       
            
        try: 
           os.remove(name)
        except: pass
    else:
        break
cam.release()
cv2.destroyAllWindows()