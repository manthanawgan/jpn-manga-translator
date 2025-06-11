import easyocr
import cv2




reader = easyocr.Reader(['ja', 'en'])

result = reader.readtext('demo-image-jpn.jpeg', detail =1)

# img = cv2.imread('demo-image-jpn.jpeg')
# result = reader.readtext(img)

# with open("demo-image-jpn.jpeg", "rb") as f:
#     img = f.read()
# result = reader.readtext(img, detail = 0)

# for detection in result:
#     print(detection[1])

for detection in result:
    print(detection)