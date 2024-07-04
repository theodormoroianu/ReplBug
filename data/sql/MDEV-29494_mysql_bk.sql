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
-- Table structure for table `t_dmvax`
--

DROP TABLE IF EXISTS `t_dmvax`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dmvax` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_72_xob` double DEFAULT NULL,
  `c_zlh1ud` text DEFAULT NULL,
  `c_xcmo8c` int(11) DEFAULT NULL,
  `c_wwyiz` int(11) DEFAULT NULL,
  `c_s7edob` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_dmvax`
--

LOCK TABLES `t_dmvax` WRITE;
/*!40000 ALTER TABLE `t_dmvax` DISABLE KEYS */;
INSERT INTO `t_dmvax` VALUES
(6,34000,83.9,'ta76fd',NULL,78,NULL),
(6,35000,NULL,'jv3vgb',NULL,32,NULL),
(6,36000,NULL,NULL,NULL,99,NULL),
(8,43000,90.44,'yh2u_',99,NULL,78),
(8,44000,69.21,'sk8djd',18,NULL,46),
(8,45000,68.48,'7yjo8',60,NULL,71),
(10,54000,79.54,'giyn0c',27,NULL,67),
(10,55000,30.1,'ylxulc',11,NULL,22),
(10,56000,23.86,'yn_sfd',42,NULL,54),
(10,57000,57.3,'q4_nqc',48,NULL,42),
(10,58000,61.26,'zvjqzd',27,NULL,46),
(10,59000,39.92,'r4ski',51,NULL,78),
(11,60000,80.95,'i4lj9d',NULL,24,18),
(11,61000,48.97,'zcoc1b',NULL,18,76),
(11,62000,12.66,'jdomob',NULL,8,99),
(11,63000,39.39,'6wc41d',NULL,27,91),
(11,64000,35.19,NULL,NULL,26,48),
(11,65000,35.61,'ioip1',NULL,86,98),
(11,66000,15.9,NULL,NULL,67,47);
/*!40000 ALTER TABLE `t_dmvax` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_esb_id`
--

DROP TABLE IF EXISTS `t_esb_id`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_esb_id` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_y3v2ud` text DEFAULT NULL,
  `c_t2zrt` text DEFAULT NULL,
  `c_fvch6` int(11) DEFAULT NULL,
  `c_jtjr_c` int(11) DEFAULT NULL,
  `c_uq1mvd` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_esb_id`
--

LOCK TABLES `t_esb_id` WRITE;
/*!40000 ALTER TABLE `t_esb_id` DISABLE KEYS */;
INSERT INTO `t_esb_id` VALUES
(1,11000,'gjjtv','s14rvb',3,54,NULL),
(1,12000,'pxkm9c',NULL,16,53,NULL),
(1,13000,'fe6c0d','izdnlc',71,11,NULL),
(1,14000,'iot45b','rkmr4c',86,38,NULL),
(2,15000,NULL,'wckpwb',34,53,67),
(2,16000,NULL,'yrhs8c',58,49,35),
(2,17000,NULL,'kitrmb',32,15,91),
(2,18000,NULL,'3za5ab',92,47,18),
(2,19000,NULL,'evzu8b',52,76,29),
(2,20000,NULL,'pwt0kb',27,78,53),
(2,21000,NULL,'wyebvd',32,69,97),
(3,22000,'uzru9','tvuxsb',34,48,3),
(3,23000,'nunfmc',NULL,23,23,13),
(3,24000,'pcv7w','sqdezd',94,47,51),
(3,25000,'1iefuc',NULL,60,75,100),
(4,26000,NULL,'r2s6cb',19,63,99),
(4,27000,NULL,'v1yokd',73,71,78),
(4,28000,NULL,'wnkh_d',87,46,11),
(5,29000,NULL,'glhoh',NULL,33,89),
(5,30000,NULL,'ixnvgd',NULL,62,15),
(5,31000,NULL,'txd8ub',NULL,63,1),
(5,32000,NULL,'v3l_cb',NULL,40,73),
(5,33000,NULL,'gitx0d',NULL,42,40),
(7,37000,NULL,'r5ddyc',57,65,96),
(7,38000,NULL,'4li_ab',100,42,71),
(7,39000,NULL,'cewbfd',63,18,24),
(7,40000,NULL,'ko9pb',80,61,84),
(7,41000,NULL,NULL,71,67,37),
(7,42000,NULL,'u95kz',86,35,95),
(9,46000,NULL,NULL,26,NULL,81),
(9,47000,NULL,NULL,41,NULL,51),
(9,48000,NULL,NULL,48,NULL,65),
(9,49000,NULL,NULL,72,NULL,82),
(9,50000,NULL,NULL,23,NULL,35),
(9,51000,NULL,NULL,88,NULL,26),
(9,52000,NULL,NULL,75,NULL,80),
(9,53000,NULL,NULL,47,NULL,13),
(12,67000,'wr78bd','he339c',38,NULL,54),
(12,68000,'n8djb','j82bv',45,NULL,48),
(12,69000,'ezlvc','3i0j1b',17,NULL,2),
(12,70000,'2ikhyc','n1x0o',67,NULL,29),
(13,71000,NULL,NULL,NULL,81,8),
(13,72000,NULL,'fgwjdd',NULL,42,75),
(13,73000,NULL,'gx93gd',NULL,27,35),
(13,74000,NULL,'yc4ouc',NULL,99,71),
(13,75000,NULL,'mfyumb',NULL,20,71),
(13,76000,NULL,'qwqeic',NULL,15,97),
(13,77000,NULL,'ek6gec',NULL,86,73),
(14,78000,'h6rfrc','cfubq',NULL,NULL,34),
(14,79000,'k3dzbd',NULL,NULL,NULL,50),
(14,80000,'njjry','js8rac',NULL,NULL,76),
(15,81000,'u1i1jd','foj9yc',55,4,NULL),
(15,82000,'3vtvxd','segeac',39,26,NULL),
(15,83000,'philtc','qdqlw',97,70,NULL),
(15,84000,'_z1zjb','9gppfd',75,44,NULL),
(15,85000,NULL,'rtg5',87,34,NULL);
/*!40000 ALTER TABLE `t_esb_id` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-07 15:15:41
