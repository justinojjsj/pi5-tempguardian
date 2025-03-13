-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: container_tempguardian_db
-- Tempo de geração: 13/03/2025 às 18:59
-- Versão do servidor: 11.3.2-MariaDB-1:11.3.2+maria~ubu2204
-- Versão do PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `db_tempguardian`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `weather_history`
--

CREATE TABLE `weather_history` (
  `id` int(11) NOT NULL,
  `temperature` double(5,2) NOT NULL,
  `humidity` double(5,2) NOT NULL,
  `date` date DEFAULT NULL,
  `hour` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Table with historical temperature and humidity data';

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `weather_history`
--
ALTER TABLE `weather_history`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `weather_history`
--
ALTER TABLE `weather_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
