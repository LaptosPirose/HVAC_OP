import os

current_path = os.getcwd()
print(current_path)

# Path to images
image_path = os.path.join(current_path, 'windows/images/')

images = {
    0: image_path + "icon.png",
    1: image_path + "python.png",
    2: image_path + "mario.gif"
}

print(images.keys())
print(images.values())
