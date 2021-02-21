
import jieba
import jieba.analyse
import codecs
import re
import json
from collections import Counter


class WordCounter(object):

    def count_from_file(self, file, top_limit=0):
        with codecs.open(file, 'r', 'utf-8') as f:
            content = f.read()
            content = re.sub(r'\s+', r' ', content)
            content = re.sub(r'\.+', r' ', content)
            return self.count_from_str(content, top_limit=top_limit)

    def count_from_str(self, content, top_limit=0):
        if top_limit <= 0:
            top_limit = 100
        tags = jieba.analyse.extract_tags(content, topK=100)

        words = jieba.cut(content)
        counter = Counter()
        for word in words:
            if word in tags:
                counter[word] += 1

        return counter.most_common(top_limit)


if __name__ == '__main__':
    counter = WordCounter()
    result = counter.count_from_file(r'comments.json')
    commentlist = []
    for k, v in result:
        comment = {}
        comment["name"] = k
        comment["value"] = v
        commentlist.append(comment)

    print(commentlist)

    with open('deal_comments.json','a', encoding='utf-8') as fi:
        fi.write(json.dumps(commentlist,indent=1,ensure_ascii=False))