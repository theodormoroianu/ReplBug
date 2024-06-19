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
-- Table structure for table `t_8vocx`
--

DROP TABLE IF EXISTS `t_8vocx`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_8vocx` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_sjd8xc` int(11) DEFAULT NULL,
  `c_zwkrwc` double DEFAULT NULL,
  `c_yh4m9d` int(11) DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_8vocx`
--

LOCK TABLES `t_8vocx` WRITE;
/*!40000 ALTER TABLE `t_8vocx` DISABLE KEYS */;
INSERT INTO `t_8vocx` VALUES (5,23000,NULL,90.72,NULL),(5,24000,NULL,NULL,NULL),(5,25000,NULL,60.42,NULL),(5,26000,NULL,95.24,NULL),(10,45000,NULL,39.8,NULL),(10,46000,NULL,4.2,NULL),(10,47000,NULL,52.69,NULL),(12,50000,NULL,NULL,NULL),(15,58000,NULL,55.38,NULL);
/*!40000 ALTER TABLE `t_8vocx` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_f70bwd`
--

DROP TABLE IF EXISTS `t_f70bwd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_f70bwd` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_2ipzoc` int(11) DEFAULT NULL,
  `c_6ehu` text DEFAULT NULL,
  `c_ssd3w` double DEFAULT NULL,
  `c_o_hxmd` text DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_f70bwd`
--

LOCK TABLES `t_f70bwd` WRITE;
/*!40000 ALTER TABLE `t_f70bwd` DISABLE KEYS */;
INSERT INTO `t_f70bwd` VALUES (2,13000,NULL,'7cdhgb',54.31,'7xfgsb'),(3,14000,NULL,'e37w_c',9.22,'oqn4md'),(3,15000,NULL,'mvkgvb',35.1,'djsqnc'),(3,16000,NULL,NULL,46.68,'znd67'),(3,17000,NULL,NULL,58.9,'4uphgc'),(3,18000,NULL,NULL,1.5,'4dyoad'),(3,19000,NULL,'a4_smb',66.62,'9z8nsb'),(18,66000,NULL,'k5kssd',NULL,NULL),(18,67000,NULL,'p_iwyd',49.9,'3_x7pb');
/*!40000 ALTER TABLE `t_f70bwd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_ux4d2b`
--

DROP TABLE IF EXISTS `t_ux4d2b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_ux4d2b` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_cqni2c` int(11) DEFAULT NULL,
  `c__k0iqd` double DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_ux4d2b`
--

LOCK TABLES `t_ux4d2b` WRITE;
/*!40000 ALTER TABLE `t_ux4d2b` DISABLE KEYS */;
INSERT INTO `t_ux4d2b` VALUES (4,20000,NULL,98.14),(4,21000,NULL,64.33),(4,22000,NULL,99.38),(8,34000,NULL,NULL),(8,35000,NULL,NULL),(8,36000,NULL,NULL),(8,37000,NULL,NULL),(8,38000,NULL,NULL),(8,39000,NULL,NULL),(11,48000,NULL,63.93),(11,49000,NULL,43.56),(13,51000,NULL,96.52),(13,52000,NULL,61.23),(13,53000,NULL,60.95),(13,54000,NULL,13.91),(13,55000,NULL,59.21);
/*!40000 ALTER TABLE `t_ux4d2b` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_xa9msd`
--

DROP TABLE IF EXISTS `t_xa9msd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_xa9msd` (
  `wkey` int(11) DEFAULT NULL,
  `pkey` int(11) NOT NULL,
  `c_g7yt1c` double DEFAULT NULL,
  `c_snku` text DEFAULT NULL,
  PRIMARY KEY (`pkey`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_xa9msd`
--

LOCK TABLES `t_xa9msd` WRITE;
/*!40000 ALTER TABLE `t_xa9msd` DISABLE KEYS */;
INSERT INTO `t_xa9msd` VALUES (1,11000,NULL,'lemywc'),(1,12000,NULL,'a0isuc'),(6,27000,NULL,'vcxe_d'),(6,28000,NULL,'l8rkub'),(6,29000,NULL,NULL),(7,30000,NULL,'djkeab'),(7,31000,37.33,'eh8wg'),(7,32000,8.96,'chzoub'),(7,33000,31.4,'vze5k'),(9,40000,NULL,NULL),(9,41000,61.9,'wa06zc'),(9,42000,12.15,'hwy2xb'),(9,43000,83.66,'fdsbmb'),(9,44000,70.36,'zjnr0d'),(14,56000,11.44,'1uwlbd'),(14,57000,35.72,NULL),(16,59000,46.2,'3n4cxc'),(16,60000,50.49,'egccjd'),(16,61000,76.62,'iaxsnc'),(16,62000,98.98,'q7pmfd'),(17,63000,91.99,'oshk_c'),(17,64000,41.5,'ngxceb'),(17,65000,8.24,'ttrrk');
/*!40000 ALTER TABLE `t_xa9msd` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-24 21:19:48
