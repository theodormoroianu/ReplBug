-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.25-TiDB-v5.4.0-alpha-133-g20b9a4d8c

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_berydd`
--

DROP TABLE IF EXISTS `t_berydd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_berydd` (
  `c_ymgvrd` int(11) DEFAULT NULL,
  `c_ee5vqb` int(11) DEFAULT NULL,
  `c_xsjoqb` int(11) DEFAULT NULL,
  `c_xqizm` text DEFAULT NULL,
  `c__3lu4b` int(11) DEFAULT NULL,
  `c_mp6ko` double DEFAULT NULL,
  `c_ndnhmc` double DEFAULT NULL,
  `c_cdqetd` double DEFAULT NULL,
  `c_ioru4c` double NOT NULL,
  PRIMARY KEY (`c_ioru4c`) /*T![clustered_index] NONCLUSTERED */,
  KEY `t_c1q7y` (`c_ymgvrd`,`c_ee5vqb`,`c_xsjoqb`,`c_mp6ko`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_berydd`
--

LOCK TABLES `t_berydd` WRITE;
/*!40000 ALTER TABLE `t_berydd` DISABLE KEYS */;
INSERT INTO `t_berydd` VALUES (90,6,12,'veew0',53,48.55,NULL,74.21,19.83),(66,125,NULL,NULL,92,11.66,49.27,27.17,66.14),(49,NULL,4,'isaqx',44,NULL,NULL,70.26,35.9),(NULL,48,67,'xrdjzd',89,5.2,53.12,62.33,21.82),(14,21,15,NULL,90,24.4,84.21,97.98,84.46),(62,38,53,'ydd5rd',74,61.45,NULL,64.28,22.94),(45,92,74,'bkhfnd',66,19.8,59.9,15.63,71.72),(39,12,37,'tgjwe',19,6.8,40.5,36.98,91.71),(80,52,25,NULL,0,45.1,36.85,48.38,83.65),(92,72,10,'z0axuc',NULL,25.5,47.9,8.82,85.99),(62,103,16,'qs6hkb',65,52.65,NULL,12.62,81.28),(64,47,10,'j_en6',86,88.54,61.62,31.89,91.99),(32,3,9,'j9dmjb',26,77.11,64.72,54.46,98.15),(20,72,67,'ua6z1b',4,88.92,8.71,NULL,53.43),(43,30,24,'9t_xp',765,4.87,42.89,56.97,10.77),(16,0,6,'huwyzb',25,93.64,61.59,68.3,89.55),(85,27,47,'osmemb',6,88.65,43.92,90.2,12.58),(46,0,64,'',53,38.3,58.58,68.96,90.93),(87,1118,74,'f0ukjd',41,51.28,21.95,NULL,83.26),(35,75,21,'tu4umd',0,75.75,NULL,4.26,2.43),(47,65536,885,'pohqsd',75,40.97,18.53,55.76,37.75),(39,12,0,'xbiwo',6,26.92,95.8,86.87,62.1),(50,63,0,'\'utr49b\'',19,100.17,23.85,99.51,3.42),(24,0,3,'cbs70',66,21.8,76.21,100.39,1.55),(63,127,13,'f65ylc',16,100.39,1.23,100.78,3.6),(1122,99,10,NULL,52,40.1,48.15,45.47,23.97),(5,27,4,NULL,3,22.16,40.13,24.5575,79.99),(40,23,77,'5hbpf',54,NULL,73.36,96.82,45.76),(NULL,0,37,'8ajfyd',88,16.86,82.2,10.43,63.9),(36,0,NULL,'n_pa5b',30,NULL,27.17,21.9,21.42),(12,33,0,'tp146',74,NULL,28.14,61.85,18.17),(6,47,87,'_hihkb',67,20.64,NULL,56.33,73.36),(33,58,51,'_wpqld',505,22.82,23.31,5.39,13.88),(43,1,52,NULL,23,84.1,14.11,81.91,74.51),(45,17,6,'50l0zd',29,59.92,87.86,72.93,54.67),(121,27,19,'xvuypd',63,95.8,5.78,55.45,42.75),(0,97,-60,'fb9god',93,80.47,90.43,71.9,52.38),(56,41,58,NULL,60,NULL,NULL,75.51,19.23),(56,57,44,'bmhrqc',6,65.17,409.18,46.75,15.7),(43,36,44,'yuzu8c',0,73.14,NULL,57.12,82.88),(86,5,49,'vsgecb',7,34.49,52.87,18.1,16.5);
/*!40000 ALTER TABLE `t_berydd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_kqoy4`
--

DROP TABLE IF EXISTS `t_kqoy4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_kqoy4` (
  `c_embscb` int(11) DEFAULT NULL,
  `c_gi3pxb` text DEFAULT NULL,
  `c_fif_7c` text DEFAULT NULL,
  `c_scsjqb` double DEFAULT NULL,
  `c_cxqb1` text DEFAULT NULL,
  `c_w1ibr` int(11) DEFAULT NULL,
  `c_0lknib` double DEFAULT NULL,
  `c_qfdzbd` double NOT NULL,
  `c_7kdcs` double DEFAULT NULL,
  PRIMARY KEY (`c_qfdzbd`) /*T![clustered_index] NONCLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_kqoy4`
--

LOCK TABLES `t_kqoy4` WRITE;
/*!40000 ALTER TABLE `t_kqoy4` DISABLE KEYS */;
INSERT INTO `t_kqoy4` VALUES (2,'uqjwsb','g2szy',48.38,'mzuotd',9,NULL,56.39,12.44),(98,'hg83eb','yedqwc',NULL,'8wk8sc',67,62.42,34.22,11.45),(43,NULL,'mk4l8b',5.39,'',0,19.63,6.3,52.92),(74,NULL,'en0_kd',36.9,'28anr',71,2.24,15.92,14.7),(905,'xbiwo','',7.56,'huwyzb',78,88.47,5.51,NULL),(5,'hc2_kc','ipyn9b',73.36,'laf0vd',98,39.55,29.46,45.16),(40,'n_pa5b','im7pbc',27.17,'chghub',4,2147483648.1,98.27,54.5),(33,'vhaykd','z79jg',82.75,'vlobd',27,5.16,22.3,7.74),(26,'khk3qc','hildkd',49.49,'a4ojr',9,15.45,34.86,48.52),(38,'','8fwbk',78.18,'396A6E357963',0,95.52,71.21,97.6),(12,'6A6578646E63','70gy0d',82.27,'jkral',0,45.39,71.49,2147483648.1),(33,NULL,'94vamc',4.16,'bz5cjc',0,23.73,49.81,NULL),(59,'','ui9pzd',NULL,NULL,10,3.92,48.55,63.54),(55,'zgcood','1lv8yb',45.54,'ydd5rd',88,59.67,52.98,43.23),(0,'fc8cud',NULL,10.55,NULL,21,42.47,55.64,3.9),(7,NULL,'bagcm',5.2,NULL,47,46.42,40.38,71.45);
/*!40000 ALTER TABLE `t_kqoy4` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-29  9:21:53
