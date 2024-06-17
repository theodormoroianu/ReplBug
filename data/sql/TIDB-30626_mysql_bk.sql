-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.25-TiDB-v5.4.0-alpha-311-g28446605c

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
-- Table structure for table `t__zzgcb`
--

DROP TABLE IF EXISTS `t__zzgcb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t__zzgcb` (
  `c_pixrzd` int(11) DEFAULT NULL,
  `c_g94v4` text DEFAULT NULL,
  `c_sotqsb` text DEFAULT NULL,
  `c_q4ltzb` double DEFAULT NULL,
  `c_sopgjc` int(11) DEFAULT NULL,
  `c_firz0c` double DEFAULT NULL,
  `c_wirxeb` int(11) NOT NULL,
  `c_uh3kbc` text DEFAULT NULL,
  PRIMARY KEY (`c_wirxeb`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t__zzgcb`
--

LOCK TABLES `t__zzgcb` WRITE;
/*!40000 ALTER TABLE `t__zzgcb` DISABLE KEYS */;
INSERT INTO `t__zzgcb` VALUES (41,'zxhkrc','hxwaed',7.49,42,21.52,11,'yi2b_d'),(44,'yr4ig','prfbpb',7.81,53,87.99,18,'p5x4pb'),(88,NULL,'9vejob',56.61,63,14.32,118,'dvbvtd');
/*!40000 ALTER TABLE `t__zzgcb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_cvooz`
--

DROP TABLE IF EXISTS `t_cvooz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_cvooz` (
  `c_y1xhad` int(11) NOT NULL,
  `c_gumvcc` int(11) DEFAULT NULL,
  `c_de25i` double DEFAULT NULL,
  `c_ndiwtc` int(11) NOT NULL,
  `c_v0sp5b` int(11) DEFAULT NULL,
  PRIMARY KEY (`c_ndiwtc`,`c_y1xhad`) /*T![clustered_index] NONCLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_cvooz`
--

LOCK TABLES `t_cvooz` WRITE;
/*!40000 ALTER TABLE `t_cvooz` DISABLE KEYS */;
INSERT INTO `t_cvooz` VALUES (87,36,15.13,52,4),(32,34,16.59,10,83),(95,65,38.64,54,100),(16,23,21.11,97,56),(11,53,18.92,82,63),(45,4,82.14,36,1040),(14,21,16.73,65,30),(0,53,NULL,6,32),(39,22,93.51,24,12),(0,NULL,84.63,4,0),(0,43,6.1,60,70),(82,9,13.79,5,83),(25,41,45.47,82,18),(97,104,72.83,20,0),(20,76,85.73,57,74),(79,87,6.2,14,15),(29,92,NULL,82,22),(11,58,75.99,0,81),(0,33,34.28,50,26),(64,64,NULL,21,62),(78,81,11.78,50,49),(23,64,52.47,90,52),(40,56,57.86,47,71),(3145728,96,55.4,75,6),(39,84,4.63,33,13),(66,76,4.31,66,20),(0,0,NULL,49,2686976),(75,72,95.56,7482,37),(10,12495,51.59,68,17);
/*!40000 ALTER TABLE `t_cvooz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `t_ljlaub`
--

DROP TABLE IF EXISTS `t_ljlaub`;
/*!50001 DROP VIEW IF EXISTS `t_ljlaub`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `t_ljlaub` AS SELECT 
 1 AS `c0`,
 1 AS `c2`,
 1 AS `c3`,
 1 AS `c4`,
 1 AS `c5`,
 1 AS `c6`,
 1 AS `c7`,
 1 AS `c8`,
 1 AS `c9`,
 1 AS `c10`,
 1 AS `c11`,
 1 AS `c12`,
 1 AS `c13`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `t_ljlaub`
--

/*!50001 DROP VIEW IF EXISTS `t_ljlaub`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `t_ljlaub` (`c0`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c10`, `c11`, `c12`, `c13`) AS SELECT DISTINCT `subq_0`.`c5` AS `c0`,`subq_0`.`c1` AS `c2`,`subq_0`.`c3` AS `c3`,`subq_0`.`c1` AS `c4`,`subq_0`.`c3` AS `c5`,`subq_0`.`c5` AS `c6`,CASE WHEN CASE WHEN EXISTS (SELECT DISTINCT `ref_4`.`c_de25i` AS `c0`,`ref_4`.`c_ndiwtc` AS `c1`,`ref_4`.`c_ndiwtc` AS `c2`,`ref_4`.`c_gumvcc` AS `c3` FROM `testdb`.`t_cvooz` AS `ref_4` WHERE 52>`ref_4`.`c_ndiwtc`) THEN `subq_0`.`c6` ELSE `subq_0`.`c0` END IS NOT NULL THEN `subq_0`.`c2` ELSE CASE WHEN MAX(`subq_0`.`c6`) OVER (PARTITION BY `subq_0`.`c1`, `subq_0`.`c3` ORDER BY `subq_0`.`c6`,`subq_0`.`c0`)=67 THEN 68.76 ELSE `subq_0`.`c1` END END AS `c7`,LAST_VALUE(`subq_0`.`c2`) OVER `w_bfobxb` AS `c8`,`subq_0`.`c4` AS `c9`,ABS(`subq_0`.`c1`) AS `c10`,`subq_0`.`c2` AS `c11`,`subq_0`.`c3` AS `c12`,`subq_0`.`c4` AS `c13` FROM (SELECT `ref_0`.`c_y1xhad` AS `c0`,`ref_0`.`c_de25i` AS `c1`,`ref_0`.`c_de25i` AS `c2`,LENGTH(_UTF8MB4'l8hyfd') AS `c3`,`ref_0`.`c_de25i` AS `c4`,`ref_0`.`c_v0sp5b` AS `c5`,`ref_0`.`c_gumvcc` AS `c6` FROM `testdb`.`t_cvooz` AS `ref_0` WHERE `ref_0`.`c_v0sp5b`<=`ref_0`.`c_gumvcc` ORDER BY `c0`,`c1`,`c2`,`c3`,`c4`,-`c5`,`c6`) AS `subq_0` WHERE 74!=(SELECT `ref_1`.`c_y1xhad` AS `c0` FROM `testdb`.`t_cvooz` AS `ref_1` WHERE `subq_0`.`c3`=`ref_1`.`c_v0sp5b` AND `ref_1`.`c_de25i`!=(SELECT `subq_0`.`c4` AS `c0` FROM `testdb`.`t_cvooz` AS `ref_2` WHERE `ref_2`.`c_y1xhad` BETWEEN `ref_1`.`c_gumvcc` AND `ref_1`.`c_gumvcc`) AND ((`ref_1`.`c_v0sp5b`=41) OR (0!=0)) AND (0!=0) UNION SELECT `ref_3`.`c_gumvcc` AS `c0` FROM `testdb`.`t_cvooz` AS `ref_3` WHERE `ref_3`.`c_gumvcc` BETWEEN `subq_0`.`c0` AND `subq_0`.`c0`) WINDOW `w_bfobxb` AS (PARTITION BY `subq_0`.`c0`, `subq_0`.`c4` ORDER BY `subq_0`.`c2`,`subq_0`.`c5` DESC) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-06 17:34:26