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
-- Table structure for table `household_user`
--

DROP TABLE IF EXISTS `household_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `household_user` (
  `UserID` int NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Phone` varchar(15) DEFAULT NULL,
  `Consumption_Rate` decimal(10,2) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Renewable_Capacity` decimal(10,2) DEFAULT NULL,
  `RegionID` int DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `household_user`
--

LOCK TABLES `household_user` WRITE;
/*!40000 ALTER TABLE `household_user` DISABLE KEYS */;
INSERT INTO `household_user` VALUES (54321,'Alice Johnson','alice.johnson@example.com','617-555-0101',150.75,'123 Main St, Boston, MA, USA',25.50,3),(54322,'Brian Smith','brian.smith@example.com','617-555-0102',160.20,'456 Elm St, Cambridge, MA, USA',30.00,1),(54323,'Carol Davis','carol.davis@example.com','617-555-0103',140.00,'789 Oak St, Worcester, MA, USA',22.30,6),(54324,'David Brown','david.brown@example.com','617-555-0104',180.45,'101 Pine St, Springfield, MA, USA',35.00,2),(54325,'Emily Wilson','emily.wilson@example.com','617-555-0105',200.00,'202 Maple Ave, Lowell, MA, USA',28.75,4),(54326,'Frank Miller','frank.miller@example.com','617-555-0106',175.50,'303 Cedar Rd, Lawrence, MA, USA',20.50,5),(54327,'Grace Taylor','grace.taylor@example.com','617-555-0107',190.00,'404 Birch Ln, Newton, MA, USA',33.00,1),(54328,'Henry Anderson','henry.anderson@example.com','617-555-0108',165.25,'505 Walnut St, Quincy, MA, USA',27.00,2),(54329,'Irene Thomas','irene.thomas@example.com','617-555-0109',155.75,'606 Cherry Ave, Brockton, MA, USA',26.50,3),(54330,'Jack Moore','jack.moore@example.com','617-555-0110',185.00,'707 Poplar Dr, Fall River, MA, USA',32.00,6),(54331,'Karen Martin','karen.martin@example.com','617-555-0111',170.50,'808 Ash St, Lynn, MA, USA',21.50,5),(54332,'Larry Jackson','larry.jackson@example.com','617-555-0112',160.00,'909 Chestnut St, New Bedford, MA, USA',23.75,4),(54333,'Monica White','monica.white@example.com','617-555-0113',210.00,'111 Spruce St, Salem, MA, USA',40.00,2),(54334,'Nathan Harris','nathan.harris@example.com','617-555-0114',195.00,'222 Fir St, Framingham, MA, USA',34.50,1),(54335,'Olivia Clark','olivia.clark@example.com','617-555-0115',180.00,'333 Willow Ln, Peabody, MA, USA',29.00,6),(54336,'Peter Lewis','peter.lewis@example.com','617-555-0116',165.00,'444 Sycamore Ave, Medford, MA, USA',25.00,3),(54337,'Quinn Robinson','quinn.robinson@example.com','617-555-0117',155.00,'555 Cypress Rd, Waltham, MA, USA',20.00,4),(54338,'Rachel Walker','rachel.walker@example.com','617-555-0118',175.00,'666 Redwood Blvd, Malden, MA, USA',30.25,5),(54339,'Steven Hall','steven.hall@example.com','617-555-0119',185.25,'777 Sequoia St, Everett, MA, USA',27.75,2),(54340,'Tina Allen','tina.allen@example.com','617-555-0120',160.75,'888 Magnolia Ave, Revere, MA, USA',24.50,1);
/*!40000 ALTER TABLE `household_user` ENABLE KEYS */;
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
