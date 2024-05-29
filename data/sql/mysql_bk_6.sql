-- MariaDB dump 10.19  Distrib 10.8.3-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	10.8.3-MariaDB-debug

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_qrsdpb`
--

DROP TABLE IF EXISTS `t_qrsdpb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_qrsdpb` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_hhsy0b` int(11) DEFAULT NULL,
  `c_bwdaw` double DEFAULT NULL,
  `c_e5jxgb` double DEFAULT NULL,
  PRIMARY KEY (`pkey`),
  KEY `t_x6dij` (`wkey`,`pkey`,`c_bwdaw`,`c_e5jxgb`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_qrsdpb`
--

LOCK TABLES `t_qrsdpb` WRITE;
/*!40000 ALTER TABLE `t_qrsdpb` DISABLE KEYS */;
INSERT INTO `t_qrsdpb` VALUES
(1,11000,71,NULL,NULL),
(1,12000,79,NULL,NULL),
(1,13000,8,NULL,NULL),
(1,14000,63,NULL,NULL),
(4,29000,47,27.25,38.21),
(4,30000,10,73.14,8.5),
(4,31000,51,9.3,13.15),
(4,32000,31,20.77,72.93),
(4,33000,38,53.89,NULL),
(4,34000,32,17.69,67.11),
(4,35000,37,9.14,9.49),
(5,36000,23,1.58,49.3),
(5,37000,51,18.53,78.7),
(5,38000,23,80.57,27.3),
(5,39000,60,32.94,89.29),
(5,40000,27,NULL,51.53),
(8,56000,83,78.2,20.53),
(8,57000,31,27.4,72.73),
(8,58000,66,39.9,34.6),
(12,76000,13,97.39,NULL),
(12,77000,67,17.62,73.49),
(12,78000,26,NULL,24.18),
(12,79000,62,44.9,91.87),
(12,80000,96,45.46,4.27),
(12,81000,89,12.26,73.14),
(12,82000,69,67.2,71.1),
(12,83000,57,54.61,92.66);
/*!40000 ALTER TABLE `t_qrsdpb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_yynypc`
--

DROP TABLE IF EXISTS `t_yynypc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_yynypc` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_acfajc` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_yynypc`
--

LOCK TABLES `t_yynypc` WRITE;
/*!40000 ALTER TABLE `t_yynypc` DISABLE KEYS */;
INSERT INTO `t_yynypc` VALUES
(2,15000,89),
(2,16000,17),
(2,17000,9),
(2,18000,10),
(2,19000,87),
(2,20000,67),
(3,21000,85),
(3,22000,92),
(3,23000,68),
(3,24000,78),
(3,25000,35),
(3,26000,60),
(3,27000,30),
(3,28000,12),
(6,41000,64),
(6,42000,35),
(6,43000,4),
(6,44000,23),
(6,45000,31),
(6,46000,87),
(6,47000,21),
(9,59000,30),
(9,60000,3),
(9,61000,27),
(9,62000,30),
(9,63000,55),
(9,64000,56),
(9,65000,24),
(9,66000,18),
(11,73000,30),
(11,74000,87),
(11,75000,98);
/*!40000 ALTER TABLE `t_yynypc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_zefkic`
--

DROP TABLE IF EXISTS `t_zefkic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_zefkic` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_kkpzcd` text DEFAULT NULL,
  `c_gov3_` text DEFAULT NULL,
  `c_bkmkf` text DEFAULT NULL,
  `c_cjydxb` double DEFAULT NULL,
  `c_48luqd` int(11) DEFAULT NULL,
  `c_k0ztk` text DEFAULT NULL,
  `c_so8a2b` double DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_zefkic`
--

LOCK TABLES `t_zefkic` WRITE;
/*!40000 ALTER TABLE `t_zefkic` DISABLE KEYS */;
INSERT INTO `t_zefkic` VALUES
(7,48000,'zbqsyc','zlatwc','3mhst',82.61,24,'ogsl',NULL),
(7,49000,NULL,'op1wkb','_rfivd',72.37,83,'8bs1lb',NULL),
(7,50000,'4_lidb','azxxsd','ojpd4b',18.1,93,'36toec',NULL),
(7,51000,'hypmf','dboevb','dib0',NULL,30,'6nbm6',NULL),
(7,52000,'tsc2k','xuimcb','hnm96d',5.18,88,NULL,NULL),
(7,53000,'emvzed','5hrinc','ke2h9c',30.8,46,NULL,NULL),
(7,54000,'yhlnac',NULL,'ngwsod',38.15,19,'ccamn',NULL),
(7,55000,'ozo19d','pwoded','ku5ew',43.24,18,'lqnm6',NULL),
(10,67000,NULL,NULL,'iokrfc',31.35,53,'4alvxc',NULL),
(10,68000,'rzqelb',NULL,'hcckab',73.7,56,'nreja',NULL),
(10,69000,'unak9c',NULL,'awfbp',13.89,28,'pyzkwb',NULL),
(10,70000,'kydgec',NULL,'gay_b',64.23,55,'emzm2d',NULL),
(10,71000,'skn74d',NULL,'u3pod',10.32,42,'l43lq',NULL),
(10,72000,'cjyied',NULL,'5edq0b',46.1,42,'9o0hed',NULL);
/*!40000 ALTER TABLE `t_zefkic` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-14  1:25:45
