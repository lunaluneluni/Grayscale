from PIL import Image

# Created by Luna
# Last updated: 3/20/18

# Picture credit: @matthewhenry on Unsplash

# Creating tuples
black = (0, 0, 0)
dark_gray = (80, 80, 80)
gray = (120, 120, 120)
light_gray = (140, 140, 140)
lighter_gray = (160, 160, 160)
lightest_gray = (200, 200, 200)
white = (255, 255, 255)

pug = Image.open(r"pug.jpg")
pug_list = pug.getdata() # Set pixel values of the image to pug_list
pug_list = list(pug_list) # Converting pug_list to a list

recolor = []

for pixel in pug_list:
    intensity = pixel[0] + pixel[1] + pixel[2]

    if intensity <= 0:
        recolor.append(white)
    elif intensity >= 220 and intensity < 300:
        recolor.append(lightest_gray)
    elif intensity >= 300 and intensity < 350:
        recolor.append(lighter_gray)
    elif intensity >= 350 and intensity < 410:
        recolor.append(light_gray)
    elif intensity >= 410 and intensity < 480:
        recolor.append(gray)
    elif intensity >= 480 and intensity < 600:
        recolor.append(dark_gray)
    else:
        recolor.append(black)

new_pug = Image.new("RGB", pug.size) # Creating new image
new_pug.putdata(recolor) # Copying the data into the new image
new_pug.show()
new_pug.save("recolored.jpg", "jpeg")
