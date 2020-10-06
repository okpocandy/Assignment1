import numpy as np
from PIL import Image
import matplotlib.pylab as plt


image = Image.open("./lenna.png")

plt.imshow(image)
plt.show()

image_reverse = image.transpose(Image.FLIP_LEFT_RIGHT)

plt.imshow(image_reverse)
plt.show()

image_rotate = image.transpose(Image.ROTATE_180)

plt.imshow(image_rotate)
plt.show()

image_resize = image.size
print(image_resize)

image_resize = image.resize((int(image_resize[0]*(0.5)),int(image_resize[1]*(0.5))))

plt.imshow(image_resize)
plt.show()



