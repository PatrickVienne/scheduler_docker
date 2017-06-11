import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { ActivatedRoute, Params } from '@angular/router';
import { ServiceLocationService } from '../../services/servicelocation.service';
import { ServiceLocation } from '../../models/servicelocation';
import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'app-servicelocation-detail',
  templateUrl: './servicelocation-detail.component.html',
  styleUrls: ['./servicelocation-detail.component.css']
})
export class ServicelocationDetailComponent implements OnInit {

  servicelocation: ServiceLocation;
  exists: boolean;

  constructor(private servicelocationService: ServiceLocationService, private router: ActivatedRoute, private location: Location) { }

  ngOnInit() {
    console.log("ID:", +this.router.params['id']);
    console.log("ID-snapshot:", +this.router.snapshot.params['id']);
    this.router.params
      .switchMap((params: Params) => this.servicelocationService.get(+params['id'])) // (+) converts string 'id' to a number
      .subscribe(servicelocation => {
        this.servicelocation = servicelocation;
        console.log(this.servicelocation);
      }
      );
  }

  save(): void {
    if (this.servicelocation.id != 0) {
      this.servicelocationService.update(this.servicelocation).then(() => this.location.back());
    } else {
      this.servicelocationService.create(this.servicelocation).then(() => this.location.back());
    }

  }

  cancel(): void {
    this.location.back();
  }
}
