import matplotlib.pyplot as plt
from PIL import Image
import math



class ImageMatrix:
    def __init__(self, folder_path, figsize=(10, 10), axis='off'):
        self.folder_path = folder_path
        self.figsize = figsize
        self.axis = axis
        self.random = False

    def rand(self):
        self.random = True
        return self

    def display_image(self, grid_dimensions, print_all=True, display_name=False):
        num_columns = grid_dimensions[1]
        images = os.listdir(self.folder_path)
        num_images = len(images)
        num_rows = math.ceil(num_images / num_columns) if print_all else grid_dimensions[0]

        if self.random:
            images = random.sample(images, min(num_rows * num_columns, num_images))

        fig, axs = plt.subplots(num_rows, num_columns, figsize=self.figsize)
        for i in range(num_rows):
            for j in range(num_columns):
                index = i * num_columns + j
                if index < len(images):
                    img = Image.open(os.path.join(self.folder_path, images[index]))
                    axs[i, j].imshow(img)
                    axs[i, j].axis(self.axis)
                    if display_name:
                        axs[i, j].set_title(images[index])
                else:
                    axs[i, j].axis('off')

        plt.tight_layout()
        plt.show()
