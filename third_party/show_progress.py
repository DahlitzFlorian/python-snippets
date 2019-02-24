from time import sleep
from progressbar import ProgressBar

bar = ProgressBar()
for i in bar(range(50)):
    sleep(0.5)
