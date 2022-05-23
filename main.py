import random
from PIL import Image

random_no = random.randint(1, 6)

img = Image.open('test.png')
img.show()

