-- Tables for employees, reviews, and departments
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    hire_date DATE,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE PerformanceReviews (
    review_id INT PRIMARY KEY,
    employee_id INT REFERENCES Employees(employee_id),
    score DECIMAL(3,2),
    feedback TEXT,
    review_date DATE DEFAULT CURRENT_DATE
);

-- Sample stored procedure (for promotion readiness)
DELIMITER //
CREATE PROCEDURE CalculatePromotionReadiness()
BEGIN
    SELECT e.name, AVG(pr.score) AS avg_score
    FROM Employees e
    JOIN PerformanceReviews pr ON e.employee_id = pr.employee_id
    GROUP BY e.employee_id
    HAVING AVG(pr.score) >= 4.0;
END //
DELIMITER ;