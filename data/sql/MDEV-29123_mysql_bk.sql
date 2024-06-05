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
-- Table structure for table `t_0w18nc`
--

DROP TABLE IF EXISTS `t_0w18nc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_0w18nc` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_yt72zb` int(11) DEFAULT NULL,
  `c_i_flqc` text DEFAULT NULL,
  `c_ysip6d` text DEFAULT NULL,
  `c__rw_jb` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`),
  UNIQUE KEY `t_afv3ab` (`pkey`),
  KEY `t_bu6w8d` (`wkey`,`pkey`,`c_yt72zb`,`c__rw_jb`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_0w18nc`
--

LOCK TABLES `t_0w18nc` WRITE;
/*!40000 ALTER TABLE `t_0w18nc` DISABLE KEYS */;
INSERT INTO `t_0w18nc` VALUES
(2,19000,75,'ejcpjd','60hbec',NULL),
(2,20000,92,'wkm2sc','mmdc7d',NULL),
(2,21000,85,'zcpjdb','lmulu',NULL),
(2,22000,18,'_3_bsb','iynhec',NULL),
(2,23000,38,'zjj53c','o1y6ec',NULL),
(2,24000,46,'bpczfb',NULL,NULL),
(2,25000,12,'l3s7cb','ek2djd',NULL),
(2,26000,23,'a8s_ad',NULL,NULL),
(8,52000,NULL,NULL,'v5xswc',62),
(8,53000,NULL,'c1pond','mv1m8d',42),
(8,54000,NULL,NULL,'qiwbd',48),
(8,55000,NULL,'quud_','xpn1_',76),
(8,56000,NULL,'lss6oc','8v8xkc',38),
(8,57000,NULL,'aqsno','wmgye',53),
(10,65000,16,'mx16lc','u084hb',24),
(10,66000,26,'eoyr3c',NULL,4),
(10,67000,5,'it5rtd','wlmvkb',82),
(10,68000,71,'jpsth','qvekw',55),
(10,69000,10,'xqxqsd',NULL,18),
(11,70000,74,'icmnyd','by3xfc',78),
(11,71000,24,'qumx2','nl8z2',58),
(11,72000,77,'wxjykc','j91ky',8),
(13,77000,60,'paxgnd','jsl5',NULL),
(13,78000,99,'ukxv8','rjlimc',NULL),
(13,79000,21,'yclfbc',NULL,NULL),
(13,80000,33,'en6hid','shu01b',NULL),
(13,81000,20,'syfifc','p_gk6',NULL),
(13,82000,51,'jmicgd',NULL,NULL);
/*!40000 ALTER TABLE `t_0w18nc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_4rbssc`
--

DROP TABLE IF EXISTS `t_4rbssc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_4rbssc` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_umaal` text DEFAULT NULL,
  `c_qrgwb` text DEFAULT NULL,
  `c_wzm9wc` int(11) DEFAULT NULL,
  `c_8u7ipc` double DEFAULT NULL,
  `c_mqgwfb` int(11) DEFAULT NULL,
  `c_sbxs3c` int(11) DEFAULT NULL,
  `c_kkizw` text DEFAULT NULL,
  `c_7j_zjb` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_4rbssc`
--

LOCK TABLES `t_4rbssc` WRITE;
/*!40000 ALTER TABLE `t_4rbssc` DISABLE KEYS */;
INSERT INTO `t_4rbssc` VALUES
(3,27000,'vbaf_b',NULL,51,15.8,53,NULL,NULL,18),
(3,28000,'zvemlb',NULL,26,1.45,77,NULL,NULL,85),
(3,29000,'mn8zid',NULL,20,2.97,33,NULL,NULL,14),
(3,30000,NULL,NULL,61,97.85,55,NULL,NULL,33),
(3,31000,NULL,NULL,25,31.81,13,NULL,NULL,17),
(3,32000,'m2ygwd',NULL,42,NULL,14,NULL,NULL,40),
(3,33000,'zpct_',NULL,89,26.12,26,NULL,NULL,55),
(4,34000,'4bquu','entwob',87,84.64,93,5,'glalkc',47),
(4,35000,'2w5lsc',NULL,6,42.97,86,1,'evgzfc',77),
(4,36000,'_wacsb','3_7us',100,91.97,77,51,'mf8txb',79),
(4,37000,'obkbfb','ku0pmd',74,97.73,47,41,NULL,19),
(4,38000,'yzdmqb','sfxi_c',66,22.93,79,96,'xjkqb',56),
(5,39000,'svncqc','x9lbjb',NULL,NULL,NULL,NULL,'cmelcb',100),
(5,40000,'p5ehvd','gfk5jd',NULL,77.27,NULL,NULL,'z0oy5c',87),
(5,41000,'gr6lkb','ikaxgb',NULL,NULL,NULL,NULL,'7hcrgc',62),
(5,42000,'9bzwnb','noxkqb',NULL,58.73,NULL,NULL,'gh3bvc',49),
(5,43000,'fjr0qb','cfdwgc',NULL,75.31,NULL,NULL,'54mc_d',86),
(9,58000,'aufhb','pklph',NULL,NULL,NULL,87,'mehz7d',57),
(9,59000,'ukdszc',NULL,NULL,NULL,NULL,48,NULL,46),
(9,60000,'tk4qsb','klkjp',NULL,NULL,NULL,60,'q9qcd',6),
(9,61000,'ovt4vc','lrv7gd',NULL,NULL,NULL,35,NULL,7),
(9,62000,'lrp7a','oyt5n',NULL,NULL,NULL,59,'wepgod',51),
(9,63000,'wvvd9b','q9lupc',NULL,NULL,NULL,4,'sy5icd',43),
(9,64000,'o_ermc','jmhnad',NULL,NULL,NULL,81,'vatd7d',57),
(12,73000,'ghijhc',NULL,38,NULL,88,10,NULL,23),
(12,74000,'1mtvgc',NULL,17,NULL,54,37,'fmfmzc',42),
(12,75000,NULL,NULL,81,NULL,84,15,'whfc8d',9),
(12,76000,'3wxi9d',NULL,10,NULL,69,26,'06azlb',49);
/*!40000 ALTER TABLE `t_4rbssc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t__w2gab`
--

DROP TABLE IF EXISTS `t__w2gab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t__w2gab` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_ntsmbb` text DEFAULT NULL,
  `c_gt5hk` text DEFAULT NULL,
  `c_sjxrx` text DEFAULT NULL,
  `c_lba4ac` double DEFAULT NULL,
  `c_79u9mc` double DEFAULT NULL,
  `c_baxlp` int(11) DEFAULT NULL,
  `c_ckip3c` text DEFAULT NULL,
  `c_stq_eb` double DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t__w2gab`
--

LOCK TABLES `t__w2gab` WRITE;
/*!40000 ALTER TABLE `t__w2gab` DISABLE KEYS */;
INSERT INTO `t__w2gab` VALUES
(1,11000,NULL,'ymhvbc',NULL,40.81,71.83,NULL,'bwsy_b',48.32),
(1,12000,NULL,'9apidc',NULL,NULL,87.3,NULL,'bwbmz',96.72),
(1,13000,NULL,'ebszkd',NULL,2147483648.1,10.26,NULL,'rzack',79.77),
(1,14000,NULL,'jdw4db',NULL,59.48,67.29,NULL,'ad5f8d',5.14),
(1,15000,NULL,'lprka',NULL,59.32,36.57,NULL,'jzjied',31.65),
(1,16000,NULL,'tl6b9c',NULL,70.46,85.26,NULL,NULL,33.42),
(1,17000,NULL,'ipcgb',NULL,3.59,72.92,NULL,'fayt2b',25.67),
(1,18000,NULL,'tmlkgd',NULL,37.64,78.8,NULL,'ryd2rd',94.17),
(6,44000,'j2nim','c5qcjd','ubeb1b',98.54,96.85,1,'glc_d',75.17),
(6,45000,'1nt3xd','odxgsb','mc0y9',64.86,28.99,39,'xfm2fc',73.88),
(6,46000,'uafrsb',NULL,'5v3lic',NULL,NULL,15,'3t_bg',38.12),
(6,47000,'uwsxsc','ngfywd','af12rb',47.74,86.4,24,'rxme8b',37.43),
(6,48000,'kwrmr','wgb5cc','sjuqhc',66.2,55.63,2,NULL,97.39),
(7,49000,'2njzac','emjut',NULL,24.82,60.5,52,'i5dilc',33.39),
(7,50000,'hiblxb','etjzyd',NULL,59.91,58.16,89,'3iwybb',33.52),
(7,51000,'w_mgob',NULL,NULL,69.26,72.15,94,'dxbeub',NULL),
(14,83000,'tu0x_','4xfdnb','7xzpvd',45.91,NULL,NULL,'6w1ngd',60.67),
(14,84000,'zq5pvc','mtg3_b','u7qhzd',53.96,NULL,NULL,'au1kpc',91.4),
(14,85000,'8tgkud','mxidgc','vv9mrd',63.4,NULL,NULL,'kkwzzc',64.93),
(14,86000,'sn_hoc','07bak','o7xnwd',19.55,NULL,NULL,'vl0dbb',87.65),
(14,87000,'n4hyx','3desx','q_wem',72.75,NULL,NULL,'gyrqcc',NULL),
(15,88000,'nr6k9','cmyid','n9g3b',13.11,67.18,NULL,NULL,60.83),
(15,89000,'lay_tb','6ycncb','spcqvc',7.5,64.83,NULL,NULL,60.98),
(15,90000,'7zolab','iaz8rc','uklyfd',97.79,80.44,NULL,NULL,98.75),
(15,91000,'fxigec','d4bstc','wummmd',69.2,84.87,NULL,NULL,52.18),
(15,92000,'o_cqib','j6fr4d','tg9esc',12.93,60.2,NULL,NULL,23.87);
/*!40000 ALTER TABLE `t__w2gab` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-14  8:13:17
