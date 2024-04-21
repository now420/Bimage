from PIL import Image

def encode(text, image_size=(100, 100), output_file="bw_image.png"):
    image = Image.new("L", image_size, color=255)  # "L" mode for grayscale

    binary_data = ''.join(format(ord(char), '08b') for char in text)

    pixels = image.load()
    k = 0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if k < len(binary_data):
                pixels[i, j] = int(binary_data[k]) * 255
                k += 1

    image.save(output_file)
    print("Image saved as", output_file)
  
# Usage
encode("Your text here.")
