-- @Author: Freator
-- @Email: tbcong@qq.com
-- @Github: https://github.com/Freator
-- @Version: MySQL 5.5.27

-- 创建数据库
CREATE DATABASE doubanSpider DEFAULT CHARACTER SET utf8;
-- 使用此数据库
USE doubanSpider;
-- 创建数学类书籍信息表
CREATE TABLE Math(
序号 int,
书名 varchar(100),
评分 float(10,2),
评分人数 int,
作者_译者 varchar(150),
出版信息 varchar(300)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 创建计算机类书籍信息表
CREATE TABLE Computer(
序号 int,
书名 varchar(100),
评分 float(10,2),
评分人数 int,
作者_译者 varchar(150),
出版信息 varchar(300)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 创建python类书籍信息表
CREATE TABLE Python(
序号 int,
书名 varchar(100),
评分 float(10,2),
评分人数 int,
作者_译者 varchar(150),
出版信息 varchar(300)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 创建旅行类书籍信息表
CREATE TABLE Journey(
序号 int,
书名 varchar(100),
评分 float(10,2),
评分人数 int,
作者_译者 varchar(150),
出版信息 varchar(300)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 创建教育类书籍信息表
CREATE TABLE Education(
序号 int,
书名 varchar(100),
评分 float(10,2),
评分人数 int,
作者_译者 varchar(150),
出版信息 varchar(300)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;