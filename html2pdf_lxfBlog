# -*- coding: utf-8 -*-
# py_version: 3.6.1

"""
爬取廖雪峰的python教程，转化成PDF文档

@author: yunpoyue
"""
import requests
from bs4 import BeautifulSoup
import pdfkit
import re
import os

# 备用url
urlBegin = "http://www.liaoxuefeng.com"
url = "http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>

"""


def parse_url_to_html(url, name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    body = soup.find_all(class_="x-wiki-content")[0]
    # 标题
    title = soup.find('h4').get_text()
    # 标题加入到正文的最前面，居中显示
    center_tag = soup.new_tag("center")
    title_tag = soup.new_tag('h1')
    title_tag.string = title
    center_tag.insert(1, title_tag)
    body.insert(1, center_tag)
    html = str(body)
    # body中的img标签的src相对路径的改成绝对路径
    pattern = "(<img .*?src=\")(.*?)(\")"

    def func(m):
        if not m.group(3).startswith("http"):
            rtn = m.group(1) + "http://www.liaoxuefeng.com" + \
                m.group(2) + m.group(3)
            return rtn
        else:
            return m.group(1) + m.group(2) + m.group(3)

    html = re.compile(pattern).sub(func, html)
    html = html_template.format(content=html)
    html = html.encode("utf-8")
    with open(name, "wb") as f:
        f.write(html)
    return name


def get_url_list(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for li in menu_tag.find_all("li"):
        url = urlBegin + li.a.get('href')
        urls.append(url)
    return urls


def save_pdf(htmls, file_name):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    # 环境变量不起作用，解决意外报错：IOError: No wkhtmltopdf executable found: ""
    path_wkthmltopdf = r'C:\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_file(htmls, file_name, options=options, configuration=config)


urls = get_url_list(url)
file_name = "Python3.pdf"
htmls = [parse_url_to_html(l, str(index) + ".html")
         for index, l in enumerate(urls)]
save_pdf(htmls, file_name)

for html in htmls:
    os.remove(html)
