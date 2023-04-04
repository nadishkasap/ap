-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 04, 2023 at 06:10 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quiz`
--

-- --------------------------------------------------------

--
-- Table structure for table `exam_marks`
--

DROP TABLE IF EXISTS `exam_marks`;
CREATE TABLE IF NOT EXISTS `exam_marks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `exam_id` varchar(10) NOT NULL,
  `marks` float NOT NULL,
  `Status` varchar(7) NOT NULL,
  `date_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `exam_marks`
--

INSERT INTO `exam_marks` (`id`, `user_id`, `exam_id`, `marks`, `Status`, `date_time`) VALUES
(2, 2, 'FGSMIT2022', 50, 'Pass', '2023-04-04 03:25:42'),
(3, 2, 'FGSMIT2023', 100, 'Pass', '2023-04-04 03:25:49'),
(4, 2, 'FGSMIT2022', 0, 'Fail', '2023-04-04 19:20:07'),
(5, 2, 'FGSMIT2022', 100, 'Pass', '2023-04-04 19:20:16'),
(6, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 19:48:51'),
(7, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 19:56:24'),
(8, 2, 'FGSMIT2021', 100, 'Pass', '2023-04-04 20:13:34'),
(9, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 20:15:57'),
(10, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 20:17:19'),
(11, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:20:57'),
(12, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:21:14'),
(13, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:21:58'),
(14, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:22:12'),
(15, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:22:32'),
(16, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 20:24:21'),
(17, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 20:24:36'),
(18, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:25:47'),
(19, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:25:58'),
(20, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:26:22'),
(21, 2, 'FGSMIT2021', 100, 'Pass', '2023-04-04 20:31:44'),
(22, 2, 'FGSMIT2021', 100, 'Pass', '2023-04-04 20:31:56'),
(23, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:32:15'),
(24, 2, 'FGSMIT2021', 100, 'Pass', '2023-04-04 20:32:36'),
(25, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:34:57'),
(26, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:35:35'),
(27, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:36:46'),
(28, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:37:52'),
(29, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:38:32'),
(30, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 20:39:26'),
(31, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 20:42:47'),
(32, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 20:54:58'),
(33, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 20:57:41'),
(34, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 21:00:52'),
(35, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 21:46:35'),
(36, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 21:47:24'),
(37, 4, 'FGSMIT2022', 0, 'Fail', '2023-04-04 22:02:35'),
(38, 2, 'FGSMIT2021', 0, 'Fail', '2023-04-04 22:03:41'),
(39, 2, 'FGSMIT2021', 100, 'Pass', '2023-04-04 22:04:25'),
(40, 2, 'FGSMIT2021', 50, 'Pass', '2023-04-04 22:04:37');

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
CREATE TABLE IF NOT EXISTS `question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` varchar(255) DEFAULT NULL,
  `answer1` varchar(255) DEFAULT NULL,
  `answer2` varchar(255) DEFAULT NULL,
  `answer3` varchar(255) DEFAULT NULL,
  `answert4` varchar(255) DEFAULT NULL,
  `correctAnswer` int DEFAULT NULL,
  `examType` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`id`, `question`, `answer1`, `answer2`, `answer3`, `answert4`, `correctAnswer`, `examType`) VALUES
(6, '____ appear at the bottom of the Excel window.', 'Title bar', 'Formula bar', 'Work sheet tabs', 'Name box', 3, 'FGSMIT2021'),
(7, 'What are the basic rectangular building blocks of a spreadsheet?', 'Cells', 'Zoom slider', 'Help button', 'All of these', 2, 'FGSMIT2021'),
(8, 'Which of the following is not a term pertaining to spreadsheets?', 'Cell', 'Character', 'Browser', 'Formula', 3, 'FGSMIT2022'),
(9, 'Another name for a pre-programmed formula in Excel is', 'Cell', 'Graph', 'Function', 'Range', 3, 'FGSMIT2022'),
(10, 'Excel is a program that is used to prepare a', 'Slide presentation', 'Spreadsheet', 'Text document', 'Database', 2, 'FGSMIT2023');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(255) DEFAULT NULL,
  `lname` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `passW` varchar(255) DEFAULT NULL,
  `userType` int DEFAULT NULL,
  `marks` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `fname`, `lname`, `email`, `passW`, `userType`, `marks`) VALUES
(1, 'Sheyan', 'Suraweera', 'sheyanns@gmail.com', '123456', 1, NULL),
(2, 'Gayan', 'Prasad', 'gayan@gmail.com', '123789', 2, NULL),
(4, 'Amith', 'Prasannaa', 'saman@gmail.com', '123666', 2, NULL),
(5, 'Anjula', 'Student', 'anjula@gmail.com', '554466', 1, NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
