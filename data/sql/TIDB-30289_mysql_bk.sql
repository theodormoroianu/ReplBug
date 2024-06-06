-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.25-TiDB-v5.4.0-alpha-133-g20b9a4d8c

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
-- Temporary view structure for view `t_aqzphd`
--

DROP TABLE IF EXISTS `t_aqzphd`;
/*!50001 DROP VIEW IF EXISTS `t_aqzphd`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `t_aqzphd` AS SELECT 
 1 AS `c0`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `t_czevbc`
--

DROP TABLE IF EXISTS `t_czevbc`;
/*!50001 DROP VIEW IF EXISTS `t_czevbc`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `t_czevbc` AS SELECT 
 1 AS `c0`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `t_p2n_bb`
--

DROP TABLE IF EXISTS `t_p2n_bb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_p2n_bb` (
  `c_grbrfc` int(11) NOT NULL,
  `c_ko4ll` int(11) NOT NULL,
  PRIMARY KEY (`c_grbrfc`,`c_ko4ll`) /*T![clustered_index] NONCLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_p2n_bb`
--

LOCK TABLES `t_p2n_bb` WRITE;
/*!40000 ALTER TABLE `t_p2n_bb` DISABLE KEYS */;
INSERT INTO `t_p2n_bb` VALUES (-58,8),(0,5),(0,34),(2,94),(3,4),(3,55),(4,52),(6,37),(11,87),(13,33),(13,88),(14,31),(14,66),(15,18),(15,71),(18,39),(22,48),(24,5),(25,23),(26,51),(29,0),(30,41),(35,-2),(36,55),(37,77),(40,65),(40,97),(41,87),(44,4),(45,54),(45,78),(46,4),(47,41),(48,4),(49,36),(50,31),(54,0),(54,24),(54,98),(55,96),(56,0),(58,24),(67,64),(67,82),(70,77),(71,1),(79,2),(83,36),(84,89),(88,21),(89,53),(92,20),(92,38),(94,25),(95,43),(95,93),(96,1),(96,96),(98,54),(100,46);
/*!40000 ALTER TABLE `t_p2n_bb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `t_vzifnb`
--

DROP TABLE IF EXISTS `t_vzifnb`;
/*!50001 DROP VIEW IF EXISTS `t_vzifnb`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `t_vzifnb` AS SELECT 
 1 AS `c0`,
 1 AS `c1`,
 1 AS `c2`,
 1 AS `c3`,
 1 AS `c4`,
 1 AS `c5`,
 1 AS `c7`,
 1 AS `c8`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `t_xgqzcb`
--

DROP TABLE IF EXISTS `t_xgqzcb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_xgqzcb` (
  `c_lc0obb` int(11) NOT NULL,
  `c_2psjsc` double DEFAULT NULL,
  `c_goymkc` double NOT NULL,
  `c_rk9c_c` text DEFAULT NULL,
  `c_xjbxpd` text DEFAULT NULL,
  `c_8eufm` double DEFAULT NULL,
  PRIMARY KEY (`c_goymkc`,`c_lc0obb`) /*T![clustered_index] NONCLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_xgqzcb`
--

LOCK TABLES `t_xgqzcb` WRITE;
/*!40000 ALTER TABLE `t_xgqzcb` DISABLE KEYS */;
INSERT INTO `t_xgqzcb` VALUES (23,33.17,81.42,'_yr2ib','emqyyd',25.91),(75,NULL,78.45,'afkbpd','dxvpt',52.69),(44,26.2,13.7,NULL,'vw8mdc',84.67),(24,100.8,98.56,NULL,'j8wftb',NULL),(90,83.18,59.69,'onjgm','g2f1vd',9.21),(57,35.65,46.24,'sehnxc','phtbdc',11.66),(41,26.51,95.23,'kjad_d','9bbrqc',85.94),(81,6.34,24.26,'4hilic','griewb',43.57),(4,65.62,28.37,'\'jd5fmc\'','hlpuyb',2147483648.1),(54,1.3,23.69,'f4wei','1wjlwd',45.28);
/*!40000 ALTER TABLE `t_xgqzcb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `t_aqzphd`
--

/*!50001 DROP VIEW IF EXISTS `t_aqzphd`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */
/*!50001 VIEW `t_aqzphd` (`c0`) AS SELECT 29 AS `c0` FROM `testdb`.`t_xgqzcb` AS `ref_0` JOIN (SELECT `ref_1`.`c3` AS `c0`,`ref_1`.`c1` AS `c1`,`ref_1`.`c2` AS `c2`,`ref_1`.`c4` AS `c3` FROM `testdb`.`t_vzifnb` AS `ref_1` WHERE `ref_1`.`c8` IS NULL) AS `subq_0` WHERE (CASE WHEN `ref_0`.`c_lc0obb`>`ref_0`.`c_lc0obb` THEN `ref_0`.`c_lc0obb` ELSE `ref_0`.`c_lc0obb` END>>`ref_0`.`c_lc0obb`) NOT IN (SELECT COUNT(CAST(`subq_1`.`c5` AS SIGNED)) OVER (PARTITION BY `subq_1`.`c6` ORDER BY `subq_1`.`c5`) AS `c0` FROM (SELECT `ref_3`.`c_grbrfc` AS `c0`,`ref_2`.`c_lc0obb` AS `c1`,`ref_3`.`c_ko4ll` AS `c2`,`ref_2`.`c_2psjsc` AS `c3`,`ref_3`.`c_ko4ll` AS `c4`,`ref_3`.`c_grbrfc` AS `c5`,`ref_3`.`c_grbrfc` AS `c6` FROM `testdb`.`t_xgqzcb` AS `ref_2` JOIN `testdb`.`t_p2n_bb` AS `ref_3` WHERE `ref_3`.`c_grbrfc` BETWEEN `ref_3`.`c_ko4ll` AND `ref_3`.`c_ko4ll` AND (`ref_2`.`c_lc0obb`<=`ref_2`.`c_lc0obb`) OR ((`ref_2`.`c_lc0obb` BETWEEN `ref_2`.`c_lc0obb` AND `ref_2`.`c_lc0obb`) OR (`ref_3`.`c_ko4ll`<`ref_3`.`c_grbrfc`)) ORDER BY `c0`,`c1`,`c2`,`c3`,`c4`,`c5`,-`c6`) AS `subq_1` WHERE (_UTF8MB4'n_w7sc' OR _UTF8MB4'l4mlvb') NOT LIKE _UTF8MB4'u_aw_c' ORDER BY `c0` DESC) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `t_czevbc`
--

/*!50001 DROP VIEW IF EXISTS `t_czevbc`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */
/*!50001 VIEW `t_czevbc` (`c0`) AS SELECT `subq_1`.`c1` AS `c0` FROM (SELECT `subq_0`.`c1` AS `c0`,`subq_0`.`c5` AS `c1`,`subq_0`.`c5` AS `c2`,`subq_0`.`c6` AS `c3` FROM (SELECT `ref_0`.`c_ko4ll` AS `c0`,`ref_0`.`c_grbrfc` AS `c1`,`ref_0`.`c_ko4ll` AS `c2`,`ref_0`.`c_grbrfc` AS `c3`,`ref_0`.`c_grbrfc` AS `c4`,`ref_0`.`c_ko4ll` AS `c5`,`ref_0`.`c_ko4ll` AS `c6`,`ref_0`.`c_ko4ll` AS `c7` FROM `testdb`.`t_p2n_bb` AS `ref_0` WHERE (SELECT `c_lc0obb` AS `c_lc0obb` FROM `testdb`.`t_xgqzcb` ORDER BY `c_lc0obb` LIMIT 4,1)>`ref_0`.`c_grbrfc`) AS `subq_0` WHERE `subq_0`.`c5` BETWEEN `subq_0`.`c1` AND `subq_0`.`c4`) AS `subq_1` WHERE `subq_1`.`c3` IN (SELECT `ref_1`.`c_ko4ll` AS `c0` FROM `testdb`.`t_p2n_bb` AS `ref_1` WHERE (54*`ref_1`.`c_grbrfc`)=(SELECT `ref_1`.`c_grbrfc` AS `c0` FROM `testdb`.`t_vzifnb` AS `ref_2` WHERE `ref_1`.`c_grbrfc`>=(SELECT DISTINCT `ref_1`.`c_ko4ll` AS `c0` FROM `testdb`.`t_aqzphd` AS `ref_3` WHERE _UTF8MB4'dahwrd' LIKE _UTF8MB4'hl8s_b' UNION SELECT DISTINCT `ref_1`.`c_ko4ll` AS `c0` FROM `testdb`.`t_p2n_bb` AS `ref_4` WHERE EXISTS (SELECT `ref_5`.`c_grbrfc` AS `c0` FROM `testdb`.`t_p2n_bb` AS `ref_5` WHERE 0!=0)) UNION SELECT `ref_6`.`c_grbrfc` AS `c0` FROM `testdb`.`t_p2n_bb` AS `ref_6` WHERE (`ref_1`.`c_grbrfc` BETWEEN 88 AND `ref_6`.`c_ko4ll`) AND (`ref_1`.`c_grbrfc` IN (`ref_6`.`c_grbrfc`,`ref_1`.`c_ko4ll`,`ref_1`.`c_grbrfc`,`ref_6`.`c_grbrfc`,`ref_6`.`c_grbrfc`))) ORDER BY `c0`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `t_vzifnb`
--

/*!50001 DROP VIEW IF EXISTS `t_vzifnb`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`127.0.0.1` SQL SECURITY DEFINER */
/*!50001 VIEW `t_vzifnb` (`c0`, `c1`, `c2`, `c3`, `c4`, `c5`, `c7`, `c8`) AS SELECT `subq_0`.`c2` AS `c0`,93 AS `c1`,MIN(CAST(`subq_0`.`c7` AS SIGNED)) OVER (PARTITION BY `subq_0`.`c3` ORDER BY `subq_0`.`c7`) AS `c2`,CAST(COALESCE(`subq_0`.`c6`, `subq_0`.`c7`) AS SIGNED) AS `c3`,`subq_0`.`c4` AS `c4`,CAST(COALESCE(CASE WHEN (SELECT `c_grbrfc` AS `c_grbrfc` FROM `testdb`.`t_p2n_bb` ORDER BY `c_grbrfc` LIMIT 32,1) NOT IN (SELECT `ref_1`.`c_ko4ll` AS `c0` FROM `testdb`.`t_p2n_bb` AS `ref_1` WHERE `ref_1`.`c_ko4ll`>=`ref_1`.`c_ko4ll` WINDOW `amauqb` AS (PARTITION BY `ref_1`.`c_ko4ll` ORDER BY `ref_1`.`c_grbrfc`,`ref_1`.`c_ko4ll` DESC) UNION SELECT `ref_2`.`c_grbrfc` AS `c0` FROM `testdb`.`t_p2n_bb` AS `ref_2` WHERE `ref_2`.`c_grbrfc`!=`ref_2`.`c_grbrfc`) THEN `subq_0`.`c2` ELSE `subq_0`.`c0` END, `subq_0`.`c4`) AS DOUBLE) AS `c5`,ROUND(CAST(`subq_0`.`c2` AS DOUBLE), CAST(`subq_0`.`c7` AS SIGNED)) AS `c7`,(SELECT `c_grbrfc` AS `c_grbrfc` FROM `testdb`.`t_p2n_bb` ORDER BY `c_grbrfc` LIMIT 2,1) AS `c8` FROM (SELECT MAX(CAST(CAST(NULLIF((SELECT `c_2psjsc` AS `c_2psjsc` FROM `testdb`.`t_xgqzcb` ORDER BY `c_2psjsc` LIMIT 11,1), (SELECT `c_2psjsc` AS `c_2psjsc` FROM `testdb`.`t_xgqzcb` ORDER BY `c_2psjsc` LIMIT 4,1)) AS DOUBLE) AS DOUBLE)) AS `c0`,MAX(CAST(`ref_0`.`c_ko4ll` AS SIGNED)) AS `c1`,AVG(CAST(CAST(NULLIF((SELECT `c_2psjsc` AS `c_2psjsc` FROM `testdb`.`t_xgqzcb` ORDER BY `c_2psjsc` LIMIT 6,1), (SELECT `c_2psjsc` AS `c_2psjsc` FROM `testdb`.`t_xgqzcb` ORDER BY `c_2psjsc` LIMIT 6,1)) AS DOUBLE) AS DOUBLE)) AS `c2`,MIN(CAST((SELECT COUNT(`c_2psjsc`) AS `count(c_2psjsc)` FROM `testdb`.`t_xgqzcb`) AS SIGNED)) AS `c3`,SUM(CAST(ABS(CAST((SELECT AVG(`c_2psjsc`) AS `avg(c_2psjsc)` FROM `testdb`.`t_xgqzcb`) AS DOUBLE)) AS DOUBLE)) AS `c4`,`ref_0`.`c_ko4ll` AS `c5`,MAX(CAST(97 AS SIGNED)) AS `c6`,AVG(CAST(`ref_0`.`c_ko4ll` AS SIGNED)) AS `c7` FROM `testdb`.`t_p2n_bb` AS `ref_0` WHERE `ref_0`.`c_ko4ll` IS NULL GROUP BY `ref_0`.`c_ko4ll`) AS `subq_0` WHERE `subq_0`.`c5`<`subq_0`.`c1` ORDER BY `c0`,`c1`,`c2`,`c3`,`c4`,`c5`,`c7`,-`c8` */;
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

-- Dump completed on 2021-11-30 13:18:53
