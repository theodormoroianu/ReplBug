-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.25-TiDB-v6.0.0

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
-- Table structure for table `t__ti1_d`
--

DROP TABLE IF EXISTS `t__ti1_d`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t__ti1_d` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_l3pcj` double DEFAULT NULL,
  `c_ksp1hc` text DEFAULT NULL,
  `c_5vhjk` double DEFAULT NULL,
  `c_azzk8c` int(11) DEFAULT NULL,
  `c_g0jc6d` int(11) DEFAULT NULL,
  `c_jqg9yd` int(11) DEFAULT NULL,
  `c__qdjic` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,
  KEY `t_bnu1bb` (`wkey`,`pkey`,`c_jqg9yd`),
  KEY `t_bl1red` (`wkey`,`c_l3pcj`,`c_5vhjk`,`c_azzk8c`,`c_g0jc6d`,`c_jqg9yd`,`c__qdjic`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t__ti1_d`
--

LOCK TABLES `t__ti1_d` WRITE;
/*!40000 ALTER TABLE `t__ti1_d` DISABLE KEYS */;
INSERT INTO `t__ti1_d` VALUES (107,130000,NULL,'_dry8b',19.798874920631782,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `t__ti1_d` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_yexe_d`
--

DROP TABLE IF EXISTS `t_yexe_d`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_yexe_d` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_px23g` text DEFAULT NULL,
  `c_qpljbb` text DEFAULT NULL,
  `c_vqpj9c` double DEFAULT NULL,
  `c_jq8xvc` text DEFAULT NULL,
  `c_krnwjd` text DEFAULT NULL,
  `c_4ufgxd` double DEFAULT NULL,
  `c_ibx81c` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_yexe_d`
--

LOCK TABLES `t_yexe_d` WRITE;
/*!40000 ALTER TABLE `t_yexe_d` DISABLE KEYS */;
INSERT INTO `t_yexe_d` VALUES (3,17000,'c3rq0b','veyde',87.91,NULL,NULL,80.89,NULL),(11,50000,'esdxsb',NULL,98.56,NULL,NULL,16.9,NULL),(14,60000,NULL,NULL,50.58,NULL,NULL,NULL,NULL),(14,61000,NULL,NULL,50.74,NULL,NULL,NULL,NULL),(142,63000,'7oo_zb',NULL,45.19,'0konkb','0konkb',45.19,63000);
/*!40000 ALTER TABLE `t_yexe_d` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-25  9:11:15
