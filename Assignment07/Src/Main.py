'''
Created on Feb 26, 2020

@author: nicomp
'''

from Assignment07 import generate_captcha

result = generate_captcha(7,"C:\\Users\\graye\\git\\Captcha-Generator\\Assignment07\\Src\\CaptchaImages\\captcha.png")
print(result[0])
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()


