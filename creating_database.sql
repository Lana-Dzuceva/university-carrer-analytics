CREATE DATABASE IF NOT EXISTS hh_data CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hh_data;

CREATE TABLE IF NOT EXISTS vacancies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_vacancy VARCHAR(64),
    name TEXT,
    premium BOOLEAN,
    billing_type VARCHAR(64),
    area_id VARCHAR(64),
    area_name VARCHAR(255),
    salary_from INT,
    salary_to INT,
    salary_currency VARCHAR(10),
    salary_gross BOOLEAN,
    type VARCHAR(64),
    city VARCHAR(128),
    street VARCHAR(128),
    building VARCHAR(64),
    lat DOUBLE,
    lng DOUBLE,
    experience VARCHAR(128),
    schedule VARCHAR(128),
    employment VARCHAR(128),
    employer_id VARCHAR(64),
    employer_name VARCHAR(255),
    employer_url TEXT,
    published_at DATETIME,
    description LONGTEXT,
    key_skills JSON
);

USE hh_data;

ALTER TABLE vacancies
ADD COLUMN group_tag TEXT;

CREATE INDEX idx_area_name ON vacancies (area_name(100));
CREATE INDEX idx_group_tag ON vacancies (group_tag(100));