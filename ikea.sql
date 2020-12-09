CREATE DATABASE  IF NOT EXISTS `ikea` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ikea`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: ikea
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
-- Table structure for table `carritosdecompras`
--

DROP TABLE IF EXISTS `carritosdecompras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carritosdecompras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numeroCarrito` int NOT NULL,
  `idUsuario` int NOT NULL,
  `idProducto` int NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `carritos-productos_idx` (`idProducto`),
  KEY `carritos-usuarios_idx` (`idUsuario`),
  CONSTRAINT `carritos-productos` FOREIGN KEY (`idProducto`) REFERENCES `productos` (`id`),
  CONSTRAINT `carritos-usuarios` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carritosdecompras`
--

LOCK TABLES `carritosdecompras` WRITE;
/*!40000 ALTER TABLE `carritosdecompras` DISABLE KEYS */;
INSERT INTO `carritosdecompras` VALUES (1,1,1,1,1),(2,2,2,3,2),(3,3,3,4,1),(4,1,1,2,2),(5,2,2,1,1),(6,3,3,2,2),(7,1,1,1,1);
/*!40000 ALTER TABLE `carritosdecompras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoriasproductos`
--

DROP TABLE IF EXISTS `categoriasproductos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoriasproductos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoriasproductos`
--

LOCK TABLES `categoriasproductos` WRITE;
/*!40000 ALTER TABLE `categoriasproductos` DISABLE KEYS */;
INSERT INTO `categoriasproductos` VALUES (1,'Muebles'),(2,'Camas y colchones'),(3,'Decoracion y espejos'),(4,'Productos de baño'),(5,'Cocinas y electrodomesticos');
/*!40000 ALTER TABLE `categoriasproductos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ciudades`
--

DROP TABLE IF EXISTS `ciudades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciudades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `idPaises` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ciudades-paises_idx` (`idPaises`),
  CONSTRAINT `ciudades-paises` FOREIGN KEY (`idPaises`) REFERENCES `paises` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudades`
--

LOCK TABLES `ciudades` WRITE;
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` VALUES (1,'San Salvador',1),(2,'Peten',2),(3,'San Jose',3),(4,'Santiago',4),(5,'Monterrey',5);
/*!40000 ALTER TABLE `ciudades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `claseproductos`
--

DROP TABLE IF EXISTS `claseproductos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `claseproductos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `idCategoriasProductos` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `clase-categorias_idx` (`idCategoriasProductos`),
  CONSTRAINT `clase-categorias` FOREIGN KEY (`idCategoriasProductos`) REFERENCES `categoriasproductos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `claseproductos`
--

LOCK TABLES `claseproductos` WRITE;
/*!40000 ALTER TABLE `claseproductos` DISABLE KEYS */;
INSERT INTO `claseproductos` VALUES (1,'Mesas',1),(2,'Sillones',1),(3,'Camas',2),(4,'Espejos',3),(5,'Jarrones',3),(6,'Duchas',4),(7,'Cocinas',5);
/*!40000 ALTER TABLE `claseproductos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entregas`
--

DROP TABLE IF EXISTS `entregas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entregas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idFacturas` int NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `lugar` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `entregas-facturas_idx` (`idFacturas`),
  CONSTRAINT `entregas-facturas` FOREIGN KEY (`idFacturas`) REFERENCES `facturas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entregas`
--

LOCK TABLES `entregas` WRITE;
/*!40000 ALTER TABLE `entregas` DISABLE KEYS */;
INSERT INTO `entregas` VALUES (1,1,'2020-09-10','08:30:00','Casa'),(2,2,'2020-06-26','08:30:00','Casa'),(3,3,'2020-08-14','08:30:00','Oficina'),(4,1,'2020-10-03','08:30:00','Oficina');
/*!40000 ALTER TABLE `entregas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `existencias`
--

DROP TABLE IF EXISTS `existencias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `existencias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idProductos` int NOT NULL,
  `idSucursales` int NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `existencias-productos_idx` (`idProductos`),
  KEY `existencias-sucursales_idx` (`idSucursales`),
  CONSTRAINT `existencias-productos` FOREIGN KEY (`idProductos`) REFERENCES `productos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `existencias-sucursales` FOREIGN KEY (`idSucursales`) REFERENCES `sucursales` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `existencias`
--

LOCK TABLES `existencias` WRITE;
/*!40000 ALTER TABLE `existencias` DISABLE KEYS */;
INSERT INTO `existencias` VALUES (1,1,1,10),(2,2,2,15),(3,3,3,25),(4,4,4,6),(5,1,5,12),(6,2,1,22),(9,1,4,5);
/*!40000 ALTER TABLE `existencias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas`
--

DROP TABLE IF EXISTS `facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idUsuarios` int NOT NULL,
  `tipoDePago` varchar(45) NOT NULL,
  `idSucursales` int NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `numeroCarrito` int NOT NULL,
  `total` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `facturas-usuarios_idx` (`idUsuarios`),
  KEY `facturas-sucursales_idx` (`idSucursales`),
  CONSTRAINT `facturas-sucursales` FOREIGN KEY (`idSucursales`) REFERENCES `sucursales` (`id`),
  CONSTRAINT `facturas-usuarios` FOREIGN KEY (`idUsuarios`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas`
--

LOCK TABLES `facturas` WRITE;
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
INSERT INTO `facturas` VALUES (1,1,'Efectivo',1,'2020-06-14','08:30:00',1,350),(2,2,'Efectivo',2,'2020-08-24','14:00:00',2,325),(3,3,'Efectivo',3,'2020-11-09','16:00:35',3,130),(4,1,'Tarjeta',4,'2020-04-02','08:45:22',1,350),(5,2,'Tarjeta',1,'2020-06-12','06:30:00',2,325),(6,3,'Tarjeta',5,'2020-09-24','22:30:00',3,130);
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paises`
--

DROP TABLE IF EXISTS `paises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paises` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paises`
--

LOCK TABLES `paises` WRITE;
/*!40000 ALTER TABLE `paises` DISABLE KEYS */;
INSERT INTO `paises` VALUES (1,'El Salvador'),(2,'Guatemala'),(3,'Costa Rica'),(4,'Panama'),(5,'Mexico');
/*!40000 ALTER TABLE `paises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `precio` double NOT NULL,
  `dimensiones` varchar(45) NOT NULL,
  `materiales` varchar(45) NOT NULL,
  `coloresDisponibles` varchar(45) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `garantia` varchar(45) NOT NULL,
  `idClaseProductos` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `prodcutos-clase_idx` (`idClaseProductos`),
  CONSTRAINT `prodcutos-clase` FOREIGN KEY (`idClaseProductos`) REFERENCES `claseproductos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Mesa',125,'1.20x2.00x1.00 [m]','Madera','Negro, Blanco, Café','Modelo ME-01','1 año',1),(2,'Sillon',50,'0.70x1.00x1.00 [m]','Cuero','Negro, Blanco','Modelo SI-01','6 meses',2),(3,'Cama',100,'1.30x2.00x0.5 [m]','Espuma','Blanco, Beige','Model CA-01','1 año',3),(4,'Espejo',30,'radio 0.15 [m]','Vidrio','Blanco, Negro','Modelo ES-01','2 semanas',4);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sucursales`
--

DROP TABLE IF EXISTS `sucursales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sucursales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `direccion` varchar(45) NOT NULL,
  `idCiudades` int NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `horarios` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sucursales-ciudades_idx` (`idCiudades`),
  CONSTRAINT `sucursales-ciudades` FOREIGN KEY (`idCiudades`) REFERENCES `ciudades` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sucursales`
--

LOCK TABLES `sucursales` WRITE;
/*!40000 ALTER TABLE `sucursales` DISABLE KEYS */;
INSERT INTO `sucursales` VALUES (1,'Centro de San Salvador',1,'7465-2642','6:00 a.m - 8:00 p.m'),(2,'Centro de Peten',2,'7395-2526','6:00 a.m - 8:00 p.m'),(3,'Centro de San Jose',3,'7142-6468','6:00 a.m - 8:00 p.m'),(4,'Centro de Santiago',4,'7306-3729','6:00 a.m - 8:00 p.m'),(5,'Centro de Monterrey',5,'7149-0174','6:00 a.m - 8:00 p.m');
/*!40000 ALTER TABLE `sucursales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombreUsuario` varchar(45) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `segundoApellido` varchar(45) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `idioma` varchar(45) NOT NULL,
  `correoElectronico` varchar(45) NOT NULL,
  `contrasenna` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'pamelaabrego','Pamela','Abrego','Ramirez','7658-6598','Español','pamela@gmail.com','pamela1','San Salvador'),(2,'franciscofuentes','Francisco','Fuentes','--','7549-9246','Español','francisco@gmail.com','francisco1','San Miguel'),(3,'javierosorio','Javier','Osorio','Echeverria','7490-2486','Ingles','javier@gmail.com','javier1','San Salvador'),(32,'as','as','as','as','as','as','as','as','as');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-07 22:46:57
