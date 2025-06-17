-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Июн 17 2025 г., 16:46
-- Версия сервера: 8.0.42
-- Версия PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+03:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `solarmonitoring_db`
--

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'users');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can moderate content', 6, 'can_moderate'),
(26, 'Can view analytics', 6, 'can_view_analytics'),
(27, 'Can add solar station', 7, 'add_solarstation'),
(28, 'Can change solar station', 7, 'change_solarstation'),
(29, 'Can delete solar station', 7, 'delete_solarstation'),
(30, 'Can view solar station', 7, 'view_solarstation'),
(31, 'Can add energy data', 8, 'add_energydata'),
(32, 'Can change energy data', 8, 'change_energydata'),
(33, 'Can delete energy data', 8, 'delete_energydata'),
(34, 'Can view energy data', 8, 'view_energydata'),
(35, 'Can add sale advertisement', 9, 'add_saleadvertisement'),
(36, 'Can change sale advertisement', 9, 'change_saleadvertisement'),
(37, 'Can delete sale advertisement', 9, 'delete_saleadvertisement'),
(38, 'Can view sale advertisement', 9, 'view_saleadvertisement'),
(39, 'Can add support request', 10, 'add_supportrequest'),
(40, 'Can change support request', 10, 'change_supportrequest'),
(41, 'Can delete support request', 10, 'delete_supportrequest'),
(42, 'Can view support request', 10, 'view_supportrequest'),
(43, 'Can add Станция', 11, 'add_station'),
(44, 'Can change Станция', 11, 'change_station'),
(45, 'Can delete Станция', 11, 'delete_station'),
(46, 'Can view Станция', 11, 'view_station');

-- --------------------------------------------------------

--
-- Структура таблицы `core_energydata`
--

