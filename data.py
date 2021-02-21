import urllib.request
import re
import time

headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
first_id = "1613573389059"
comment_id = "6716706003418103507"  #  初始评论 id
url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(comment_id)+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_="+str(first_id)
path = '"content":"(.*?)",'
data = urllib.request.urlopen(url).read().decode("utf-8")
resut = re.compile(path).findall(data)
print(resut)


