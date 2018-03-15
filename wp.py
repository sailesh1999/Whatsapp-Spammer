from pyautogui import *
from time import sleep
import sys
import webbrowser


	
name=input('Enter name: ')
no=int(input('Enter no of times message should be sent: '))
msg=input('Enter message that is to be sent: ')

controller=webbrowser.get('google-chrome')
#m=57
#n=538

controller.open('https://web.whatsapp.com/')
coOr=None
x=1
while coOr==None:
	sleep(5)
	coOr=locateOnScreen('/home/sailesh/Desktop/searchbar.png')
	'''print('iteration',x)
	x+=1
	'''

'''
coOr=locateOnScreen('/home/sailesh/Desktop/searchbar.png')
print(coOr)
'''
x1,y1=center(coOr)
#x2,y2=size()
moveTo(x1,y1)
click()
typewrite(name,interval=0.2)
sleep(2)
press('enter')

c=confirm(text="Did the program selected right person? Note: Once started, the program can't be terminated until task is completed", title='Continue?', buttons=['Yes', 'Cancel'])


#c=input('Continue (y/n)')
if c=='Cancel':
	sys.exit()

'''
x=x1
y=((m*y2)+(n*y1))/(m+n)
print(y)

moveTo(x,y)
click()
sleep(5)
'''
x3,y3=locateCenterOnScreen('/home/sailesh/Desktop/msgbox.png')
moveTo(x3,y3)
click()
sleep(2)
for i in range(no):
    typewrite(msg)
    press('enter')	

print('program completed')

