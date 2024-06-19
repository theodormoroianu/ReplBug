-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.25-TiDB-v6.3.0-20220913

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
-- Table structure for table `t_cp0sl`
--

DROP TABLE IF EXISTS `t_cp0sl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_cp0sl` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_1_kgbc` int(11) DEFAULT NULL,
  `c_dw8ly` double DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,
  KEY `t_py61ed` (`wkey`,`pkey`,`c_1_kgbc`,`c_dw8ly`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_cp0sl`
--

LOCK TABLES `t_cp0sl` WRITE;
/*!40000 ALTER TABLE `t_cp0sl` DISABLE KEYS */;
INSERT INTO `t_cp0sl` VALUES (2,15000,NULL,75.37),(2,16000,NULL,100.57),(2,17000,NULL,34.89);
/*!40000 ALTER TABLE `t_cp0sl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_d0c_g`
--

DROP TABLE IF EXISTS `t_d0c_g`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_d0c_g` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_p5i5kc` int(11) DEFAULT NULL,
  `c_eephud` text DEFAULT NULL,
  `c_dmlxnb` text DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_d0c_g`
--

LOCK TABLES `t_d0c_g` WRITE;
/*!40000 ALTER TABLE `t_d0c_g` DISABLE KEYS */;
INSERT INTO `t_d0c_g` VALUES (1,11000,NULL,'fiwppc','r_pgdd'),(1,12000,NULL,'livapd','h2hxxc'),(1,13000,NULL,'615gyd','pvbjxb'),(1,14000,NULL,'9hupkc','gh3_'),(6,31000,NULL,'zbsrzd','oojmqc'),(6,32000,NULL,'wdgkx','romj9b'),(6,33000,NULL,'hatukb','h4i85c'),(6,34000,NULL,'0vpjzb','hqzddd'),(8,39000,NULL,NULL,'7tlaz'),(8,40000,NULL,NULL,'xnggwb'),(8,41000,NULL,NULL,'f2cmrc'),(8,42000,NULL,NULL,'xeiuld'),(10,49000,NULL,NULL,'hitgt'),(10,50000,NULL,'ekdgr','jhhm5d'),(10,51000,NULL,'0alpkb','2c0ypc'),(10,52000,NULL,'0ipm5','sdle6b'),(10,53000,NULL,'zf4gcb','msu2jd'),(11,54000,NULL,NULL,'fwxjib'),(11,55000,NULL,'_zrtlb','iwkw_d'),(11,56000,NULL,'ridui','bktoxb'),(11,57000,NULL,'n49lv','rqcxub'),(11,58000,NULL,'1u5rrb','wvkojc'),(11,59000,NULL,'il65yb','odx15b'),(11,60000,NULL,'gdo9_c','gafkvb'),(11,61000,NULL,'e_21x','hnhz7d'),(15,80000,NULL,NULL,'ub3xf'),(15,81000,NULL,'b7hy_d','kfahid'),(15,82000,NULL,'mul3td','v0dol'),(15,83000,NULL,'5jxh5d','rsfdi'),(15,84000,NULL,'rty7kc','zhgdwd'),(15,85000,NULL,'w9vssb','bjmdeb');
/*!40000 ALTER TABLE `t_d0c_g` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-24 13:16:02
