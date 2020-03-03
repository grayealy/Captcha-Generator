'''
Created on Feb 26, 2020

@author: nicomp
'''

from Assignment07 import generate_captcha

result = generate_captcha(11,"blah")
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()

