import random


class GlitchWrapper:
    def __init__(self, pixels, width, height): # initialize class
        self.pixels = pixels
        self.width = width
        self.height = height

    def mix_block(self):    # all pixels in rect are average of these pixels' values
        x1 = random.randint(0, self.width - 1)
        y1 = random.randint(0, self.height - 1)
        x2 = random.randint(x1 + 1, self.width)
        y2 = random.randint(y1 + 1, self.height)

        sum_r, sum_g, sum_b = 0, 0, 0

        for x in range(x1, x2):
            for y in range(y1, y2):
                sum_r += self.pixels[x, y][0]
                sum_g += self.pixels[x, y][1]
                sum_b += self.pixels[x, y][2]

        area = (x2 - x1) * (y2 - y1)
        mid_r, mid_g, mid_b = int(
            sum_r / area), int(sum_g / area), int(sum_b / area)

        for x in range(x1, x2):
            for y in range(y1, y2):
                self.pixels[x, y] = (mid_r, mid_g, mid_b)

    def invert_block(self): # invert all pixels in rect
        x1 = random.randint(0, self.width - 1)
        y1 = random.randint(0, self.height - 1)
        x2 = random.randint(x1 + 1, self.width)
        y2 = random.randint(y1 + 1, self.height)

        for x in range(x1, x2):
            for y in range(y1, y2):
                self.pixels[x, y] = tuple(
                    map(lambda t: 255 - t, self.pixels[x, y]))

    def fill_block(self): # fill block with color
        x1 = random.randint(0, self.width - 1)
        y1 = random.randint(0, self.height - 1)
        x2 = random.randint(x1 + 1, self.width)
        y2 = random.randint(y1 + 1, self.height)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        a = random.uniform(0, 1)

        for x in range(x1, x2):
            for y in range(y1, y2):
                new_r = int(self.pixels[x, y][0] * (1 - a) + r)
                new_g = int(self.pixels[x, y][1] * (1 - a) + g)
                new_b = int(self.pixels[x, y][2] * (1 - a) + b)

                self.pixels[x, y] = (new_r, new_g, new_b)

    def pixelize_block(self): # like mix_block but works with few rects
        x1 = random.randint(0, self.width - 1)
        y1 = random.randint(0, self.height - 1)
        x2 = random.randint(x1 + 1, self.width)
        y2 = random.randint(y1 + 1, self.height)

        seed_size_x = random.randint(1, x2 - x1 // 2)
        seed_size_y = random.randint(1, y2 - y1 // 2)

        randomly = random.choice((False, True)) # put average randomly

        for x in range(x1, x2, seed_size_x):
            for y in range(y1, y2, seed_size_y):
                sum_r, sum_g, sum_b = 0, 0, 0

                for xi in range(x, min(x2, x + seed_size_x)):
                    for yi in range(y, min(y2, y + seed_size_y)):
                        sum_r += self.pixels[xi, yi][0]
                        sum_g += self.pixels[xi, yi][1]
                        sum_b += self.pixels[xi, yi][2]

                area = (min(x2, x + seed_size_x) - x) * \
                    (min(y2, y + seed_size_y) - y)

                mid_r, mid_g, mid_b = int(
                    sum_r / area), int(sum_g / area), int(sum_b / area)

                if randomly:
                    if random.choice((True, False)):
                        continue

                for xi in range(x, min(x2, x + seed_size_x)):
                    for yi in range(y, min(y2, y + seed_size_y)):
                        if randomly:
                            if random.choices((True, False), k=1, weights=(1, 5))[0]:
                                continue

                        self.pixels[xi, yi] = mid_r, mid_g, mid_b

    def move_block(self):
        x1 = random.randint(0, self.width - 1)
        y1 = random.randint(0, self.height - 1)
        x2 = random.randint(x1 + 1, self.width)
        y2 = random.randint(y1 + 1, self.height)

        x_new = random.randint(0, self.width)
        y_new = random.randint(0, self.height)

        color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

        pixels_list = list()

        for x in range(x1, x2):
            for y in range(y1, y2):
                pixels_list.append(self.pixels[x, y])
                self.pixels[x, y] = color
        i = -1
        for x in range(x1, x2):
            for y in range(y1, y2):
                i += 1
                if x_new + x >= self.width or y_new + y >= self.height:
                    continue

                self.pixels[x_new + x, y_new + y] = pixels_list[i]

    def clone_block(self):
        x1 = random.randint(0, self.width - 1)
        y1 = random.randint(0, self.height - 1)
        x2 = random.randint(x1 + 1, self.width)
        y2 = random.randint(y1 + 1, self.height)

        x_new = random.randint(0, self.width)
        y_new = random.randint(0, self.height)

        for x in range(x1, x2):
            for y in range(y1, y2):
                if x_new + x >= self.width or y_new + y >= self.height:
                    continue
                self.pixels[x_new + x, y_new + y] = self.pixels[x, y]

    def strange_invert_block(self): # idk how it works its just strange
        x1 = random.randint(0, self.width - 1)
        y1 = random.randint(0, self.height - 1)
        x2 = random.randint(x1 + 1, self.width)
        y2 = random.randint(y1 + 1, self.height)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        for x in range(x1, x2):
            for y in range(y1, y2):
                new_r = abs(r - self.pixels[x, y][0])
                new_g = abs(g - self.pixels[x, y][1])
                new_b = abs(b - self.pixels[x, y][2])

                self.pixels[x, y] = (new_r, new_g, new_b)

    def noise_rect(self): # apply noise with random alpha
        x1 = random.randint(0, self.width - 1)
        y1 = random.randint(0, self.height - 1)
        x2 = random.randint(x1 + 1, self.width)
        y2 = random.randint(y1 + 1, self.height)

        a = random.uniform(0, 1)
        colored = random.choice((False, True))

        for x in range(x1, x2):
            for y in range(y1, y2):
                if colored:
                    noise = (random.randint(0, 255), random.randint(
                        0, 255), random.randint(0, 255))
                else:
                    color = random.randint(0, 255)
                    noise = (color, color, color)
                self.pixels[x, y] = tuple(
                    map(lambda i: int(self.pixels[x, y][i] * (1 - a) + noise[i]), range(3)))
    glitches = [clone_block, fill_block, invert_block, mix_block,
                move_block, noise_rect, pixelize_block, strange_invert_block]
    cool_glithes = [clone_block, invert_block, noise_rect, pixelize_block, strange_invert_block]
    weights = [1, 1, 1, 1, 1]

    def random_glitches(self, n=-1, max_n=len(cool_glithes)):
        if n == -1:
            chosens = random.choices(self.cool_glithes,
                                     k=random.randint(2, max_n), weights=self.weights)
        else:
            chosens = random.choices(self.cool_glithes, k=n, weights=self.weights)

        for e in chosens:
            e.__call__(self)

    def random_glitch(self):
        chosen = random.choice(self.cool_glithes)

        chosen.__call__(self)
