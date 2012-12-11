-- phpMyAdmin SQL Dump
-- version 3.3.7deb7
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 11, 2012 at 08:26 PM
-- Server version: 5.1.49
-- PHP Version: 5.3.3-7+squeeze14

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `wallet`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'admin', 'ADMIN', 'Super', 'asd@asda.cc', 'pbkdf2_sha256$10000$6UznhEbwDy8y$qNe4HTvIOyt7WLqw+GFPg/aDBE9S0xS1YEcpmdg7THo=', 1, 1, 1, '2012-12-10 09:19:19', '2012-12-10 09:19:09'),
(2, 'Tom', 'Tom', 'Allen', '1@222.co', 'pbkdf2_sha256$10000$wcKYJW4kpg8F$GDpev4NrN4ypeMnenu1e+1qppthTCFpA5LSYPM4Lotw=', 0, 1, 0, '2012-12-10 09:19:41', '2012-12-10 09:19:41'),
(3, 'Alice', 'Alice', 'Chan', 'asd@as.cc', 'pbkdf2_sha256$10000$fTGZfg9hVfNq$nuPdAG4ALxl68D3cRkzn4S+pzFvhueW/9bsH/1XXnBM=', 0, 1, 0, '2012-12-10 09:20:01', '2012-12-10 09:20:01'),
(4, 'Jama', 'Jama', 'PUMA', 'asd@as.cc', 'pbkdf2_sha256$10000$ZEnDXAry4lct$QePY5gNuj95P1/PP+AjePBZqpk9/9G65bzGoGjHyDpI=', 0, 1, 0, '2012-12-10 09:20:22', '2012-12-10 09:20:22'),
(7, 'Tim', 'Tim', 'AAAAADDDMIN', 'asd@as.cc', 'pbkdf2_sha256$10000$p39wILM7goWB$uC3XRCoqXTwCJLYuEsR1oP2RJzlzFgcb+vB1Yw7MhKg=', 0, 1, 0, '2012-12-11 06:29:19', '2012-12-11 06:29:19');

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_article`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `meta_id` int(11) NOT NULL,
  `version` int(10) unsigned NOT NULL,
  `content` longtext NOT NULL,
  `time` datetime NOT NULL,
  `is_draft` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_article_9805f4bb` (`meta_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `wallet_wiki_article`
--

INSERT INTO `wallet_wiki_article` (`id`, `meta_id`, `version`, `content`, `time`, `is_draft`) VALUES
(1, 1, 0, '0', '2012-12-10 09:23:54', 0),
(2, 1, 1, '1', '2012-12-10 09:24:24', 0),
(3, 2, 0, '0', '2012-12-10 09:24:55', 0),
(4, 3, 0, '0', '2012-12-11 03:21:24', 0);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_articlemeta`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_articlemeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_articlemeta_cc846901` (`author_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `wallet_wiki_articlemeta`
--

INSERT INTO `wallet_wiki_articlemeta` (`id`, `title`, `author_id`) VALUES
(1, 'How to install Ubuntu', 2),
(2, 'Android2.3 clock design', 3),
(3, 'FreeBSD Network Configuration', 2);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_articlemeta_category`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_articlemeta_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `articlemeta_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `articlemeta_id` (`articlemeta_id`,`category_id`),
  KEY `wallet_wiki_articlemeta_category_3c93f1e` (`articlemeta_id`),
  KEY `wallet_wiki_articlemeta_category_42dc49bc` (`category_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `wallet_wiki_articlemeta_category`
--

INSERT INTO `wallet_wiki_articlemeta_category` (`id`, `articlemeta_id`, `category_id`) VALUES
(4, 1, 3),
(2, 2, 2),
(3, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_articlemeta_keyword`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_articlemeta_keyword` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `articlemeta_id` int(11) NOT NULL,
  `keyword_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `articlemeta_id` (`articlemeta_id`,`keyword_id`),
  KEY `wallet_wiki_articlemeta_keyword_3c93f1e` (`articlemeta_id`),
  KEY `wallet_wiki_articlemeta_keyword_a6434082` (`keyword_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `wallet_wiki_articlemeta_keyword`
--


-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_articlemeta_siting_article`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_articlemeta_siting_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_articlemeta_id` int(11) NOT NULL,
  `to_articlemeta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `from_articlemeta_id` (`from_articlemeta_id`,`to_articlemeta_id`),
  KEY `wallet_wiki_articlemeta_siting_article_4fac9428` (`from_articlemeta_id`),
  KEY `wallet_wiki_articlemeta_siting_article_4354934b` (`to_articlemeta_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `wallet_wiki_articlemeta_siting_article`
--

INSERT INTO `wallet_wiki_articlemeta_siting_article` (`id`, `from_articlemeta_id`, `to_articlemeta_id`) VALUES
(1, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_attachment`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_attachment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attachment_type` varchar(100) NOT NULL,
  `attachment_file` varchar(100) NOT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_attachment_30525a19` (`article_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `wallet_wiki_attachment`
--


-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_category`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `category_name` (`category_name`),
  KEY `wallet_wiki_category_63f17a16` (`parent_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `wallet_wiki_category`
--

INSERT INTO `wallet_wiki_category` (`id`, `category_name`, `parent_id`) VALUES
(1, 'Unix', NULL),
(2, 'Android', 3),
(3, 'Linux', 1);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_collection`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_collection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `collect_time` datetime NOT NULL,
  `belong_to_id` int(11) NOT NULL,
  `is_private` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_collection_30525a19` (`article_id`),
  KEY `wallet_wiki_collection_f6751186` (`belong_to_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `wallet_wiki_collection`
--

INSERT INTO `wallet_wiki_collection` (`id`, `article_id`, `collect_time`, `belong_to_id`, `is_private`) VALUES
(1, 3, '2012-12-10 09:25:09', 2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_collection_keyword`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_collection_keyword` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collection_id` int(11) NOT NULL,
  `keyword_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `collection_id` (`collection_id`,`keyword_id`),
  KEY `wallet_wiki_collection_keyword_26d6361e` (`collection_id`),
  KEY `wallet_wiki_collection_keyword_a6434082` (`keyword_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `wallet_wiki_collection_keyword`
--


-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_comment`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `content` longtext NOT NULL,
  `author_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_comment_cc846901` (`author_id`),
  KEY `wallet_wiki_comment_30525a19` (`article_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `wallet_wiki_comment`
--

INSERT INTO `wallet_wiki_comment` (`id`, `time`, `content`, `author_id`, `article_id`) VALUES
(1, '2012-12-11 11:56:44', 'Nice!\r\n', 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_inbox`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_inbox` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `wallet_wiki_inbox`
--

INSERT INTO `wallet_wiki_inbox` (`id`, `user_id`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(7, 7);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_keyword`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_keyword` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword_name` varchar(20) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_keyword_cc846901` (`author_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `wallet_wiki_keyword`
--

INSERT INTO `wallet_wiki_keyword` (`id`, `keyword_name`, `author_id`) VALUES
(1, 'linux system', 2),
(2, 'android tips', 3);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_userprofile`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `portrait` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `wallet_wiki_userprofile`
--

INSERT INTO `wallet_wiki_userprofile` (`id`, `user_id`, `nickname`, `portrait`) VALUES
(1, 1, 'Admin~~~', ''),
(2, 2, 'TOM', ''),
(3, 3, 'ALICE', ''),
(4, 4, 'JAMA', ''),
(7, 7, 'TIM', '');

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_userprofile_following`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_userprofile_following` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_userprofile_id` int(11) NOT NULL,
  `to_userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `from_userprofile_id` (`from_userprofile_id`,`to_userprofile_id`),
  KEY `wallet_wiki_userprofile_following_18161f41` (`from_userprofile_id`),
  KEY `wallet_wiki_userprofile_following_7e78b31c` (`to_userprofile_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `wallet_wiki_userprofile_following`
--

INSERT INTO `wallet_wiki_userprofile_following` (`id`, `from_userprofile_id`, `to_userprofile_id`) VALUES
(1, 3, 2),
(5, 2, 3),
(3, 4, 2),
(4, 4, 3);
