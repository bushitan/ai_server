/*
Navicat MySQL Data Transfer

Source Server         : a
Source Server Version : 50096
Source Host           : localhost:3306
Source Database       : ai_server

Target Server Type    : MYSQL
Target Server Version : 50096
File Encoding         : 65001

Date: 2019-02-15 09:20:28
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 群组', '7', 'add_group');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 群组', '7', 'change_group');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 群组', '7', 'delete_group');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 店铺', '8', 'add_shop');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 店铺', '8', 'change_shop');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 店铺', '8', 'delete_shop');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 用户', '9', 'add_user');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 用户', '9', 'change_user');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 用户', '9', 'delete_user');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 浏览记录', '10', 'add_trace');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 浏览记录', '10', 'change_trace');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 浏览记录', '10', 'delete_trace');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `password` varchar(128) NOT NULL,
  `last_login` datetime default NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$20000$XJd8BQBuxZeo$8ffsZQ++lcZMNNfaGosabaCx9EnPtrYODIQOHGwQneM=', '2019-02-15 01:16:37', '1', 'root', '', '', '3@163.com', '1', '1', '2019-02-05 13:41:49');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL auto_increment,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) default NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-02-05 14:58:49', '1', '店铺1', '1', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-02-05 14:59:02', '2', '店铺2', '1', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2019-02-05 14:59:09', '3', '店铺3', '1', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2019-02-05 14:59:18', '1', '用户1', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2019-02-05 14:59:20', '2', '用户2', '1', '', '9', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2019-02-05 15:00:05', '3', '3', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2019-02-05 15:00:12', '4', '4', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2019-02-05 15:00:17', '5', '5', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2019-02-05 15:00:23', '6', '6', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2019-02-05 15:00:28', '7', '7', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2019-02-05 15:36:17', '1', '店铺1', '2', '已修改 title，summary 和 cover 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2019-02-05 15:36:27', '2', '店铺2', '2', '已修改 title，summary 和 cover 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2019-02-05 15:36:34', '3', '店铺3', '2', '已修改 title，summary 和 cover 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2019-02-05 15:41:39', '1', '店铺1', '2', '已修改 user 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2019-02-05 15:41:43', '2', '店铺2', '2', '已修改 user 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2019-02-05 15:47:45', '3', '店铺3', '2', '已修改 user 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2019-02-05 15:49:52', '1', '店铺1', '2', '已修改 content 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2019-02-05 15:49:57', '2', '店铺2', '2', '已修改 content 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2019-02-05 15:50:01', '3', '店铺3', '2', '已修改 content 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2019-02-05 15:51:51', '4', '', '1', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2019-02-05 16:01:57', '5', '', '1', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2019-02-05 16:02:00', '5', '', '2', '没有字段被修改。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2019-02-05 16:02:59', '6', '', '1', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2019-02-05 16:25:38', '1', '用户1', '2', '已修改 wx_session_key 。', '9', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2019-02-06 01:16:47', '8', '8', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2019-02-06 01:16:50', '9', '9', '1', '', '10', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2019-02-06 01:28:19', '1', '店铺1', '2', '已修改 cover 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2019-02-06 01:29:24', '3', '店铺3', '2', '已修改 cover 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2019-02-06 01:31:19', '3', '店铺3', '2', '已修改 cover 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2019-02-06 02:05:01', '7', '', '2', '已修改 user 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2019-02-06 02:07:22', '3', '店铺3', '2', '已修改 user 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2019-02-06 02:07:26', '1', '店铺1', '2', '已修改 user 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2019-02-06 02:18:27', '1', '店铺1', '2', '已修改 content 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2019-02-07 05:33:58', '1', '店铺1', '2', '已修改 address 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2019-02-08 02:36:39', '1', '店铺1', '2', '已修改 latitude 和 longitude 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2019-02-08 02:36:53', '3', '店铺3', '2', '已修改 latitude 和 longitude 。', '8', '1');
INSERT INTO `django_admin_log` VALUES ('37', '2019-02-15 01:19:20', '67', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2019-02-15 01:19:20', '66', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2019-02-15 01:19:20', '65', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2019-02-15 01:19:20', '64', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2019-02-15 01:19:20', '63', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2019-02-15 01:19:20', '62', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2019-02-15 01:19:20', '61', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('44', '2019-02-15 01:19:20', '60', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('45', '2019-02-15 01:19:20', '59', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('46', '2019-02-15 01:19:20', '58', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('47', '2019-02-15 01:19:20', '57', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('48', '2019-02-15 01:19:20', '56', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('49', '2019-02-15 01:19:20', '55', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('50', '2019-02-15 01:19:20', '54', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('51', '2019-02-15 01:19:20', '53', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('52', '2019-02-15 01:19:20', '52', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('53', '2019-02-15 01:19:20', '51', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('54', '2019-02-15 01:19:20', '50', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('55', '2019-02-15 01:19:20', '49', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('56', '2019-02-15 01:19:20', '48', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('57', '2019-02-15 01:19:20', '47', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('58', '2019-02-15 01:19:20', '46', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('59', '2019-02-15 01:19:20', '45', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('60', '2019-02-15 01:19:20', '44', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('61', '2019-02-15 01:19:20', '43', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('62', '2019-02-15 01:19:20', '42', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('63', '2019-02-15 01:19:20', '41', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('64', '2019-02-15 01:19:20', '40', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('65', '2019-02-15 01:19:20', '39', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('66', '2019-02-15 01:19:20', '38', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('67', '2019-02-15 01:19:20', '37', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('68', '2019-02-15 01:19:20', '36', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('69', '2019-02-15 01:19:20', '35', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('70', '2019-02-15 01:19:20', '34', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('71', '2019-02-15 01:19:20', '33', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('72', '2019-02-15 01:19:20', '32', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('73', '2019-02-15 01:19:20', '31', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('74', '2019-02-15 01:19:20', '30', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('75', '2019-02-15 01:19:20', '29', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('76', '2019-02-15 01:19:20', '28', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('77', '2019-02-15 01:19:20', '27', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('78', '2019-02-15 01:19:20', '26', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('79', '2019-02-15 01:19:20', '25', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('80', '2019-02-15 01:19:20', '24', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('81', '2019-02-15 01:19:20', '23', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('82', '2019-02-15 01:19:20', '21', '', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('83', '2019-02-15 01:19:20', '16', '', '3', '', '8', '1');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('7', 'lite', 'group');
INSERT INTO `django_content_type` VALUES ('8', 'lite', 'shop');
INSERT INTO `django_content_type` VALUES ('10', 'lite', 'trace');
INSERT INTO `django_content_type` VALUES ('9', 'lite', 'user');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL auto_increment,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-02-05 13:41:31');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-02-05 13:41:32');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-02-05 13:41:32');
INSERT INTO `django_migrations` VALUES ('4', 'contenttypes', '0002_remove_content_type_name', '2019-02-05 13:41:32');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0002_alter_permission_name_max_length', '2019-02-05 13:41:32');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0003_alter_user_email_max_length', '2019-02-05 13:41:32');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0004_alter_user_username_opts', '2019-02-05 13:41:32');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0005_alter_user_last_login_null', '2019-02-05 13:41:32');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0006_require_contenttypes_0002', '2019-02-05 13:41:32');
INSERT INTO `django_migrations` VALUES ('10', 'sessions', '0001_initial', '2019-02-05 13:41:32');
INSERT INTO `django_migrations` VALUES ('11', 'lite', '0001_initial', '2019-02-05 13:43:33');
INSERT INTO `django_migrations` VALUES ('12', 'lite', '0002_auto_20190205_2221', '2019-02-05 14:21:26');
INSERT INTO `django_migrations` VALUES ('13', 'lite', '0003_auto_20190205_2236', '2019-02-05 14:36:26');
INSERT INTO `django_migrations` VALUES ('14', 'lite', '0004_auto_20190205_2256', '2019-02-05 14:57:13');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('1gcdz56ipo0snkzwubtlrgzrq3venonj', 'NzJlODZmNGY2ZmVmODFhNWEyMDE5ODg3ZTM4YThmMjlkYmIzM2E4ODp7Il9hdXRoX3VzZXJfaGFzaCI6ImYwZTNlMzYwZGEyYWVlNTY0MjJjZTZkNzFmNjRjZDg0NjNiN2EzOGUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-02-19 13:42:13');
INSERT INTO `django_session` VALUES ('38daim7hfh8nlyxsucf1s7np7jo258fu', 'NzJlODZmNGY2ZmVmODFhNWEyMDE5ODg3ZTM4YThmMjlkYmIzM2E4ODp7Il9hdXRoX3VzZXJfaGFzaCI6ImYwZTNlMzYwZGEyYWVlNTY0MjJjZTZkNzFmNjRjZDg0NjNiN2EzOGUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-02-25 01:25:24');
INSERT INTO `django_session` VALUES ('9f2z620jjk3jx8ok8ebgwijuw95qf6j0', 'NzJlODZmNGY2ZmVmODFhNWEyMDE5ODg3ZTM4YThmMjlkYmIzM2E4ODp7Il9hdXRoX3VzZXJfaGFzaCI6ImYwZTNlMzYwZGEyYWVlNTY0MjJjZTZkNzFmNjRjZDg0NjNiN2EzOGUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-03-01 01:16:37');
INSERT INTO `django_session` VALUES ('tanmwwlsslrbhn9jvx2fr9krunvop9ji', 'NzJlODZmNGY2ZmVmODFhNWEyMDE5ODg3ZTM4YThmMjlkYmIzM2E4ODp7Il9hdXRoX3VzZXJfaGFzaCI6ImYwZTNlMzYwZGEyYWVlNTY0MjJjZTZkNzFmNjRjZDg0NjNiN2EzOGUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-02-21 05:30:01');

-- ----------------------------
-- Table structure for `lite_group`
-- ----------------------------
DROP TABLE IF EXISTS `lite_group`;
CREATE TABLE `lite_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) default NULL,
  `mode` int(11) NOT NULL,
  `keyword` varchar(100) default NULL,
  `qr_url` varchar(100) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of lite_group
-- ----------------------------

-- ----------------------------
-- Table structure for `lite_poi`
-- ----------------------------
DROP TABLE IF EXISTS `lite_poi`;
CREATE TABLE `lite_poi` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(32) default NULL,
  `type` int(11) NOT NULL,
  `latitude` double default NULL,
  `longitude` double default NULL,
  `phone` varchar(32) default NULL,
  `address` varchar(50) default NULL,
  `postcode` varchar(32) default NULL,
  `category` varchar(32) default NULL,
  `boundary` varchar(32) default NULL,
  `panoinfo` varchar(100) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of lite_poi
-- ----------------------------

-- ----------------------------
-- Table structure for `lite_shop`
-- ----------------------------
DROP TABLE IF EXISTS `lite_shop`;
CREATE TABLE `lite_shop` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(32) default NULL,
  `logo` varchar(500) default NULL,
  `cover` varchar(500) default NULL,
  `shop_time` varchar(32) default NULL,
  `display_type` int(11) NOT NULL,
  `content` longtext,
  `wx_content_url` varchar(500) default NULL,
  `type` int(11) NOT NULL,
  `latitude` double default NULL,
  `longitude` double default NULL,
  `phone` varchar(32) default NULL,
  `address` varchar(50) default NULL,
  `postcode` varchar(32) default NULL,
  `category` varchar(32) default NULL,
  `boundary` varchar(32) default NULL,
  `panoinfo` varchar(100) default NULL,
  `date` varchar(100) default NULL,
  `group_id` int(11) default NULL,
  `summary` varchar(32) default NULL,
  `title` varchar(32) default NULL,
  `user_id` int(11) default NULL,
  PRIMARY KEY  (`id`),
  KEY `lite_shop_group_id_f9caaa8_fk_lite_group_id` (`group_id`),
  KEY `lite_shop_e8701ad4` (`user_id`),
  CONSTRAINT `lite_shop_group_id_f9caaa8_fk_lite_group_id` FOREIGN KEY (`group_id`) REFERENCES `lite_group` (`id`),
  CONSTRAINT `lite_shop_user_id_167056e1_fk_lite_user_id` FOREIGN KEY (`user_id`) REFERENCES `lite_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of lite_shop
-- ----------------------------
INSERT INTO `lite_shop` VALUES ('1', '店铺1', '', '../../images/group2.jpg', '', '0', '<img class=\"xing-img\" style=\"width: 100%\" src=\"http://img.12xiong.top/ai_server_2019_02_03_16_10_41.jpg\" _height=\"1\" _uploaded=\"true\"></img><p class=\"xing-p\">321321</p><p class=\"xing-p\">sadsad</p>', '', '0', '22.8367877155', '108.2931911945', '', '请求区东路', '', '', '', '', '', null, '简介1', '标题1321321', '3');
INSERT INTO `lite_shop` VALUES ('2', '店铺2', '', '封面2', '', '0', '展示内容222', '', '0', '1', '1', '', '', '', '', '', '', '', null, '简介2', '标题2', '2');
INSERT INTO `lite_shop` VALUES ('3', '店铺3', '', '../../images/group1.jpg', '', '0', '展示内容333', '', '0', '22.8371535653', '108.2913136482', '', '', '', '', '', '', '', null, '简介3', '标题3', '3');

-- ----------------------------
-- Table structure for `lite_trace`
-- ----------------------------
DROP TABLE IF EXISTS `lite_trace`;
CREATE TABLE `lite_trace` (
  `id` int(11) NOT NULL auto_increment,
  `shop_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `lite_trace_shop_id_7afb0ea2_fk_lite_shop_id` (`shop_id`),
  KEY `lite_trace_e8701ad4` (`user_id`),
  CONSTRAINT `lite_trace_shop_id_7afb0ea2_fk_lite_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `lite_shop` (`id`),
  CONSTRAINT `lite_trace_user_id_449e375d_fk_lite_user_id` FOREIGN KEY (`user_id`) REFERENCES `lite_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of lite_trace
-- ----------------------------
INSERT INTO `lite_trace` VALUES ('3', '1', '1');
INSERT INTO `lite_trace` VALUES ('4', '2', '1');
INSERT INTO `lite_trace` VALUES ('5', '3', '1');
INSERT INTO `lite_trace` VALUES ('6', '1', '2');
INSERT INTO `lite_trace` VALUES ('7', '2', '2');
INSERT INTO `lite_trace` VALUES ('8', '1', '3');
INSERT INTO `lite_trace` VALUES ('9', '3', '3');

-- ----------------------------
-- Table structure for `lite_user`
-- ----------------------------
DROP TABLE IF EXISTS `lite_user`;
CREATE TABLE `lite_user` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) default NULL,
  `nick_name` varchar(100) default NULL,
  `avatar_url` varchar(100) default NULL,
  `gender` varchar(100) default NULL,
  `city` varchar(100) default NULL,
  `province` varchar(100) default NULL,
  `country` varchar(100) default NULL,
  `wx_open_id` varchar(50) default NULL,
  `wx_session_key` varchar(128) default NULL,
  `wx_union_id` varchar(50) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of lite_user
-- ----------------------------
INSERT INTO `lite_user` VALUES ('1', '用户1', '', '', '', '', '', '', '', '123', '');
INSERT INTO `lite_user` VALUES ('2', '用户2', '', '', '', '', '', '', '', '', '');
INSERT INTO `lite_user` VALUES ('3', '', null, null, null, null, null, null, 'oVM294kPuEBgUzb7Q5HCFLAnoOE8', 'Kzaz6rmQQplQ+OKd+y7fxg==', 'oAmjlw_UfKePdYbf1XWudgxSZjis');
INSERT INTO `lite_user` VALUES ('4', '', null, null, null, null, null, null, 'oVM294kGn7OExagdeqUO8Lfx-C_M', 'zRkwDWj4qI7bSkycwMTotQ==', 'oAmjlw0h5P0BtjOwwa_JmwurqLIw');
