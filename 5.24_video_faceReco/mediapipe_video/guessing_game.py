import copy
import random
import time
import cv2
import numpy as np
B0X_ROCK = 1
B0X_PAPER = 2
BOX_SCISSORS = 3


class Guessing:
    def __init__(self):
        self.width = None
        self.height = None
        self.box_image = cv2.imread(r"media_image/box.png")
        self.rock = None
        self.scissors = None
        self.paper = None
        self.box_list = None
        # box尺寸
        self.h = None
        self.w = None
        self.stop = False
        self.create_box()

    def create_box(self):
        height, width = self.box_image.shape[:2]
        self.scissors = self.box_image[:, 50: width // 3 - 50]
        self.h, self.w = self.scissors.shape[:2]
        self.rock = self.box_image[:, width * 2 // 3 - 50: -50]
        self.paper = self.box_image[:, width // 3 - 50: width * 2 // 3 - 50]
        self.rock = cv2.resize(self.rock, (self.w, self.h))
        self.paper = cv2.resize(self.paper, (self.w, self.h))
        self.paper = cv2.cvtColor(self.paper, cv2.COLOR_BGR2RGB)
        self.rock = cv2.cvtColor(self.rock, cv2.COLOR_BGR2RGB)
        self.scissors = cv2.cvtColor(self.scissors, cv2.COLOR_BGR2RGB)
        self.box_list = [self.rock, self.paper, self.scissors]

    def paste_random_image(self, image, random_type=True, location="l", box_type=B0X_ROCK):
        self.height, self.width = image.shape[:2]
        self.height //= 3
        self.width //= 4

        if random_type is True and location == "l" and self.stop is False:
            image_temp = image[0: self.height, 0: self.width]
            random.shuffle(self.box_list)
            box = self.box_list[0]
            image[0: self.height, 0: self.width] = self.past_image(box, image_temp)
            return image

        if random_type is True and location == "l" and self.stop is True:
            image_temp = image[0: self.height, 0: self.width]
            box = self.box_list[0]
            image[0: self.height, 0: self.width] = self.past_image(box, image_temp)

            return image

        elif random_type is True and location == "r":
            image_temp = image[0: self.height:, -self.width:]
            random.shuffle(self.box_list)
            box = self.box_list[0]
            image[0: self.height, -self.width:] = self.past_image(box, image_temp)
            return image

        elif random_type is False and location == "r":
            image_temp = image[0: self.height:, -self.width:]
            if box_type == B0X_ROCK:
                image[0: self.height, -self.width:] = self.past_image(self.rock, image_temp)
            if box_type == B0X_PAPER:
                image[0: self.height, -self.width:] = self.past_image(self.paper, image_temp)
            if box_type == BOX_SCISSORS:
                image[0: self.height, -self.width:] = self.past_image(self.scissors, image_temp)
            return image

    def past_image(self, box, image_temp):
        box = cv2.resize(box, (self.width, self.height))
        mask = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)
        mask = np.dstack((mask, mask, mask))
        return np.where(mask < 230, box, image_temp)

    def playing(self, image, points):
        # self.create_box()
        self.stop = False
        if points is None:
            return self.paste_random_image(image)
        else:
            img_temp = self.make_move(points, image)
            img = self.paste_random_image(img_temp)
            return img

    def make_move(self, points, image):
        distance = []
        sub = []
        if points is None:
            image_temp = self.paste_random_image(image, True, "r")
            image_rand = self.paste_random_image(image_temp)
            return image_rand
        for j in range(1, 6):
            distance.append([np.linalg.norm(points[j * 4 - i] - points[0]) for i in range(0, 4)])
        for i in range(0, 5):
            sub.append(distance[i][0] - distance[i][2])
        if all(x > 0 for x in sub):
            image = self.paste_random_image(image, False, "r", B0X_PAPER)
            self.stop = True
        elif all(x < 0 for x in sub[1:]):
            image = self.paste_random_image(image, False, "r", B0X_ROCK)
            self.stop = True
        elif sub[3] < 0 and sub[4] < 0 and all(x > 0 for x in sub[1:3]):
            image = self.paste_random_image(image, False, "r", BOX_SCISSORS)
            self.stop = True
        else:
            image = self.paste_random_image(image, True, "r")
        return image










