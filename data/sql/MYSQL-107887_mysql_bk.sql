-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: testdb
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `t_b0ohxc`
--

DROP TABLE IF EXISTS `t_b0ohxc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_b0ohxc` (
  `wkey` int DEFAULT NULL,
  `pkey` int NOT NULL,
  `c_mkslo` double DEFAULT NULL,
  `c_amzxlc` text,
  `c_etye8` text,
  `c_npcctc` int DEFAULT NULL,
  `c_rrzxyc` double DEFAULT NULL,
  `c_7zch8` text,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_b0ohxc`
--

LOCK TABLES `t_b0ohxc` WRITE;
/*!40000 ALTER TABLE `t_b0ohxc` DISABLE KEYS */;
INSERT INTO `t_b0ohxc` VALUES (1,11000,68.78,'_4oysc','qojvcb',35,NULL,'sr4hv'),(1,12000,25.6,'wo1vk',NULL,79,NULL,'re_qjb'),(1,13000,79.45,'u9odkc','pxfenb',35,NULL,'u3201'),(1,14000,36.23,'vs_2vc','imhd6d',73,NULL,'e0dw0b'),(6,37000,61.76,NULL,'jpkkec',95,7.64,NULL),(6,38000,NULL,'wfbmod','f4y2ob',45,31.99,'wca7wb'),(6,39000,47.29,'i5h3jb','_k22pc',85,55.51,'tu_jb'),(6,40000,62.26,'on_ygc','o6bemb',58,26.48,'tooz0b'),(6,41000,52.66,'o_1xid','7xwzyb',68,32.9,'z5nvjc'),(10,60000,66.12,'rq_4hd','j6chx',91,82.41,NULL),(10,61000,90.41,'nkpsuc','7x3otb',5,63.8,NULL),(10,62000,72.52,'peaswb','aprrjb',9,68.6,NULL),(10,63000,1.85,'olkiyc','gysif',24,22.8,NULL),(10,64000,NULL,'se3dcc','m58pg',46,96.48,NULL),(10,65000,24.93,'00wmcd','dl9eoc',14,8.74,NULL),(12,72000,13.37,'kvq83c','yq8zj',79,NULL,NULL),(12,73000,22.58,'y8xx5d','ejvyyd',70,71.6,NULL),(12,74000,49.76,NULL,'40tje',2,19.98,NULL);
/*!40000 ALTER TABLE `t_b0ohxc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_b9lvzc`
--

DROP TABLE IF EXISTS `t_b9lvzc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_b9lvzc` (
  `wkey` int DEFAULT NULL,
  `pkey` int NOT NULL,
  `c_ujt1ud` text,
  `c_l_b6hd` text,
  `c_lszpl` int DEFAULT NULL,
  `c_1xf8oc` double DEFAULT NULL,
  `c_t41kdd` int DEFAULT NULL,
  `c_myvn4d` double DEFAULT NULL,
  PRIMARY KEY (`pkey`),
  KEY `t_zsnvpb` (`wkey`,`pkey`,`c_lszpl`,`c_1xf8oc`,`c_t41kdd`,`c_myvn4d`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_b9lvzc`
--

LOCK TABLES `t_b9lvzc` WRITE;
/*!40000 ALTER TABLE `t_b9lvzc` DISABLE KEYS */;
INSERT INTO `t_b9lvzc` VALUES (4,30000,NULL,'42au3',38,5.81,NULL,62.16),(4,31000,'nm51k','xc0m5d',31,34.66,NULL,96.51),(4,32000,'tpqod','avhfxc',49,63.64,NULL,81.38),(4,33000,'gw_zmd','cmc6sb',55,70.9,NULL,22.84),(7,42000,NULL,'muirmc',91,76.42,NULL,9.17),(7,43000,NULL,'8sf8jc',53,1.72,NULL,36.61),(7,44000,NULL,'elldqc',78,7.44,NULL,25.1),(7,45000,NULL,'eo2zjc',57,99.84,NULL,NULL),(7,46000,NULL,'cn8_cb',40,62.83,NULL,NULL),(11,66000,'3dkcbd','qxi6db',10,22.51,30,100.23),(11,67000,'qz_4zb','hf1dpc',50,75.64,73,NULL),(11,68000,'c7oldc','wegsod',29,4.65,5,27.43),(11,69000,'j4q_0c','b0t7y',57,78.22,23,54.65),(11,70000,'zwdn9d','08dqf',81,22.48,55,51.48),(11,71000,NULL,'hbbs_',39,60.87,1,58.4);
/*!40000 ALTER TABLE `t_b9lvzc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_cqieb`
--

DROP TABLE IF EXISTS `t_cqieb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_cqieb` (
  `wkey` int DEFAULT NULL,
  `pkey` int NOT NULL,
  `c_jyr9r` double DEFAULT NULL,
  `c_abru9d` int DEFAULT NULL,
  `c_ljfbec` int DEFAULT NULL,
  `c_u91c6b` int DEFAULT NULL,
  `c_8ylmeb` double DEFAULT NULL,
  `c_rejdnc` double DEFAULT NULL,
  `c_zyinj` double DEFAULT NULL,
  `c_llfuod` int DEFAULT NULL,
  `c_lda_vb` int DEFAULT NULL,
  PRIMARY KEY (`pkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_cqieb`
--

LOCK TABLES `t_cqieb` WRITE;
/*!40000 ALTER TABLE `t_cqieb` DISABLE KEYS */;
INSERT INTO `t_cqieb` VALUES (2,15000,42.63,27,85,19,NULL,NULL,54.97,25,49),(2,16000,31.55,59,90,84,NULL,NULL,50.66,87,93),(2,17000,23.2,98,21,16,NULL,NULL,59.85,84,66),(2,18000,11.81,46,7,79,NULL,NULL,68.98,47,47),(2,19000,95.31,14,71,2,NULL,NULL,33.39,50,7),(2,20000,63.37,90,50,13,NULL,NULL,15.92,8,91),(2,21000,7.5,81,34,52,NULL,NULL,46.26,14,17),(2,22000,NULL,82,65,52,NULL,NULL,51.44,23,44),(3,23000,NULL,71,7,93,9.45,76.89,NULL,99,87),(3,24000,70.78,97,12,92,34.26,63.38,68.8,30,7),(3,25000,6.34,69,62,19,8.84,41.67,64.44,54,51),(3,26000,22.75,23,52,84,19.1,NULL,NULL,35,88),(3,27000,66.45,53,24,73,2.99,88.18,78.63,7,21),(3,28000,43.32,6,32,16,94.92,5.36,53.85,61,63),(3,29000,58.99,11,88,36,NULL,60.13,71.18,34,99),(5,34000,38.56,66,46,39,32.13,69.18,98.71,86,41),(5,35000,88.28,44,28,90,39.77,66.84,12.67,76,100),(5,36000,58.65,96,9,12,62.27,17.29,2147483648.1,70,39),(8,47000,51.65,49,31,88,74.95,40.75,NULL,8,79),(8,48000,76.6,6,4,80,16.88,2147483648.1,NULL,50,43),(8,49000,18.35,92,4,52,7.59,12.63,NULL,94,40),(8,50000,59.1,27,82,38,7.3,90.74,NULL,81,75),(8,51000,NULL,88,54,49,24.62,75.2,NULL,44,44),(8,52000,50.85,68,54,49,58.59,55.84,NULL,5,6),(8,53000,34.49,55,20,10,19.37,35.59,NULL,96,66),(9,54000,NULL,4,77,8,NULL,NULL,NULL,23,50),(9,55000,NULL,48,48,44,NULL,NULL,39.65,91,65),(9,56000,NULL,58,23,85,NULL,NULL,NULL,63,85),(9,57000,NULL,89,65,86,NULL,NULL,NULL,7,45),(9,58000,NULL,29,43,30,NULL,NULL,47.66,79,62),(9,59000,NULL,93,8,86,NULL,NULL,93.1,44,59),(13,75000,90.32,95,16,96,44.26,68.44,53.35,74,67),(13,76000,37.23,85,10,100,98.99,NULL,25.8,82,8),(13,77000,75.92,59,83,31,55.31,15.89,NULL,40,68),(13,78000,9.49,39,35,11,NULL,52.68,60.82,4,68),(13,79000,NULL,87,24,1,21.39,38.37,24.47,22,92),(13,80000,99.81,49,21,57,15.22,NULL,NULL,70,84),(13,81000,96.86,68,98,86,33.98,24.4,31.39,5,6),(13,82000,44.51,20,22,59,90.67,63.3,43.95,100,75);
/*!40000 ALTER TABLE `t_cqieb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-01 10:13:29
