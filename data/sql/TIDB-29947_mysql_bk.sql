drop table if exists t_tir89b, t_vejdy;

CREATE TABLE `t_tir89b` (
`c_3pcik` int(11) DEFAULT NULL,
`c_0b6nxb` text DEFAULT NULL,
`c_qytrlc` double NOT NULL,
`c_sroc_c` int(11) DEFAULT NULL,
PRIMARY KEY (`c_qytrlc`) /*T![clustered_index] NONCLUSTERED */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `t_tir89b` VALUES (66,'cjd1o',87.77,NULL),(134217728,'d_unpd',76.66,NULL),(50,'_13gs',1.46,32),(49,'xclvsc',64.7,48),(7,'1an13',70.86,7),(29,NULL,6.26,6),(8,'hc485b',47.44,2),(84,'d_nlmd',99.3,76),(14,'lbny1c',61.1,47),(45,'9r5bid',25.37,95),(49,'jbz5r',72.99,49),(18,'uode3d',7.21,992),(-8945040,'ftrtib',47.47,20),(29,'algrj',6.28,24),(96,NULL,67.83,24),(5,'s1gfz',89.18,78),(74,'ggqbl',83.89,68),(61,'5n1q7',26.92,6),(10,'4gflb',33.84,28),(48,'xoe0cd',84.71,77),(6,'xkh6i',53.83,19),(5,NULL,89.1,46),(49,'4q6nx',31.5,384),(1,'pgs1',66.8,77),(19,'lltflc',33.49,63),(87,'vd4htc',39.92,-5367008),(47,NULL,28.3,10),(29,'15jqfc',100.11,64),(45,'ii6pm',52.41,61),(0,NULL,85.27,19),(104,'ikpxnb',40.66,955),(40,'gzryzd',36.23,42),(18,'7UPNE',84.27,14),(32,NULL,84.8,53),(51,'2c5lfb',18.98,74),(97,NULL,22.89,6),(70,'guyzyc',96.29,89),(34,'dvdoqb',53.82,1),(94,'6eop6b',81.77,90),(42,'p7vsnd',62.54,NULL);

CREATE TABLE `t_vejdy` (
`c_iovir` int(11) NOT NULL,
`c_r_mw3d` double DEFAULT NULL,
`c_uxhghb` int(11) DEFAULT NULL,
`c_rb7otb` int(11) NOT NULL,
`c_dplyac` int(11) DEFAULT NULL,
`c_lmcqed` double DEFAULT NULL,
`c_ayaoed` text DEFAULT NULL,
`c__zbqr` int(11) DEFAULT NULL,
PRIMARY KEY (`c_iovir`,`c_rb7otb`) /*T![clustered_index] NONCLUSTERED */,
KEY `t_e1ejcd` (`c_uxhghb`),
KEY `t_o6ui_b` (`c_iovir`,`c_r_mw3d`,`c_uxhghb`,`c_rb7otb`,`c_dplyac`,`c_lmcqed`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `t_vejdy` VALUES (49,100.11,68,57,44,17.93,NULL,84),(38,56.91,78,30,0,53.28,'cjd1o',2),(6,NULL,NULL,88,81,93.47,'0jftkb',54),(73,91.51,31,82,3,38.12,'buesob',40),(7,26.73,7,78,9,NULL,'fd5kgd',49),(80,70.57,4,47,43,25.59,'glpoq',44),(79,94.16,15,0,0,79.55,'0ok94d',56),(58,NULL,50,69,2,65.46,'sm6rj',29),(41472,6.51,70,1080,100,43.18,'fofk4c',43),(0,6.2,57,97,2,56.17,'zqpzq',56),(72,76.66,97,88,95,75.47,'hikxqb',34),(27,1.11,134217728,57,25,NULL,'4gflb',0),(64,NULL,47,69,6,72.5,'w7jmhd',45),(-134217679,88.74,33,82,85,59.89,NULL,26),(59,97.98,37,28,33,61.1,'xioxdd',45),(6,47.31,0,0,-19,38.77,'uxmdlc',17),(82,28.62,36,70,39,11.79,'zzi8cc',2),(33,37.3,55,86,69,60.56,'mn_xx',0),(7,NULL,80,0,17,59.79,'5n1q7',97),(88,50.81,15,30,63,25.37,'ordwed',29),(48,4.32,90,48,38,84.62,'lclx',32),(10,NULL,95,75,1,21.64,NULL,85),(62,NULL,0,30,10,NULL,'7bacud',5),(50,38.81,6,0,6,64.28,'gpibn',57),(1,46.8,21,32,46,33.38,NULL,6),(29,NULL,38,7,91,31.5,'pdzdl',24),(54,6.26,1,85,22,75.63,'gl4_7',29),(1,90.37,63,63,6,61.2,'wvw23b',86),(47,NULL,82,73,0,95.79,'uipcf',NULL),(46,48.1,37,6,1,52.33,'gthpic',0),(41,75.1,7,44,5,84.16,'fe_e5',58),(43,87.71,81,32,28,91.98,'9e5nvc',66),(20,58.21,88,75,92,43.64,'kagroc',66),(91,52.75,22,14,80,NULL,'\'_YN6MD\'',6),(72,94.83,0,49,5,57.82,NULL,23),(7,100.11,0,92,13,6.28,NULL,0);