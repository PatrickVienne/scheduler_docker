
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { ServiceLocationService } from '../../services/servicelocation.service';

import { ServiceLocation } from '../../models/servicelocation';


@Component({
  selector: 'app-servicelocations',
  templateUrl: './servicelocations.component.html',
  styleUrls: ['./servicelocations.component.css']
})
export class ServicelocationsComponent implements OnInit {

  servicelocations: ServiceLocation[];

  constructor(private servicelocationService: ServiceLocationService,
    private router: Router) { }

  ngOnInit() {
    this.getServiceLocations();
  }


  getServiceLocations(): void {
    this.servicelocationService.getServiceLocations()
      .then(servicelocationFromPromise => this.servicelocations = servicelocationFromPromise);
  }

  delete(servicelocation: ServiceLocation): void {
    this.servicelocationService.delete(servicelocation.id)
      .then(() => {
        this.servicelocations = this.servicelocations.filter(e => e !== servicelocation);
        //if (this.selectedHero === hero) { this.selectedHero = null; }
      })
  }

  edit(servicelocation: ServiceLocation): void {
    console.log(servicelocation.id)
    this.router.navigate(["/servicelocation_detail", servicelocation.id]);
  }

  create(servicelocation: ServiceLocation): void {
    this.router.navigate(["/servicelocation_detail", 0]);
  }

}
