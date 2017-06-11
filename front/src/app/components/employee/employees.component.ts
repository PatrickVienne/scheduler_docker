import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { EmployeeService } from '../../services/employee.service';

import { Employee } from '../../models/employee';

@Component({
  selector: 'app-employees',
  templateUrl: './employees.component.html',
  styleUrls: ['./employees.component.css']
})
export class EmployeesComponent implements OnInit {

  employees: Employee[];

  constructor(private employeeService: EmployeeService,
    private router: Router) { }

  ngOnInit() {
    this.getEmployees();
  }


  getEmployees(): void {
    this.employeeService.getEmployees()
      .then(employeesFromPromise => this.employees = employeesFromPromise);
  }

  delete(employee: Employee): void {
    this.employeeService.delete(employee.id)
      .then(() => {
        this.employees = this.employees.filter(e => e !== employee);
        //if (this.selectedHero === hero) { this.selectedHero = null; }
      })
  }

  edit(employee: Employee): void {
    console.log(employee.id)
    this.router.navigate(["/employee_detail", employee.id]);
  }

  create(employee: Employee): void {
    this.router.navigate(["/employee_detail", 0]);
  }

}
