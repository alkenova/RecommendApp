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

  
  public isEmployee = false;
  public authorized = false;
  public login='';
  public password='';
  public email='';
  
  constructor(private router: Router, private provider: ProviderService) { }

  ngOnInit() {

  }

  hide = () => {
   this.router.navigateByUrl('');
  }
  signUp() {
    if (this.login !== '' || this.password !== '' || this.email !=='') {
      this.provider.createUser(this.login, this.password, this.email).then( res => {
              alert('You have succesfully registred');
          });
     }
  }
}
