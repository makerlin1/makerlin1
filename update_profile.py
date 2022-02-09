import requests
import json
from io import BytesIO
from PIL import Image

url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1614319565639&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
res = requests.get(url)
source = "https://bing.com" + json.loads(res.text)["images"][0]["url"]
res = requests.get(source)
p_img = Image.open(BytesIO(res.content))   # BytesIO实现了在内存中读写Bytes
p_img.save("bing_img.png")
