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
-- Temporary view structure for view `t_f32hfd`
--

DROP TABLE IF EXISTS `t_f32hfd`;
/*!50001 DROP VIEW IF EXISTS `t_f32hfd`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `t_f32hfd` AS SELECT 
 1 AS `c0`,
 1 AS `c1`,
 1 AS `c2`,
 1 AS `c3`,
 1 AS `c4`,
 1 AS `c5`,
 1 AS `c7`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `t_rxrf9c`
--

DROP TABLE IF EXISTS `t_rxrf9c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_rxrf9c` (
  `c_u3bwg` int(11) NOT NULL,
  `c_a_p8b` int(11) DEFAULT NULL,
  `c_09ew1d` double NOT NULL,
  `c_wylqr` int(11) DEFAULT NULL,
  PRIMARY KEY (`c_09ew1d`,`c_u3bwg`) /*T![clustered_index] NONCLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_rxrf9c`
--

LOCK TABLES `t_rxrf9c` WRITE;
/*!40000 ALTER TABLE `t_rxrf9c` DISABLE KEYS */;
INSERT INTO `t_rxrf9c` VALUES (6,24,53.56,59);
/*!40000 ALTER TABLE `t_rxrf9c` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_xkzvqb`
--

DROP TABLE IF EXISTS `t_xkzvqb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_xkzvqb` (
  `c_0q_i3b` int(11) DEFAULT NULL,
  `c__ckpid` int(11) DEFAULT NULL,
  `c_s4e7jc` double DEFAULT NULL,
  `c_k_dsxd` text DEFAULT NULL,
  `c_ofdx2c` double NOT NULL,
  `c__9zs7d` int(11) DEFAULT NULL,
  PRIMARY KEY (`c_ofdx2c`) /*T![clustered_index] NONCLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_xkzvqb`
--

LOCK TABLES `t_xkzvqb` WRITE;
/*!40000 ALTER TABLE `t_xkzvqb` DISABLE KEYS */;
INSERT INTO `t_xkzvqb` VALUES (36,59,3.26,'li53c',83.25,6);
/*!40000 ALTER TABLE `t_xkzvqb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `t_f32hfd`
--

/*!50001 DROP VIEW IF EXISTS `t_f32hfd`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `t_f32hfd` (`c0`, `c1`, `c2`, `c3`, `c4`, `c5`, `c7`) AS SELECT DISTINCT `ref_2`.`c_wylqr` AS `c0`,`subq_0`.`c5` AS `c1`,CUME_DIST() OVER (PARTITION BY `ref_1`.`c__9zs7d` ORDER BY `subq_0`.`c1`,`ref_1`.`c__9zs7d`) AS `c2`,`subq_0`.`c1` AS `c3`,CASE WHEN `subq_1`.`c2` NOT LIKE _UTF8MB4'nf%zyd' THEN (_UTF8MB4'6ddkrb' OR `ref_1`.`c_k_dsxd`) ELSE `subq_1`.`c2` END AS `c4`,NULLIF(CASE WHEN `subq_0`.`c1`>=`subq_1`.`c4` THEN `subq_1`.`c1` ELSE `subq_1`.`c5` END, `subq_1`.`c3`) AS `c5`,(`ref_1`.`c__ckpid`*COALESCE(`ref_1`.`c__ckpid`, `ref_1`.`c__ckpid`)) AS `c7` FROM ((SELECT `ref_0`.`c_09ew1d` AS `c0`,`ref_0`.`c_u3bwg` AS `c1`,`ref_0`.`c_09ew1d` AS `c2`,`ref_0`.`c_09ew1d` AS `c3`,`ref_0`.`c_u3bwg` AS `c4`,`ref_0`.`c_a_p8b` AS `c5` FROM `testdb`.`t_rxrf9c` AS `ref_0` WHERE (`ref_0`.`c_wylqr`!=`ref_0`.`c_u3bwg`) OR (`ref_0`.`c_a_p8b`>`ref_0`.`c_a_p8b`)) AS `subq_0` JOIN `testdb`.`t_xkzvqb` AS `ref_1`) JOIN (`testdb`.`t_rxrf9c` AS `ref_2` LEFT JOIN (SELECT `ref_3`.`c_0q_i3b` AS `c0`,`ref_3`.`c__ckpid` AS `c1`,`ref_3`.`c_k_dsxd` AS `c2`,`ref_3`.`c_0q_i3b` AS `c3`,`ref_3`.`c_0q_i3b` AS `c4`,`ref_3`.`c__9zs7d` AS `c5`,`ref_3`.`c_ofdx2c` AS `c6` FROM `testdb`.`t_xkzvqb` AS `ref_3` WHERE `ref_3`.`c_0q_i3b` BETWEEN `ref_3`.`c__9zs7d` AND `ref_3`.`c__ckpid`) AS `subq_1` ON (`ref_2`.`c_wylqr`=`subq_1`.`c0`)) ON (`ref_1`.`c_0q_i3b`=`ref_2`.`c_u3bwg`) WHERE (`ref_1`.`c_k_dsxd` OR `ref_1`.`c_k_dsxd`) LIKE _UTF8MB4'3x__' */;
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

-- Dump completed on 2021-12-05  4:37:07
