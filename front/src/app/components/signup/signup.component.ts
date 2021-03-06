import { Component, OnInit } from '@angular/core';
import { Route } from '@angular/compiler/src/core';
import { Router } from '@angular/router';
import { ProviderService } from 'src/app/services/provider.service';
import { IUser } from 'src/app/models/models';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  
  public isMember = false;
  public authorized = false;
  public username='';
  public password='';
  public email='';
  public surname='';
  public name='';
  
  constructor(private router: Router, private provider: ProviderService) { }

  ngOnInit() {

  }

  hide = () => {
   this.router.navigateByUrl('');
  }
  signUp() {
    if (this.username !== '' || this.password !== '' || this.email !==''|| this.surname !=='' || this.name !== '') {
      this.provider.createUser(this.username, this.password, this.email, this.name, this.surname).then( res => {
              alert('You have succesfully registred');
              this.router.navigateByUrl('');
          });
     }
  }
}
