import xlrd
import pymysql
dataSum = 0
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("book_list-数学-计算机-python-旅行-教育.xlsx")
sheetNames = book.sheet_names()
#建立一个MySQL连接
conn = pymysql.connect(
        host='localhost', 
        user='root', 
        passwd='root',  
        db='doubanSpider',  
        port=3306,  
        charset='utf8'
        )
# 获得游标
cur = conn.cursor()
# 创建插入SQL语句
dict = {'数学':'math', '计算机':'computer', 'python':'python', '旅行':'journey', '教育':'education', 'Sheet':'sheet'}
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for sheetName in sheetNames:
    if dict[sheetName] != 'sheet':
        sheet = book.sheet_by_name(sheetName)
        query = 'insert into ' + dict[sheetName] + ' (''序号'',''书名'',''评分'',''评分人数'',''作者_译者'',''出版信息'') values (%s, %s, %s, %s, %s, %s)'
        for r in range(1, sheet.nrows):
            book_id = int(sheet.row_values(r)[0])
            book_name = sheet.row_values(r)[1]
            rating = sheet.row_values(r)[2]
            people_num = int(sheet.row_values(r)[3])
            author_info = sheet.row_values(r)[4][7:]
            pub_info = sheet.row_values(r)[5][7:]
            values = [book_id, book_name, rating, people_num, author_info, pub_info]
            # 执行sql语句
            cur.execute(query, values)
        columns = str(sheet.ncols)
        rows = str(sheet.nrows)
        dataSum += sheet.nrows
        print ("导入 " + columns + " 列 " + rows + " 行数据到 " + dict[sheetName] + "数据表!")
cur.close()
conn.commit()
conn.close()
print ("%d 行数据已全部导入到MySQL数据库!" %(dataSum))