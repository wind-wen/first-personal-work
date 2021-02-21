# first-personal-work

### 词云图

步骤 | 具体做法
 ---- | -----   
 第一步: 进行数据采集:  | 采集腾讯视频里电视剧《在一起》的全部评论信息  
 第二步: 进行数据处理:  | 把所有数据下载到本地保存到json文件里面comments.json, 页面用js读取文件
 第三步: 数据分析展示:  | 将采集到的评论信息做成词云图
 

 ### 具体想法：
 ##### 1.Python爬虫
 在某些网站 ，当我们滑下去的时候才会显示出后面的内容，就像淘宝一样，滑下去才逐渐显示其他商品，这个就是采用 Ajax 做的，然后我们现在就是要编写这样的爬虫。
 我们需要分析加载评论的规律，首先使用谷歌浏览器打开腾讯视频里电视剧《在一起》的全部评论信息，然后再多次点击查看更多评论，按F12，可以得到多个变化的网址，经过观察，寻找规律，可以发下如下规律（请求URL 中只有 cursor 和 source 进行了改变，其他是不变的：cursor 其实是上一个用户data中的last所对应的数值； source 是在第一个的基础上进行加一操作）；同时发现评论内容在 content 里面

 ##### 2.数据的处理
首先从一个文本文件读入文本，并作了一些简单的替换，比如替换多个空格为单空格等。
使用关键词提取功能，提取权重最高的10个关键词。
使用精确模式对文件内容分词。
根据关键词和分词结果，统计词频。
排序并返回词频最高的单词和出现次数。

 ##### 3.数据分析展示
利用echarts.js制作词云