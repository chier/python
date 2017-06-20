#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 5-storeWikiLinks
# @Date    : 2017-06-20 16:21
# @Author  : zzl
"""
   python_version  2.7.11
"""
"""
SQL语句
/*
SQLyog Trial v10.2
MySQL - 5.6.20 : Database - scraping
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`scraping` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;

USE `scraping`;

/*Table structure for table `pages` */

CREATE TABLE `pages` (
  `id` bigint(7) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `content` text COLLATE utf8mb4_bin,
  `created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

/*Data for the table `pages` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

"""
from urllib2 import  urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host="127.0.0.1",
                       port=3356,
                       # unix_socket="/tmp/mysql.sock",
                       user="root",
                       passwd="secret",
                       charset="utf8"
                       )
cur = conn.cursor()
cur.execute("USE scraping")
random.seed(datetime.datetime.now())

def store(title,content):
    cur.execute("INSERT INTO pages (title,content) VALUES (\"%s\",\"%s\")",(title,content))
    cur.connection.commit()

def getLinks(articlueUrl):
    html = urlopen("http://en.wikipedia.org" + articlueUrl)
    htmlStr = html.read()
    print(htmlStr)
    bsObj = BeautifulSoup(htmlStr,"html5lib")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div",{"id":"mw-content-text"}).find("p").get_text()
    store(title,content)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",
                    href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links) >0:
        newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
        print (newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()