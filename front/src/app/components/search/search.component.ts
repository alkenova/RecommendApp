import { Component, OnInit } from '@angular/core';
import { IProduct , ICategory} from 'src/app/models/models';
import { ProviderService } from 'src/app/services/provider.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {


  constructor(private provider: ProviderService, private router: Router) { }

  
  public search_list='';
  public products: IProduct[] = [];
  public categories: ICategory[]=[];

  ngOnInit() {
  }
searchList(){
    this.provider.searchProductByName(this.search_list).then(res=>{
      this.products=res;
    });
  }
}
