# Imageio is a Python library that provides an easy interface to read and write a wide range of image data. It runs on Python 3.5 and above.

import imageio.v3 as iio

filenames = ['codedex1.jpg', 'codedex2.jpg'] # List of image files to include in the GIF
images = [] # List to hold the image data

for filename in filenames:
    try:
        images.append(iio.imread(filename)) # Read each image and append to the list
    except FileNotFoundError:
        print(f"Warning: file not found, skipping: {filename}")
    except Exception as e:
        print(f"Warning: failed to read {filename}: {e}")

# Write the images to a GIF file with specified duration (seconds per frame) and loop settings
if images:
    iio.imwrite('codedex.gif', images, duration=0.5, loop=0)
else:
    print("No images were loaded; GIF not created.")