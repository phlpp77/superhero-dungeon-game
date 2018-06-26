# Purpose:
#   - easily display all images supplied from MapConstructor
#   - binding keys for navigation


class Interface:
    """A class providing easy support for displaying an image-tilemap"""
    def __init__(self):
        self.windowsize = [1080, 1920]
        self.max_block_res, self.block_scale = 0, 0
        self.map_buffer = [[]]  # buffer for the last imagelist
        self.refresh_buffer = [[]]  # buffer for the changed images
        self.buffer_height, self.buffer_width = len(self.map_buffer), len(self.map_buffer[0])

    def next_lvl(self, imagelist: [[[(str, float)]]]):
        """
        Method refreshing the displayed fields and their dimensions on screen
        :param imagelist: [[[(str, float)]]]
        """
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

        # refreshing the buffered map
        self.map_buffer, self.buffer_height, self.buffer_width = imagelist, list_height, list_width

    def refresh_lvl_map(self, imagelist: [[[(str, float)]]]):
        """
        Method refreshing the display of images that have changed
        :param imagelist: [[[(str, float)]]]
        """
        list_height, list_width = len(imagelist), len(imagelist[0])
        # if the new map is smaller than the one in the buffer, out-of-bounds exceptions have to be avoided
        if self.buffer_height > list_height:
            self.buffer_height = list_height
        if self.buffer_width > list_width:
            self.buffer_width = list_width

        # deleting the elements already being displayed
        for x in range(self.buffer_height):
            for y in range(self.buffer_width):
                if imagelist[x][y] != self.map_buffer[x][y]:
                    self.refresh_single(x, y, imagelist[x][y])
        # refreshing the buffered map
        self.map_buffer, self.buffer_height, self.buffer_width = imagelist, list_height, list_width

    def refresh_single(self, x, y, field: [(str, float)]):
        """
        Method that, given the coordinates of the field in the imagelist and the imagelist-alpha-tupe,
            TODO displays the field on screen
        :param x: int
        :param y: int
        :param field: [(str, float)]
        """
        coords_in_window = [x * self.max_block_res, y * self.max_block_res]
        images, alpha = field[0], field[1]
        for image in images:
            # display over each other, with rgba = 1,1,1,alpha
            print(coords_in_window, image)
