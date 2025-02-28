CREATE DATABASE chatbot_favip;
USE chatbot_favip;

CREATE TABLE phones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    phone VARCHAR(25) NOT NULL UNIQUE
);

SELECT * FROM phones;