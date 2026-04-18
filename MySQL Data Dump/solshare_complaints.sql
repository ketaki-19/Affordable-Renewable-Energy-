-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: solshare
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `complaints`
--

DROP TABLE IF EXISTS `complaints`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `complaints` (
  `ComplaintID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `Complaint_Date` date DEFAULT NULL,
  `Complaint_Description` text,
  `EmployeeID` int NOT NULL,
  `Status` varchar(20) DEFAULT NULL,
  `Resolution_Date` date DEFAULT NULL,
  PRIMARY KEY (`ComplaintID`),
  KEY `fk_employee_complaints` (`EmployeeID`),
  CONSTRAINT `fk_employee_complaints` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `complaints`
--

LOCK TABLES `complaints` WRITE;
/*!40000 ALTER TABLE `complaints` DISABLE KEYS */;
INSERT INTO `complaints` VALUES (7001,54321,'2025-03-15','Billing error',1002,'Resolved','2025-03-16'),(7002,54322,'2025-03-16','Service outage',1003,'Pending',NULL),(7003,54323,'2025-03-17','Meter malfunction',1004,'Resolved','2025-03-18'),(7004,54324,'2025-03-18','Incorrect charges',1005,'Resolved','2025-03-19'),(7005,54325,'2025-03-19','Customer service issue',1002,'Pending',NULL),(7006,54326,'2025-03-20','Delayed response',1006,'Resolved','2025-03-21'),(7007,54327,'2025-03-21','Overbilling',1007,'Pending',NULL),(7008,54328,'2025-03-22','Technical issue',1008,'Resolved','2025-03-23'),(7009,54329,'2025-03-23','Installation error',1009,'Resolved','2025-03-24'),(7010,54330,'2025-03-24','Payment discrepancy',1010,'Pending',NULL);
/*!40000 ALTER TABLE `complaints` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-17 15:19:39
