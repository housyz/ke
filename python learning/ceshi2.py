import requests
from lxml import etree


url = "https://blog.csdn.net/qq_25990967/article/details/122498476?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522169865789216800186546688%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=169865789216800186546688&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-122498476-null-null.142^v96^pc_search_result_base8&utm_term=xpath&spm=1018.2226.3001.4187"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
html = response.text
html = etree.HTML(html)
a = html.xpath("//h2[@style='margin-left:0px;']/span")
print(str(a))
