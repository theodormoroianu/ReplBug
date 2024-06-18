-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.25-TiDB-v6.1.0-alpha-173-g32b9c1477

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
-- Table structure for table `t_wzgyvd`
--

DROP TABLE IF EXISTS `t_wzgyvd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_wzgyvd` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_oswlic` text DEFAULT NULL,
  `c_c23g6c` int(11) DEFAULT NULL,
  `c__gkztd` double DEFAULT NULL,
  `c_pqvmnd` text DEFAULT NULL,
  `c_dm4wqb` text DEFAULT NULL,
  `c_hysvi` text DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,
  UNIQUE KEY `pkey_2` (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_wzgyvd`
--

LOCK TABLES `t_wzgyvd` WRITE;
/*!40000 ALTER TABLE `t_wzgyvd` DISABLE KEYS */;
INSERT INTO `t_wzgyvd` VALUES (2,2,'kzwf6d',25,57.5,'_dhoad','zz9vjd','3hhfy'),(2,3,'wtvncd',92,97.56,'2w211c','inpfld','caqcl'),(2,4,'oxluwc',1,73.41,'zbnuud','8zh__b','wcqsgc'),(2,5,'sjfsmd',30,93.7,'3oc_4','fuqpfc','tribdd'),(2,6,'twmlzc',27,90.7,'vi_kz','peykyd','vm9t_c'),(5,15,'eglayb',6,46.32,'_xqci','yocfd','ovjyxd'),(5,16,'djfozd',64,80.27,'lz648','7tdntc','tag10c'),(5,17,'a872gb',64,89.44,'xojujc','x7zufb',NULL),(5,18,'gtqfld',55,24.77,NULL,NULL,'zyytt'),(6,19,'7otpdc',76,60.76,'jrzczb','nxn3u','e9nvsc'),(6,20,NULL,10,44.47,'lpvz9d','q5lyk','1k0r2c'),(6,21,'taaozd',42,34.7,NULL,'v4zfgb','9tu6m'),(6,22,'mnj9ic',83,71.29,'el7xob','oxyfj','2qdsbd'),(6,23,'gdu9l',22,34.1,'lsq1sd','er_qkb','wzuc9d'),(7,24,'sbnmub',8,47.21,'meky0','byaf9b',NULL),(7,25,'ytzwkd',45,95.27,'q12c4d','8yhipd','rtjssb'),(7,26,'qxy20',82,9.47,'wdsqac','8apveb','rfjybb'),(7,27,'3sv6hd',95,68.22,'lrttx','duybnc','agr6bc'),(7,28,'hvdob',50,69.96,'0mbhx','g6moqd',NULL),(7,29,'83smk',33,23.11,'v1pfj','8d4rcc','rwclr'),(9,35,'c000cb',15,2.64,'fbjn6c','ldxk0','hg_d0d'),(9,36,'taqpt',24,32.19,'fws71','85lp1',NULL),(9,37,'lpdcrc',27,5.99,'k5rrrb','sumjnb','ky2_6c'),(9,38,'rlow7',28,74.32,'_cnklb','wi2bp','jgz3nd'),(9,39,'mibsvd',7,42.7,'kbnq0','w0i_3d','1msqd'),(9,40,'gjcz4',6,88.5,'km3qwd','lfocvb','_pmf_c'),(11,45,NULL,86,56.2,'2ioa5d','vilu_','bw8kmc');
/*!40000 ALTER TABLE `t_wzgyvd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_zb_m5`
--

DROP TABLE IF EXISTS `t_zb_m5`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_zb_m5` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_4iptac` double DEFAULT NULL,
  `c_kbcikb` double DEFAULT NULL,
  `c_mu4_e` double DEFAULT NULL,
  `c_lmpznc` double DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */,
  UNIQUE KEY `pkey_2` (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_zb_m5`
--

LOCK TABLES `t_zb_m5` WRITE;
/*!40000 ALTER TABLE `t_zb_m5` DISABLE KEYS */;
INSERT INTO `t_zb_m5` VALUES (1,1,11.93,NULL,34.94,75.17),(3,7,NULL,77.8,94.21,34.47),(3,8,15.6,59.67,79.57,97.24),(4,9,41.1,34.5,21.46,7.52),(4,10,7.98,40.55,8.4,43.28),(4,11,23.81,39.22,NULL,35.82),(4,12,NULL,25.9,60.28,81.18),(4,13,14.7,NULL,67.6,77.3),(4,14,12.18,95.62,82.44,93.33),(8,30,35.41,63.47,88.35,NULL),(8,31,83.41,84.62,63.49,39.5),(8,32,25.73,95.48,18.5,22.58),(8,33,30.8,93.46,26.97,40.14),(8,34,41.9,73.7,1.6,22.13),(10,41,29.51,22.96,3.1,5.97),(10,42,67.57,37.15,55.12,56.5),(10,43,NULL,93.72,89.86,21.77),(10,44,48.38,3.17,69.3,74.11);
/*!40000 ALTER TABLE `t_zb_m5` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-16  9:16:46
