import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Handler } from '../shared/errorhandler';
import 'rxjs/add/operator/toPromise';

import{ Employee } from '../models/employee';

@Injectable()
export class EmployeeService {

  private employeeUrl = 'http://localhost:8081/employee';
  private headers = new Headers({ 'Content-Type': 'application/json' });

  constructor(private http: Http) { }

  getEmployees(): Promise<Employee[]> {
    return this.http.get(this.employeeUrl + "/get_employees")
            .toPromise()
            .then(response => response.json() as Employee[])
            .catch(Handler.handleError);
  }

  get(id: number): Promise<Employee> {
    return this.http.get(this.employeeUrl + "/get/"+id)
            .toPromise()
            .then(response => response.json() as Employee)
            .catch(Handler.handleError);
  }

  delete(id: number): Promise<void> {
      const url = `${this.employeeUrl}/delete/${id}`;
      return this.http.delete(url, { headers: this.headers })
          .toPromise()
          .then(() => null)
          .catch(Handler.handleError);
  }
  update(employee: Employee): Promise<null>{
    return this.http.put(this.employeeUrl + "/update", JSON.stringify(employee), { headers: this.headers })
            .toPromise()
            .then(()=>null)
            .catch(Handler.handleError);
  }


  create(employee: Employee): Promise<null>{
    return this.http.put(this.employeeUrl + "/create", JSON.stringify(employee), { headers: this.headers })
            .toPromise()
            .then(()=>null)
            .catch(Handler.handleError);
  }

}
