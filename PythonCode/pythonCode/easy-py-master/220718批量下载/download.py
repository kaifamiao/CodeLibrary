import urllib.request
import time

for i in range(1, 66):
    url = f'http://crossincode.com/static/{i:03d}.mp3'  
    urllib.request.urlretrieve(url, f'{i:03d}.mp3')
    print(i)
    time.sleep(0.2)