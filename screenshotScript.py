import pyautogui
import time

while True:
    name = time.localtime(time.time())
    

    imgName = str(name.tm_mday)+":"+str(name.tm_mon)+":"+str(name.tm_year)+" "+str(name.tm_hour)+":"+str(name.tm_min)+":"+str(name.tm_sec)+".png"
    print(imgName)

    img=pyautogui.screenshot()
    img.save(imgName)
    time.sleep(30)
