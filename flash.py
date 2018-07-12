from PIL import ImageGrab
import pyautogui as pag
import time
import aircv as ac
def findpositon(img):
    time.sleep(2)
    templatei=[]
    pag.screenshot('location.png')
    imsrc = ac.imread('location.png')
    imobj = ac.imread(img)
    pos = ac.find_all_template(imsrc, imobj)
    for i in pos:
        if i['confidence']>=0.8:
            templatei.append(dict(result=i['result']))
    return templatei
def oneclick(list):
    for o in range(len(list)):
        x=list[o]['result'][0]+5
        y=list[o]['result'][1]+5
        pag.click(x=x, y=y, button='left')
def threeclick(list):
    for o in range(len(list)):
        x=list[o]['result'][0]+5
        y=list[o]['result'][1]+5
        pag.click(x=x, y=y, button='left')
        time.sleep(2)
        try:
            oneclick(findpositon('submit.png'))
        except:
            print('..')
        oneclick(findpositon('continue.png'))
def playmain():
    try:
        oneclick(findpositon('logo.png'))
        threeclick(findpositon('select.png'))
    except:
        time.sleep(1)
    time.sleep(20)