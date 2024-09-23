CREATE DATABASE IF NOT EXISTS sellit_db;
CREATE USER IF NOT EXISTS 'sellit_user'@'localhost' IDENTIFIED BY 'passwd024';
GRANT ALL PRIVILEGES ON sellit_db.* TO 'sellit_user'@'localhost';
