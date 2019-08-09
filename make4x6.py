import cv2
import sys

def make4x6(correctFormatFile):
    # open the file (XxX dimensions correspond to 2 inch x 2 inch == 51 mm x 51 mm)
    print(correctFormatFile)
    img = cv2.imread(correctFormatFile)

    # head centered and size between - 1 inch x 1.4 inch == 25 and 35 mm
    # assert square photo
    # 2 2 2
    # 2 2 2    
    # Next 4x6 aspect ratio - print size : 4 inch x 6 inch


if len(sys.argv) > 1:
    make4x6(sys.argv[1])
else:
    print("python make4x4 <image>")
