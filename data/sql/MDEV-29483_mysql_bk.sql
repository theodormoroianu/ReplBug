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
-- Table structure for table `t_dcaic`
--

DROP TABLE IF EXISTS `t_dcaic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dcaic` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_m1_wb` text DEFAULT NULL,
  `c_gj5gcd` double DEFAULT NULL,
  `c_qg2bcc` text DEFAULT NULL,
  `c_thwocc` double DEFAULT NULL,
  `c_vwoeod` text DEFAULT NULL,
  `c_ccve4` double DEFAULT NULL,
  `c_rrm8eb` int(11) DEFAULT NULL,
  `c_setbm` double DEFAULT NULL,
  `c_tvgpob` int(11) DEFAULT NULL,
  `c_khjaq` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`),
  UNIQUE KEY `t_5hmxic` (`pkey`,`c_gj5gcd`,`c_ccve4`,`c_rrm8eb`,`c_setbm`,`c_tvgpob`,`c_khjaq`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_dcaic`
--

LOCK TABLES `t_dcaic` WRITE;
/*!40000 ALTER TABLE `t_dcaic` DISABLE KEYS */;
INSERT INTO `t_dcaic` VALUES
(5,32000,'b5hquc',71.81,'9ro_2',NULL,'kcajld',9.85,88,51.1,65,52),
(5,33000,'s_5oqc',96.5,'cqvzmb',NULL,'y_njwd',NULL,40,10.77,92,91),
(5,34000,'7hrppd',NULL,'icoyrc',32.27,NULL,76.15,15,94.64,1,77),
(5,35000,'ybdilb',60.37,'lfbfvb',17.77,'9sdgmb',8.68,4,20.16,45,6),
(6,36000,'yyerob',17.15,'avibfb',65.91,'ln4qec',81.96,100,19.96,53,43),
(6,37000,'_tf3ec',58.84,'ldn55',NULL,'6yamq',65.85,79,12.95,28,60),
(6,38000,'xieznb',82.43,'6euy3',99.6,NULL,NULL,8,28.83,85,80),
(10,54000,NULL,19.54,NULL,3.98,NULL,30.77,62,4.8,14,30),
(10,55000,'pmkp9d',72.88,'_pdv0b',47.35,NULL,74.86,85,10.98,34,85),
(10,56000,'_3jdhc',NULL,NULL,96.67,NULL,58.8,27,95.61,69,44),
(10,57000,'pxehub',89.5,'mcrvhc',2147483648.1,NULL,98.19,23,94.16,23,34);
/*!40000 ALTER TABLE `t_dcaic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_di9mld`
--

DROP TABLE IF EXISTS `t_di9mld`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_di9mld` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_5rytb` double DEFAULT NULL,
  `c__nyqnb` int(11) DEFAULT NULL,
  `c_iwk2e` text DEFAULT NULL,
  `c_4pmajc` text DEFAULT NULL,
  `c_r9a10c` text DEFAULT NULL,
  `c_0m1mlc` text DEFAULT NULL,
  `c__dk7dc` int(11) DEFAULT NULL,
  `c_gmwric` text DEFAULT NULL,
  `c_evw_ic` double DEFAULT NULL,
  PRIMARY KEY (`pkey`),
  KEY `t_35sxhc` (`wkey`,`pkey`,`c_5rytb`,`c__nyqnb`,`c__dk7dc`,`c_evw_ic`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_di9mld`
--

LOCK TABLES `t_di9mld` WRITE;
/*!40000 ALTER TABLE `t_di9mld` DISABLE KEYS */;
INSERT INTO `t_di9mld` VALUES
(1,11000,16.34,23,'phhcab',NULL,NULL,'x21w7',2,'rytb_c',55.82),
(1,12000,66.98,37,'uhn7rc',NULL,NULL,'rrpi9b',1,'i6fhvd',75.3),
(1,13000,80.22,9,'rnuot','qy8qs',NULL,'msedad',85,'l_apec',NULL),
(1,14000,76.5,42,'0yolid','8yudic',NULL,'mtdvdb',8,'waar4b',32.32),
(1,15000,59.22,35,'ynokq','wmyygb',NULL,'s0byd',76,NULL,60.14),
(1,16000,15.28,67,'6amsq','2rtrub',NULL,NULL,90,'qotmz',56.25),
(1,17000,90.9,17,'5yby4d','jtydkb',NULL,NULL,2,'ui_aad',31.38),
(2,18000,97.38,72,'_vd_8c',NULL,'e6vhvd','xkplyd',44,'tsxlvc',NULL),
(2,19000,12.1,67,'ugjgzb','ktbnnd','qoyw4d','jpbzgd',76,'d8wv4c',NULL),
(2,20000,68.49,85,'5nejmc','op_5pc','kgwpid','y9hfmb',98,'n8w_id',NULL),
(2,21000,40.16,79,'h4u9g','dlqlzb','gkwy_c',NULL,34,'hwtzdd',NULL),
(2,22000,81.7,23,NULL,NULL,'ln9rmc','wh4d7b',89,'kxygdc',NULL),
(2,23000,92.56,37,'kjw1sd','krific','tbc6wb','o54sbd',11,'yduhhd',NULL),
(2,24000,77.14,27,'bwy7mc','yi5tfd','piqlmb','_cq7f',15,'ovjnib',NULL),
(2,25000,82.41,55,NULL,'qemind','pqcku','8q66j',100,'0ut2d',NULL),
(3,26000,NULL,29,'lkeg1b','o_f8k','wpjlwc','8gfgz',26,NULL,NULL),
(3,27000,92.51,94,'rxp5hb',NULL,'9jck4d','napmgc',88,NULL,12.16),
(3,28000,75.92,11,'n5rubb','dla0c','mzhmeb','dhlvzc',15,NULL,6.24),
(4,29000,81.87,NULL,NULL,'mcbahb','bvwzwd','slexob',84,'xlu3id',NULL),
(4,30000,36.12,NULL,NULL,'xva0g',NULL,'db8zj',21,'hhiux',82.79),
(4,31000,88.32,NULL,NULL,'nw0uh',NULL,'8qgjf',77,'ouaj1b',NULL),
(7,39000,NULL,NULL,'_cmr3','rihsuc','_8v8wd','3rzvv',NULL,'bqkqcc',97.27),
(7,40000,NULL,NULL,'fjxau','ij8nkc','jce_5c','olzb8',NULL,'yfx4wc',71.88),
(7,41000,75.63,NULL,'oaade','mnfvi','omhps','k9c7o',NULL,'_i5dy',5.79),
(7,42000,13.81,NULL,'tz9s9c',NULL,'jobxt','b7_6l',NULL,'w7gyuc',84.95),
(8,43000,63.94,NULL,'k0sdzb','zyzbjb','h9trxd','wqjayb',NULL,'tnopab',NULL),
(8,44000,98.55,NULL,'shcckc','jjudud','ji1r_d',NULL,NULL,NULL,33.1),
(8,45000,30.99,NULL,NULL,'vrb7rd','6dsf2c','6f610b',NULL,'ayom8c',25.7),
(8,46000,NULL,NULL,'gdby8c','_ww_qc','xvnyfd','iysxxc',NULL,'pfkocb',21.63),
(8,47000,NULL,NULL,'byz2bd','jt3umd','quihmd','xjct8',NULL,'fjcxdd',88.96),
(9,48000,98.95,68,NULL,'j1mcic','fwvfzd','4wccm',17,NULL,90.68),
(9,49000,27.93,49,NULL,'htkrr','wzuspc','hcrasb',54,'hsagjc',93.21),
(9,50000,9.22,28,NULL,NULL,'bzfzcc','prxd1d',40,'bvi0e',69.83),
(9,51000,52.16,27,NULL,'rj0evc','rxc9r','flqltc',61,'2qapob',NULL),
(9,52000,77.84,69,NULL,'lspwx','_k37ed','qtplab',5,'owhnsc',36.33),
(9,53000,83.47,87,NULL,'dgobu',NULL,'ys4vw',79,'vdgobb',13.28),
(11,58000,20.63,NULL,'ycld_c','ohpggc','qcfhmb','77o6sc',25,'t7b6hc',30.43),
(11,59000,49.3,NULL,'sf_qsb',NULL,'k_tnr','d6uzhd',91,'h4ond',56.77),
(11,60000,19.93,NULL,'owv5nb','qpi_t','r6pjh','fosv3d',60,'ej_54c',1.54),
(11,61000,28.54,NULL,'jzhpgc','yvflkb','bl3zeb','hvlnnd',76,'pzbxxb',NULL),
(11,62000,98.4,NULL,'7s7cfd','397q9c',NULL,'_xghd',38,'lk2pa',91.51),
(11,63000,36.34,NULL,'ejq8b','klx_wb','_8e4kb','imarq',18,'le5q5b',44.35),
(12,64000,72.21,47,NULL,'ofrmrd','drydmc',NULL,87,'ralzo',NULL),
(12,65000,10.8,12,'2bmrbd',NULL,'1nvz0d',NULL,12,'t5wubd',NULL),
(12,66000,25.4,58,'st_jsd','p5ulfd','otnes',NULL,8,'spuic',NULL),
(13,67000,14.19,35,NULL,'_dq34d','rn41mc','venphc',9,'5nmf5b',42.22),
(13,68000,37.41,18,NULL,'tknw4c','46_loc','5hqikd',56,'1opkub',65.17),
(13,69000,31.5,29,NULL,'tpjkgc','cstk9b','tyefa',47,'1kgxrc',51.82),
(13,70000,49.7,55,NULL,'j0v0c','g2rgnd',NULL,66,'f4hojb',43.71),
(14,71000,50.12,5,'hbvv4','eganod','jtmlzd','gmxcbb',2,'qqboid',87.95),
(14,72000,30.66,21,'rji_3c','ftwldc','9lcv6',NULL,22,'63sfnc',41.3),
(14,73000,6.4,74,'npdu9','hlaoac','20bl5c','1vhbk',50,'71eo4b',95.1);
/*!40000 ALTER TABLE `t_di9mld` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-06 22:02:55
