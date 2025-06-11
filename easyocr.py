import easyocr
import cv2




reader = easyocr.Reader(['ja_tra', 'en'])

result = reader.readtext('demo-image-jpn.jpeg')

#img = cv2.imread('')