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
-- Table structure for table `t_8fjoxb`
--

DROP TABLE IF EXISTS `t_8fjoxb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_8fjoxb` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_yecif` text DEFAULT NULL,
  PRIMARY KEY (`pkey`),
  UNIQUE KEY `t_jioqrc` (`wkey`,`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_8fjoxb`
--

LOCK TABLES `t_8fjoxb` WRITE;
/*!40000 ALTER TABLE `t_8fjoxb` DISABLE KEYS */;
INSERT INTO `t_8fjoxb` VALUES
(2,17000,'72v9kd'),
(2,18000,'qnwwyd'),
(2,19000,NULL),
(2,20000,NULL),
(2,21000,'ypl5qd'),
(2,22000,'r_yb_b'),
(2,23000,'8ldecc'),
(5,35000,'275x9c'),
(5,36000,'mpwkw'),
(5,37000,'ectg3'),
(5,38000,'tc_wqb'),
(5,39000,'skrhrd'),
(5,40000,'mc1fcb'),
(5,41000,'3ckgid'),
(5,42000,'qixcqb'),
(6,43000,'rehhmc'),
(6,44000,NULL),
(6,45000,NULL),
(6,46000,'zhhau'),
(6,47000,'d0wpu'),
(6,48000,'axge2c'),
(6,49000,'5prsyb'),
(7,50000,'gjdrb'),
(7,51000,'feev2'),
(7,52000,'xniawd'),
(7,53000,'zo5agc'),
(10,65000,NULL),
(10,66000,'x1xi9d'),
(10,67000,'cg9fi'),
(10,68000,'q6dcw'),
(10,69000,'orvb2d'),
(11,70000,'kz0qy'),
(11,71000,'b3doad'),
(11,72000,'qpenm'),
(11,73000,'zfs7gb'),
(11,74000,'sozgcc'),
(11,75000,'hwsiu');
/*!40000 ALTER TABLE `t_8fjoxb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_swbayb`
--

DROP TABLE IF EXISTS `t_swbayb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_swbayb` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_ywdp4d` text DEFAULT NULL,
  PRIMARY KEY (`pkey`),
  KEY `t_nbmaqb` (`wkey`,`pkey`),
  KEY `t_qo4xpb` (`wkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_swbayb`
--

LOCK TABLES `t_swbayb` WRITE;
/*!40000 ALTER TABLE `t_swbayb` DISABLE KEYS */;
INSERT INTO `t_swbayb` VALUES
(1,11000,'jfey0'),
(1,12000,'ueyevd'),
(1,13000,'opnhw'),
(1,14000,'xhwosb'),
(1,15000,'anhfmb'),
(1,16000,'ibzdk'),
(3,24000,'nqtskc'),
(3,25000,'cj_tk'),
(3,26000,'jsa_j'),
(3,27000,'_bgt3b'),
(3,28000,'aeqcnc'),
(3,29000,'krnsh'),
(3,30000,'i9whpc'),
(4,31000,'l9c9u'),
(4,32000,'uoo9h'),
(4,33000,'7tzuk'),
(4,34000,'j_lifc'),
(8,54000,NULL),
(8,55000,NULL),
(8,56000,NULL),
(8,57000,NULL),
(9,58000,NULL),
(9,59000,NULL),
(9,60000,NULL),
(9,61000,NULL),
(9,62000,NULL),
(9,63000,NULL),
(9,64000,NULL);
/*!40000 ALTER TABLE `t_swbayb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-03 15:22:44
