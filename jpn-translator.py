import easyocr
import cv2
import sys
import io
from google import genai
from google.genai import types


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

reader = easyocr.Reader(['ja', 'en'])

result = reader.readtext('thank-you-in-jpn.jpeg', detail=0, paragraph = False)

# img = cv2.imread('demo-image-jpn.jpeg')
# result = reader.readtext(img)

# with open("demo-image-jpn.jpeg", "rb") as f:
#     img = f.read()
# result = reader.readtext(img, detail = 0)

# for detection in result:
#     print(detection[1])

for text in result:
    print(text)

Client = genai.Client(api_key='GEMINI_API_KEY')

