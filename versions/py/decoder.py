from PIL import Image

def decode(image_file):
    image = Image.open(image_file)

    binary_data = ""
    pixels = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            binary_data += "1" if pixels[i, j] > 127 else "0"

    text = ""
    for i in range(0, len(binary_data), 8):
        # Convert each 8-bit binary chunk to a character
        char = chr(int(binary_data[i:i+8], 2))
        text += char

    text = text.replace("ÿ", "")

    return text
    
# Usage
decoded_text = decode("bw_image.png")
print("Decoded Text:", decoded_text)
