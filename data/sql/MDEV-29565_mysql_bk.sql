-- MariaDB dump 10.19  Distrib 10.10.1-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	10.10.1-MariaDB-debug

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
-- Table structure for table `t_g6ckkb`
--

DROP TABLE IF EXISTS `t_g6ckkb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_g6ckkb` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_onz_dc` int(11) DEFAULT NULL,
  `c_fzhuoc` text DEFAULT NULL,
  `c_qlbh3` text DEFAULT NULL,
  `c_uns3yc` double DEFAULT NULL,
  `c_caz5t` text DEFAULT NULL,
  `c_y6oqed` text DEFAULT NULL,
  `c_g99d4d` double DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_g6ckkb`
--

LOCK TABLES `t_g6ckkb` WRITE;
/*!40000 ALTER TABLE `t_g6ckkb` DISABLE KEYS */;
INSERT INTO `t_g6ckkb` VALUES
(20,234000,NULL,'aarauc','btldnb',37.9,'7wa_b',NULL,32.5),
(56,327000,65,'kavsib','ga9slb',54.9,NULL,'xlbvfd',79.9);
/*!40000 ALTER TABLE `t_g6ckkb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_rpjlsd`
--

DROP TABLE IF EXISTS `t_rpjlsd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_rpjlsd` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_trycnb` int(11) DEFAULT NULL,
  `c_5b3h_c` text DEFAULT NULL,
  `c_pfd8ab` int(11) DEFAULT NULL,
  `c_mvgo1c` text DEFAULT NULL,
  `c_2twe2d` int(11) DEFAULT NULL,
  `c_nmcpzc` int(11) DEFAULT NULL,
  `c_loj6e` text DEFAULT NULL,
  `c_veoe1` double DEFAULT NULL,
  PRIMARY KEY (`pkey`),
  UNIQUE KEY `t_hm3u4b` (`wkey`,`pkey`,`c_trycnb`,`c_pfd8ab`,`c_2twe2d`,`c_nmcpzc`,`c_veoe1`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_rpjlsd`
--

LOCK TABLES `t_rpjlsd` WRITE;
/*!40000 ALTER TABLE `t_rpjlsd` DISABLE KEYS */;
INSERT INTO `t_rpjlsd` VALUES
(43,243000,30,NULL,8,NULL,70,NULL,'awnrab',39.83),
(57,332000,68,'_pqr1c',53,'9g7bt',NULL,75,'tb1ugc',7.62);
/*!40000 ALTER TABLE `t_rpjlsd` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-16 21:17:33
