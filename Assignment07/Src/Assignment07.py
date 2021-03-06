'''
Name: Gray Ealy
Email: ealygg@mail.uc.edu
Assignment: Assignment07
Course: IS 4010
Semester/Year: Spring 2020
Brief Description: This project demonstrates the use of image manipulation and truetype fonts fun
'''
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont

default_color_red = 228
default_color_green = 150
default_color_blue = 150

def generate_random_string(length):
    random_string = ""
    for i in range(0,length):
        random_string = random_string + random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVQXYZ')
    return random_string

def draw_random_ellipse(draw):
    # A random circle on the image
    a = random.randrange(10, 300, 1)
    b = random.randrange(10, 275, 1)
    c = a + random.randrange(10, 90, 1)
    d = b + random.randrange(10, 90, 1)
    draw.ellipse((a,b,c,d), fill=(default_color_red + random.randrange(-100,100,1), 
                                  default_color_green + random.randrange(-100,100,1), 
                                  default_color_blue + random.randrange(-100,100,1), 255), 
                                  outline = "black")

def generate_captcha(char_count, file_location):
    '''
    Generate a captcha
    :return: A tuple (image, captcha string encoded in the image)
    '''
    
    if char_count >= 6 and char_count <= 10:
        captcha_string = generate_random_string(char_count)
    else:
        print("You've entered a char_count outside of the range. Your new char_count will be random between 6 and 10")
        captcha_string = generate_random_string(random.randrange(6,10))
    
#   print(">" + captcha_string + "<")

    captcha_image = Image.new("RGBA", (400, 200), (default_color_red,default_color_green,default_color_blue))
    draw = ImageDraw.Draw(captcha_image, "RGBA")
    for i in range(1,20):
        draw_random_ellipse(draw)
    #captcha_image.save( file_location ) 
    

    styles = [ImageFont.truetype("SAEROWS DEMO.ttf", 48), ImageFont.truetype("SURVIVOR demo.ttf", 48), ImageFont.truetype("Aaargh.ttf", 48)]
    #fontStyle = ImageFont.truetype("Aaargh.ttf", 48)     # font must be in the same folder as the .py file. 

    styleChoice = random.randrange(0,2)
    # Arbitrary starting co-ordinates for the text we will write
    x = 10 + random.randrange(0, 100, 1)
    y = 79 + random.randrange(-10, 10, 1)
    for letter in captcha_string:
#       print(letter)
        draw.text((x, y), letter, (0,0,0),font=styles[styleChoice])    # Write in black
        x = x + 35
        y = y +  random.randrange(-10, 10, 1)
    
    
    new_captcha = (captcha_image, captcha_string)
    new_captcha[0].save( file_location) #saves the generated captcha out to 'CaptchaImages' folder in my Src folder. Each time the function is callled, it will save the newly generated captcha. 
    
    return (new_captcha)  # return a heterogeneous tuple
