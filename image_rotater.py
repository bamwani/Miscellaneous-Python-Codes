import cv2
import os

path_from = "./images/"
path_to = "./images1/"


# Function to rename multiple files & STORE IN NEW FOLDER
def main():
    i = 0

    for filename in os.listdir(path_from):
        # dst = str(i) + ".jpg"  # select file type
        img = cv2.imread(path_from+filename)
        (h, w) = img.shape[:2]
        center = (w / 2, h / 2)
        angle90 = 90
        scale = 1.0
        M = cv2.getRotationMatrix2D(center, angle90, scale)
        rotated90 = cv2.warpAffine(img, M, (h, w))
        cv2.imwrite(path_to+str(i)+".jpg",rotated90)

        # # rename() function will
        # # rename all the files
        # os.rename(src, dst)
        i += 1


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()


# # read image as grey scale
# img = cv2.imread('/home/arjun/Desktop/logos/python.png')
# # get image height, width
# (h, w) = img.shape[:2]
# # calculate the center of the image
# center = (w / 2, h / 2)
#
# angle90 = 90
# # angle180 = 180
# # angle270 = 270
#
# scale = 1.0
# # Perform the counter clockwise rotation holding at the center
# # 90 degrees
# M = cv2.getRotationMatrix2D(center, angle90, scale)
# rotated90 = cv2.warpAffine(img, M, (h, w))