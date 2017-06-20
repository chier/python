#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Filename: 6-6DegreesCrawlWiki
# @Date    : 2017-06-20 16:41
# @Author  : zzl
"""
   python_version  2.7.11
"""
"""
SQL语句：
/*
SQLyog Trial v10.2
MySQL - 5.6.20 : Database - wikipedia
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`wikipedia` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;

USE `wikipedia`;

/*Table structure for table `links` */

CREATE TABLE `links` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fromPageId` int(11) DEFAULT NULL,
  `toPageId` int(11) DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

/*Data for the table `links` */

insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (1,1,2,'2017-06-20 16:53:07');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (2,2,1,'2017-06-20 16:53:09');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (3,2,3,'2017-06-20 16:53:09');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (4,3,4,'2017-06-20 16:53:11');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (5,4,5,'2017-06-20 16:53:15');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (6,5,4,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (7,5,6,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (8,5,7,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (9,5,8,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (10,5,9,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (11,5,10,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (12,5,11,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (13,5,12,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (14,5,13,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (15,5,14,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (16,5,15,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (17,5,16,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (18,5,17,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (19,5,18,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (20,5,19,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (21,5,20,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (22,5,21,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (23,5,5,'2017-06-20 16:53:17');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (24,5,22,'2017-06-20 16:53:18');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (25,4,21,'2017-06-20 16:53:18');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (26,21,4,'2017-06-20 16:53:21');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (27,21,23,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (28,21,24,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (29,21,25,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (30,21,26,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (31,21,27,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (32,21,28,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (33,21,29,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (34,21,30,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (35,21,31,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (36,21,32,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (37,21,33,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (38,21,34,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (39,21,35,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (40,21,36,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (41,21,37,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (42,21,38,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (43,21,39,'2017-06-20 16:53:22');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (44,21,40,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (45,21,41,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (46,21,42,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (47,21,43,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (48,21,44,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (49,21,45,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (50,21,46,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (51,21,47,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (52,21,48,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (53,21,49,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (54,21,50,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (55,21,51,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (56,21,52,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (57,21,53,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (58,21,54,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (59,21,55,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (60,21,56,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (61,21,57,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (62,21,58,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (63,21,59,'2017-06-20 16:53:23');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (64,21,60,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (65,21,7,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (66,21,61,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (67,21,62,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (68,21,63,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (69,21,64,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (70,21,65,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (71,21,66,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (72,21,67,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (73,21,68,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (74,21,69,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (75,21,70,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (76,21,71,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (77,21,72,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (78,21,73,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (79,21,74,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (80,21,75,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (81,21,76,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (82,21,77,'2017-06-20 16:53:24');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (83,21,78,'2017-06-20 16:53:25');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (84,21,79,'2017-06-20 16:53:25');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (85,21,80,'2017-06-20 16:53:25');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (86,21,81,'2017-06-20 16:53:25');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (87,21,82,'2017-06-20 16:53:25');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (88,21,83,'2017-06-20 16:53:25');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (89,21,84,'2017-06-20 16:53:25');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (90,21,85,'2017-06-20 16:53:25');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (91,21,86,'2017-06-20 16:53:25');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (92,21,87,'2017-06-20 16:53:26');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (93,21,88,'2017-06-20 16:53:26');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (94,21,89,'2017-06-20 16:53:26');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (95,21,90,'2017-06-20 16:53:26');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (96,21,91,'2017-06-20 16:53:26');
insert  into `links`(`id`,`fromPageId`,`toPageId`,`created`) values (97,21,92,'2017-06-20 16:53:26');

/*Table structure for table `pages` */

CREATE TABLE `pages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

/*Data for the table `pages` */

insert  into `pages`(`id`,`url`,`created`) values (1,'/wiki/Kevin_Bacon','2017-06-20 16:51:19');
insert  into `pages`(`id`,`url`,`created`) values (2,'/wiki/Kevin_Bacon_(disambiguation)','2017-06-20 16:53:07');
insert  into `pages`(`id`,`url`,`created`) values (3,'/wiki/Kevin_Bacon_(producer)','2017-06-20 16:53:09');
insert  into `pages`(`id`,`url`,`created`) values (4,'/wiki/Rotherham','2017-06-20 16:53:11');
insert  into `pages`(`id`,`url`,`created`) values (5,'/wiki/Rotherham_(disambiguation)','2017-06-20 16:53:15');
insert  into `pages`(`id`,`url`,`created`) values (6,'/wiki/Rotherham_(UK_Parliament_constituency)','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (7,'/wiki/Metropolitan_Borough_of_Rotherham','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (8,'/wiki/Rotherham,_New_Zealand','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (9,'/wiki/Alan_Rotherham','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (10,'/wiki/Arthur_Rotherham','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (11,'/wiki/Gerard_Rotherham','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (12,'/wiki/Hugh_Rotherham','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (13,'/wiki/Joseph_Bryant_Rotherham','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (14,'/wiki/Roland_Rotherham','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (15,'/wiki/Thomas_Rotherham','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (16,'/wiki/Edward_Rotheram','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (17,'/wiki/Steve_Rotheram','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (18,'/wiki/HMS_Rotherham_(H09)','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (19,'/wiki/Baron_Rotherham','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (20,'/wiki/Rotherham_United_F.C.','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (21,'/wiki/Rotherham_child_sexual_exploitation_scandal','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (22,'/wiki/Main_Page','2017-06-20 16:53:17');
insert  into `pages`(`id`,`url`,`created`) values (23,'/wiki/South_Yorkshire','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (24,'/wiki/Geographic_coordinate_system','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (25,'/wiki/Child_sexual_abuse','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (26,'/wiki/The_Times','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (27,'/wiki/Jayne_Senior','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (28,'/wiki/Rape','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (29,'/wiki/Conspiracy_(criminal)','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (30,'/wiki/Aiding_and_abetting','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (31,'/wiki/Indecent_assault','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (32,'/wiki/False_imprisonment','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (33,'/wiki/Procuring_(prostitution)','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (34,'/wiki/Orwell_Prize','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (35,'/wiki/British_Press_Awards','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (36,'/wiki/Order_of_the_British_Empire','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (37,'/wiki/2016_Birthday_Honours','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (38,'/wiki/Northern_England','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (39,'/wiki/Rotherham_Metropolitan_Borough_Council','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (40,'/wiki/British-Pakistani','2017-06-20 16:53:22');
insert  into `pages`(`id`,`url`,`created`) values (41,'/wiki/Rochdale_child_sex_abuse_ring','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (42,'/wiki/House_of_Commons','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (43,'/wiki/Home_Affairs_Committee','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (44,'/wiki/Alexis_Jay','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (45,'/wiki/Gang_rape','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (46,'/wiki/Sex_trafficking','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (47,'/wiki/Race_(human_categorization)','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (48,'/wiki/Social_class','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (49,'/wiki/Gender','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (50,'/wiki/Sexism','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (51,'/wiki/Working_class','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (52,'/wiki/Ethnicity','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (53,'/wiki/Racism','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (54,'/wiki/Labour_Party_(UK)','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (55,'/wiki/Police_and_Crime_Commissioner','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (56,'/wiki/South_Yorkshire_Police','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (57,'/wiki/Independent_Police_Complaints_Commission','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (58,'/wiki/National_Crime_Agency','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (59,'/wiki/Louise_Casey','2017-06-20 16:53:23');
insert  into `pages`(`id`,`url`,`created`) values (60,'/wiki/Whistleblower','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (61,'/wiki/United_Kingdom_Census_2011','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (62,'/wiki/Demography_of_the_United_Kingdom','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (63,'/wiki/Christian','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (64,'/wiki/Muslim','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (65,'/wiki/Hindu','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (66,'/wiki/Sikh','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (67,'/wiki/Jew','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (68,'/wiki/Buddhist','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (69,'/wiki/Public_housing_in_the_United_Kingdom','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (70,'/wiki/Sarah_Champion_(politician)','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (71,'/wiki/Conservative_Party_(UK)','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (72,'/wiki/UK_Independence_Party','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (73,'/wiki/Independent_politician#United_Kingdom','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (74,'/wiki/Department_for_Education','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (75,'/wiki/Online_grooming','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (76,'/wiki/Localised_grooming','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (77,'/wiki/British_Asian','2017-06-20 16:53:24');
insert  into `pages`(`id`,`url`,`created`) values (78,'/wiki/Red-light_district','2017-06-20 16:53:25');
insert  into `pages`(`id`,`url`,`created`) values (79,'/wiki/Home_Office','2017-06-20 16:53:25');
insert  into `pages`(`id`,`url`,`created`) values (80,'/wiki/University_of_Bedfordshire','2017-06-20 16:53:25');
insert  into `pages`(`id`,`url`,`created`) values (81,'/wiki/Panorama_(TV_series)','2017-06-20 16:53:25');
insert  into `pages`(`id`,`url`,`created`) values (82,'/wiki/Mike_Hedges','2017-06-20 16:53:25');
insert  into `pages`(`id`,`url`,`created`) values (83,'/wiki/Sheffield','2017-06-20 16:53:25');
insert  into `pages`(`id`,`url`,`created`) values (84,'/wiki/Crack_cocaine','2017-06-20 16:53:25');
insert  into `pages`(`id`,`url`,`created`) values (85,'/wiki/Shaun_Wright','2017-06-20 16:53:25');
insert  into `pages`(`id`,`url`,`created`) values (86,'/wiki/Executive_arrangements','2017-06-20 16:53:25');
insert  into `pages`(`id`,`url`,`created`) values (87,'/wiki/White_British','2017-06-20 16:53:26');
insert  into `pages`(`id`,`url`,`created`) values (88,'/wiki/Doncaster_Sheffield_Airport','2017-06-20 16:53:26');
insert  into `pages`(`id`,`url`,`created`) values (89,'/wiki/Freedom_of_Information_Act_2000','2017-06-20 16:53:26');
insert  into `pages`(`id`,`url`,`created`) values (90,'/wiki/Crown_Court','2017-06-20 16:53:26');
insert  into `pages`(`id`,`url`,`created`) values (91,'/wiki/Violent_and_Sex_Offender_Register','2017-06-20 16:53:26');
insert  into `pages`(`id`,`url`,`created`) values (92,'/wiki/Keighley_child_sex_abuse_ring','2017-06-20 16:53:26');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

"""
from bs4 import BeautifulSoup
import re
import pymysql
from urllib2 import urlopen

# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mysql', charset='utf8')
conn = pymysql.connect(host="127.0.0.1",
                       port=3356,
                       # unix_socket="/tmp/mysql.sock",
                       user="root",
                       passwd="secret",
                       charset="utf8"
                       )
cur = conn.cursor()
cur.execute("USE wikipedia")

def pageScraped(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        return False
    page = cur.fetchone()

    cur.execute("SELECT * FROM links WHERE fromPageId = %s", (int(page[0])))
    if cur.rowcount == 0:
        return False
    return True

def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)", (int(fromPageId), int(toPageId)))
        conn.commit()

def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pageScraped(link.attrs['href']):
            #We have encountered a new page, add it and search it for links
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage, recursionLevel+1)
        else:
            print("Skipping: "+str(link.attrs['href'])+" found on "+pageUrl)
getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()