from urllib.request import urlopen , urlretrieve
import json
import codecs
import os

for m in range(6):
    url = "https://www.google.com/doodles/json/2020/" + str(m+1) + "?hl=zh_TW"
    response = urlopen(url)

    doodles = json.load(response)
    for d in doodles:
        url = "https:" + d["url"]
        print(d["title"], url)
        fname = "doodles" + url.split("/")[-1]

        dirname = "doodles/" + str(m + 1) + "/"

        if not os.path.exists(dirname):
            os.mkdir(dirname)

        urlretrieve(url, dirname + fname)



        '''
        response = urlopen(url)
        img = response.read()
        with codecs.open(fname, "wb") as f:
            f.write(img)
        '''
