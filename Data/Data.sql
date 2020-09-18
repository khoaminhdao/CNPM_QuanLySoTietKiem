-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: qlstk
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `identityNumber` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  `customerName` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`identityNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('0000000000','Lâm','OU'),('0000000001','Hoài','OU'),('0000000002','Bình','OU'),('0000000005','Đăng','OU'),('0000000008','Huy','OU'),('000000012','Bá','OU'),('00001102000','Rosie','OU'),('0000310000','Hưng','OU'),('0000607000','Tuấn','OU'),('0002107000','Thành','OU'),('0002404000','Đông','OU'),('0002510000','Bắc','OU'),('0003107000','Đạt','OU'),('0007050000','Minh','OU'),('0123456789','Khoa','OU'),('100000000','Quân','OU'),('3333323212','sdsdsd','OU'),('343434','êre','OU');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deposit_form`
--

DROP TABLE IF EXISTS `deposit_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deposit_form` (
  `formID` int NOT NULL AUTO_INCREMENT,
  `savingID` int NOT NULL,
  `depositDate` datetime NOT NULL,
  `amount` float NOT NULL,
  `employeeCreated` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`formID`),
  KEY `savingID` (`savingID`),
  KEY `employeeCreated` (`employeeCreated`),
  CONSTRAINT `deposit_form_ibfk_1` FOREIGN KEY (`savingID`) REFERENCES `saving` (`savingID`),
  CONSTRAINT `deposit_form_ibfk_2` FOREIGN KEY (`employeeCreated`) REFERENCES `employee` (`identityNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deposit_form`
--

LOCK TABLES `deposit_form` WRITE;
/*!40000 ALTER TABLE `deposit_form` DISABLE KEYS */;
INSERT INTO `deposit_form` VALUES (1,1,'2020-09-18 00:52:23',2300000,'0123456789'),(2,1,'2020-09-18 00:52:56',2300000,'987654321'),(3,1,'2020-09-18 00:55:42',5000000,'987654321'),(4,6,'2020-09-18 00:56:34',2132120000,'987654321'),(5,5,'2020-09-18 00:56:53',100000,'987654321'),(6,9,'2020-09-18 00:58:43',2000000000,'987654321'),(7,13,'2020-09-18 01:32:23',100000,'987654321'),(8,19,'2020-09-18 20:21:03',1997000,'0123456789'),(9,17,'2020-09-18 20:22:20',100000,'0123456789'),(10,9,'2020-09-18 20:23:16',10000000,'0123456789'),(11,12,'2020-09-18 20:25:04',400000,'0123456789');
/*!40000 ALTER TABLE `deposit_form` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `identityNumber` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  `employeeName` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `account` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `positionID` int NOT NULL,
  `lastActive` datetime DEFAULT NULL,
  PRIMARY KEY (`identityNumber`),
  KEY `positionID` (`positionID`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`positionID`) REFERENCES `position` (`posID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('0123456789','admin','admin','21232f297a57a5a743894a0e4a801fc3',1,'2020-09-18 21:14:52'),('987654321','Khoa','khoa1','e10adc3949ba59abbe56e057f20f883e',2,'2020-09-18 21:14:59');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `position`
--

DROP TABLE IF EXISTS `position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `position` (
  `posID` int NOT NULL AUTO_INCREMENT,
  `posName` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`posID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position`
--

LOCK TABLES `position` WRITE;
/*!40000 ALTER TABLE `position` DISABLE KEYS */;
INSERT INTO `position` VALUES (1,'Manager'),(2,'Teller');
/*!40000 ALTER TABLE `position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regulation`
--

DROP TABLE IF EXISTS `regulation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regulation` (
  `regulationID` int NOT NULL AUTO_INCREMENT,
  `regulationName` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`regulationID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regulation`
--

LOCK TABLES `regulation` WRITE;
/*!40000 ALTER TABLE `regulation` DISABLE KEYS */;
INSERT INTO `regulation` VALUES (1,'Minimum deposit amount'),(2,'Minimum time ');
/*!40000 ALTER TABLE `regulation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regulation_detail`
--

DROP TABLE IF EXISTS `regulation_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regulation_detail` (
  `regulationID` int NOT NULL,
  `value` float NOT NULL,
  `applyDate` datetime NOT NULL,
  `employeeCreated` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`regulationID`,`applyDate`),
  KEY `employeeCreated` (`employeeCreated`),
  CONSTRAINT `regulation_detail_ibfk_1` FOREIGN KEY (`regulationID`) REFERENCES `regulation` (`regulationID`),
  CONSTRAINT `regulation_detail_ibfk_2` FOREIGN KEY (`employeeCreated`) REFERENCES `employee` (`identityNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regulation_detail`
--

LOCK TABLES `regulation_detail` WRITE;
/*!40000 ALTER TABLE `regulation_detail` DISABLE KEYS */;
INSERT INTO `regulation_detail` VALUES (1,100000,'2020-09-17 20:08:00','0123456789'),(2,15,'2020-09-17 20:08:00','0123456789'),(2,20,'2020-09-18 01:22:00','0123456789');
/*!40000 ALTER TABLE `regulation_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `saving`
--

DROP TABLE IF EXISTS `saving`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `saving` (
  `savingID` int NOT NULL AUTO_INCREMENT,
  `savingTypeID` int NOT NULL,
  `customerID` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `createDate` datetime NOT NULL,
  `balanceAmount` float NOT NULL,
  `allowWithdrawDate` datetime NOT NULL,
  PRIMARY KEY (`savingID`),
  KEY `savingTypeID` (`savingTypeID`),
  KEY `customerID` (`customerID`),
  CONSTRAINT `saving_ibfk_1` FOREIGN KEY (`savingTypeID`) REFERENCES `saving_type` (`savingTypeID`),
  CONSTRAINT `saving_ibfk_2` FOREIGN KEY (`customerID`) REFERENCES `customer` (`identityNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `saving`
--

LOCK TABLES `saving` WRITE;
/*!40000 ALTER TABLE `saving` DISABLE KEYS */;
INSERT INTO `saving` VALUES (1,1,'0123456789','2020-09-17 19:51:13',1009600000,'2020-09-17 19:51:00'),(2,1,'0007050000','2020-09-18 00:19:57',10000000000,'2020-10-03 00:19:58'),(3,3,'0002107000','2020-09-18 00:19:57',700000000,'2021-03-18 00:21:36'),(4,2,'0003107000','2020-09-18 00:25:59',3000000000,'2020-12-18 00:26:27'),(5,1,'0002404000','2020-09-18 00:27:27',400100000,'2020-10-03 00:27:46'),(6,1,'0002510000','2020-09-18 00:29:49',4632120000,'2020-10-03 00:30:40'),(7,2,'0000310000','2020-09-18 00:36:45',3100000,'2020-12-18 00:37:22'),(8,3,'0000607000','2020-09-18 00:37:43',1000000000,'2021-03-18 00:38:11'),(9,1,'0123456789','2020-09-18 00:37:43',2012000000,'2020-10-03 00:39:14'),(10,2,'0000000000','2020-09-18 00:40:10',100000000,'2020-12-18 00:41:33'),(11,3,'0000000001','2020-09-18 00:40:10',300000,'2021-03-18 00:42:07'),(12,3,'0000000002','2020-09-18 00:54:08',58480300000,'2021-03-18 00:55:02'),(13,1,'0003107000','2020-09-18 01:06:09',0,'2020-09-17 01:06:00'),(14,2,'0123456789','2020-09-18 01:15:34',100000,'2020-12-18 01:16:16'),(15,2,'0007050000','2020-09-18 01:20:29',10000000,'2020-09-18 01:20:58'),(16,2,'0007050000','2020-09-18 01:24:15',2123000000,'2020-12-18 01:24:38'),(17,1,'0123456789','2020-09-18 01:31:22',1000100000,'2020-09-18 01:31:32'),(18,2,'0000000008','2020-09-18 13:50:31',10000000000,'2020-12-18 13:51:29'),(19,1,'00001102000','2020-09-18 14:02:20',1102000000,'2020-09-18 14:03:32'),(20,2,'0000000005','2020-09-18 20:06:18',150000000,'2020-12-18 20:07:05'),(21,1,'000000012','2020-09-18 20:08:23',1200000000,'2020-10-08 20:08:41'),(22,3,'3333323212','2020-09-18 20:10:21',1333330000000,'2021-03-18 20:10:50'),(23,1,'343434','2020-09-18 20:11:31',9000000,'2020-10-08 20:11:48'),(24,2,'100000000','2020-09-18 20:12:37',10000000000,'2020-12-18 20:13:03');
/*!40000 ALTER TABLE `saving` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `saving_type`
--

DROP TABLE IF EXISTS `saving_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `saving_type` (
  `savingTypeID` int NOT NULL AUTO_INCREMENT,
  `savingName` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `term` int NOT NULL,
  `interestRate` float NOT NULL,
  `applyDate` datetime NOT NULL,
  PRIMARY KEY (`savingTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `saving_type`
--

LOCK TABLES `saving_type` WRITE;
/*!40000 ALTER TABLE `saving_type` DISABLE KEYS */;
INSERT INTO `saving_type` VALUES (1,'No term',0,0.15,'2020-09-17 19:09:00'),(2,'3 months',3,0.5,'2020-09-17 19:09:00'),(3,'6 months',6,0.55,'2020-09-17 19:09:00');
/*!40000 ALTER TABLE `saving_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `withdrawal_form`
--

DROP TABLE IF EXISTS `withdrawal_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `withdrawal_form` (
  `formID` int NOT NULL AUTO_INCREMENT,
  `savingID` int NOT NULL,
  `withdrawDate` datetime NOT NULL,
  `amount` float NOT NULL,
  `employeeCreated` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`formID`),
  KEY `savingID` (`savingID`),
  KEY `employeeCreated` (`employeeCreated`),
  CONSTRAINT `withdrawal_form_ibfk_1` FOREIGN KEY (`savingID`) REFERENCES `saving` (`savingID`),
  CONSTRAINT `withdrawal_form_ibfk_2` FOREIGN KEY (`employeeCreated`) REFERENCES `employee` (`identityNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `withdrawal_form`
--

LOCK TABLES `withdrawal_form` WRITE;
/*!40000 ALTER TABLE `withdrawal_form` DISABLE KEYS */;
INSERT INTO `withdrawal_form` VALUES (1,13,'2020-09-18 17:51:51',99900000,'0123456789'),(2,19,'2020-09-18 20:26:26',1997000,'0123456789');
/*!40000 ALTER TABLE `withdrawal_form` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-18 23:35:36
