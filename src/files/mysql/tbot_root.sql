-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 06. Apr 2017 um 10:20
-- Server-Version: 10.0.17-MariaDB-wsrep
-- PHP-Version: 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `tbot_root`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `tbot_results`
--

CREATE TABLE `tbot_results` (
  `tbot_id` int(5) NOT NULL,
  `test_date` datetime DEFAULT NULL,
  `toolchain` varchar(100) DEFAULT NULL,
  `binaryversion` varchar(250) DEFAULT NULL,
  `defname` varchar(100) DEFAULT NULL,
  `testcase` varchar(100) DEFAULT NULL,
  `success` tinyint(1) DEFAULT NULL,
  `stats_img` longblob,
  `stats_mimetype` varchar(32) DEFAULT NULL,
  `dot_img` longblob
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `tbot_results`
--
ALTER TABLE `tbot_results`
  ADD PRIMARY KEY (`tbot_id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `tbot_results`
--
ALTER TABLE `tbot_results`
  MODIFY `tbot_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
