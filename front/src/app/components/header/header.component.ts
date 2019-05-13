import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/services/provider.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  logged

  constructor(private provider: ProviderService, router: Router) { }

  ngOnInit() {
  }

  logout(){
    this.provider.logout().then( res=>{
      localStorage.clear();
      this.logged=false;
    })
  }

}
