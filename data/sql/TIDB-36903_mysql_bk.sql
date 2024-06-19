-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.25-TiDB-v6.1.0

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
-- Table structure for table `t_5mspyb`
--

DROP TABLE IF EXISTS `t_5mspyb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_5mspyb` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_dugmmc` int(11) DEFAULT NULL,
  `c_q0rdv` text DEFAULT NULL,
  `c_0bhxq` int(11) DEFAULT NULL,
  `c_qpz_v` text DEFAULT NULL,
  `c_rgl8pc` double DEFAULT NULL,
  `c_yisj0d` int(11) DEFAULT NULL,
  `c_n9hfnb` text DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_5mspyb`
--

LOCK TABLES `t_5mspyb` WRITE;
/*!40000 ALTER TABLE `t_5mspyb` DISABLE KEYS */;
INSERT INTO `t_5mspyb` VALUES (1,11000,NULL,'ff4_db',NULL,'fiubu',69.66,NULL,'fqjfyd'),(1,12000,NULL,'xyaxtc',NULL,'zv78g',63.16,NULL,'kfvyzc'),(1,13000,NULL,'eam_y',NULL,'pa81sb',NULL,NULL,'rdqfbc'),(1,14000,NULL,'qe4lbc',NULL,'_h7coc',23.65,NULL,'kvmyzb'),(3,22000,NULL,'o_bph',NULL,'lec_mc',52.63,NULL,'sj6g0b'),(3,23000,NULL,'yflbgb',NULL,'hwpnkb',25.2,NULL,'koqxsc'),(3,24000,NULL,'4rbcnc',NULL,NULL,8.68,NULL,NULL),(5,28000,NULL,'xqyfad',NULL,'npprs',39.47,NULL,'g3ouc'),(5,29000,NULL,NULL,NULL,'xanh8c',NULL,NULL,'8tvcwc'),(5,30000,NULL,'fuxhk',NULL,'ynm36d',69.1,NULL,'7begec'),(5,31000,NULL,'hcz2nb',NULL,'spqrgd',38.89,NULL,'fw7brb'),(5,32000,NULL,'v6ubic',NULL,'nxm_cd',63.42,NULL,'5cuirc'),(6,33000,NULL,NULL,NULL,'yutwnc',44.12,NULL,'gsxe6'),(6,34000,NULL,NULL,NULL,'5gxiib',64.24,NULL,'dpyq5c'),(6,35000,NULL,NULL,NULL,'zppxbc',68.3,NULL,'jpdlxd'),(6,36000,NULL,NULL,NULL,'cdzlfb',74.24,NULL,'9ajvec'),(8,43000,NULL,'yosmf',NULL,'ksmihd',NULL,NULL,'cormd'),(8,44000,NULL,'5sohwb',NULL,'zlv6bc',12.46,NULL,NULL),(8,45000,NULL,'r_3m9c',NULL,'ggodad',90.89,NULL,NULL),(8,46000,NULL,'lnsdr',NULL,'sxqybd',78.84,NULL,'eylied'),(8,47000,NULL,'2my8qd',NULL,'iuokj',84.9,NULL,'pl9czd'),(9,48000,NULL,'fpexk',NULL,'r3xngb',83.51,NULL,'lkierc'),(9,49000,NULL,'crbnt',NULL,'hpamu',2147483648.1,NULL,'rurs7b'),(9,50000,NULL,'g3nkvd',NULL,'urkf8b',34.67,NULL,'qjacz'),(9,51000,NULL,'1g5rqc',NULL,'yp1swd',89.37,NULL,'d9yp3c'),(9,52000,NULL,NULL,NULL,NULL,NULL,NULL,'2lpdu'),(9,53000,NULL,'fsk1pd',NULL,'x11ald',83.6,NULL,'nc8uvb'),(10,54000,NULL,'qkdfi',NULL,NULL,70.64,NULL,'vfi7s'),(10,55000,NULL,'t0lod',NULL,NULL,92.86,NULL,'hqjp6b'),(10,56000,NULL,'dhxfld',NULL,NULL,43.36,NULL,'rriqkb'),(10,57000,NULL,'nhirq',NULL,NULL,23.98,NULL,'q4vt1d'),(10,58000,NULL,'hehajb',NULL,NULL,15.84,NULL,'_skjxc'),(10,59000,NULL,NULL,NULL,NULL,1.2,NULL,NULL),(10,60000,NULL,NULL,NULL,NULL,12.63,NULL,'06oajd'),(10,61000,NULL,'doev1c',NULL,NULL,59.2,NULL,'i_y4cc');
/*!40000 ALTER TABLE `t_5mspyb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_vwvgdc`
--

DROP TABLE IF EXISTS `t_vwvgdc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_vwvgdc` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_rdsfbc` double DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,
  KEY `t_8dsy1c` (`wkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_vwvgdc`
--

LOCK TABLES `t_vwvgdc` WRITE;
/*!40000 ALTER TABLE `t_vwvgdc` DISABLE KEYS */;
INSERT INTO `t_vwvgdc` VALUES (2,15000,61.75),(2,16000,NULL),(2,17000,95.36),(2,18000,53.71),(2,19000,10.16),(2,20000,16.55),(2,21000,35.24),(4,25000,27.73),(4,26000,95.33),(4,27000,37.1),(7,37000,NULL),(7,38000,NULL),(7,39000,NULL),(7,40000,NULL),(7,41000,NULL),(7,42000,NULL),(11,62000,14.7),(11,63000,32.35),(11,64000,11.35),(11,65000,36.43),(11,66000,49.99),(11,67000,48.52),(12,68000,55.13),(12,69000,42.28),(12,70000,79.2),(12,71000,20.69),(12,72000,12.85),(12,73000,62.39),(12,74000,87.72);
/*!40000 ALTER TABLE `t_vwvgdc` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-01 23:11:26
