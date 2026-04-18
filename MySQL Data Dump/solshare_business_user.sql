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
-- Table structure for table `business_user`
--

DROP TABLE IF EXISTS `business_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `business_user` (
  `UserID` int NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Phone` varchar(15) DEFAULT NULL,
  `Consumption_Rate` decimal(10,2) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Renewable_Capacity` decimal(10,2) DEFAULT NULL,
  `regionID` int DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_user`
--

LOCK TABLES `business_user` WRITE;
/*!40000 ALTER TABLE `business_user` DISABLE KEYS */;
INSERT INTO `business_user` VALUES (54341,'Acme Corporation','acme.corporation@example.com','617-555-0201',210.00,'10 Corporate Plaza, Boston, MA, USA',35.50,4),(54342,'Beta Solutions','beta.solutions@example.com','617-555-0202',220.00,'20 Business Rd, Cambridge, MA, USA',36.00,2),(54343,'Gamma Industries','gamma.industries@example.com','617-555-0203',205.50,'30 Industrial Way, Worcester, MA, USA',34.25,6),(54344,'Delta Enterprises','delta.enterprises@example.com','617-555-0204',215.75,'40 Commerce St, Springfield, MA, USA',33.00,3),(54345,'Epsilon Trading','epsilon.trading@example.com','617-555-0205',230.00,'50 Market Ave, Lowell, MA, USA',38.00,1),(54346,'Zeta Logistics','zeta.logistics@example.com','617-555-0206',240.50,'60 Innovation Dr, Lawrence, MA, USA',37.50,5),(54347,'Eta Manufacturing','eta.manufacturing@example.com','617-555-0207',225.25,'70 Enterprise Blvd, Newton, MA, USA',32.50,2),(54348,'Theta Services','theta.services@example.com','617-555-0208',235.00,'80 Venture St, Quincy, MA, USA',39.00,1),(54349,'Iota Retail','iota.retail@example.com','617-555-0209',210.75,'90 Executive Ave, Brockton, MA, USA',31.50,6),(54350,'Kappa Technologies','kappa.technologies@example.com','617-555-0210',220.50,'100 Trade St, Fall River, MA, USA',30.00,3),(54351,'Lambda Consulting','lambda.consulting@example.com','617-555-0211',215.00,'110 Office Park, Lynn, MA, USA',35.00,5),(54352,'Mu Investments','mu.investments@example.com','617-555-0212',230.25,'120 Commerce Pkwy, New Bedford, MA, USA',36.50,4),(54353,'Nu Energy','nu.energy@example.com','617-555-0213',240.00,'130 Business Loop, Salem, MA, USA',38.25,2),(54354,'Xi Systems','xi.systems@example.com','617-555-0214',225.75,'140 Corporate Ct, Framingham, MA, USA',33.75,3),(54355,'Omicron Holdings','omicron.holdings@example.com','617-555-0215',235.25,'150 Innovation Way, Peabody, MA, USA',34.50,1),(54356,'Pi Innovations','pi.innovations@example.com','617-555-0216',210.50,'160 Executive Blvd, Medford, MA, USA',32.00,6),(54357,'Rho Electronics','rho.electronics@example.com','617-555-0217',220.75,'170 Enterprise Ave, Waltham, MA, USA',31.25,4),(54358,'Sigma Foods','sigma.foods@example.com','617-555-0218',215.50,'180 Trade Rd, Malden, MA, USA',30.75,5),(54359,'Tau Construction','tau.construction@example.com','617-555-0219',230.50,'190 Market St, Everett, MA, USA',37.00,2),(54360,'Upsilon Media','upsilon.media@example.com','617-555-0220',240.25,'200 Corporate Dr, Revere, MA, USA',36.25,3);
/*!40000 ALTER TABLE `business_user` ENABLE KEYS */;
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
