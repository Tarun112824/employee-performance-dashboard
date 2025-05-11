package com.employee.controller;

import org.springframework.web.bind.annotation.*;
import com.employee.model.Employee;
import com.employee.service.EmployeeService;
import java.util.List;

@RestController
@RequestMapping("/api/employees")
public class EmployeeController {

    private final EmployeeService employeeService;

    public EmployeeController(EmployeeService employeeService) {
        this.employeeService = employeeService;
    }

    @GetMapping("/top-performers")
    public List<Employee> getTopPerformers(
        @RequestParam(defaultValue = "4.0") double minScore
    ) {
        return employeeService.findTopPerformers(minScore);
    }

    @PostMapping("/{id}/review")
    public void addPerformanceReview(
        @PathVariable int id,
        @RequestBody PerformanceReview review
    ) {
        employeeService.addReview(id, review);
    }
}