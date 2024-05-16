-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: fb_server
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `access_record`
--

DROP TABLE IF EXISTS `access_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `access_record` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `access_date` date NOT NULL,
  `count` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_record`
--

LOCK TABLES `access_record` WRITE;
/*!40000 ALTER TABLE `access_record` DISABLE KEYS */;
INSERT INTO `access_record` VALUES (1,'192.168.31.122','2024-04-02',184),(2,'192.168.31.94','2024-04-02',1),(3,'192.168.31.140','2024-04-02',3),(4,'192.168.31.140','2024-04-03',429),(5,'192.168.31.122','2024-04-03',294),(6,'192.168.31.140','2024-04-04',233),(7,'192.168.31.140','2024-04-05',338),(8,'192.168.31.112','2024-04-06',293),(9,'192.168.31.112','2024-04-07',284),(10,'192.168.31.140','2024-04-07',171),(11,'192.168.31.112','2024-04-08',949),(12,'192.168.31.140','2024-04-08',316),(13,'192.168.31.112','2024-04-09',707),(14,'127.0.0.1','2024-04-09',835),(15,'192.168.31.16:80','2024-04-09',1),(16,'192.168.31.10','2024-04-09',1),(17,'192.168.31.11','2024-04-09',1),(18,'192.168.31.140','2024-04-09',5),(19,'192.168.31.None','2024-04-09',4),(20,'192.168.31.140','2024-04-10',349),(21,'192.168.31.112','2024-04-10',340),(22,'192.168.31.112','2024-04-11',806),(23,'192.168.31.140','2024-04-11',434),(24,'192.168.31.112','2024-04-12',291),(25,'192.168.31.140','2024-04-12',279),(26,'192.168.31.140','2024-04-13',400),(27,'192.168.31.112','2024-04-13',448),(28,'192.168.31.140','2024-04-14',382),(29,'192.168.31.112','2024-04-14',236),(30,'192.168.31.140','2024-04-15',193),(31,'192.168.31.112','2024-04-15',790),(32,'192.168.31.112','2024-04-16',1036),(33,'192.168.31.140','2024-04-16',647),(34,'192.168.31.140','2024-04-17',433),(35,'192.168.31.112','2024-04-17',488),(36,'192.168.31.112','2024-04-18',685),(37,'192.168.31.140','2024-04-18',516),(38,'192.168.31.140','2024-04-19',286),(39,'192.168.31.112','2024-04-19',212),(40,'192.168.31.140','2024-04-20',442),(41,'192.168.31.112','2024-04-20',773),(42,'192.168.31.112','2024-04-21',614),(43,'192.168.31.140','2024-04-21',178),(44,'192.168.31.None','2024-04-21',2),(45,'192.168.31.112','2024-04-22',617),(46,'192.168.31.140','2024-04-22',352),(47,'192.168.31.140','2024-04-23',692),(48,'192.168.31.112','2024-04-23',309),(49,'192.168.31.140','2024-04-24',225),(50,'192.168.31.112','2024-04-24',569),(51,'192.168.31.140','2024-04-25',511),(52,'192.168.31.112','2024-04-25',682),(53,'192.168.31.140','2024-04-26',388),(54,'192.168.31.112','2024-04-26',621),(55,'192.168.31.112','2024-04-27',1032),(56,'192.168.31.140','2024-04-27',880),(57,'192.168.31.112','2024-04-28',900),(58,'192.168.31.140','2024-04-28',476),(59,'192.168.31.112','2024-04-29',762),(60,'192.168.31.140','2024-04-29',356),(61,'192.168.31.000','2024-04-29',1),(62,'192.168.31.140','2024-04-30',273),(63,'192.168.31.112','2024-04-30',267),(64,'192.168.31.140','2024-05-01',842),(65,'192.168.31.112','2024-05-01',532),(66,'192.168.31.140','2024-05-02',433),(67,'192.168.31.112','2024-05-02',414),(68,'192.168.31.112','2024-05-03',508),(69,'192.168.31.140','2024-05-03',409),(70,'192.168.31.140','2024-05-04',362),(71,'192.168.31.112','2024-05-04',390),(72,'192.168.31.112','2024-05-05',766),(73,'192.168.31.140','2024-05-05',523),(74,'192.168.31.112','2024-05-06',953),(75,'192.168.31.140','2024-05-06',267),(76,'192.168.31.140','2024-05-07',502),(77,'192.168.31.112','2024-05-07',210),(78,'192.168.31.112','2024-05-08',299),(79,'192.168.31.140','2024-05-08',589),(80,'192.168.31.140','2024-05-09',257),(81,'192.168.31.112','2024-05-09',446),(82,'192.168.31.140','2024-05-10',159),(83,'192.168.31.112','2024-05-10',209),(84,'192.168.31.140','2024-05-11',210),(85,'192.168.31.112','2024-05-11',229),(86,'192.168.31.140','2024-05-12',200),(87,'192.168.31.112','2024-05-13',226),(88,'192.168.31.140','2024-05-13',200),(89,'192.168.31.140','2024-05-14',402),(90,'192.168.31.112','2024-05-14',228),(91,'192.168.31.140','2024-05-15',387),(92,'192.168.31.112','2024-05-15',227),(93,'192.168.31.140','2024-05-16',155);
/*!40000 ALTER TABLE `access_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `access_record_face_fri`
--

DROP TABLE IF EXISTS `access_record_face_fri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `access_record_face_fri` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `access_date` date NOT NULL,
  `count` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_record_face_fri`
--

LOCK TABLES `access_record_face_fri` WRITE;
/*!40000 ALTER TABLE `access_record_face_fri` DISABLE KEYS */;
INSERT INTO `access_record_face_fri` VALUES (1,'192.168.31.5','2024-05-07',1),(2,'192.168.31.112','2024-05-08',6),(3,'192.168.31.15','2024-05-08',5),(4,'192.168.31.140','2024-05-09',365),(5,'192.168.31.140','2024-05-10',6),(6,'192.168.31.140','2024-05-12',163),(7,'192.168.31.112','2024-05-12',224),(8,'192.168.31.140','2024-05-13',200);
/*!40000 ALTER TABLE `access_record_face_fri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `access_record_face_send_group`
--

DROP TABLE IF EXISTS `access_record_face_send_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `access_record_face_send_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `access_date` date NOT NULL,
  `count` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_record_face_send_group`
--

LOCK TABLES `access_record_face_send_group` WRITE;
/*!40000 ALTER TABLE `access_record_face_send_group` DISABLE KEYS */;
INSERT INTO `access_record_face_send_group` VALUES (1,'192.168.31.5','2024-05-07',1),(2,'192.168.31.15','2024-05-08',4),(3,'192.168.31.112','2024-05-08',6),(4,'192.168.31.140','2024-05-08',43),(5,'192.168.31.140','2024-05-09',164),(6,'192.168.31.112','2024-05-09',9),(7,'192.168.31.112','2024-05-10',307),(8,'192.168.31.140','2024-05-10',295),(9,'192.168.31.140','2024-05-11',163),(10,'192.168.31.112','2024-05-11',232),(11,'192.168.31.140','2024-05-12',163),(12,'192.168.31.112','2024-05-12',208),(13,'192.168.31.112','2024-05-13',566),(14,'192.168.31.140','2024-05-13',155),(15,'192.168.31.112','2024-05-14',552),(16,'192.168.31.140','2024-05-14',197),(17,'192.168.31.112','2024-05-15',493),(18,'192.168.31.140','2024-05-15',193),(19,'192.168.31.112','2024-05-16',1),(20,'192.168.31.140','2024-05-16',79);
/*!40000 ALTER TABLE `access_record_face_send_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `access_record_ins`
--

DROP TABLE IF EXISTS `access_record_ins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `access_record_ins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `access_date` date NOT NULL,
  `count` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `access_record_ins`
--

LOCK TABLES `access_record_ins` WRITE;
/*!40000 ALTER TABLE `access_record_ins` DISABLE KEYS */;
INSERT INTO `access_record_ins` VALUES (1,'127.0.0.1','2024-04-28',0),(2,'192.168.31.15','2024-04-28',6),(3,'192.168.31.140','2024-04-28',12),(4,'192.168.31.112','2024-04-28',4),(5,'192.168.31.140','2024-04-29',169),(6,'192.168.31.112','2024-04-29',30),(7,'192.168.31.140','2024-04-30',85),(8,'192.168.31.112','2024-04-30',30),(9,'192.168.31.140','2024-05-03',67),(10,'192.168.31.112','2024-05-03',30),(11,'192.168.31.140','2024-05-04',74),(12,'192.168.31.112','2024-05-05',30),(13,'192.168.31.140','2024-05-05',73),(14,'192.168.31.140','2024-05-06',221),(15,'192.168.31.112','2024-05-06',44),(16,'192.168.31.112','2024-05-07',91),(17,'192.168.31.140','2024-05-07',74),(18,'192.168.31.140','2024-05-08',148),(19,'192.168.31.112','2024-05-08',119),(20,'192.168.31.112','2024-05-09',150),(21,'192.168.31.140','2024-05-09',134),(22,'192.168.31.140','2024-05-10',139),(23,'192.168.31.112','2024-05-10',146),(24,'192.168.31.140','2024-05-11',102),(25,'192.168.31.112','2024-05-11',30),(26,'192.168.31.140','2024-05-12',74),(27,'192.168.31.140','2024-05-13',74),(28,'192.168.31.112','2024-05-13',90),(29,'192.168.31.140','2024-05-14',148),(30,'192.168.31.112','2024-05-14',120),(31,'192.168.31.140','2024-05-15',146),(32,'192.168.31.112','2024-05-15',55);
/*!40000 ALTER TABLE `access_record_ins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `browser`
--

DROP TABLE IF EXISTS `browser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `browser` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '浏览器id_数据库',
  `index` int NOT NULL COMMENT '浏览器编号',
  `browser_name` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '唯一标识',
  `group` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '分组',
  `remarks` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '备注',
  `tags` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '标签',
  `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '状态',
  `last_update` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '上一次使用时间',
  `ip_address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'IP地址',
  `current_operation` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '当前操作',
  `is_delete` int DEFAULT '0',
  `platform_type` varchar(50) COLLATE utf8mb4_general_ci DEFAULT 'overseas',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `browser`
--

LOCK TABLES `browser` WRITE;
/*!40000 ALTER TABLE `browser` DISABLE KEYS */;
INSERT INTO `browser` VALUES (1,348,'jfxoejo','TikTok分组2',NULL,'tiktok4.13,tiktok,ins_test','success','2024-04-11 14:19:07','108.165.214.12--ca','Tiktok养号',0,'overseas'),(2,347,'jfxoejn','TikTok分组2',NULL,'tiktok2_2,facebook4.10,tiktok,facebook','wait','2024-05-16 10:24:48','108.165.214.226--ca','Fb获取小组新人',0,'overseas'),(3,346,'jfxoejm','TikTok分组2',NULL,'Fb4.13,fb身份证验证,facebook','success','2024-04-11 14:19:07','193.222.111.213--ca','Fb获取小组新人',0,'overseas'),(4,345,'jfxoejl','TikTok分组2',NULL,'facebook4.10,tiktok4.16,tiktok,facebook,Tk正常账号','wait','2024-05-16 10:24:48','193.222.111.156--ca','Fb获取小组新人',0,'overseas'),(5,344,'jfxoejk','TikTok分组2',NULL,'ins_test,facebook4.10,tiktok4.16,tiktok,facebook','success','2024-05-16 11:09:16','193.222.111.37--ca','Fb获取小组新人',0,'overseas'),(6,343,'jfxoejj','TikTok分组2',NULL,'tiktok2_2,ins_test,Fb4.13,tiktok,facebook,fb身份证验证,whatsapp,Ins登录异常','success','2024-04-11 14:19:07','193.222.111.29--ca','Ws获取群组号码',0,'overseas'),(7,342,'jfxoejh','TikTok分组2',NULL,'tiktok2_2,ins_test,facebook4.10,fb身份证验证,tiktok,facebook,whatsapp,Tk正常账号,Ins登录异常','error','2024-05-16 08:04:35','193.222.111.188--ca','Tiktok养号',0,'overseas'),(8,341,'jfxoejg','TikTok分组2',NULL,'ins_test,facebook4.10,tiktok4.16,tiktok,facebook,Tk正常账号,Ins登录异常','wait','2024-05-16 10:24:48','193.222.111.146--ca','Fb获取小组新人',0,'overseas'),(9,340,'jfxoejf','TikTok分组2',NULL,'tiktok2_2,ins_test,facebook4.10,tiktok,facebook,Tk正常账号,Ins登录异常','running','2024-05-16 11:10:09','193.222.111.138--ca','Fb获取小组新人',0,'overseas'),(10,339,'jfxoejd','TikTok分组2',NULL,'tiktok2_2,ins_test,facebook4.10,fb身份证验证,tiktok,facebook,Ins登录异常','wait','2024-04-11 14:19:07','193.222.111.205--ca','Ins获取用户粉丝',0,'overseas'),(11,338,'jfvrkim','TikTok分组2',NULL,'tiktok老号,facebook4.10,fb身份证验证,tiktok,facebook,Tk正常账号','error','2024-05-16 09:06:44','104.234.145.11--ca','Tiktok养号',0,'overseas'),(12,337,'jfvrkil','TikTok分组2',NULL,'tiktok,4.8手机号,facebook4.10,facebook,Tk正常账号','running','2024-05-16 11:10:09','104.234.145.203--ca','Fb获取小组新人',0,'overseas'),(13,336,'jfvrkik','TikTok分组2',NULL,'tiktok老号,facebook4.10,fb身份证验证,tiktok,facebook','success','2024-04-11 14:19:07','104.234.145.91--ca','Tiktok养号',0,'overseas'),(14,335,'jfvrkij','TikTok分组2',NULL,'tiktok,4.9新号,Fb4.13,fb身份证验证,facebook,whatsapp,Tk正常账号,ws账号退出','error','2024-05-16 10:19:32','104.234.145.59--ca','Tiktok养号',0,'overseas'),(15,334,'jfvqed5','TikTok分组2',NULL,'facebook4.10,tiktok4.14,fb身份证验证,tiktok,facebook,Tk正常账号','error','2024-05-16 10:09:06','45.149.100.229--ca','Tiktok养号',0,'overseas'),(16,333,'jfvqed3','TikTok分组2',NULL,'tiktok,0.95新号,facebook4.10,fb身份证验证,facebook,whatsapp','success','2024-04-11 14:19:07','108.165.214.12--ca','Ws获取群组号码',0,'overseas'),(17,332,'jfvqed2','TikTok分组2',NULL,'facebook4.10,tiktok4.14,tiktok,facebook,Tk正常账号','success','2024-05-16 10:47:18','108.165.214.226--ca','Fb获取小组新人',0,'overseas'),(18,331,'jfvqed1','TikTok分组2',NULL,'tiktok,0.95新号,Fb4.13,facebook','wait','2024-05-16 10:24:48','193.222.111.213--ca','Fb获取小组新人',0,'overseas'),(19,330,'jfvqed0','TikTok分组2',NULL,'facebook4.10,tiktok4.16,tiktok,facebook','wait','2024-05-16 10:24:48','193.222.111.156--ca','Fb获取小组新人',0,'overseas'),(20,329,'jfvqecy','TikTok分组2',NULL,'tiktok,0.95新号,facebook4.10,facebook,fb身份证验证','success','2024-04-11 14:19:07','193.222.111.37--ca','Fb获取小组新人',0,'overseas'),(21,328,'jfvqecx','TikTok分组2',NULL,'Fb4.13,tiktok4.16,tiktok,facebook','wait','2024-05-16 10:24:48','193.222.111.29--ca','Fb获取小组新人',0,'overseas'),(22,327,'jfvqecw','TikTok分组2',NULL,'facebook4.10,tiktok4.14,tiktok,facebook,Tk正常账号','success','2024-05-16 11:09:09','193.222.111.188--ca','Fb获取小组新人',0,'overseas'),(23,326,'jfvqecv','TikTok分组2',NULL,'facebook4.10,tiktok4.16,tiktok,facebook,fb身份证验证,whatsapp,Tk正常账号','error','2024-05-16 08:33:58','193.222.111.146--ca','Tiktok养号',0,'overseas'),(24,325,'jfvqecu','TikTok分组2',NULL,'tiktok,0.95新号,facebook4.10,facebook,tiktok账号退出','wait','2024-05-16 10:24:48','193.222.111.138--ca','Fb获取小组新人',0,'overseas'),(25,324,'jfvqect','TikTok分组2',NULL,'facebook4.10,tiktok4.16,tiktok,facebook,tiktok账号退出','success','2024-05-16 11:09:44','193.222.111.205--ca','Fb获取小组新人',0,'overseas'),(26,323,'jfuv0ot','TikTok分组2',NULL,'tiktok,facebook,0.95新号','success','2024-05-16 10:47:11','178.253.33.106--ca','Fb获取小组新人',0,'overseas'),(27,322,'jfuv0os','TikTok分组2',NULL,'facebook,tiktok4.17,tiktok','wait','2024-05-16 10:24:48','104.234.145.11--ca','Fb获取小组新人',0,'overseas'),(28,321,'jfuv0or','TikTok分组2',NULL,'facebook,tiktok,fb身份证验证,Telegram','success','2024-05-14 15:12:30','104.234.145.203--ca','Fb获取小组新人',0,'overseas'),(29,320,'jfuv0oq','TikTok分组2',NULL,'Fb4.13,fb身份证验证,tiktok4.17,tiktok,facebook,ws测试主号','wait','2024-05-15 08:55:57','104.234.145.91--ca','Tiktok养号',0,'overseas'),(30,319,'jfuv0op','TikTok分组2',NULL,'facebook,tiktok4.17,tiktok,tiktok账号退出','wait','2024-05-16 10:24:48','104.234.145.59--ca','Fb获取小组新人',0,'overseas'),(31,318,'jfuv0oo','TikTok分组2',NULL,'facebook,tiktok4.17,tiktok','running','2024-05-16 11:10:09','104.234.145.21--ca','Fb获取小组新人',0,'overseas'),(32,317,'jfuv0om','TikTok分组2',NULL,'tiktok,facebook,4.9新号,fb身份证验证,whatsapp','wait','2024-04-11 14:19:07','104.234.145.49--ca','Ws获取群组号码',0,'overseas'),(33,316,'jfuv0ok','TikTok分组2',NULL,'facebook,tiktok4.14,tiktok,fb身份证验证','success','2024-04-11 14:19:07','45.149.100.241--ca','Fb获取小组新人',0,'overseas'),(34,315,'jfuv0oj','TikTok分组2',NULL,'tiktok,facebook,0.95新号','wait','2024-05-16 10:24:48','45.149.100.65--ca','Fb获取小组新人',0,'overseas'),(35,314,'jfuv0oh','TikTok分组2',NULL,'tiktok,0.95新号,Fb4.13,facebook','wait','2024-05-16 10:24:48','45.149.100.229--ca','Fb获取小组新人',0,'overseas'),(36,313,'jfuuf1w','TikTok分组2',NULL,'tiktok,4.9新号,Fb4.13,facebook,Tk正常账号','wait','2024-05-16 10:24:48','45.149.100.65--ca','Fb获取小组新人',0,'overseas'),(37,312,'jfuuf1v','TikTok分组2',NULL,'tiktok老号,fb账号退出,tiktok,facebook,Tk正常账号','error','2024-05-16 09:08:00','45.149.100.229--ca','Tiktok养号',0,'overseas'),(38,311,'jfuuf1u','TikTok分组2',NULL,'tiktok老号,facebook,tiktok,Tk正常账号','wait','2024-05-16 10:24:48','108.165.214.12--ca','Fb获取小组新人',0,'overseas'),(39,310,'jfuuf1t','TikTok分组2',NULL,'tiktok老号,fb账号退出,tiktok,facebook,Tk正常账号','error','2024-05-16 08:58:15','108.165.214.226--ca','Tiktok养号',0,'overseas'),(40,309,'jfuuf1s','TikTok分组2',NULL,'tiktok老号,facebook,tiktok','success','2024-05-16 11:09:33','193.222.111.213--ca','Fb获取小组新人',0,'overseas'),(41,308,'jfuuf1r','TikTok分组2',NULL,'tiktok老号,facebook,tiktok','wait','2024-05-16 10:24:48','193.222.111.156--ca','Fb获取小组新人',0,'overseas'),(42,307,'jfuuf1q','TikTok分组2',NULL,'tiktok老号,facebook,tiktok,Tk正常账号','success','2024-05-16 10:47:16','193.222.111.37--ca','Fb获取小组新人',0,'overseas'),(43,306,'jfuuf1p','TikTok分组2',NULL,'tiktok老号,facebook,tiktok,Tk正常账号','wait','2024-05-16 10:24:48','193.222.111.29--ca','Fb获取小组新人',0,'overseas'),(44,305,'jfuuf1o','TikTok分组2',NULL,'tiktok老号,facebook,tiktok,fb身份证验证,whatsapp,ws账号退出,Tk正常账号','error','2024-05-16 08:29:39','193.222.111.188--ca','Tiktok养号',0,'overseas'),(45,304,'jfuuf1n','TikTok分组2',NULL,'tiktok老号,facebook,tiktok,BM账户,fb身份证验证,whatsapp,Tk正常账号','success','2024-05-16 10:11:18','193.222.111.146--ca','Tiktok养号',0,'overseas'),(46,293,'jfutnsv','TikTok分组2',NULL,'tiktok老号,Fb4.13,tiktok,facebook,Tk正常账号','wait','2024-05-16 10:24:48','193.222.111.138--ca','Fb获取小组新人',0,'overseas'),(47,262,'jfumcfm','TikTok分组2',NULL,'tiktok老号,facebook4.10,fb身份证验证,tiktok,facebook,Tk正常账号','error','2024-05-16 08:29:06','223.76.232.28--cn','Tiktok养号',0,'overseas'),(48,261,'jfuleuv','TikTok分组2',NULL,'tiktok手机新号,facebook4.10,fb身份证验证,tiktok,facebook,Tk正常账号','running','2024-05-16 10:23:45','223.76.232.28--cn','Tiktok养号',0,'overseas'),(49,260,'jful6bg','TikTok分组2',NULL,'tiktok老号,Fb4.13,tiktok,facebook,fb身份证验证,Tk正常账号','error','2024-05-16 08:30:19','223.76.232.28--cn','Tiktok养号',0,'overseas'),(50,259,'jfukgpa','TikTok分组2',NULL,'tiktok手机新号,Fb4.13,fb身份证验证,tiktok,facebook,Tk正常账号','running','2024-05-16 10:23:45','191.96.211.56--us','Tiktok养号',0,'overseas'),(51,258,'jfdfett','tiktok分组1',NULL,'facebook,tiktok4.11,tiktok,Tk正常账号','wait','2024-05-16 10:24:48','184.174.66.136--us','Fb获取小组新人',0,'overseas'),(52,257,'jfdfets','tiktok分组1',NULL,'facebook,tiktok4.12,tiktok,Tk正常账号','success','2024-05-16 10:46:56','2.59.59.42--us','Fb获取小组新人',0,'overseas'),(53,256,'jfdfetq','tiktok分组1',NULL,'tiktok,facebook,4.8手机号,Tk正常账号','wait','2024-05-16 10:24:48','166.0.131.77--us','Fb获取小组新人',0,'overseas'),(54,255,'jfdfetp','tiktok分组1',NULL,'facebook,tiktok4.11,tiktok,','wait','2024-05-16 10:24:48','45.150.59.127--us','Fb获取小组新人',0,'overseas'),(55,254,'jfdfeto','tiktok分组1',NULL,'facebook,tiktok4.11,tiktok,Tk正常账号','wait','2024-05-16 10:24:48','152.89.248.199--us','Fb获取小组新人',0,'overseas'),(56,253,'jfdfetn','tiktok分组1',NULL,'facebook,tiktok4.11,tiktok,Tk正常账号','success','2024-05-16 11:10:07','184.174.90.79--us','Fb获取小组新人',0,'overseas'),(57,252,'jfdfetm','tiktok分组1',NULL,'facebook,tiktok4.12,tiktok,Tk正常账号','success','2024-05-16 10:46:05','194.5.149.146--us','Fb获取小组新人',0,'overseas'),(58,251,'jfdfetl','tiktok分组1',NULL,'tiktok4.13,Fb4.13,tiktok,facebook,Tk正常账号','wait','2024-05-16 10:24:48','209.145.43.97--us','Fb获取小组新人',0,'overseas'),(59,250,'jfdfetk','tiktok分组1',NULL,'tiktok,facebook,4.8手机号,Tk正常账号','success','2024-05-16 10:47:28','194.113.227.193--us','Fb获取小组新人',0,'overseas'),(60,249,'jfdfe4m','tiktok分组1',NULL,'facebook,tiktok4.16,tiktok,','running','2024-05-16 11:10:09','152.89.248.199--us','Fb获取小组新人',0,'overseas'),(61,248,'jfdfe4k','tiktok分组1',NULL,'facebook4.10,tiktok4.13,tiktok,facebook,Tk正常账号','success','2024-05-16 11:10:04','184.174.90.79--us','Fb获取小组新人',0,'overseas'),(62,247,'jfdfe4h','tiktok分组1',NULL,'fb身份证验证,tiktok4.16,tiktok,facebook,tiktok账号退出','success','2024-04-11 14:19:07','194.5.149.146--us','Tiktok评论',0,'overseas'),(63,246,'jfdfe4f','tiktok分组1',NULL,'tiktok,4.8手机号,fb身份证验证,facebook,Tk正常账号','error','2024-05-16 09:36:41','209.145.43.97--us','Tiktok养号',0,'overseas'),(64,245,'jfdfe4d','tiktok分组1',NULL,'facebook4.10,tiktok4.14,tiktok,facebook,Tk正常账号','running','2024-05-16 11:10:09','194.113.227.193--us','Fb获取小组新人',0,'overseas'),(65,244,'jfdfe4b','tiktok分组1',NULL,'tiktok,4.8手机号,facebook4.10,facebook,Tk正常账号','wait','2024-05-16 10:24:48','102.129.208.9--us','Fb获取小组新人',0,'overseas'),(66,243,'jfdfe49','tiktok分组1',NULL,'tiktok手机新号,facebook4.10,fb身份证验证,tiktok,facebook,Tk正常账号','error','2024-05-16 09:08:56','45.156.58.217--us','Tiktok养号',0,'overseas'),(67,242,'jfdfe46','tiktok分组1',NULL,'tiktok,4.8手机号,facebook4.10,fb身份证验证,facebook,whatsapp,Tk正常账号','running','2024-05-16 10:23:45','216.177.139.123--us','Tiktok养号',0,'overseas'),(68,241,'jfdfe43','tiktok分组1',NULL,'tiktok手机新号,fb身份证验证,tiktok,facebook,whatsapp','wait','2024-04-11 14:19:07','2.59.59.42--us','Ws获取群组号码',0,'overseas'),(69,240,'jfdfe40','tiktok分组1',NULL,'facebook4.10,tiktok4.12,tiktok,facebook,Tk正常账号','wait','2024-05-16 10:24:48','23.230.250.108--us','Fb获取小组新人',0,'overseas'),(70,239,'jfdfae7','tiktok分组1',NULL,'tiktok手机新号,facebook4.10,tiktok,facebook,fb身份证验证,whatsapp,Tk正常账号','success','2024-05-16 09:27:00','166.0.131.77--us','Tiktok养号',0,'overseas'),(71,238,'jfdfae6','tiktok分组1',NULL,'tiktok手机新号,facebook4.10,fb身份证验证,tiktok,facebook,Tk正常账号','running','2024-05-16 10:23:45','45.150.59.127--us','Tiktok养号',0,'overseas'),(72,237,'jfdfae4','tiktok分组1',NULL,'tiktok,4.8手机号,facebook4.10,facebook,Tk正常账号','wait','2024-05-16 10:24:48','176.57.63.46--us','Fb获取小组新人',0,'overseas'),(73,236,'jfdfae3','tiktok分组1',NULL,'facebook4.10,tiktok,facebook,tiktok账号退出','wait','2024-05-16 10:24:48','184.174.50.81--us','Fb获取小组新人',0,'overseas'),(74,235,'jfdfae2','tiktok分组1',NULL,'tiktok,4.8手机号,facebook4.10,facebook,Tk正常账号','success','2024-05-16 10:27:29','45.146.83.249--us','Fb获取小组新人',0,'overseas'),(75,234,'jfdfae1','tiktok分组1',NULL,'tiktok手机新号,Fb4.13,fb身份证验证,tiktok,facebook,ins_test','error','2024-04-11 14:19:07','104.224.74.220--us','Tiktok养号',0,'overseas'),(76,233,'jfdfae0','tiktok分组1',NULL,'facebook4.10,fb身份证验证,tiktok手机主号,tiktok,facebook','success','2024-05-14 10:57:30','213.109.155.29--us','Tk获取主账号评论',0,'overseas'),(77,232,'jfdfady','tiktok分组1',NULL,'facebook4.10,tiktok4.13,tiktok,facebook,Tk正常账号','wait','2024-05-16 10:24:48','185.242.111.101--us','Fb获取小组新人',0,'overseas'),(78,231,'jfdfadx','tiktok分组1',NULL,'tiktok手机新号,tiktok,facebook,Fb广告账户,fb身份证验证','success','2024-04-11 14:19:07','45.133.58.180--us','Facebook养号',0,'overseas'),(79,230,'jfdfadw','tiktok分组1',NULL,'tiktok4.12,Fb4.13,fb身份证验证,tiktok,facebook,whatsapp,Tk正常账号','success','2024-05-16 10:23:40','203.17.123.206--us','Tiktok养号',0,'overseas'),(80,229,'jfddo00','tiktok分组1',NULL,'tiktok手机新号,Fb4.13,tiktok,facebook,Tk正常账号','success','2024-05-16 11:12:24','45.147.133.176--us','Fb获取小组新人',0,'overseas'),(81,228,'jfddnyy','tiktok分组1',NULL,'tiktok手机新号,facebook4.10,fb身份证验证,tiktok,facebook,whatsapp','success','2024-04-11 14:19:07','184.174.66.136--us','Ws获取群组号码',0,'overseas'),(82,227,'jfddnyx','tiktok分组1',NULL,'tiktok手机新号,facebook4.10,fb身份证验证,tiktok,facebook,whatsapp,Tk正常账号','error','2024-05-16 10:10:03','140.99.220.106--us','Tiktok养号',0,'overseas'),(83,226,'jfddnyv','tiktok分组1',NULL,'facebook4.10,tiktok4.13,tiktok,facebook,Tk正常账号','success','2024-05-16 11:10:07','203.17.123.206--us','Fb获取小组新人',0,'overseas'),(84,225,'jfddnyu','tiktok分组1',NULL,'facebook4.10,tiktok4.13,tiktok,facebook,Tk正常账号','success','2024-05-16 11:12:16','140.99.116.96--us','Fb获取小组新人',0,'overseas'),(85,224,'jfddnyt','tiktok分组1',NULL,'facebook4.10,tiktok4.16,tiktok,facebook,Tk正常账号','wait','2024-05-16 10:24:48','45.133.58.180--us','Fb获取小组新人',0,'overseas'),(86,223,'jfddnys','tiktok分组1',NULL,'tiktok手机新号,facebook4.10,fb身份证验证,tiktok,facebook,Tk正常账号,ins_test','error','2024-05-16 08:04:09','193.37.220.150--us','Tiktok养号',0,'overseas'),(87,222,'jfddnyp','tiktok分组1',NULL,'facebook4.10,tiktok4.16,tiktok,facebook,Tk正常账号,fb身份证验证','success','2024-05-16 10:14:47','185.242.111.101--us','Tiktok养号',0,'overseas'),(88,221,'jfddnyo','tiktok分组1',NULL,'Fb4.13,tiktok4.17,tiktok,facebook,Tk正常账号','wait','2024-05-16 10:24:48','213.109.155.29--us','Fb获取小组新人',0,'overseas'),(89,220,'jfddnyn','tiktok分组1',NULL,'tiktok手机新号,facebook4.10,fb身份证验证,facebook,Tk正常账号,tiktok,ins_test','success','2024-05-16 08:45:48','104.234.255.166--us','Tiktok养号',0,'overseas'),(90,218,'jf9yo4r','tiktok分组1',NULL,'tiktok手机新号,tiktok,Tk正常账号,ins_test','success','2024-05-16 08:47:54','104.234.145.15--ca','Tiktok养号',0,'overseas'),(91,217,'jf9yo4q','tiktok分组1',NULL,'tiktok手机新号,tiktok,Tk正常账号','success','2024-05-16 09:13:02','206.53.49.167--ca','Tiktok养号',0,'overseas'),(92,216,'jf9yo4p','tiktok分组1',NULL,'tiktok,TkAds注册4.17,Tk正常账号,ins_test','error','2024-05-16 09:28:29','89.44.102.251--ca','Tiktok养号',0,'overseas'),(93,215,'jf9yo4o','tiktok分组1',NULL,'tiktok手机新号,tiktok,Tk正常账号,ins_test','error','2024-05-16 09:55:48','104.234.68.124--ca','Tiktok养号',0,'overseas'),(94,214,'jf9yo4n','tiktok分组1',NULL,'tiktok手机新号,tiktok,Tk正常账号','error','2024-05-16 09:36:30','108.165.214.52--ca','Tiktok养号',0,'overseas'),(95,213,'jf9yo4m','tiktok分组1',NULL,'tiktok,能发评论','error','2024-04-11 14:19:07','45.149.100.207--ca','Tiktok养号',0,'overseas'),(96,212,'jf9yo4l','tiktok分组1',NULL,'tiktok,能发评论','success','2024-04-11 14:19:07','193.222.111.82--ca','Tiktok养号',0,'overseas'),(97,211,'jf9yo4k','tiktok分组1',NULL,'tiktok,能发评论,ins_test','success','2024-04-11 14:19:07','154.16.109.210--ca','Tiktok养号',0,'overseas'),(98,210,'jf9yo4h','tiktok分组1',NULL,'tiktok,能发评论,ins_test','success','2024-04-11 14:19:07','104.234.130.59--ca','Tiktok养号',0,'overseas'),(99,209,'jf9yo4g','tiktok分组1',NULL,'tiktok,能发评论,Tk正常账号','success','2024-05-16 09:47:14','104.234.130.229--ca','Tiktok养号',0,'overseas'),(100,207,'jf8r69r','测试项目',NULL,'tiktok老号,tiktok','success','2024-04-11 14:19:07','176.57.63.46--us','Tiktok养号',0,'overseas');
/*!40000 ALTER TABLE `browser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `browser_copy1`
--

DROP TABLE IF EXISTS `browser_copy1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `browser_copy1` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '浏览器id_数据库',
  `index` int NOT NULL COMMENT '浏览器编号',
  `browser_name` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '唯一标识',
  `group` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '分组',
  `remarks` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '备注',
  `tags` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '标签',
  `status` int DEFAULT NULL COMMENT '状态 0关闭，1打开',
  `last_update` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '上一次使用时间',
  `ip_address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'IP地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `browser_copy1`
--

LOCK TABLES `browser_copy1` WRITE;
/*!40000 ALTER TABLE `browser_copy1` DISABLE KEYS */;
INSERT INTO `browser_copy1` VALUES (1,348,'jfxoejo','TikTok分组2',NULL,'tiktok2_2',0,'2024-04-06 15:45:12','108.165.214.12--ca'),(2,347,'jfxoejn','TikTok分组2',NULL,'tiktok2_2',0,'2024-04-06 15:45:12','108.165.214.226--ca'),(3,346,'jfxoejm','TikTok分组2',NULL,'tiktok2_2',0,'2024-04-06 15:45:12','193.222.111.213--ca'),(4,345,'jfxoejl','TikTok分组2',NULL,'tiktok2_2',0,'2024-04-06 15:45:12','193.222.111.156--ca'),(5,344,'jfxoejk','TikTok分组2',NULL,'tiktok2_2,ins_test',0,'2024-04-06 15:45:12','193.222.111.37--ca'),(6,343,'jfxoejj','TikTok分组2',NULL,'tiktok2_2,ins_test',0,'2024-04-06 15:45:12','193.222.111.29--ca'),(7,342,'jfxoejh','TikTok分组2',NULL,'tiktok2_2,ins_test',0,'2024-04-06 15:45:12','193.222.111.188--ca'),(8,341,'jfxoejg','TikTok分组2',NULL,'tiktok2_2,ins_test',0,'2024-04-06 15:45:12','193.222.111.146--ca'),(9,340,'jfxoejf','TikTok分组2',NULL,'tiktok2_2,ins_test',0,'2024-04-06 15:45:12','193.222.111.138--ca'),(10,339,'jfxoejd','TikTok分组2',NULL,'tiktok2_2,ins_test',0,'2024-04-06 15:45:12','193.222.111.205--ca'),(11,338,'jfvrkim','TikTok分组2',NULL,'tiktok老号',0,'2024-04-06 15:45:12','104.234.145.11--ca'),(12,337,'jfvrkil','TikTok分组2',NULL,NULL,0,'2024-04-06 15:45:12','104.234.145.203--ca'),(13,336,'jfvrkik','TikTok分组2',NULL,'tiktok老号',0,'2024-04-06 15:45:12','104.234.145.91--ca'),(14,335,'jfvrkij','TikTok分组2',NULL,'tiktok老号',0,'2024-04-06 15:45:12','104.234.145.59--ca'),(15,334,'jfvqed5','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','45.149.100.229--ca'),(16,333,'jfvqed3','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','108.165.214.12--ca'),(17,332,'jfvqed2','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','108.165.214.226--ca'),(18,331,'jfvqed1','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','193.222.111.213--ca'),(19,330,'jfvqed0','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','193.222.111.156--ca'),(20,329,'jfvqecy','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','193.222.111.37--ca'),(21,328,'jfvqecx','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','193.222.111.29--ca'),(22,327,'jfvqecw','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','193.222.111.188--ca'),(23,326,'jfvqecv','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','193.222.111.146--ca'),(24,325,'jfvqecu','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','193.222.111.138--ca'),(25,324,'jfvqect','TikTok分组2',NULL,'0.95新号2',0,'2024-04-06 15:45:12','193.222.111.205--ca'),(26,323,'jfuv0ot','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','178.253.33.106--ca'),(27,322,'jfuv0os','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','104.234.145.11--ca'),(28,321,'jfuv0or','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','104.234.145.203--ca'),(29,320,'jfuv0oq','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','104.234.145.91--ca'),(30,319,'jfuv0op','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','104.234.145.59--ca'),(31,318,'jfuv0oo','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','104.234.145.21--ca'),(32,317,'jfuv0om','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','104.234.145.49--ca'),(33,316,'jfuv0ok','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','45.149.100.241--ca'),(34,315,'jfuv0oj','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','45.149.100.65--ca'),(35,314,'jfuv0oh','TikTok分组2',NULL,'0.95新号,facebook',0,'2024-04-06 15:45:12','45.149.100.229--ca'),(36,313,'jfuuf1w','TikTok分组2',NULL,'3.2 新号,facebook',0,'2024-04-06 15:45:12','45.149.100.65--ca'),(37,312,'jfuuf1v','TikTok分组2',NULL,'3.2 新号,tiktok老号,facebook',0,'2024-04-06 15:45:12','45.149.100.229--ca'),(38,311,'jfuuf1u','TikTok分组2',NULL,'3.2 新号,tiktok老号,facebook',0,'2024-04-06 15:45:12','108.165.214.12--ca'),(39,310,'jfuuf1t','TikTok分组2',NULL,'3.2 新号,tiktok老号',0,'2024-04-06 15:45:12','108.165.214.226--ca'),(40,309,'jfuuf1s','TikTok分组2',NULL,'3.2 新号,tiktok老号,facebook',0,'2024-04-06 15:45:12','193.222.111.213--ca'),(41,308,'jfuuf1r','TikTok分组2',NULL,'3.2 新号,tiktok老号,facebook',0,'2024-04-06 15:45:12','193.222.111.156--ca'),(42,307,'jfuuf1q','TikTok分组2',NULL,'3.2 新号,tiktok老号,facebook',0,'2024-04-06 15:45:12','193.222.111.37--ca'),(43,306,'jfuuf1p','TikTok分组2',NULL,'3.2 新号,tiktok老号,facebook',0,'2024-04-06 15:45:12','193.222.111.29--ca'),(44,305,'jfuuf1o','TikTok分组2',NULL,'3.2 新号,tiktok老号,facebook',0,'2024-04-06 15:45:12','193.222.111.188--ca'),(45,304,'jfuuf1n','TikTok分组2',NULL,'3.2 新号,登录,tiktok老号,facebook',0,'2024-04-06 15:45:12','193.222.111.146--ca'),(46,293,'jfutnsv','TikTok分组2',NULL,'tiktok老号',0,'2024-04-06 15:45:12','193.222.111.138--ca'),(47,262,'jfumcfm','TikTok分组2',NULL,'tiktok老号',0,'2024-04-06 15:45:12','223.76.232.28--cn'),(48,261,'jfuleuv','TikTok分组2',NULL,'tiktok手机新号',0,'2024-04-06 15:45:12','223.76.232.28--cn'),(49,260,'jful6bg','TikTok分组2',NULL,NULL,0,'2024-04-06 15:45:12','223.76.232.28--cn'),(50,259,'jfukgpa','TikTok分组2',NULL,'tiktok手机新号',0,'2024-04-06 15:45:12','191.96.211.56--us'),(51,258,'jfdfett','tiktok分组1',NULL,'tiktok5,美国IP,facebook,facebook测试,之前能发评论',0,'2024-04-06 15:45:12','184.174.66.136--us'),(52,257,'jfdfets','tiktok分组1',NULL,'tiktok5,美国IP,facebook,之前能发评论',0,'2024-04-06 15:45:12','2.59.59.42--us'),(53,256,'jfdfetq','tiktok分组1',NULL,'tiktok5,美国IP,facebook',0,'2024-04-06 15:45:12','166.0.131.77--us'),(54,255,'jfdfetp','tiktok分组1',NULL,'tiktok5,美国IP,facebook',0,'2024-04-06 15:45:12','45.150.59.127--us'),(55,254,'jfdfeto','tiktok分组1',NULL,'tiktok5,美国IP,facebook',0,'2024-04-06 15:45:12','152.89.248.199--us'),(56,253,'jfdfetn','tiktok分组1',NULL,'tiktok5,美国IP,facebook',0,'2024-04-06 15:45:12','184.174.90.79--us'),(57,252,'jfdfetm','tiktok分组1',NULL,'tiktok5,美国IP,facebook',0,'2024-04-06 15:45:12','194.5.149.146--us'),(58,251,'jfdfetl','tiktok分组1',NULL,'tiktok5,美国IP,facebook,之前能发评论',0,'2024-04-06 15:45:12','209.145.43.97--us'),(59,250,'jfdfetk','tiktok分组1',NULL,'tiktok5,美国IP,facebook',0,'2024-04-06 15:45:12','194.113.227.193--us'),(60,249,'jfdfe4m','tiktok分组1',NULL,'tiktok4,美国IP,facebook',0,'2024-04-06 15:45:12','152.89.248.199--us'),(61,248,'jfdfe4k','tiktok分组1',NULL,'tiktok4,美国IP,之前能发评论',0,'2024-04-06 15:45:12','184.174.90.79--us'),(62,247,'jfdfe4h','tiktok分组1',NULL,'tiktok4,美国IP',0,'2024-04-06 15:45:12','194.5.149.146--us'),(63,246,'jfdfe4f','tiktok分组1',NULL,'tiktok4,美国IP',0,'2024-04-06 15:45:12','209.145.43.97--us'),(64,245,'jfdfe4d','tiktok分组1',NULL,'tiktok4,美国IP,之前能发评论',0,'2024-04-06 15:45:12','194.113.227.193--us'),(65,244,'jfdfe4b','tiktok分组1',NULL,'tiktok4,美国IP',0,'2024-04-06 15:45:12','102.129.208.9--us'),(66,243,'jfdfe49','tiktok分组1',NULL,'tiktok4,美国IP,tiktok手机新号',0,'2024-04-06 15:45:12','45.156.58.217--us'),(67,242,'jfdfe46','tiktok分组1',NULL,'tiktok4,美国IP',0,'2024-04-06 15:45:12','216.177.139.123--us'),(68,241,'jfdfe43','tiktok分组1',NULL,'tiktok4,美国IP,tiktok手机新号',0,'2024-04-06 15:45:12','2.59.59.42--us'),(69,240,'jfdfe40','tiktok分组1',NULL,'tiktok4,美国IP,之前能发评论',0,'2024-04-06 15:45:12','23.230.250.108--us'),(70,239,'jfdfae7','tiktok分组1',NULL,'tiktok3,美国IP,tiktok手机新号',0,'2024-04-06 15:45:12','166.0.131.77--us'),(71,238,'jfdfae6','tiktok分组1',NULL,'tiktok3,美国IP,tiktok手机新号',0,'2024-04-06 15:45:12','45.150.59.127--us'),(72,237,'jfdfae4','tiktok分组1',NULL,'tiktok3,美国IP',0,'2024-04-06 15:45:12','176.57.63.46--us'),(73,236,'jfdfae3','tiktok分组1',NULL,'tiktok3,美国IP,tiktok手机新号',0,'2024-04-06 15:45:12','184.174.50.81--us'),(74,235,'jfdfae2','tiktok分组1',NULL,'tiktok3,美国IP',0,'2024-04-06 15:45:13','45.146.83.249--us'),(75,234,'jfdfae1','tiktok分组1',NULL,'tiktok3,美国IP,tiktok手机新号',0,'2024-04-06 15:45:13','104.224.74.220--us'),(76,233,'jfdfae0','tiktok分组1',NULL,'tiktok3,美国IP,之前能发评论',0,'2024-04-06 15:45:13','213.109.155.29--us'),(77,232,'jfdfady','tiktok分组1',NULL,'tiktok3,美国IP,之前能发评论',0,'2024-04-06 15:45:13','185.242.111.101--us'),(78,231,'jfdfadx','tiktok分组1',NULL,'tiktok3,美国IP,tiktok手机新号',0,'2024-04-06 15:45:13','45.133.58.180--us'),(79,230,'jfdfadw','tiktok分组1',NULL,'tiktok3,美国IP,之前能发评论',0,'2024-04-06 15:45:13','203.17.123.206--us'),(80,229,'jfddo00','tiktok分组1',NULL,'tiktok2,美国IP,tiktok手机新号',0,'2024-04-06 15:45:13','45.147.133.176--us'),(81,228,'jfddnyy','tiktok分组1',NULL,'tiktok2,美国IP,tiktok手机新号',0,'2024-04-06 15:45:13','184.174.66.136--us'),(82,227,'jfddnyx','tiktok分组1',NULL,'tiktok2,美国IP,tiktok手机新号',0,'2024-04-06 15:45:13','140.99.220.106--us'),(83,226,'jfddnyv','tiktok分组1',NULL,'tiktok2,美国IP,之前能发评论',0,'2024-04-06 15:45:13','203.17.123.206--us'),(84,225,'jfddnyu','tiktok分组1',NULL,'tiktok2,美国IP,之前能发评论',0,'2024-04-06 15:45:13','140.99.116.96--us'),(85,224,'jfddnyt','tiktok分组1',NULL,'tiktok2,美国IP',0,'2024-04-06 15:45:13','45.133.58.180--us'),(86,223,'jfddnys','tiktok分组1',NULL,'tiktok2,美国IP,tiktok手机新号',0,'2024-04-06 15:45:13','193.37.220.150--us'),(87,222,'jfddnyp','tiktok分组1',NULL,'tiktok2,美国IP,之前能发评论',0,'2024-04-06 15:45:13','185.242.111.101--us'),(88,221,'jfddnyo','tiktok分组1',NULL,'tiktok2,美国IP,之前能发评论',0,'2024-04-06 15:45:13','213.109.155.29--us'),(89,220,'jfddnyn','tiktok分组1',NULL,'tiktok2,美国IP,tiktok手机新号',0,'2024-04-06 15:45:13','104.234.255.166--us'),(90,218,'jf9yo4r','tiktok分组1',NULL,'tiktok1,tiktok手机新号',0,'2024-04-06 15:45:13','104.234.145.15--ca'),(91,217,'jf9yo4q','tiktok分组1',NULL,'tiktok1,tiktok手机新号',0,'2024-04-06 15:45:13','206.53.49.167--ca'),(92,216,'jf9yo4p','tiktok分组1',NULL,'tiktok1,tiktok手机新号,账号退出',0,'2024-04-06 15:45:13','89.44.102.251--ca'),(93,215,'jf9yo4o','tiktok分组1',NULL,'tiktok1,tiktok手机新号',0,'2024-04-06 15:45:13','104.234.68.124--ca'),(94,214,'jf9yo4n','tiktok分组1',NULL,'tiktok1,tiktok手机新号',0,'2024-04-06 15:45:13','108.165.214.52--ca'),(95,213,'jf9yo4m','tiktok分组1',NULL,'tiktok1,能发评论',0,'2024-04-06 15:45:13','45.149.100.207--ca'),(96,212,'jf9yo4l','tiktok分组1',NULL,'tiktok1,能发评论',0,'2024-04-06 15:45:13','193.222.111.82--ca'),(97,211,'jf9yo4k','tiktok分组1',NULL,'tiktok1,能发评论',0,'2024-04-06 15:45:13','154.16.109.210--ca'),(98,210,'jf9yo4h','tiktok分组1',NULL,'tiktok1,能发评论',0,'2024-04-06 15:45:13','104.234.130.59--ca'),(99,209,'jf9yo4g','tiktok分组1',NULL,'tiktok1,能发评论',0,'2024-04-06 15:45:13','104.234.130.229--ca'),(100,207,'jf8r69r','测试项目',NULL,'百度,美国IP',0,'2024-04-06 15:45:13','176.57.63.46--us');
/*!40000 ALTER TABLE `browser_copy1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `browser_domestic`
--

DROP TABLE IF EXISTS `browser_domestic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `browser_domestic` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '浏览器id_数据库',
  `index` int NOT NULL COMMENT '浏览器编号',
  `browser_name` varchar(10) COLLATE utf8mb4_general_ci NOT NULL COMMENT '唯一标识',
  `group` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '分组',
  `remarks` text COLLATE utf8mb4_general_ci COMMENT '备注',
  `tags` text COLLATE utf8mb4_general_ci COMMENT '标签',
  `status` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '状态',
  `last_update` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '上一次使用时间',
  `ip_address` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'IP地址',
  `is_delete` int NOT NULL COMMENT '状态 1删除，0正常',
  `current_operation` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '当前操作',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `browser_domestic`
--

LOCK TABLES `browser_domestic` WRITE;
/*!40000 ALTER TABLE `browser_domestic` DISABLE KEYS */;
/*!40000 ALTER TABLE `browser_domestic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fb_account`
--

DROP TABLE IF EXISTS `fb_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fb_account` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `fb_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT 'Fb账号id',
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '邮箱',
  `password` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '密码',
  `fa_2` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '2FA验证码',
  `create_time` datetime NOT NULL COMMENT '添加时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `fb_id` (`fb_id`)
) ENGINE=InnoDB AUTO_INCREMENT=300 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fb_account`
--

LOCK TABLES `fb_account` WRITE;
/*!40000 ALTER TABLE `fb_account` DISABLE KEYS */;
INSERT INTO `fb_account` VALUES (1,'61558457243314','ofg34025@fosiq.com','Avijit1122','6BNLGGGJ4I7KK5H4Y7MQNPTRMAXQX4NR','2024-04-16 15:07:03'),(2,'61558342738168','etl31663@fosiq.com','Avijit1122','NCH372CTJBQBBLTFB2DE3UZ3DZKEMRVB','2024-04-16 15:07:03'),(3,'61558423856226','xnu58349@fosiq.com','Avijit1122','GLRUARLEPJGCEYRVZ5YPHTYQF2Y2H3UU','2024-04-16 15:07:03'),(4,'61557885434515','qer40540@romog.com','Avijit1122','NVVF2SNYEMOSPDVB7ZYJ6XHVIZPV4I3L','2024-04-16 15:07:03'),(5,'61557640277450','golava5923@dacgu.com','@Hridoy22','RYDKLO55RRXQ3E2CDKBNKYJJU3V6UN6V','2024-04-16 15:07:03'),(6,'61557835029859','lirejit461@felibg.com','@Hridoy22','JNI26BC53NJOSTVYPWF2BREKYFIC7ZEF','2024-04-16 15:07:03'),(7,'61558372256121','amz29920@romog.com','Avijit1122','JXOMNGTKJ45M6RFNTA2EXKA2X7G5OQHJ','2024-04-16 15:07:03'),(8,'61558452082316','how66153@romog.com','Avijit1122','DCGGEBZ5YJVUJAUJEBDCCVK7N3CYJ2R6','2024-04-16 15:07:03'),(9,'61557852944479','eze97597@romog.com','Avijit1122','CUKAI2NE5FFYC323XSS73PSHVQQDZJQV','2024-04-16 15:07:03'),(10,'61558228765750','oha95754@vogco.com','sajib1122','VOARDPO4WYEDTLDY2IZ2HNHUENEKZ33Y','2024-04-16 15:07:03'),(11,'61558424120876','znh19271@fosiq.com','sajib1122','DYBQMPB34HZIGZ4WHUCLQ6PF7QTA5ZX2','2024-04-16 15:07:03'),(12,'61558187370622','anq21334@fosiq.com','Avijit1122','B2LCAOSQWBLUQMC5JZIP4PLGTUCYFQPD','2024-04-16 15:07:03'),(13,'61558382935640','rjf92590@vogco.com','Avijit1122','W5VZROWP4MIPPNFUSTJYR7HOLOMPAYLP','2024-04-16 15:07:03'),(14,'61558365592999','vtm81469@romog.com','Avijit1122','2DX63BQT2BCLYLENTUKKIG3RN47JTHKO','2024-04-16 15:07:03'),(15,'61558104966041','sbu76135@fosiq.com','Avijit1122','IU6SADBNAOGXIIUFHSYVIGSRKEGERFXA','2024-04-16 15:07:03'),(16,'61557941922347','qfp68659@fosiq.com','Avijit1122','Q5WJ53PTW7XICRRQLSIG3CFLCD3DFBP5','2024-04-16 15:07:03'),(17,'61558305476854','bkf13139@romog.com','avijit1122','57GSEFRCHYAW5MKF2H2PQMMQ3MYEEVD2','2024-04-16 15:07:04'),(18,'61558223969448','ujt01504@romog.com','avijit1122','H2PRSDEEBBCSY63I3J4LRLNPINIT3LFX','2024-04-16 15:07:04'),(19,'61557917651099','vcn44262@vogco.com','avijit1122','PCE7A4X7FTJ4CRDVA5B2KZB6QZWUJHRD','2024-04-16 15:07:04'),(20,'61557836745741','qeh43918@vogco.com','Avijit1122','H76NPIQCK5R72YAZJDT3CAOOMKCGBNVH','2024-04-16 15:07:04'),(21,'61558329833097','sififok749@otixero.com','Joty1234','KFRBCJQB2JVVH7AJGALUSUEMYC7BIEXV','2024-04-16 15:07:04'),(22,'61558241455576','fxn11947@fosiq.com','sajib1122','6WP4MKK3JNXOZXHKHBKOE7IYX7XKTUTI','2024-04-16 15:07:04'),(23,'61558205129757','zpk05562@vogco.com','avijit1122','RGOP47THAJPRBZYATQK6RUUFETTBSJ4A','2024-04-16 15:07:04'),(24,'61558041035650','fzg66489@romog.com','avijit1122','GUB7TEKRUDNY2MAK2LTP3YS5HZ47BXCM','2024-04-16 15:07:04'),(25,'61557779815773','ghc97530@fosiq.com','sajib1122','KVMIB6TSNV3NNCMW4LZPMJYWWQJ5HNA2','2024-04-16 15:07:04'),(26,'61557885862492','ctn48874@vogco.com','sajib1122','FVMIB6TSNV3NNCMW4LZPMJYWWQJ5HNA2','2024-04-16 15:07:04'),(27,'61557721258299','uol38361@romog.com','sajib1122','RDBWYET7G6CS6MSUTL2MDRVZ4C7W2W5G','2024-04-16 15:07:04'),(28,'61557904632558','tia63425@romog.com','avijit1122','6EK73XQMWNEKIW6SY5FJ2X3O6SYY45IX','2024-04-16 15:07:04'),(29,'61558114293541','xjk80159@fosiq.com','avijit1122','NWA7477VYRCZP27TZYX6UBPJB2KJ5P7Z','2024-04-16 15:07:04'),(30,'61558118373931','pvx14821@romog.com','avijit1122','KXZC5MUJKRYY75OWBFA42ZF3J26WU4HH','2024-04-16 15:07:04'),(31,'61558319367290','yem43092@fosiq.com','avijit1122','6GSZFYTI2GTVXWEAYLVARUXJBZTZYTKR','2024-04-16 15:07:04'),(32,'61558242239459','ahu24654@vogco.com','avijit1122','5J7XFMI55VQVAIY7XLJ2SMRAEXW4ZI33','2024-04-16 15:07:04'),(33,'61558164452206','iat56624@vogco.com','avijit1122','ONMDLLMRKMCADVYDQQAAIVQH2CO4C64Y','2024-04-16 15:07:04'),(34,'61557960760305','kot92772@fosiq.com','avijit1122','OLL7BEOAIG5ZKYUQLTG752FNLSITHUCV','2024-04-16 15:07:04'),(35,'61558222920458','ezl66703@fosiq.com','avijit1122','AYO5UG7FFX2CLM77IAQBQN4RYXMEJQRM','2024-04-16 15:07:04'),(36,'61558473591519','wigado9025@hbkio.com','Joty1234','ROZR43ITSPJS46BKOH6TV3J7FYPS4JPL','2024-04-16 15:07:04'),(37,'61557757903626','yihobog385@otixero.com','Joty1234','T26MYT7LIRVXAEMN7CB6PZBBSZV4FDGM','2024-04-16 15:07:04'),(38,'61557797866416','navewop922@omg6.com','hridoy90','5QF43H7KOCEXX2P3V4BAIF7JI7XBVJAB','2024-04-16 15:07:04'),(39,'61558382635870','hefoy35048@omg6.com','hridoy90','RJ34LDSKENXVTWN7Z7V3CL54B4F7XWMJ','2024-04-16 15:07:04'),(40,'61557848204401','kehil52678@kunderh.com','hridoy90','H425C62QQGIEMFFSWFE7EXH3UXMMQKKM','2024-04-16 15:07:04'),(41,'61557870673454','hijap50256@otixero.com','hridoy90','XKUVA46C4PNPG5E5W7VRYYHOWCZNULEN','2024-04-16 15:07:04'),(42,'61558368593179','hitiro4124@otixero.com','hridoy90','FPHPE3W32KKBQ4TBDSYGBX2SNM7JHYJ6','2024-04-16 15:07:04'),(43,'61558164331719','lenawa3030@omg6.com','hridoy90','UMAKHJ4SQ3UW7T4M4XG7P2BUY4VPBCWZ','2024-04-16 15:07:04'),(44,'61557953530291','haneb43606@otixero.com','hridoy90','5IUGOPBW7T3WAS737K7M3UTNAWCLGKRS','2024-04-16 15:07:04'),(45,'61558158361824','jocox22078@omg6.com','hridoy90','VN6NQ3ELYA2ZDO3EUEQY7TXECC44YF32','2024-04-16 15:07:04'),(46,'61557776685889','peg07861@romog.com','avijit1122','ISQXKZNDRJ7ZLH6GIWQIXFOKA6WJM47N','2024-04-16 15:07:04'),(47,'61558382574254','yadeg22932@otixero.com','hridoy90','QCAWWHLQIYD22NHE74IOYA5Y46BEBPQJ','2024-04-16 15:07:04'),(48,'61557905832908','cosebex222@otixero.com','hridoy90','LEV6ZMRG5V53HNPNEPWL7DZIZRLG2SXJ','2024-04-16 15:07:04'),(49,'61558153653065','namakos431@omg6.com','hridoy90','AR2OCHL6RZJ572QAMVU2FSGJUWF6AL3R','2024-04-16 15:07:04'),(50,'61558037527236','doyihiy208@omg6.com','hridoy90','N3Q4NLGLIREPZDCSSXIDRMWCTDTME7Z4','2024-04-16 15:07:04'),(51,'61558436813245','ofd86294@vogco.com','Avijit1122','SXA2YHX44JPUQHE4RCJFZG5ZZZJCMDHA','2024-04-16 15:07:04'),(52,'61558356866561','ocx97354@vogco.com','Avijit1122','AQ6N7HZXR3PY7WMNHYQVXTMQKX4VXZIS','2024-04-16 15:07:04'),(53,'61558222620473','qdk56041@romog.com','Avijit1122','ZT6RR6I4NSQCE2EFAGR54JY4SPYFTROX','2024-04-16 15:07:04'),(54,'61558191631309','nmk05851@fosiq.com','Avijit1122','NPXQSD5Q3NNUX22HO5V7E7WDUKU4X3IR','2024-04-16 15:07:04'),(55,'61558349337005','cimaj88585@felibg.com','Avijit1122','SG3WF4HKNHPHV37CLFPCDEQU4FGJTGVE','2024-04-16 15:07:04'),(56,'61558213110919','rekoy56890@evimzo.com','Avijit1122','KPREMKUPVT3UN2VAXABD7RI4GY4QETXH','2024-04-16 15:07:04'),(57,'61558277068424','vth28210@vogco.com','avijit1122','MC2NLNUGDRL4BEVII7I6OUXKI4HXSXQ3','2024-04-16 15:07:04'),(58,'61558322607700','barova4901@hbkio.com','Joty1234','H2H67W23XASSPTLYK35X7MKKKDPUGNA2','2024-04-16 15:07:04'),(59,'61557850484936','kogey43160@kunderh.com','Joty1234','DJR3TLQY32FD2ZWQ46VZI3DUYVHU342D','2024-04-16 15:07:04'),(60,'61557766097273','xfx25725@romog.com','avijit1122','JVFIOHMS4EITMUQTLAFW3E6XLVAUEWR4','2024-04-16 15:07:04'),(61,'61558014607975','cmv92286@romog.com','avijit1122','M5LLUGW4PW2WSFDBVP7ML2AZ5ZDB3RDK','2024-04-16 15:07:04'),(62,'61558179241341','udt83536@romog.com','avijit1122','DIMWPVTZIXZFHUZTUNHF7QCUG4RXXXQT','2024-04-16 15:07:04'),(63,'61558158212479','gepew78683@kunderh.com','Joty1234','5FJIFGRKOPEWQBLAEYSXASMBF4CL3PLK','2024-04-16 15:07:04'),(64,'61557906372837','becexo4458@hbkio.com','Joty1234','6O2OD2DFYEEY7O2KIF66TYX3LG5FWVJK','2024-04-16 15:07:04'),(65,'61558061016030','lirage8937@otixero.com','milon888','TB2KEIN56WUBBKM5H3VDNH6WVYWNJRLS','2024-04-16 15:07:04'),(66,'61558481931017','defeco7501@otixero.com','milon888','FIYICY57CUU4ZXPSZUPPDIBJREEMW4YI','2024-04-16 15:07:04'),(67,'61557846435067','namihe4572@omg6.com','milon888','DPNU2RN5QXT6OWSVM7LYLFNUUE6BWS37','2024-04-16 15:07:04'),(68,'61557790636570','yacicec380@omg6.com','milon888','LBRHIUYYQMYQBABBXXUQAGV66QC7T5IB','2024-04-16 15:07:04'),(69,'61558087144768','govov36753@omg6.com','milon888','TB4KIQSETH7BM3ZAC733ZVUASV57S6NV','2024-04-16 15:07:04'),(70,'61558167032262','skk87803@fosiq.com','Avijit1122','ELZAAP4IRI56DRSSWT5R64E4OM5OQYZB','2024-04-16 15:07:04'),(143,'61556993095305','qllbkegsas@rambler.ru','E75l8#8XaO!U','GBWID44ZKESXDV7ZNDIRW75RY4YPFCPU','2024-04-16 15:13:31'),(144,'61556571823159','niuhlxevot@rambler.ru','l63m2#8KyY@O','MHKDWHMWI6DSOH7X7OULGFECA6ZF3RPR','2024-04-16 15:13:31'),(145,'61556543115327','zavaydmvdm@rambler.ru','d65t5#7Y9l#F','UJCXI32UPBGT5TX7KQQS7WTJLIAPVOIH','2024-04-16 15:13:31'),(146,'61556724215962','ijjdaxqlyu@rambler.ru','JC5V5#5Lv9@N','2ZEIFJP2DNVDJ3XAXGWVHUAWMCWZ7AOS','2024-04-16 15:13:32'),(147,'61556561624166','jjfafhault@rambler.ru','DT0z1#8NXa@L','CA4735FYFSAI57QZXJM4QE5W7QVHLBLT','2024-04-16 15:13:32'),(148,'61556845560314','ivqdmxrpmm@rambler.ru','Qs233#7y8y@B','QVCSB4HSEC6HB5MF7MVBLXLELRTZN2ZV','2024-04-16 15:13:32'),(149,'61556465687635','xrlhifeugq@rambler.ru','Rs5L4!9cEz#R','6MP2BISZGHOZQQTQTNN4Q7YFS7VPK7ED','2024-04-16 15:13:32'),(150,'61556626090918','tfwmxrbbrw@rambler.ru','rc759!7Iye!1','ZQCXHLEPY3YCV6P6SWMSKOXV6CUTC2ZO','2024-04-16 15:13:32'),(151,'61556723466510','sqkmtqkppe@rambler.ru','LL8m2@2E5c@E','OT2NSJX7JOIIFII7DKRFBT7DA2H6ZGJS','2024-04-16 15:13:32'),(152,'61556513926478','vntcxpmwnf@rambler.ru','Hh1N8#45MZ@T','6RO5P5PMUACODHNXGEDT4VLRBKEJG6JB','2024-04-16 15:13:32'),(153,'61557911146952','vecer29694@vcrnn.com','uttam2024','ISMVUPCRGKZK7CG4LLJ3B4UJFDUPVOVD','2024-04-16 15:32:06'),(154,'61558235584007','cefivab566@w3fax.com','uttam2024','EOABP2CVWLAZ5SNHYDACWKHZUNRI2NJY','2024-04-16 15:32:06'),(155,'61558534523139','jadofoc575@vcrnn.com','uttam2024','4APD3MKQ3GWCAZHKR57M2ZKVH6RIHPVH','2024-04-16 15:32:06'),(156,'61558325611839','bosar18592@vcrnn.com','uttam2024','TTWOFPKIYA6XZQDLCAUK3ABFYWDJ7ZEU','2024-04-16 15:32:06'),(157,'61557942225418','dexek65930@vcrnn.com','uttam2024','CDH4GJ4HC5EEW5KRTOW6F3YSOKIK4755','2024-04-16 15:32:06'),(158,'61558599950800','poniham254@w3fax.com','uttam2024','XOCVCUSRSJDJUEWKJVHG6KDFABB3L3LR','2024-04-16 15:32:06'),(159,'61557901757223','xobak64631@vcrnn.com','uttam2024','W45IWB7HXJSWSW5MKX2UMN7NITSM6462','2024-04-16 15:32:06'),(160,'61558512384173','tekac88336@vcrnn.com','uttam2024','4IFW75ZSNKXG75FD7ZEIIB5C7OEIVZPY','2024-04-16 15:32:06'),(161,'61558184195589','sibopot422@vcrnn.com','uttam2024','VLSEP7VVBIZAML737U3DLAJ5EOTJADTG','2024-04-16 15:32:06'),(162,'61558243804189','mejela3018@vcrnn.com','uttam2024','QZ5XYXXUHZHFWUYHIEOJLUOBJWUYXBWY','2024-04-16 15:32:06'),(163,'61558407958507','i2nn541sxb@zlorkun.com','muyrfd5601','4O7TZKLHPN44OZB4TGQPFW3KUDYG54IS','2024-04-16 15:32:06'),(164,'61558198832802','lolohip461@otixero.com','sana11','J4ZDOE3JBJGGGFYUXPUQ3PYJAPUJ2HJQ','2024-04-16 15:32:06'),(165,'61558076617670','raganij511@otixero.com','sana11','72W3SGBWAHUTREAOOMMWQ4TNOCL5LY4Q','2024-04-16 15:32:06'),(166,'61557981791709','ninov60627@otixero.com','sana11','VVAJB4GVEEEQ6AVJMIKBGAGB2ERBBWMH','2024-04-16 15:32:06'),(167,'61558427456886','bakop51312@vcrnn.com','uttam2024','UX447K6ZDSAHFRA2G4EEEDC2EA3SYSPL','2024-04-16 15:32:06'),(168,'61557989142308','hocori6619@vcrnn.com','uttam2024','CA34HHTGWVNXKYVUEUZIP2A2VJXN24KA','2024-04-16 15:32:06'),(169,'61557995561985','sodex10671@w3fax.com','uttam2024','M4VF7FI54W53CLX7ZOSIGWTVNRIQJMD5','2024-04-16 15:32:06'),(187,'61554278467417','diliv88360@taiwea.com','Arpan1234','SSZOEDMAZPWEATRJIFNTCM366QVTAGLC','2024-04-16 15:35:17'),(188,'61554278499297','tobaj31241@taiwea.com','ktm000','I6DRLCJ5IMTNKONRJBVPJDDEKVCTIPOP','2024-04-16 15:35:17'),(189,'61554280116106','katowi6670@raknife.com','Deba4321','G5BY3CHFMWSEQJI5MIJUJRLACQLRXM2P','2024-04-16 15:35:17'),(220,'61557217004604','none_email','L29651','none_2fa','2024-04-16 15:45:43'),(221,'61557217963156','none_email','Hh1N8#45MZ@T','none_2fa','2024-04-16 15:45:43'),(222,'61557217963875','none_email','Y17241793','none_2fa','2024-04-16 15:45:43'),(223,'61557219494591','none_email','6448C6558','none_2fa','2024-04-16 15:45:43'),(224,'61557219794332','none_email','R655847','none_2fa','2024-04-16 15:45:43'),(225,'61557180675268','none_email','79344E50','none_2fa','2024-04-16 15:45:43'),(226,'61557174614587','none_email','71990W528','none_2fa','2024-04-16 15:45:43'),(227,'61557211034342','none_email','I00439','none_2fa','2024-04-16 15:45:43'),(228,'61557177584592','none_email','128I2635','none_2fa','2024-04-16 15:45:43'),(229,'61557178634384','none_email','243878L57','none_2fa','2024-04-16 15:45:43'),(230,'61557177344953','none_email','D720575','none_2fa','2024-04-16 15:45:43'),(231,'61557230173519','none_email','F49592437','none_2fa','2024-04-16 15:45:43'),(232,'61557230562948','none_email','W00470259','none_2fa','2024-04-16 15:45:43'),(233,'61557231553747','none_email','1632E7','none_2fa','2024-04-16 15:45:43'),(234,'61557233442937','none_email','W963913','none_2fa','2024-04-16 15:45:43'),(235,'61557235993365','none_email','520633011','none_2fa','2024-04-16 15:45:43'),(236,'61557176445715','none_email','6359P5','none_2fa','2024-04-16 15:45:43'),(237,'61557238482539','none_email','976I11','none_2fa','2024-04-16 15:45:43'),(238,'61557239173423','none_email','41657270','none_2fa','2024-04-16 15:45:43'),(239,'61557240073329','none_email','777627614','none_2fa','2024-04-16 15:45:43');
/*!40000 ALTER TABLE `fb_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operation`
--

DROP TABLE IF EXISTS `operation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operation` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '操作id',
  `operate_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '操作名称',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `function_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '方法名称',
  `is_delete` int NOT NULL DEFAULT '0' COMMENT '是否弃用',
  `type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '其他操作' COMMENT '操作类型',
  `platform_type` varchar(50) COLLATE utf8mb4_general_ci DEFAULT 'overseas',
  PRIMARY KEY (`id`),
  UNIQUE KEY `function_name` (`function_name`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operation`
--

LOCK TABLES `operation` WRITE;
/*!40000 ALTER TABLE `operation` DISABLE KEYS */;
INSERT INTO `operation` VALUES (1,'打开选中浏览器','2024-04-11 09:20:54','open_browser',0,'其他操作','overseas'),(2,'Tiktok养号','2024-04-11 09:21:40','tk_brushVideo',0,'Tiktok','overseas'),(3,'Tiktok上传视频','2024-04-11 09:22:18','tk_uploadVideo',0,'Tiktok','overseas'),(4,'Tiktok评论','2024-04-11 09:23:16','tk_comment',0,'Tiktok','overseas'),(5,'Facebook养号','2024-04-11 09:24:17','fb_brushPost',0,'Facebook','overseas'),(6,'Fb监控小组评论','2024-04-11 09:25:53','listen_fb_comment',0,'Facebook','overseas'),(7,'Fb获取小组新人','2024-04-11 09:26:49','get_fb_newMember',0,'Facebook','overseas'),(8,'Fb获取小组信息','2024-04-11 09:28:12','get_fb_groupInfo',0,'Facebook','overseas'),(9,'Tk获取用户粉丝','2024-04-16 16:42:16','get_tk_fans',0,'Tiktok','overseas'),(10,'Ws获取群组号码','2024-04-24 16:11:38','ws_get_groupTel',0,'Whatsapp','overseas'),(11,'Ins获取用户粉丝','2024-04-26 16:42:23','ins_get_user_fans',0,'Ins','overseas'),(12,'Tk获取主账号评论','2024-05-05 08:58:54','get_self_comments',0,'Tiktok','overseas');
/*!40000 ALTER TABLE `operation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `search_keyword`
--

DROP TABLE IF EXISTS `search_keyword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `search_keyword` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '关键词id',
  `keyword` varchar(50) COLLATE utf8mb4_general_ci NOT NULL COMMENT '关键词名称',
  `type_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL COMMENT '关键词类型',
  `update_time` varchar(50) COLLATE utf8mb4_general_ci NOT NULL COMMENT '更新日期',
  `is_delete` varchar(1) COLLATE utf8mb4_general_ci NOT NULL COMMENT '删除标记 1:删除,0:可用',
  `delete_id` int DEFAULT NULL COMMENT '删除id 用于防重复数据',
  `platform_type` varchar(50) COLLATE utf8mb4_general_ci DEFAULT 'overseas',
  PRIMARY KEY (`id`),
  UNIQUE KEY `keyword` (`keyword`,`delete_id`,`type_name`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search_keyword`
--

LOCK TABLES `search_keyword` WRITE;
/*!40000 ALTER TABLE `search_keyword` DISABLE KEYS */;
INSERT INTO `search_keyword` VALUES (1,'bag Online stores','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(2,'Messenger bag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(3,'Shoulder bag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(4,'Monogram Canvas','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(5,'Bottega Veneta','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(6,'Speedy','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(7,'Chanel','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(8,'Luxury bag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(9,'Second-hand Luxury bag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(10,'Michael Kors','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(11,'Paddington','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(12,'Alexander McQueen','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(13,'Bucket bag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(14,'Dior','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(15,'Dionysus','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(16,'Neverfull','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(17,'Wallet','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(18,'Balenciaga','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(19,'Belt bag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(20,'Backpack','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(21,'Clutch','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(22,'Saint Laurent','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(23,'Handbag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(24,'Peekaboo','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(25,'Le Pliage','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(26,'Celine','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(27,'Crossbody bag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(28,'Chloe','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(29,'Fendi','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(30,'Tote bag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(31,'GG Marmont','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(32,'Herm猫s','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(33,'Coach','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(34,'Gucci','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(35,'Satchel','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(36,'Burberry','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(37,'Prada','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(38,'Valentino','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(39,'Pouch','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(40,'Birkin','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(41,'Miu Miu','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(42,'Versace','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(43,'Givenchy','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(44,'Alma','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(45,'2.55','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(46,'Louis Vuitton','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(47,'Hobo bag','face_group','2024-05-12 16:27:26','0',-1,'overseas'),(48,'cosmetic','ins_search','2024-05-12 16:27:39','0',-1,'overseas'),(49,'lipstick','ins_search','2024-05-12 16:27:39','0',-1,'overseas'),(50,'Makeup','ins_search','2024-05-12 16:27:39','0',-1,'overseas'),(51,'test_keyword','face_group','2024-05-12 16:27:57','0',-1,'overseas');
/*!40000 ALTER TABLE `search_keyword` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `search_keyword_type`
--

DROP TABLE IF EXISTS `search_keyword_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `search_keyword_type` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '关键词类型id',
  `type_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL COMMENT '类型名称',
  `type_comment` text COLLATE utf8mb4_general_ci NOT NULL COMMENT '类型备注',
  `is_delete` varchar(1) COLLATE utf8mb4_general_ci NOT NULL COMMENT '删除标记 1:删除,0:可用',
  `update_time` varchar(50) COLLATE utf8mb4_general_ci NOT NULL COMMENT '更新时间',
  `platform_type` varchar(50) COLLATE utf8mb4_general_ci DEFAULT 'overseas',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search_keyword_type`
--

LOCK TABLES `search_keyword_type` WRITE;
/*!40000 ALTER TABLE `search_keyword_type` DISABLE KEYS */;
INSERT INTO `search_keyword_type` VALUES (1,'face_group','Facebook小组搜索','0','2024-05-12 11:16:52','overseas'),(2,'ins_search','Ins搜索用来采集粉丝的用户','0','2024-05-12 11:17:46','overseas');
/*!40000 ALTER TABLE `search_keyword_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tag` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '标签id_数据库',
  `tag_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '标签名称',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_delete` int NOT NULL DEFAULT '0' COMMENT '状态 1删除，0正常',
  `type_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'primary' COMMENT '标签类型',
  `platform` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '平台' COMMENT '平台类型',
  `platform_type` varchar(50) COLLATE utf8mb4_general_ci DEFAULT 'overseas',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (1,'facebook','2024-04-08 10:42:03',0,'success','平台','overseas'),(2,'tiktok','2024-04-08 10:42:21',0,'success','平台','overseas'),(3,'tiktok账号退出','2024-04-08 10:42:29',0,'danger','Tiktok','overseas'),(4,'ins_test','2024-04-08 10:42:39',0,'success','平台','overseas'),(5,'之前能发评论','2024-04-08 10:42:54',1,'primary','Tiktok','overseas'),(6,'能发评论','2024-04-08 10:43:07',1,'primary','Tiktok','overseas'),(7,'tiktok手机新号','2024-04-08 10:43:20',1,'primary','Tiktok','overseas'),(8,'tiktok2_2','2024-04-08 10:43:27',1,'primary','Tiktok','overseas'),(9,'facebook测试','2024-04-08 10:43:55',1,'primary','Facebook','overseas'),(10,'tiktok老号','2024-04-08 10:44:08',1,'primary','Tiktok','overseas'),(11,'0.95新号','2024-04-08 10:44:16',1,'primary','Tiktok','overseas'),(12,'0.95新号2','2024-04-08 10:44:32',1,'primary','Tiktok','overseas'),(13,'临时标签','2024-04-11 11:54:16',1,'primary','平台','overseas'),(14,'4.9新号','2024-04-11 15:21:46',1,'primary','Tiktok','overseas'),(15,'tiktok4.11','2024-04-11 15:22:21',1,'primary','Tiktok','overseas'),(16,'4.8手机号','2024-04-11 15:22:33',1,'primary','Tiktok','overseas'),(17,'fb180天','2024-04-11 15:23:00',1,'danger','Facebook','overseas'),(18,'facebook4.10','2024-04-11 15:23:25',0,'primary','Facebook','overseas'),(19,'代理中断','2024-04-11 15:24:03',0,'danger','平台','overseas'),(20,'fb身份证验证','2024-04-12 14:51:48',0,'danger','Facebook','overseas'),(21,'tiktok4.12','2024-04-12 16:11:55',1,'primary','Tiktok','overseas'),(22,'手机扫不上','2024-04-13 11:24:57',0,'danger','Tiktok','overseas'),(23,'tiktok4.13','2024-04-13 11:25:06',1,'primary','Tiktok','overseas'),(24,'Fb4.13','2024-04-13 16:09:53',0,'primary','Facebook','overseas'),(25,'tiktok4.14','2024-04-14 11:19:33',1,'primary','Tiktok','overseas'),(26,'tiktok手机主号','2024-04-16 09:47:18',0,'warning','Tiktok','overseas'),(27,'tiktok4.16','2024-04-16 09:57:11',1,'primary','Tiktok','overseas'),(28,'TkAds注册4.17','2024-04-17 10:54:49',1,'primary','Tiktok','overseas'),(29,'tiktok4.17','2024-04-17 11:07:30',1,'primary','Tiktok','overseas'),(30,'fb账号退出','2024-04-17 14:34:57',0,'danger','Facebook','overseas'),(31,'Tk手机注册4.17','2024-04-17 17:49:08',1,'primary','平台','overseas'),(32,'whatsapp','2024-04-24 16:10:20',0,'success','平台','overseas'),(33,'ws账号退出','2024-04-30 14:19:26',0,'danger','WhatsApp','overseas'),(34,'Tk正常账号','2024-04-30 14:42:08',0,'primary','Tiktok','overseas'),(35,'Telegram','2024-05-09 14:33:22',0,'success','平台','overseas'),(36,'Fb广告账户','2024-05-09 15:03:52',0,'warning','Facebook','overseas'),(37,'Ins登录异常','2024-05-09 15:51:31',0,'danger','Instagrame','overseas'),(38,'ws测试主号','2024-05-15 08:55:11',0,'warning','WhatsApp','overseas');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-16 11:25:46
