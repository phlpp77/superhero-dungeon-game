# Purpose:
#   - easily display all images supplied from MapConstructor
#   - binding keys for navigation

import kivy
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty


class Interface:
    def __init__(self):
        self.windowsize = [1080, 1920]
        self.max_block_res = 0
        self.block_scale = 0

    def refresh_all(self, imagelist):
        # getting the dimensions of a single image
        dimensions = [imagelist[0][0][0][0].width, imagelist[0][0][0][0].height]
        list_height, list_width = len(imagelist), len(imagelist[0])

        # determining the maximum block resolution so that all images fit into the window
        scalex, scaley = self.windowsize[0] / list_height, self.windowsize[1] / list_width
        self.max_block_res = scalex if scalex < scaley else scaley
        self.block_scale = self.max_block_res / dimensions[0]

        # displaying all images
        for x in range(list_height):
            for y in range(list_width):
                self.refresh_single(x, y, imagelist[x][y])

    # given the coordinates of the field in the imagelist and the imagelist-alpha tuple
    # TODO displays the field on the screen
    def refresh_single(self, x, y, field):
        coords_in_window = [x * self.max_block_res, y * self.max_block_res]
        images, alpha = field[0], field[1]
        for image in images:
            # display over each other, with rgba = 1,1,1,alpha
            print(coords_in_window, image)
