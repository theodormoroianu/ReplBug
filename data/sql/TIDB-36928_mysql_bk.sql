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
-- Table structure for table `t_kkdrvd`
--

DROP TABLE IF EXISTS `t_kkdrvd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_kkdrvd` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c__8xz3b` text DEFAULT NULL,
  `c_4wxknd` double DEFAULT NULL,
  `c_ej6xe` double DEFAULT NULL,
  `c_ikl9s` text DEFAULT NULL,
  `c_wimsj` text DEFAULT NULL,
  `c_uv5e9c` int(11) DEFAULT NULL,
  `c_c_9yqc` text DEFAULT NULL,
  `c_w9vqqb` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_kkdrvd`
--

LOCK TABLES `t_kkdrvd` WRITE;
/*!40000 ALTER TABLE `t_kkdrvd` DISABLE KEYS */;
INSERT INTO `t_kkdrvd` VALUES (2,14000,'otljo',NULL,33.4,'xs_xhc','saydqd',NULL,'h7khr',NULL),(2,15000,'8megkc',62.26,72.25,'hop2fb','00boec',NULL,'j0e5vd',NULL),(2,16000,'cbe1q',91.93,92.71,'ggxvtd',NULL,NULL,'_h6ldd',NULL),(2,17000,'k7hgad',26.19,NULL,'6kctzd','sldkab',NULL,'tngocc',NULL),(6,35000,'d5clk',62.28,40.94,'ddgutd',NULL,NULL,'wpb2s',NULL),(6,36000,'mu7dgc',62.27,73.3,'5xfcsc',NULL,NULL,'yuqvjb',NULL),(6,37000,'jowpp',89.8,72.37,'ou9tp',NULL,NULL,'cpx88',NULL),(6,38000,'hmbg8d',93.26,35.83,'uumeg',NULL,NULL,'h5et3',NULL),(6,39000,'6gszsc',38.43,53.4,'ot2iv',NULL,NULL,'nrae7d',NULL);
/*!40000 ALTER TABLE `t_kkdrvd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_pjxdzd`
--

DROP TABLE IF EXISTS `t_pjxdzd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_pjxdzd` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_nemsqb` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_pjxdzd`
--

LOCK TABLES `t_pjxdzd` WRITE;
/*!40000 ALTER TABLE `t_pjxdzd` DISABLE KEYS */;
INSERT INTO `t_pjxdzd` VALUES (1,11000,NULL),(1,12000,NULL),(1,13000,NULL),(5,27000,NULL),(5,28000,NULL),(5,29000,NULL),(5,30000,NULL),(5,31000,NULL),(5,32000,NULL),(5,33000,NULL),(5,34000,NULL),(7,40000,NULL),(7,41000,NULL),(7,42000,NULL),(8,43000,NULL),(8,44000,NULL),(8,45000,NULL),(8,46000,NULL),(8,47000,NULL),(8,48000,NULL),(8,49000,NULL),(8,50000,NULL),(12,67000,NULL),(12,68000,NULL),(12,69000,NULL),(12,70000,NULL),(13,71000,NULL),(13,72000,NULL),(13,73000,NULL),(13,74000,NULL),(13,75000,NULL),(13,76000,NULL),(13,77000,NULL),(13,78000,NULL),(14,79000,NULL),(14,80000,NULL),(14,81000,NULL),(14,82000,NULL),(14,83000,NULL),(14,84000,NULL),(14,85000,NULL);
/*!40000 ALTER TABLE `t_pjxdzd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_uxamvc`
--

DROP TABLE IF EXISTS `t_uxamvc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_uxamvc` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_wbuaud` int(11) DEFAULT NULL,
  `c_sk7x_d` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,
  KEY `t_m42c` (`pkey`,`c_wbuaud`,`c_sk7x_d`),
  KEY `t_zfmvd` (`wkey`,`pkey`,`c_wbuaud`,`c_sk7x_d`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_uxamvc`
--

LOCK TABLES `t_uxamvc` WRITE;
/*!40000 ALTER TABLE `t_uxamvc` DISABLE KEYS */;
INSERT INTO `t_uxamvc` VALUES (3,18000,NULL,NULL),(3,19000,NULL,NULL),(3,20000,NULL,NULL),(4,21000,NULL,NULL),(4,22000,NULL,NULL),(4,23000,NULL,NULL),(4,24000,NULL,NULL),(4,25000,NULL,NULL),(4,26000,NULL,NULL),(9,51000,NULL,NULL),(9,52000,NULL,NULL),(9,53000,NULL,NULL),(9,54000,NULL,NULL),(9,55000,NULL,NULL),(10,56000,NULL,NULL),(10,57000,NULL,NULL),(10,58000,NULL,NULL),(10,59000,NULL,NULL),(10,60000,NULL,NULL),(11,61000,NULL,NULL),(11,62000,NULL,NULL),(11,63000,NULL,NULL),(11,64000,NULL,NULL),(11,65000,NULL,NULL),(11,66000,NULL,NULL),(15,86000,NULL,NULL),(15,87000,NULL,NULL),(15,88000,NULL,NULL),(15,89000,NULL,NULL),(15,90000,NULL,NULL),(15,91000,NULL,NULL),(15,92000,NULL,NULL);
/*!40000 ALTER TABLE `t_uxamvc` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-04 13:07:29
