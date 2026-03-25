CREATE DATABASE procrastination_tracker;

USE procrastination_tracker;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    deadline DATE,
    priority VARCHAR(20),
    status VARCHAR(20),
    delay_count INT DEFAULT 0,
    created_date DATE,
    completed_date DATE
);
