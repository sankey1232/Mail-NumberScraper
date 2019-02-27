#! /usr/bin/python3
import re
import pyperclip

text = pyperclip.paste()

phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?        #Area Code(optional)
(\s|-)                          #Separator 1
(\d\d\d)                        #First 3 digits
(-)                             #Separator 2
(\d\d\d\d)                      #Last 4 digits
)
''', re.VERBOSE)

emailRegex = re.compile(r''' 
(
[a-z0-9_-]+                      #user name
@                               #@(at the rate)
[a-z0-9_]+                      #domain name               
(\.[a-z]{2,5})                  #post-domain part
)''', re.VERBOSE|re.I)
 
extractPhone=phoneRegex.findall(text)
extractMail=emailRegex.findall(text)

numbers=[]
emails=[]

for i in extractPhone:
    numbers.append(i[0])
for j in extractMail:
    emails.append(j[0])

output="\n".join(numbers)+"\n"+"\n".join(emails)
pyperclip.copy(output)