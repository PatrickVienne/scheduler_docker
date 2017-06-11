# Frontend

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 1.0.0.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive/pipe/service/class/module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `-prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).
Before running the tests make sure you are serving the app via `ng serve`.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).




# WARNING

Router not good.
Breaking compatibility.
Watch out for version updates.

if router modules have a problem, router-outlet error warning appears

# angular-cli version update

problem:
angular beta30 had no ng init anymore
cannot initialize project

solution:
update angular-cli to latest version (look up github description), create a new project folder with ng new.
copy old app to new project. ONLY App folder (htmls, ts files, not package.json or angular-cli.json)

# bootstrap 4 integration
problem:
integrate bootstrap 4
solution:
follow
https://www.npmjs.com/package/ngx-bootstrap
https://github.com/valor-software/ngx-bootstrap/blob/development/docs/getting-started/ng-cli.md


-- description bootstrap from websites:
npm install ngx-bootstrap --save
<!--- index.html -->
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" rel="stylesheet">

open .angular-cli.json and insert a new entry into the styles array
      "styles": [
         "../node_modules/bootstrap/dist/css/bootstrap.min.css",
        "styles.css",
      ],

# navbar collaps
problem:
navbar collapse button not working (not opening navbar on small windows on click)
solution:
http://stackoverflow.com/questions/37438683/is-there-a-way-to-build-the-mobile-nav-bar-in-ng2-bootsrap

1)first you import the directive
import { CollapseDirective } from 'ng2-bootstrap'

2)Directives (in the current stable version of angular 2) are no longer placed in the @Component attribute.
They are included in the NgModule attribute.
@NgModule({ declarations: [CollapseDirective] })

3)then in your controller create a variable to keep track of whether or not it's collapsed
export class MyController {
 public isCollapsed: boolean = true;
}

4)and in your template the line that looks like this 
<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" >
you'll want to toggle the variable
<button type="button" class="navbar-toggle collapsed" (click)="isCollapsed = !isCollapsed" >

5)And also in your template you'll want to change the line that says
<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1"> to include the directive
<div id="navbar" class="navbar-collapse collapse" [collapse]="isCollapsed">