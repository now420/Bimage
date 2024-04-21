# Version 2 (Python) of Bimage by @now420 on github, saqqwd on discord.
from PIL import Image

def decode(input_file="bw_image.png"):
    image = Image.open(input_file)
    pixels = image.load()

    binary_data = ""
    width, height = image.size

    for i in range(width):
        for j in range(height):
            pixel_value = pixels[i, j]
            binary_data += '1' if pixel_value == 0 else '0'

    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        text += chr(int(byte, 2))

    return text

# Usage
decoded_text = decode("bw_image.png")
print("Decoded text:", decoded_text)
