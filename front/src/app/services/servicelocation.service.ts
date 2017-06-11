import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Handler } from '../shared/errorhandler';
import 'rxjs/add/operator/toPromise';

import{ ServiceLocation } from '../models/servicelocation';

@Injectable()
export class ServiceLocationService {

  private servicelocationUrl = 'http://localhost:8081/servicelocation';
  private headers = new Headers({ 'Content-Type': 'application/json' });

  constructor(private http: Http) { }

  getServiceLocations(): Promise<ServiceLocation[]> {
    return this.http.get(this.servicelocationUrl + "/get_servicelocations")
            .toPromise()
            .then(response => response.json() as ServiceLocation[])
            .catch(Handler.handleError);
  }

  get(id: number): Promise<ServiceLocation> {
    return this.http.get(this.servicelocationUrl + "/get/"+id)
            .toPromise()
            .then(response => response.json() as ServiceLocation)
            .catch(Handler.handleError);
  }

  delete(id: number): Promise<void> {
      const url = `${this.servicelocationUrl}/delete/${id}`;
      return this.http.delete(url, { headers: this.headers })
          .toPromise()
          .then(() => null)
          .catch(Handler.handleError);
  }



  update(serviceLocation: ServiceLocation): Promise<null>{
    return this.http.put(this.servicelocationUrl + "/update", JSON.stringify(serviceLocation), { headers: this.headers })
            .toPromise()
            .then(()=>null)
            .catch(Handler.handleError);
  }


  create(serviceLocation: ServiceLocation): Promise<null>{
    return this.http.put(this.servicelocationUrl + "/create", JSON.stringify(serviceLocation), { headers: this.headers })
            .toPromise()
            .then(()=>null)
            .catch(Handler.handleError);
  }

}
