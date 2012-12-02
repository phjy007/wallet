-- phpMyAdmin SQL Dump
-- version 3.3.7deb7
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 01, 2012 at 03:44 PM
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
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`

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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'admin', 'Admin', 'Super', 'asd@ad.cc', 'pbkdf2_sha256$10000$py6oa09adjyA$D8HE9AOTCHeIqkjy8j8s1ru8okWDPRKyqJj8IxTUT/0=', 1, 1, 1, '2012-11-30 12:50:43', '2012-11-30 12:50:22'),
(2, 'Jama', 'Jama', 'Chan', 'tom@gmail.com', 'pbkdf2_sha256$10000$gCdo2B0XEvi0$wndwRT7n2Z1+4T8/GPmdBkiYKNmGE638Kd3XUwU+eWo=', 0, 1, 0, '2012-11-30 12:51:34', '2012-11-30 12:51:34'),
(3, 'Tom', 'Tom', 'Allen', 'phjy007@gmail.com', 'pbkdf2_sha256$10000$fUbrvPorLczf$D+oFDRG3Hp63G/q+KbobED79slf9wJoKl7WXKcn1a38=', 0, 1, 0, '2012-11-30 12:54:37', '2012-11-30 12:54:37'),
(4, 'Alice', 'Alice', 'Chan', 'tom@gmail.com', 'pbkdf2_sha256$10000$yO56CBMVkWy9$vX3128lwE3ttwPEKO4cUb8KY4N2m4tPZ21IG4hNbXfI=', 0, 1, 0, '2012-11-30 12:55:21', '2012-11-30 12:55:21');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_groups`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=44 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2012-11-30 12:50:50', 1, 10, '1', 'admin''s profile', 2, 'Changed nickname.'),
(2, '2012-11-30 12:53:37', 1, 10, '2', 'Jama''s profile', 2, 'Changed nickname.'),
(3, '2012-11-30 12:54:37', 1, 3, '3', 'Tom', 1, ''),
(4, '2012-11-30 12:54:58', 1, 3, '3', 'Tom', 2, 'Changed password, first_name, last_name and email. Changed nickname for user profile "Tom''s profile".'),
(5, '2012-11-30 12:55:22', 1, 3, '4', 'Alice', 1, ''),
(6, '2012-11-30 12:55:37', 1, 3, '4', 'Alice', 2, 'Changed password, first_name, last_name and email. Changed nickname and following for user profile "Alice''s profile".'),
(7, '2012-11-30 12:55:44', 1, 3, '3', 'Tom', 2, 'Changed password. Changed following for user profile "Tom''s profile".'),
(8, '2012-11-30 12:59:50', 1, 14, '1', 'Linux Webserver', 1, ''),
(9, '2012-11-30 13:00:05', 1, 14, '2', 'Android Security', 1, ''),
(10, '2012-11-30 13:00:15', 1, 14, '3', 'Unix History', 1, ''),
(11, '2012-11-30 13:00:29', 1, 14, '4', 'Programming tips', 1, ''),
(12, '2012-11-30 13:01:43', 1, 10, '2', 'Jama''s profile', 2, 'Changed following.'),
(13, '2012-11-30 13:26:48', 1, 13, '1', 'Linux', 1, ''),
(14, '2012-11-30 13:26:53', 1, 13, '2', 'Windows', 1, ''),
(15, '2012-11-30 13:26:56', 1, 13, '3', 'Unix', 1, ''),
(16, '2012-11-30 13:27:00', 1, 13, '1', 'Linux', 2, 'Changed parent.'),
(17, '2012-11-30 13:27:05', 1, 13, '4', 'Android', 1, ''),
(18, '2012-11-30 13:27:12', 1, 13, '5', 'OS X', 1, ''),
(19, '2012-11-30 13:45:53', 1, 15, '1', 'META -How to install Ubuntu', 1, ''),
(20, '2012-11-30 13:46:16', 1, 15, '2', 'META -The way to uninstall Windows 7', 1, ''),
(21, '2012-11-30 13:46:40', 1, 15, '3', 'META -Limit the power consumer for Android', 1, ''),
(22, '2012-11-30 13:47:07', 1, 15, '4', 'META -How to install Ubuntu12.04', 1, ''),
(23, '2012-11-30 13:53:06', 1, 14, '5', 'OS installation', 1, ''),
(24, '2012-11-30 13:53:26', 1, 14, '6', 'Ubuntu Operation', 1, ''),
(25, '2012-11-30 13:53:56', 1, 14, '7', 'Mobile', 1, ''),
(26, '2012-11-30 13:54:06', 1, 14, '8', 'Android Tips', 1, ''),
(27, '2012-11-30 13:54:30', 1, 15, '1', 'META -How to install Ubuntu', 2, 'Changed keyword.'),
(28, '2012-11-30 13:54:39', 1, 15, '3', 'META -Limit the power consumer for Android', 2, 'Changed keyword.'),
(29, '2012-11-30 13:56:48', 1, 16, '1', 'ARTICLE -How to install Ubuntu', 1, ''),
(30, '2012-11-30 13:56:51', 1, 16, '1', 'ARTICLE -How to install Ubuntu', 2, 'No fields changed.'),
(31, '2012-11-30 13:57:01', 1, 16, '2', 'ARTICLE -How to install Ubuntu', 1, ''),
(32, '2012-11-30 13:57:09', 1, 16, '3', 'ARTICLE -How to install Ubuntu', 1, ''),
(33, '2012-11-30 13:57:16', 1, 16, '4', 'ARTICLE -Limit the power consumer for Android', 1, ''),
(34, '2012-11-30 13:57:32', 1, 16, '5', 'ARTICLE -Limit the power consumer for Android', 1, ''),
(35, '2012-12-01 02:44:45', 1, 17, '4', 'Collection object', 1, ''),
(36, '2012-12-01 02:48:02', 1, 17, '3', 'How to install Ubuntu12.04 v2', 2, 'Changed belong_to.'),
(37, '2012-12-01 03:59:29', 1, 18, '1', 'Comment object', 1, ''),
(38, '2012-12-01 04:14:31', 1, 18, '2', 'Limit the power consumer for Android v0', 1, ''),
(39, '2012-12-01 04:32:51', 1, 3, '1', 'admin', 2, 'Changed password. Changed portrait for user profile "admin''s profile".'),
(40, '2012-12-01 04:33:02', 1, 3, '2', 'Jama', 2, 'Changed password, first_name, last_name and email.'),
(41, '2012-12-01 04:40:42', 1, 19, '1', 'How to install Ubuntu v2', 1, ''),
(42, '2012-12-01 04:41:49', 1, 19, '1', 'How to install Ubuntu v2', 3, ''),
(43, '2012-12-01 04:41:59', 1, 19, '2', 'How to install Ubuntu v2', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--
-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('48db1bbd9bbe998c7a781efca1b79151', 'OGZmMTcxNWNkYzE4NzkxYTMzODJkMGQ2ZGZkM2NhNmQwZGE3ZTc4MjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2012-12-14 12:50:43');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

-- --------------------------------------------------------

--
-- Table structure for table `tastypie_apiaccess`
--

CREATE TABLE IF NOT EXISTS `tastypie_apiaccess` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identifier` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `request_method` varchar(10) NOT NULL,
  `accessed` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `tastypie_apiaccess`
--


-- --------------------------------------------------------

--
-- Table structure for table `tastypie_apikey`
--

CREATE TABLE IF NOT EXISTS `tastypie_apikey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `key` varchar(256) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `tastypie_apikey`
--


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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `wallet_wiki_article`
--

INSERT INTO `wallet_wiki_article` (`id`, `meta_id`, `version`, `content`, `time`, `is_draft`) VALUES
(1, 1, 0, 'version 0', '2012-11-30 13:56:51', 0),
(2, 1, 1, 'version 1', '2012-11-30 13:57:01', 0),
(3, 1, 2, 'version 2', '2012-11-30 13:57:09', 0),
(4, 3, 0, 'version 1', '2012-11-30 13:57:16', 0),
(5, 3, 1, 'version 1\r\n', '2012-11-30 13:57:32', 0);

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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `wallet_wiki_articlemeta`
--

INSERT INTO `wallet_wiki_articlemeta` (`id`, `title`, `author_id`) VALUES
(1, 'How to install Ubuntu', 3),
(2, 'The way to uninstall Windows 7', 4),
(3, 'Limit the power consumer for Android', 2),
(4, 'How to install Ubuntu12.04', 2);

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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `wallet_wiki_articlemeta_category`
--

INSERT INTO `wallet_wiki_articlemeta_category` (`id`, `articlemeta_id`, `category_id`) VALUES
(5, 1, 1),
(2, 2, 2),
(6, 3, 4),
(4, 4, 1);

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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `wallet_wiki_articlemeta_keyword`
--

INSERT INTO `wallet_wiki_articlemeta_keyword` (`id`, `articlemeta_id`, `keyword_id`) VALUES
(1, 1, 5),
(2, 1, 6),
(3, 3, 8),
(4, 3, 7);

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
(1, 4, 1);

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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `wallet_wiki_attachment`
--

INSERT INTO `wallet_wiki_attachment` (`id`, `attachment_type`, `attachment_file`, `article_id`) VALUES
(2, 'Image', 'attachment/Tom/How to install Ubuntu/afa552adb67463651f17a2b4.jpg', 3);

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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `wallet_wiki_category`
--

INSERT INTO `wallet_wiki_category` (`id`, `category_name`, `parent_id`) VALUES
(1, 'Linux', 3),
(2, 'Windows', NULL),
(3, 'Unix', NULL),
(4, 'Android', 1),
(5, 'OS X', 3);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_collection`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_collection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_meta_id` int(11) NOT NULL,
  `article_version` int(10) unsigned NOT NULL,
  `collect_time` datetime NOT NULL,
  `belong_to_id` int(11) NOT NULL,
  `is_private` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_collection_da6361b6` (`article_meta_id`),
  KEY `wallet_wiki_collection_f6751186` (`belong_to_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `wallet_wiki_collection`
--

INSERT INTO `wallet_wiki_collection` (`id`, `article_meta_id`, `article_version`, `collect_time`, `belong_to_id`, `is_private`) VALUES
(3, 4, 2, '2012-12-01 02:48:02', 3, 0);

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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `wallet_wiki_comment`
--

INSERT INTO `wallet_wiki_comment` (`id`, `time`, `content`, `author_id`, `article_id`) VALUES
(1, '2012-12-01 03:59:29', 'Good wiki!', 4, 3),
(2, '2012-12-01 04:14:31', 'Nice wiki!', 2, 4);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_inbox`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_inbox` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `wallet_wiki_inbox`
--


-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_inboxitem`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_inboxitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `inbox_id` int(11) NOT NULL,
  `msg_type` int(11) NOT NULL,
  `brief_content` longtext NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_inboxitem_e569965d` (`inbox_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `wallet_wiki_inboxitem`
--


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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `wallet_wiki_keyword`
--

INSERT INTO `wallet_wiki_keyword` (`id`, `keyword_name`, `author_id`) VALUES
(1, 'Linux Webserver', 1),
(2, 'Android Security', 3),
(3, 'Unix History', 4),
(4, 'Programming tips', 2),
(5, 'OS installation', 3),
(6, 'Ubuntu Operation', 3),
(7, 'Mobile', 2),
(8, 'Android Tips', 2);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_message`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_user_id` int(11) NOT NULL,
  `to_user_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  `time` datetime NOT NULL,
  `has_read` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `from_user_id` (`from_user_id`),
  UNIQUE KEY `to_user_id` (`to_user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `wallet_wiki_message`
--


-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_region`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `name` varchar(30) NOT NULL,
  `region_type` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_region_63f17a16` (`parent_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `wallet_wiki_region`
--


-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_ticket`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `create_ts` datetime NOT NULL,
  `submitter_email` varchar(75) NOT NULL,
  `priority` varchar(1) NOT NULL,
  `description` longtext NOT NULL,
  `status` varchar(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `wallet_wiki_ticket`
--


-- --------------------------------------------------------

--
-- Table structure for table `wallet_wiki_ticketcomment`
--

CREATE TABLE IF NOT EXISTS `wallet_wiki_ticketcomment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ticket_id` int(11) NOT NULL,
  `comment_ts` datetime NOT NULL,
  `commenter_email` varchar(75) NOT NULL,
  `comment` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wallet_wiki_ticketcomment_d0fb4622` (`ticket_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `wallet_wiki_ticketcomment`
--


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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `wallet_wiki_userprofile`
--

INSERT INTO `wallet_wiki_userprofile` (`id`, `user_id`, `nickname`, `portrait`) VALUES
(1, 1, 'Admin~~~', 'user/admin/portrait/h_large_Mvgn_55a300001ff61375.jpg'),
(2, 2, 'JamaLIN!!!', ''),
(3, 3, 'TOM_NO_!', ''),
(4, 4, 'ALICE', '');

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
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `wallet_wiki_userprofile_following`
--

INSERT INTO `wallet_wiki_userprofile_following` (`id`, `from_userprofile_id`, `to_userprofile_id`) VALUES
(1, 4, 3),
(2, 3, 4),
(3, 2, 3),
(4, 2, 4);
