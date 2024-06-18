-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.25-TiDB-v6.1.0-alpha-173-g32b9c1477

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
-- Table structure for table `t_3nyn_c`
--

DROP TABLE IF EXISTS `t_3nyn_c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_3nyn_c` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_kgkc7c` double DEFAULT NULL,
  `c_6preq` int(11) DEFAULT NULL,
  `c_dufiib` int(11) DEFAULT NULL,
  `c_9kited` int(11) DEFAULT NULL,
  `c_lhficd` text DEFAULT NULL,
  `c_ks83mc` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,
  UNIQUE KEY `pkey_2` (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_3nyn_c`
--

LOCK TABLES `t_3nyn_c` WRITE;
/*!40000 ALTER TABLE `t_3nyn_c` DISABLE KEYS */;
INSERT INTO `t_3nyn_c` VALUES (3,6,51.38,84,68,20,'_lfw1',4),(3,7,89.44,8,5,74,'k38i2c',75),(6,11,10.18,76,62,26,'9_ykvc',47),(6,12,NULL,13,52,57,'towgz',17),(6,13,84.72,88,14,34,'xaml4c',97),(8,20,36.22,38,91,90,'u25qs',19),(8,21,20.56,54,25,73,'v_2vw',57),(8,22,98.27,28,4,48,'6fuvkc',54),(8,23,2.23,56,27,25,'x_tr9d',54),(8,24,76.39,96,86,82,'j_buzd',31),(8,25,65.99,46,80,32,'c1vqyd',85),(9,26,55.14,98,67,33,'yfufmc',77),(9,27,18.49,80,33,50,'ewktud',83),(9,28,34.91,50,23,19,NULL,40),(9,29,2.6,93,59,32,'jyytrb',5),(9,30,97.77,59,75,46,'kcx81b',85),(10,31,1.8,48,43,51,'8zywqb',91),(10,32,45.5,76,17,29,'j4ftgd',42),(10,33,50.26,96,35,53,'2g8e3c',97),(10,34,51.82,20,96,70,'lddeob',60),(13,38,36.8,59,27,71,'kchd7b',6),(13,39,50.8,69,98,75,'gj1drc',90),(13,40,19.38,87,31,73,'gka4p',51),(13,41,21.45,96,89,21,'qimjid',32),(13,42,96.1,18,61,97,'suvzk',71),(17,52,84.56,58,2,96,'2_b1j',78);
/*!40000 ALTER TABLE `t_3nyn_c` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_rtu0od`
--

DROP TABLE IF EXISTS `t_rtu0od`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_rtu0od` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_wvbclc` int(11) DEFAULT NULL,
  `c_eejioc` int(11) DEFAULT NULL,
  `c_qnvjud` text DEFAULT NULL,
  `c_aw4fcc` int(11) DEFAULT NULL,
  `c_96usr` double DEFAULT NULL,
  `c_9rybl` double DEFAULT NULL,
  `c_utisnc` text DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,
  UNIQUE KEY `pkey_2` (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_rtu0od`
--

LOCK TABLES `t_rtu0od` WRITE;
/*!40000 ALTER TABLE `t_rtu0od` DISABLE KEYS */;
INSERT INTO `t_rtu0od` VALUES (5,10,95,32,'nrl_kd',50,68.8,15.85,'sooa7b'),(15,44,1,76,'4nj9nb',1,49.83,44.78,'3xdyh'),(15,45,48,63,NULL,78,2147483648.1,68.2,NULL),(15,46,62,35,'wegllb',20,49.38,49.21,'lqokrd'),(15,47,25,75,'6akhxb',60,75.29,NULL,'lhtpod');
/*!40000 ALTER TABLE `t_rtu0od` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_wvccid`
--

DROP TABLE IF EXISTS `t_wvccid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_wvccid` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_bracr` double DEFAULT NULL,
  `c_ttshqd` double DEFAULT NULL,
  `c_lv_m0` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,
  UNIQUE KEY `pkey_2` (`pkey`),
  KEY `t_mpgywb` (`wkey`,`pkey`,`c_bracr`,`c_ttshqd`,`c_lv_m0`),
  UNIQUE KEY `t_r0tn5b` (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_wvccid`
--

LOCK TABLES `t_wvccid` WRITE;
/*!40000 ALTER TABLE `t_wvccid` DISABLE KEYS */;
INSERT INTO `t_wvccid` VALUES (1,1,8.79,95.77,16),(2,2,21.45,23.81,68),(2,3,60.28,NULL,77),(2,4,82.64,20.62,70),(2,5,69.21,NULL,45),(4,8,28.41,32.74,13),(4,9,94.45,33.18,59),(7,14,5.11,70.37,73),(7,15,4.22,2147483648.1,34),(7,16,NULL,2147483648.1,78),(7,17,26.41,60.29,15),(7,18,38.58,43.39,51),(7,19,26.95,57.6,34),(11,35,15.67,4.81,47),(12,36,82.64,NULL,87),(12,37,40.4,59.71,98),(14,43,NULL,91.4,9),(16,48,42.7,5.51,100),(16,49,NULL,3.31,63),(16,50,68.33,32.57,48),(16,51,51.42,NULL,79),(18,53,89.58,31.56,42),(18,54,37.6,42.2,56),(18,55,NULL,9.99,89),(18,56,82.2,98.98,4),(19,57,43.56,83.59,27),(19,58,92.16,93.28,58),(19,59,43.26,86.47,6),(19,60,60.97,37.12,21),(19,61,7.14,97.37,11),(19,62,83.22,65.89,83);
/*!40000 ALTER TABLE `t_wvccid` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-15 21:21:04
