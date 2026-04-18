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
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `PaymentID` int NOT NULL,
  `TransactionID` int NOT NULL,
  `Payment_Date` date DEFAULT NULL,
  `Payment_Status` varchar(20) DEFAULT NULL,
  `Amount_Paid` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`PaymentID`),
  KEY `fk_transaction_payment` (`TransactionID`),
  CONSTRAINT `fk_transaction_payment` FOREIGN KEY (`TransactionID`) REFERENCES `energy_transaction` (`Transaction_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (6001,5001,'2025-03-02','Completed',100.00),(6002,5002,'2025-03-02','Completed',110.00),(6003,5003,'2025-03-02','Completed',120.00),(6004,5004,'2025-03-02','Completed',130.00),(6005,5005,'2025-03-02','Completed',140.00),(6006,5006,'2025-03-02','Completed',150.00),(6007,5007,'2025-03-03','Completed',160.00),(6008,5008,'2025-03-03','Completed',170.00),(6009,5009,'2025-03-03','Completed',180.00),(6010,5010,'2025-03-03','Completed',190.00),(6011,5011,'2025-03-04','Completed',200.00),(6012,5012,'2025-03-04','Completed',210.00),(6013,5013,'2025-03-04','Completed',220.00),(6014,5014,'2025-03-04','Completed',230.00),(6015,5015,'2025-03-05','Completed',240.00),(6016,5016,'2025-03-05','Completed',250.00),(6017,5017,'2025-03-05','Completed',260.00),(6018,5018,'2025-03-05','Completed',270.00),(6019,5019,'2025-03-06','Completed',280.00),(6020,5020,'2025-03-06','Completed',290.00),(6021,5021,'2025-03-06','Completed',111.00),(6022,5022,'2025-03-06','Completed',121.00),(6023,5023,'2025-03-06','Completed',131.00),(6024,5024,'2025-03-06','Completed',141.00),(6025,5025,'2025-03-06','Completed',151.00),(6026,5026,'2025-03-06','Completed',161.00),(6027,5027,'2025-03-07','Completed',171.00),(6028,5028,'2025-03-07','Completed',181.00),(6029,5029,'2025-03-07','Completed',191.00),(6030,5030,'2025-03-07','Completed',201.00),(6031,5031,'2025-03-08','Completed',211.00),(6032,5032,'2025-03-08','Completed',221.00),(6033,5033,'2025-03-08','Completed',231.00),(6034,5034,'2025-03-08','Completed',241.00),(6035,5035,'2025-03-09','Completed',251.00),(6036,5036,'2025-03-09','Completed',261.00),(6037,5037,'2025-03-09','Completed',271.00),(6038,5038,'2025-03-09','Completed',281.00),(6039,5039,'2025-03-10','Completed',291.00),(6040,5040,'2025-03-10','Completed',301.00),(6041,5041,'2025-03-11','Completed',104.50),(6042,5042,'2025-03-11','Completed',114.50),(6043,5043,'2025-03-11','Completed',124.50),(6044,5044,'2025-03-11','Completed',134.50),(6045,5045,'2025-03-11','Completed',144.50),(6046,5046,'2025-03-11','Completed',154.50),(6047,5047,'2025-03-11','Completed',164.50),(6048,5048,'2025-03-11','Completed',174.50),(6049,5049,'2025-03-11','Completed',184.50),(6050,5050,'2025-03-11','Completed',194.50),(6051,5051,'2025-03-12','Completed',204.50),(6052,5052,'2025-03-12','Completed',214.50),(6053,5053,'2025-03-12','Completed',224.50),(6054,5054,'2025-03-12','Completed',234.50),(6055,5055,'2025-03-12','Completed',244.50),(6056,5056,'2025-03-12','Completed',254.50),(6057,5057,'2025-03-12','Completed',264.50),(6058,5058,'2025-03-12','Completed',274.50),(6059,5059,'2025-03-12','Completed',284.50),(6060,5060,'2025-03-12','Completed',294.50),(6061,5061,'2025-03-13','Completed',107.50),(6062,5062,'2025-03-13','Completed',117.50),(6063,5063,'2025-03-13','Completed',127.50),(6064,5064,'2025-03-13','Completed',137.50),(6065,5065,'2025-03-13','Completed',147.50),(6066,5066,'2025-03-13','Completed',157.50),(6067,5067,'2025-03-13','Completed',167.50),(6068,5068,'2025-03-13','Completed',177.50),(6069,5069,'2025-03-13','Completed',187.50),(6070,5070,'2025-03-13','Completed',197.50),(6071,5071,'2025-03-14','Completed',207.50),(6072,5072,'2025-03-14','Completed',217.50),(6073,5073,'2025-03-14','Completed',227.50),(6074,5074,'2025-03-14','Completed',237.50),(6075,5075,'2025-03-14','Completed',247.50),(6076,5076,'2025-03-14','Completed',257.50),(6077,5077,'2025-03-14','Completed',267.50),(6078,5078,'2025-03-14','Completed',277.50),(6079,5079,'2025-03-14','Completed',287.50),(6080,5080,'2025-03-14','Completed',297.50);
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-17 15:19:40
