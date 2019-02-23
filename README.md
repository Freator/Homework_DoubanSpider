# DoubanSpider
这是一个豆瓣图书爬取项目，将图书的相关信息爬取到Excel文件中，
然后再链接MySQL数据库，将爬取到的数据存入数据库中。  
1. 爬取数据  
主要爬取了**数学、计算机、python、旅行、教育**这5个类别的书籍数据（每个类别爬取了5页数据），
每一组书籍数据包括：**序号,书名,评分,评价人数,作者,出版社**这几个属性。
![正在下载](./Pictures/downloading.png "downloading")  
![完成下载](./Pictures/downloaded.png "downloaded")