-- MySQL Setup Script for Django Login & Registration Backend

-- Create database
CREATE DATABASE IF NOT EXISTS login_reg_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Show that database was created
SHOW DATABASES;

-- Use the database
USE login_reg_db;

-- Show current database
SELECT DATABASE();

-- Optional: Create dedicated user (uncomment if needed)
-- CREATE USER IF NOT EXISTS 'django_user'@'localhost' IDENTIFIED BY 'secure_password123';
-- GRANT ALL PRIVILEGES ON login_reg_db.* TO 'django_user'@'localhost';
-- FLUSH PRIVILEGES;

-- Show current user
SELECT USER();

-- Show tables (should be empty initially)
SHOW TABLES;
