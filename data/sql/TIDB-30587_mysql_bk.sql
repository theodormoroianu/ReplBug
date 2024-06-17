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
-- Temporary view structure for view `t_d_6mnc`
--

DROP TABLE IF EXISTS `t_d_6mnc`;
/*!50001 DROP VIEW IF EXISTS `t_d_6mnc`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `t_d_6mnc` AS SELECT 
 1 AS `c0`,
 1 AS `c1`,
 1 AS `c2`,
 1 AS `c3`,
 1 AS `c4`,
 1 AS `c5`,
 1 AS `c6`,
 1 AS `c7`,
 1 AS `c8`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `t_i9_d6`
--

DROP TABLE IF EXISTS `t_i9_d6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_i9_d6` (
  `c_yjs4e` int(11) DEFAULT NULL,
  `c_slkwlb` int(11) NOT NULL,
  PRIMARY KEY (`c_slkwlb`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_i9_d6`
--

LOCK TABLES `t_i9_d6` WRITE;
/*!40000 ALTER TABLE `t_i9_d6` DISABLE KEYS */;
INSERT INTO `t_i9_d6` VALUES (NULL,0),(24,2),(79,3),(0,6),(6,10),(63,11),(NULL,13),(85,15),(87,30),(10,36),(61,38),(40,39),(50,42),(60,44),(41,54),(NULL,55),(56,63),(21,64),(85,66),(12,78),(33,86),(38,100),(71,1850);
/*!40000 ALTER TABLE `t_i9_d6` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `t_wqimqc`
--

DROP TABLE IF EXISTS `t_wqimqc`;
/*!50001 DROP VIEW IF EXISTS `t_wqimqc`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `t_wqimqc` AS SELECT 
 1 AS `c0`,
 1 AS `c1`,
 1 AS `c2`,
 1 AS `c3`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `t_yva4kd`
--

DROP TABLE IF EXISTS `t_yva4kd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_yva4kd` (
  `c_ewsrpb` int(11) DEFAULT NULL,
  `c_14680` int(11) DEFAULT NULL,
  `c__oktod` int(11) DEFAULT NULL,
  `c_lgnyl` text DEFAULT NULL,
  `c_ymp3ib` int(11) DEFAULT NULL,
  `c_wszs1c` text DEFAULT NULL,
  `c_sjmctc` int(11) NOT NULL,
  `c_0mux4b` int(11) DEFAULT NULL,
  PRIMARY KEY (`c_sjmctc`) /*T![clustered_index] CLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_yva4kd`
--

LOCK TABLES `t_yva4kd` WRITE;
/*!40000 ALTER TABLE `t_yva4kd` DISABLE KEYS */;
INSERT INTO `t_yva4kd` VALUES (1261568,59,15,'',53,'j0qw1d',11,5),(6,0,54,'o7ihdb',22,'noquob',17,51),(NULL,7,12,'wlf6yc',47,NULL,57,3),(29,14,76,'50uq0c',49,NULL,66,29),(2,17,98,NULL,86,'39357A3068',78,12),(51,4,5,NULL,NULL,'gl14nc',90,NULL),(54,35,64,'i74pnd',1,'yhvnod',1450,1);
/*!40000 ALTER TABLE `t_yva4kd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `t_d_6mnc`
--

/*!50001 DROP VIEW IF EXISTS `t_d_6mnc`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `t_d_6mnc` (`c0`, `c1`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`) AS SELECT MAX(`subq_0`.`c3`) AS `c0`,MAX(`subq_0`.`c3`) AS `c1`,SUM(`subq_0`.`c1`) AS `c2`,MIN(NULLIF(`subq_0`.`c0`, `subq_0`.`c3`)) AS `c3`,MIN(`subq_0`.`c3`) AS `c4`,COUNT((SELECT `c2` AS `c2` FROM `testdb`.`t_wqimqc` ORDER BY `c2` LIMIT 2,1)) AS `c5`,`subq_0`.`c2` AS `c6`,COUNT(1) AS `c7`,SUM(`subq_0`.`c1`) AS `c8` FROM (SELECT (`ref_0`.`c__oktod`>>`ref_0`.`c__oktod`) AS `c0`,`ref_0`.`c__oktod` AS `c1`,`ref_0`.`c_wszs1c` AS `c2`,`ref_0`.`c_sjmctc` AS `c3`,`ref_0`.`c_sjmctc` AS `c4` FROM `testdb`.`t_yva4kd` AS `ref_0` WHERE 3 NOT IN (SELECT `ref_1`.`c_yjs4e` AS `c0` FROM `testdb`.`t_i9_d6` AS `ref_1` WHERE `ref_1`.`c_slkwlb` IS NOT NULL UNION SELECT `ref_2`.`c2` AS `c0` FROM `testdb`.`t_wqimqc` AS `ref_2` WHERE `ref_2`.`c2`<=`ref_2`.`c2`)) AS `subq_0` WHERE `subq_0`.`c0`<=`subq_0`.`c0` AND `subq_0`.`c1` BETWEEN `subq_0`.`c1` AND `subq_0`.`c1` AND `subq_0`.`c0` IS NULL GROUP BY `subq_0`.`c2` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `t_wqimqc`
--

/*!50001 DROP VIEW IF EXISTS `t_wqimqc`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `t_wqimqc` (`c0`, `c1`, `c2`, `c3`) AS SELECT COUNT(`ref_0`.`c_lgnyl`) AS `c0`,AVG(ABS(NULLIF(CASE WHEN `ref_0`.`c_sjmctc`<`ref_0`.`c_sjmctc` THEN COALESCE(50.97, NULL) ELSE 54.52 END, CASE WHEN (`ref_0`.`c_ymp3ib`>=`ref_0`.`c_14680`) OR (`ref_0`.`c_ymp3ib` IN (SELECT `ref_1`.`c_yjs4e` AS `c0` FROM `testdb`.`t_i9_d6` AS `ref_1` WHERE `ref_1`.`c_slkwlb`>`ref_1`.`c_yjs4e` WINDOW `w_p9pie` AS (PARTITION BY `ref_1`.`c_yjs4e` ORDER BY `ref_1`.`c_yjs4e` DESC))) THEN NULL ELSE 99.42 END))) AS `c1`,`ref_0`.`c_sjmctc` AS `c2`,COUNT(COALESCE(ABS(74.32), 10.79)) AS `c3` FROM `testdb`.`t_yva4kd` AS `ref_0` WHERE `ref_0`.`c_14680` IS NOT NULL GROUP BY `ref_0`.`c_sjmctc` */;
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

-- Dump completed on 2021-12-06 17:27:07
