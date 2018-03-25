from pyautogui import *
from time import sleep
import sys
import webbrowser

path1=' '  #Paste the path of "searchbar.png" image here         
path2=' '    #Paste the path of "msgbox.png" image here


name = input('Enter name: ')
no = int(input('Enter no of times message should be sent: '))
msg = input('Enter message that is to be sent: ')

controller = webbrowser.get('google-chrome')


controller.open('https://web.whatsapp.com/')
coOr = None
x = 1

while coOr == None:
    sleep(5)
    coOr = locateOnScreen(path1)



x1, y1 = center(coOr)

moveTo(x1, y1)
click()
typewrite(name, interval=0.2)
sleep(2)
press('enter')

c = confirm(
    text="Did the program selected right person? Note: Once started, the program can't be terminated until task is completed",
    title='Continue?', buttons=['Yes', 'Cancel'])


if c == 'Cancel':
    sys.exit()


x3, y3 = locateCenterOnScreen(path2)
moveTo(x3, y3)
click()
sleep(2)
for i in range(no):
    typewrite(msg)
    press('enter')

print('Program completed')
