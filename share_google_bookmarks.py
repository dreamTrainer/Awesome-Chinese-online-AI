import re
import pandas as pd
from bs4 import BeautifulSoup

def dfs(tag,parent_name,result):
    # 打印当前标签
    new = parent_name
    if tag:
        if tag.name == 'a':
            result.append({'parent':new, 'text':tag.text,'url':tag.get('href')})
            #print({'parent':new,'tag':tag.name,'text':tag.text,'url':tag.get('href')})
        else:
            #print(parent_name,tag.name,tag.text)
            # 遍历当前标签的所有子标签
            for child in tag.children:
                # 如果子标签是BeautifulSoup的NavigableString类型，则跳过
                if isinstance(child, str):
                    continue
                if child.name == 'h3':
                    #new = parent_name+'/'+child.text
                    new = parent_name+'/'+child.text
                    continue
                else:
                    # 递归调用dfs函数
                    dfs( child,new,result)
                    new = parent_name

if __name__ == '__main__':
    # 假设你的Google书签HTML文件路径如下
    file_path = 'books/bookmarks_2024_7_20.html'
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # 解析HTML内容
    soup = BeautifulSoup(content, 'html.parser')
    result = []
    # 从根节点开始深度优先遍历
    datas = []
    dfs(soup,'root',datas)
    df = pd.DataFrame(datas)
    print(len(df))
    df = df.drop_duplicates(subset='url')
    print('去重后数量',len(df))
    # 正则表达式匹配IPv4地址
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    # 示例文本
    text = "访问网站 http://192.168.1.1 或者 http://10.0.0.1 查看更多信息。"
    # 检查文本中是否有IP地址
    df['是否是部署服务']  =df['url'].apply(lambda x: 1 if ip_pattern.search(x) or 'localhost' in x else 0)
    df['NSFW'] = df['url'].apply(lambda x:1 if 'lihu' in x  else 0)
    df = df[df['是否是部署服务']==0]
    df = df[df['NSFW']==0]
    df['prefix'] = df['url'].apply(lambda x: '/'.join(x.split('/')[:3]))
    del df['是否是部署服务']
    del df['NSFW']
    print('网站个数',len(df['prefix'].unique()))
    df.to_csv('books/bookmarks_2024_7_20.csv',index=False,encoding='utf-8-sig')

 

