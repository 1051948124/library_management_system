-- MySQL dump 10.13  Distrib 5.5.15, for Win32 (x86)
--
-- Host: localhost    Database: library_management_system
-- ------------------------------------------------------
-- Server version	5.5.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book_information`
--

DROP TABLE IF EXISTS `book_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book_information` (
  `name` text,
  `brief_introduction` varchar(200) DEFAULT NULL,
  `stock` tinyint(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_information`
--

LOCK TABLES `book_information` WRITE;
/*!40000 ALTER TABLE `book_information` DISABLE KEYS */;
INSERT INTO `book_information` VALUES ('python study','information',19),('西游记','《西游记》是中国古代一部浪漫主义长篇神魔小说，主要描写了唐僧、孙悟空、猪八戒猪悟能、沙僧沙悟净师徒四人去西天取经，历经九九八十一难最后终于取得真经的故事。',20),('红楼梦','《红楼梦》，别名《石头记》等，中国古代章回体长篇小说，中国古典四大名著之一。其通行本共120回，一般认为前80回是清代作家曹雪芹所著，后40回作者为无名氏，整理者为程伟元、高鹗。小说以贾、史、王、薛四大家族的兴衰为背景，以富贵公子贾宝玉为视角，以贾宝玉与林黛玉、薛宝钗的爱情婚姻悲剧为主线，描绘了一些闺阁佳人的人生百态，展现了真正的人性美和悲剧美，是一部从各个角度展现女性美以及中国古代社会百态的史诗',20),('水浒传','《水浒传》是元末明初施耐庵（现存刊本署名大多有施耐庵、罗贯中两人中的一人，或两人皆有）编著的章回体长篇小说。',20),('三国演义','《三国演义》（全名为《三国志通俗演义》，又称《三国志演义》）是元末明初小说家罗贯中根据陈寿《三国志》和裴松之注解以及民间三国故事传说经过艺术加工创作而成的长篇章回体历史演义小说，与《西游记》《水浒传》《红楼梦》并称为中国古典四大名著。该作品成书后有嘉靖壬午本等多个版本传于世，到了明末清初，毛宗岗对《三国演义》整顿回目、修正文辞、改换诗文，该版本也成为诸多版本中水平最高、流传最广的版本。',20),('java','21天学会java',20),('php','21天学会php',19),('盗墓笔记','故事详情...',0);
/*!40000 ALTER TABLE `book_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_borrow_book`
--

DROP TABLE IF EXISTS `user_borrow_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_borrow_book` (
  `student_id` varchar(20) DEFAULT NULL,
  `book_name` text,
  `ISBN` text,
  `borrow_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_borrow_book`
--

LOCK TABLES `user_borrow_book` WRITE;
/*!40000 ALTER TABLE `user_borrow_book` DISABLE KEYS */;
INSERT INTO `user_borrow_book` VALUES ('1','python study',NULL,NULL),('4','盗墓笔记',NULL,NULL),('4','php',NULL,NULL),('4','盗墓笔记',NULL,NULL),('1','php',NULL,NULL);
/*!40000 ALTER TABLE `user_borrow_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_information`
--

DROP TABLE IF EXISTS `user_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_information` (
  `student_id` varchar(20) DEFAULT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_information`
--

LOCK TABLES `user_information` WRITE;
/*!40000 ALTER TABLE `user_information` DISABLE KEYS */;
INSERT INTO `user_information` VALUES ('root','admin','123456'),('4','5','6'),('1','4','3'),('12','234','5');
/*!40000 ALTER TABLE `user_information` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-24 17:49:54
