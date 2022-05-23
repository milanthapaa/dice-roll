import random
from PIL import Image

random_no = random.randint(1, 6)

img = Image.open(f'img/inverted-dice-{random_no}.png')
img.show()

