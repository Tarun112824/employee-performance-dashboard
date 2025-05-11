// Business logic
package com.employee.service;

import com.employee.repository.EmployeeRepository;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class EmployeeService {

    private final EmployeeRepository employeeRepository;

    public EmployeeService(EmployeeRepository employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    public List<Employee> findTopPerformers(double minScore) {
        return employeeRepository.findByAverageScoreGreaterThan(minScore);
    }
}