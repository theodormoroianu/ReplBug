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
-- Table structure for table `t_davsbd`
--

DROP TABLE IF EXISTS `t_davsbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_davsbd` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_xcyuvb` int(11) DEFAULT NULL,
  `c_4pccrc` text DEFAULT NULL,
  `c_cuvggc` double DEFAULT NULL,
  `c_60x9qc` int(11) DEFAULT NULL,
  `c_agrvrd` int(11) DEFAULT NULL,
  `c_kj8rj` text DEFAULT NULL,
  `c_bldsc` int(11) DEFAULT NULL,
  `c_dvfwbc` double DEFAULT NULL,
  `c_u8gg_d` double DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_davsbd`
--

LOCK TABLES `t_davsbd` WRITE;
/*!40000 ALTER TABLE `t_davsbd` DISABLE KEYS */;
INSERT INTO `t_davsbd` VALUES
(3,25000,72,NULL,78.22,77,69,'ya99id',35,35.84,NULL),
(3,26000,45,NULL,77.45,67,77,'wjp6jc',48,53.85,37.89),
(3,27000,11,NULL,38.36,9,50,NULL,81,58.36,31.54),
(3,28000,69,NULL,38.87,5,66,'yulahb',76,92.91,6.78),
(3,29000,52,NULL,97.8,93,42,'os_tld',74,69.56,37.51),
(4,30000,55,'515f6',51.85,15,NULL,'ko4pmb',11,85.33,62.31),
(4,31000,16,'_8qpgb',75.67,100,NULL,'0sr5yd',6,32.9,27.34),
(4,32000,27,'6yy0nc',NULL,44,NULL,'tgsskd',19,94.35,62.21),
(4,33000,72,'5zuba',29.69,21,NULL,'_c6kld',7,70.61,3.93),
(5,34000,79,'hziu_b',NULL,66,16,NULL,7,68.57,47.28),
(5,35000,99,'yz4zpd',NULL,56,73,'t_zwl',35,86.13,2147483648.1),
(5,36000,93,'qnyv0c',NULL,53,22,'sutgxc',69,34.1,NULL),
(5,37000,57,NULL,NULL,16,63,'gnlbu',80,87.6,86.85),
(5,38000,98,'jpyoz',NULL,66,48,'fgvavb',42,47.3,76.15),
(5,39000,72,'xdk5k',NULL,72,70,'bxtqk',72,NULL,77.51),
(5,40000,25,NULL,NULL,19,18,'6wwpz',48,87.14,4.14),
(5,41000,76,'pqse4',NULL,23,58,'oxqzob',47,40.11,84.96),
(10,66000,88,'dwvoic',82.28,65,7,NULL,79,NULL,NULL),
(10,67000,56,'9patl',52.2,16,9,NULL,27,NULL,NULL),
(10,68000,86,'hfoytd',28.35,69,94,NULL,60,NULL,NULL),
(10,69000,98,'j9fwvd',13.8,2,73,NULL,38,NULL,NULL),
(10,70000,46,'xznjh',9.15,99,8,NULL,38,NULL,NULL),
(10,71000,55,'_9pu1',14.3,38,34,NULL,47,NULL,NULL),
(10,72000,93,'_zcxuc',81.23,59,9,NULL,40,NULL,NULL),
(11,73000,14,'xp0pv',55.93,99,88,NULL,23,6.23,NULL),
(11,74000,96,'j_ff7c',28.7,26,41,NULL,72,NULL,NULL),
(11,75000,93,'t1m7ud',69.91,43,11,NULL,86,84.12,NULL),
(11,76000,46,'79_yx',64.64,42,3,NULL,56,90.87,NULL),
(11,77000,69,'exhivc',67.14,7,27,NULL,65,11.35,NULL),
(11,78000,88,'t2kwob',40.25,100,10,NULL,57,31.25,NULL),
(11,79000,93,'7ofgu',51.7,11,21,NULL,96,21.41,NULL),
(11,80000,10,'yioc3d',26.14,37,62,NULL,53,62.51,NULL);
/*!40000 ALTER TABLE `t_davsbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_iqij_c`
--

DROP TABLE IF EXISTS `t_iqij_c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_iqij_c` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_svp9sc` int(11) DEFAULT NULL,
  `c_anyvkb` text DEFAULT NULL,
  `c_mh2cm` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`),
  UNIQUE KEY `t__vjgtc` (`wkey`,`pkey`,`c_svp9sc`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_iqij_c`
--

LOCK TABLES `t_iqij_c` WRITE;
/*!40000 ALTER TABLE `t_iqij_c` DISABLE KEYS */;
INSERT INTO `t_iqij_c` VALUES
(1,11000,85,'vcn8x',64),
(1,12000,94,NULL,5),
(1,13000,45,NULL,14),
(1,14000,26,'1xqnfb',97),
(1,15000,9,NULL,45),
(1,16000,48,'10ob0d',78),
(6,42000,46,'yoefpb',87),
(6,43000,32,'ol4rmb',61),
(6,44000,52,'pp5gx',15),
(6,45000,6,'tjojob',3),
(6,46000,87,'a8dddc',14),
(6,47000,76,'pzxs6c',77),
(6,48000,5,'esgfm',29);
/*!40000 ALTER TABLE `t_iqij_c` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_j4mbqd`
--

DROP TABLE IF EXISTS `t_j4mbqd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_j4mbqd` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_ilrr3` int(11) DEFAULT NULL,
  `c_oxaor` int(11) DEFAULT NULL,
  `c_fpoubb` text DEFAULT NULL,
  `c_9d3uzb` int(11) DEFAULT NULL,
  `c_egm4x` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_j4mbqd`
--

LOCK TABLES `t_j4mbqd` WRITE;
/*!40000 ALTER TABLE `t_j4mbqd` DISABLE KEYS */;
INSERT INTO `t_j4mbqd` VALUES
(24,17000,4,44,'zuylu',28,NULL),
(24,18000,66,45,'vb44v',4,NULL),
(24,19000,0,110,'mlg5qd',29,NULL),
(24,20000,54,77,'zpkzm',38,NULL),
(24,21000,0,44,'eosfuc',8,NULL),
(24,22000,3,5,'vgqx6d',26,NULL),
(24,23000,2,NULL,'qqyxz',44,NULL),
(24,24000,66,84,NULL,84,NULL);
/*!40000 ALTER TABLE `t_j4mbqd` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-18  9:18:08
