import random
import urllib.request


def down_web_img(url):
    name = 'Love.jpg'
    urllib.request.urlretrieve(url, name)

down_web_img('https://pbs.twimg.com/profile_images/712703916358537217/mcOketun_400x400.jpg')

fw = open('sample.txt', 'w')
fw.write = ('1st line\n')
fw.write = ('2nd line\n')
fw.write = ('3rd line\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
