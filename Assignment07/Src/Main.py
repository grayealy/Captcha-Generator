'''
Name: Gray Ealy
Email: ealygg@mail.uc.edu
Assignment: Assignment07
Course: IS 4010
Semester/Year: Spring 2020
Brief Description: This project demonstrates the use of image manipulation and truetype fonts fun
Citations: N/A
'''

from Assignment07 import generate_captcha
from PIL.Image import Image

file_location = "C:\\Users\\graye\\git\\Captcha-Generator\\Assignment07\\Src\\CaptchaImages\\captcha.png" #have to add double back slashes because the character assignment for "\" is a return.
result = generate_captcha(7, file_location) 
print(result[0])
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()


