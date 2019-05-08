import { Component } from '@angular/core';
import { ICategory } from './main/models/models';
import { ProviderService } from './main/services/provider.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  public categories:ICategory[]=[];


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getCategories().then(res=>{
      this.categories = res;
    });
  }
}
