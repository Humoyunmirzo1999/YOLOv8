from PIL import Image

# Load your image
image = Image.open('car.jpg')

# Define the coordinates (x, y) of the top-left corner and the width and height for the crop
x = 81.8120 #640
y = 391 #638
width = 324
height = 164

# Crop the image
cropped_image = image.crop((x, y, x + width, y + height))

# Save or display the cropped image
cropped_image.save('./runs/detect/cut/1.jpg')
# or
cropped_image.show()