CREATE TABLE `core_energydata` (
  `id` bigint NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `station_id` bigint NOT NULL,
  `efficiency` double DEFAULT NULL,
  `generation` double NOT NULL,
  `temperature` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `core_saleadvertisement`
--

CREATE TABLE `core_saleadvertisement` (
  `id` bigint NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `core_solarstation`
--

CREATE TABLE `core_solarstation` (
  `id` bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `capacity` double NOT NULL,
  `owner_id` bigint NOT NULL,
  `installation_date` date NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `last_checked` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `core_station`
--

CREATE TABLE `core_station` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `location` longtext NOT NULL,
  `system_type` varchar(50) NOT NULL,
  `installed_power` double NOT NULL,
  `installation_date` date NOT NULL,
  `panel_count` int UNSIGNED NOT NULL,
  `panel_type` varchar(50) NOT NULL,
  `panel_power` double NOT NULL,
  `panel_manufacturer` varchar(255) NOT NULL,
  `tilt_angle` double NOT NULL,
  `orientation` varchar(50) NOT NULL,
  `inverter_type` varchar(50) NOT NULL,
  `inverter_power` double NOT NULL,
  `inverter_manufacturer` varchar(255) NOT NULL,
  `controller_type` varchar(50) NOT NULL,
  `battery_type` varchar(50) NOT NULL,
  `battery_count` int UNSIGNED NOT NULL,
  `battery_capacity_single` double NOT NULL,
  `battery_voltage` varchar(10) NOT NULL,
  `battery_manufacturer` varchar(255) NOT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL
) ;

--
-- Дамп данных таблицы `core_station`
--

INSERT INTO `core_station` (`id`, `name`, `location`, `system_type`, `installed_power`, `installation_date`, `panel_count`, `panel_type`, `panel_power`, `panel_manufacturer`, `tilt_angle`, `orientation`, `inverter_type`, `inverter_power`, `inverter_manufacturer`, `controller_type`, `battery_type`, `battery_count`, `battery_capacity_single`, `battery_voltage`, `battery_manufacturer`, `latitude`, `longitude`) VALUES
(1, 'СЭС на крыше дома', 'ул. Ленина, д. 45, г. Москва', 'Гибридная', 6, '2023-05-15', 24, 'Монокристалл', 300, 'SunPower', 35, 'Южное', 'Гибридный', 5, 'Growatt', 'MPPT', 'Литиевые', 8, 2.5, '48 В', 'Pylontech', 55.751244, 37.618423),
(2, 'Солнечная станция \"Запад\"', 'г. Екатеринбург, ул. Космонавтов, д. 12', 'Сетевая', 10, '2022-09-20', 40, 'Поликристалл', 250, 'Canadian Solar', 45, 'Юго-западное', 'Сетевой', 10, 'SMA', 'PWM', 'AGM', 4, 2, '24 В', 'EnerSys', 56.838746, 60.606596),
(3, 'Автономная СЭС на даче', 'Ленинградская область, посёлок Солнечный', 'Автономная', 2.5, '2024-03-10', 10, 'Тонкая плёнка', 250, 'First Solar', 20, 'Южное', 'Автономный', 3, 'OutBack', 'MPPT', 'Свинцово-кислотные', 6, 1.5, '12 В', 'Exide', 59.222759, 30.498888),
(4, 'bykki', 'Локнянский муниципальный округ, Псковская область, Северо-Западный федеральный округ, Россия', 'Сетевая', 4, '2023-12-04', 5, 'Поликристалл', 4, '5', 5, '5', 'Гибридный', 5, '5', 'PWM', 'AGM', 5, 5, '24 В', '5', 57.088515327886505, 30.651855468750004);

-- --------------------------------------------------------

--
-- Структура таблицы `core_supportrequest`
--

CREATE TABLE `core_supportrequest` (
  `id` bigint NOT NULL,
  `subject` varchar(200) NOT NULL,
  `message` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `core_user`
--

CREATE TABLE `core_user` (
  `id` bigint NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `is_operator` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `core_user`
--

INSERT INTO `core_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `phone`, `is_operator`) VALUES
(1, 'pbkdf2_sha256$1000000$u1pnYNYT694sMRDZ4ncedb$TaaJ755FHKp6lhPWcBGm4DsJ8HnuxIYwrc6QLA0RckE=', '2025-06-08 01:22:05.353842', 1, 'root', '', '', 'za-zhegalka@internet.ru', 1, 1, '2025-05-24 12:31:52.924419', '', 1),
(2, 'pbkdf2_sha256$1000000$LgpAulzzYS3NAUW9QfOqve$Fh6gLmwZuNQE6o5SL6YPpdsAjY1mA/hodLAf6fazBMU=', '2025-06-17 12:41:45.460320', 0, 'user1', '', '', 'email1@email.com', 0, 1, '2025-05-24 18:03:21.000000', '', 0),
(3, 'pbkdf2_sha256$1000000$S9wLVXByIXOOiMWpQLNLDM$pgTpIKvlDVZJhb19cBVSdEQNdDzVMwBMTcIO9lilJKU=', '2025-06-03 01:50:01.993981', 0, 'operator1', '', '', 'email@email.com', 0, 1, '2025-05-24 18:03:22.000000', '', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `core_user_groups`
--

CREATE TABLE `core_user_groups` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `core_user_user_permissions`
--

CREATE TABLE `core_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ;

-- --------------------------------------------------------

--
-- Структура таблицы `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(8, 'core', 'energydata'),
(9, 'core', 'saleadvertisement'),
(7, 'core', 'solarstation'),
(11, 'core', 'station'),
(10, 'core', 'supportrequest'),
(6, 'core', 'user'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Структура таблицы `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-06-03 02:20:09.004197'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-06-03 02:20:09.196997'),
(3, 'auth', '0001_initial', '2025-06-03 02:20:09.698506'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-06-03 02:20:09.879619'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-06-03 02:20:09.893496'),
(6, 'auth', '0004_alter_user_username_opts', '2025-06-03 02:20:09.907560'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-06-03 02:20:09.917703'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-06-03 02:20:09.924304'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-06-03 02:20:09.937227'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-06-03 02:20:09.973413'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-06-03 02:20:09.982810'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-06-03 02:20:10.019779'),
(13, 'auth', '0011_update_proxy_permissions', '2025-06-03 02:20:10.028333'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-06-03 02:20:10.037339'),
(15, 'core', '0001_initial', '2025-06-03 02:20:10.611839'),
(16, 'admin', '0001_initial', '2025-06-03 02:20:10.893275'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-06-03 02:20:10.905183'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-03 02:20:10.920994'),
(19, 'core', '0002_solarstation_energydata', '2025-06-03 02:20:11.200938'),
(20, 'core', '0003_alter_energydata_options_alter_solarstation_options', '2025-06-03 02:20:11.235252'),
(21, 'sessions', '0001_initial', '2025-06-03 02:20:11.308923'),
(22, 'core', '0004_fix_permissions', '2025-06-06 23:28:04.576562'),
(23, 'core', '0005_alter_energydata_options_alter_solarstation_options_and_more', '2025-06-06 23:28:05.706139'),
(24, 'core', '0006_station', '2025-06-06 23:28:05.769929'),
(25, 'core', '0007_station_latitude_station_longitude', '2025-06-06 23:28:05.910541'),
(26, 'core', '0008_station_user', '2025-06-07 11:34:54.835208'),
(27, 'core', '0008_solarstation_last_checked', '2025-06-17 12:41:30.106414');

-- --------------------------------------------------------

--
-- Структура таблицы `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('d97n9kc67spu2m1ca1irs5bhyft8oi46', '.eJxVjD0PAiEQRP8LtbmsLBxgaWJprKzJAku4eB8JeJXxv3smV2g5b97MS3han8WvjasfkjgJKQ6_LFB88Pwt4lK522PrLhMN463eN2emia9L4vG8u38HhVrZ1jYbkCkjAaLTKgKwk9pQtC4qlY-kKCFmacD1IBFcCL1lm2xCnR2jeH8A0283aw:1uRVvI:tTE39Sxh0VmdC9OC5NBxup2wtV5S1vHYAW935ExIn10', '2025-07-01 13:00:20.634316');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Индексы таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Индексы таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Индексы таблицы `core_energydata`
--
ALTER TABLE `core_energydata`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_energydata_station_id_e2a4b136_fk_core_solarstation_id` (`station_id`);

--
-- Индексы таблицы `core_saleadvertisement`
--
ALTER TABLE `core_saleadvertisement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_saleadvertisement_user_id_511f5484_fk_core_user_id` (`user_id`);

--
-- Индексы таблицы `core_solarstation`
--
ALTER TABLE `core_solarstation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_solarstation_owner_id_4c528476_fk_core_user_id` (`owner_id`);

--
-- Индексы таблицы `core_station`
--
ALTER TABLE `core_station`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `core_supportrequest`
--
ALTER TABLE `core_supportrequest`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_supportrequest_user_id_d0898577_fk_core_user_id` (`user_id`);

--
-- Индексы таблицы `core_user`
--
ALTER TABLE `core_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `core_user_email_92a71487_uniq` (`email`);

--
-- Индексы таблицы `core_user_groups`
--
ALTER TABLE `core_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_user_groups_user_id_group_id_c82fcad1_uniq` (`user_id`,`group_id`),
  ADD KEY `core_user_groups_group_id_fe8c697f_fk_auth_group_id` (`group_id`);

--
-- Индексы таблицы `core_user_user_permissions`
--
ALTER TABLE `core_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_user_user_permissions_user_id_permission_id_73ea0daa_uniq` (`user_id`,`permission_id`),
  ADD KEY `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` (`permission_id`);

--
-- Индексы таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_core_user_id` (`user_id`);

--
-- Индексы таблицы `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Индексы таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT для таблицы `core_energydata`
--
ALTER TABLE `core_energydata`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `core_saleadvertisement`
--
ALTER TABLE `core_saleadvertisement`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `core_solarstation`
--
ALTER TABLE `core_solarstation`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `core_station`
--
ALTER TABLE `core_station`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `core_supportrequest`
--
ALTER TABLE `core_supportrequest`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `core_user`
--
ALTER TABLE `core_user`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `core_user_groups`
--
ALTER TABLE `core_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `core_user_user_permissions`
--
ALTER TABLE `core_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT для таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ограничения внешнего ключа таблицы `core_energydata`
--
ALTER TABLE `core_energydata`
  ADD CONSTRAINT `core_energydata_station_id_e2a4b136_fk_core_solarstation_id` FOREIGN KEY (`station_id`) REFERENCES `core_solarstation` (`id`);

--
-- Ограничения внешнего ключа таблицы `core_saleadvertisement`
--
ALTER TABLE `core_saleadvertisement`
  ADD CONSTRAINT `core_saleadvertisement_user_id_511f5484_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `core_solarstation`
--
ALTER TABLE `core_solarstation`
  ADD CONSTRAINT `core_solarstation_owner_id_4c528476_fk_core_user_id` FOREIGN KEY (`owner_id`) REFERENCES `core_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `core_supportrequest`
--
ALTER TABLE `core_supportrequest`
  ADD CONSTRAINT `core_supportrequest_user_id_d0898577_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `core_user_groups`
--
ALTER TABLE `core_user_groups`
  ADD CONSTRAINT `core_user_groups_group_id_fe8c697f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `core_user_groups_user_id_70b4d9b8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `core_user_user_permissions`
--
ALTER TABLE `core_user_user_permissions`
  ADD CONSTRAINT `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `core_user_user_permissions_user_id_085123d3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
