-- Create database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create table states within database created
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`));