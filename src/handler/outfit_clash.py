# -*- coding:utf-8 -*-
# Author: 廿二月的天
import numpy
from PIL import Image, ImageDraw
from matplotlib import pyplot


class OutfitClash(object):
    """
    去同款类
    """

    def start(self, file_path):
        """
        开始去同款
        :param: file_path 图片路径
        :return: plt
        """

        image = numpy.array(Image.open(file_path).convert("RGBA"))
        width, height, dims = image.shape
        new_image = Image.new("RGBA", image.size)
        draw = ImageDraw.Draw(new_image)
        for i in range(width):
            for j in range(height):
                px = numpy.random.randint(0, 255)
                draw.point([i, j], px)

        img = Image.blend(new_image, image, 0.1)
        pyplot.imshow(img)
        pyplot.axis("off")
        return pyplot
