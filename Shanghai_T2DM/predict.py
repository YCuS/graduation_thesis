import cv2
import numpy as np

def run():
    img = cv2.imread('shanghaitech.png')
    # print(img.shape)

    for i in range (1,499):
        img = transform(img, i)

def transform(img, num):

    rows, cols, ch = img.shape
    if (rows == cols):
        n = rows
        img2 = np.zeros([rows, cols, ch])

        for x in range(0, rows):
            for y in range(0, cols):

                img2[x][y] = img[(x+y)%n][(x+2*y)%n]
        if num % 83 == 0:
            cv2.imwrite("iteration" + str(num) + ".jpg", img2)
        return img2

    else:
        print("The image is not square.")


if __name__ == "__main__":
    run()