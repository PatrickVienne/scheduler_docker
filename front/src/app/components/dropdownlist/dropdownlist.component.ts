import { Component, OnInit, Input } from '@angular/core';
import { DropdownItem } from '../../models/dropdownitem';

@Component({
  selector: 'app-dropdownlist',
  templateUrl: './dropdownlist.component.html',
  styleUrls: ['./dropdownlist.component.css']
})
export class DropdownlistComponent implements OnInit {
  @Input() dropdownitems:DropdownItem[];
  @Input() activeid:number;

  ngOnInit() {
    this.dropdownitems = this.dropdownitems
  }


  constructor() { }

}
