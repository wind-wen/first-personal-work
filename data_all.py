import urllib.request
import re
import time
import random
import json
try:
    #构建用户代理
    uapools=["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
         "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
         "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        ]
    #从用户代理池随机选取一个用户代理
    thisua = random.choice(uapools)
    headers = ("User-Agent",thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    
    first_id = 1613573389059
    comment_id = "0"  #  初始评论 id
    commentlist = []
    for i in range(1,1000):
        url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(comment_id)+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_="+str(first_id)
        content_path = '"content":"(.*?)",'  #  评论内容正则
        last_path = '"last":"(.*?)",'  #  last id 正则
        content_data = urllib.request.urlopen(url).read().decode("utf-8")
        content = re.compile(content_path).findall(content_data)  #  获取评论
        last_id = re.compile(last_path).findall(content_data)  # 获取 last id
        for j in last_id:  #  获取的 last id 是列表类型，要进行类型转换
            comment_id = j
        first_id += 1 
        commentlist.extend(content)
    
    with open('comments.json','a', encoding='utf-8') as fi:
        fi.write(json.dumps(commentlist,indent=2,ensure_ascii=False))
    
except Exception as error:
    print(error)
