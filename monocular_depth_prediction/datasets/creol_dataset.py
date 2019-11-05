import os
import numpy as np
import PIL.Image as pil

from datasets.mono_dataset import *

class CreolDataset(MonoDataset):
    def __init__(self, *args, **kwargs):
        super(CreolDataset, self).__init__(*args, **kwargs)

        self.K = np.array([[0.58, 0, 0.5, 0],
                           [0, 1.92, 0.5, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]], dtype=np.float32)

        self.full_res_shape = (1242, 375)
        self.side_map = {"2": 2, "3": 3, "l": 2, "r": 3}
        self.img_ext = '.jpg'
        self.loader = pil_loader

    def check_depth(self):
        # CREOL dataset has no ground truth depth

        return False

    def get_color(self, frame_index, do_flip, line):
        color = self.loader(self.get_image_path(frame_index, line))

        if do_flip:
            color = color.transpose(pil.FLIP_LEFT_RIGHT)

        return color

    def get_image_path(self, frame_index, line):
        f_str = "{}{}".format(frame_index, self.img_ext)
        path = line.split('/')[:-1]
        path = '/'.join(path)

        image_path = os.path.join(path, "image_{}".format(f_str))

        return image_path