import cv2
import sys
import numpy as np

def make4x6(correctFormatFile):
    # open the file (XxX dimensions correspond to 2 inch x 2 inch == 51 mm x 51 mm)
    # head centered and size between - 1 inch x 1.4 inch == 25 and 35 mm
    # assert square photo
    print(correctFormatFile)
    img = cv2.imread(correctFormatFile)

    height, width, channels = img.shape

    print(type(img))
    print(img.dtype)
    print height, width, channels

    if(height != width):
        print("height and width are not equal", height, width)
        return 0

    # 2 2 2
    # 2 2 2    
    # Next 4x6 aspect ratio - print size : 4 inch x 6 inch
    newImg = np.zeros((2*height, 3*width, channels), dtype=np.uint8)
    newHeight, newWidth, newChannels = newImg.shape
    print newHeight, newWidth, newChannels

    for i in range(height):
        for j in range(width):
            for c in range(channels):
                newImg[i, j, c] = img[i, j, c]
                newImg[width + i, j, c] = img[i, j, c]
                newImg[i, height + j, c] = img[i, j, c]
                newImg[i, 2 * height + j, c] = img[i, j, c]
                newImg[width + i, height + j, c] = img[i, j, c]
                newImg[width + i, 2 * height + j, c] = img[i, j, c]

    (name, extension) = correctFormatFile.split('.')

    cv2.imwrite(name + "_new.jpg", newImg)

if len(sys.argv) > 1:
    make4x6(sys.argv[1])
else:
    print("python make4x4 <image>")
