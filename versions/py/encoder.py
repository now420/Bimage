# Version 2 (Python) of Bimage by @now420 on github, saqqwd on discord.
from PIL import Image
from math import ceil, sqrt

def encode(text, output_file="bw_image.png"):
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    data_length = len(binary_data)

    # Calculate the optimal square image size
    image_size = int(ceil(sqrt(data_length)))

    image = Image.new("L", (image_size, image_size), color=255)
    pixels = image.load()

    k = 0
    for i in range(image_size):
        for j in range(image_size):
            if k < data_length:
                pixels[i, j] = 0 if binary_data[k] == '1' else 255
            k += 1

    image.save(output_file)
    print("Image saved as", output_file)

# Usage
encode("Your text heraaaaaaaaaaaaaaaaaaaaaaasdqwdqwdqwdqdasdwqdasdqwdasdqwde.")
