import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Handler } from '../shared/errorhandler';
import 'rxjs/add/operator/toPromise';

import{ Role } from '../models/role';

@Injectable()
export class RoleService {

  private roleUrl = 'http://localhost:8081/role';
  private headers = new Headers({ 'Content-Type': 'application/json' });

  constructor(private http: Http) { }

  getRoles(): Promise<Role[]> {
    return this.http.get(this.roleUrl + "/get_roles")
            .toPromise()
            .then(response => response.json() as Role[])
            .catch(Handler.handleError);
  }

}


