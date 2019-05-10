import { Component, OnInit } from '@angular/core';
import { ICategory, IProduct } from 'src/app/models/models';
import { ProviderService } from 'src/app/services/provider.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  constructor(private provider: ProviderService) { }
  public categoryForProducts: ICategory;
  public products: IProduct[]=[];
  ngOnInit() { 
    this.categoryForProducts = this.provider.getCategoryForProducts();
    this.provider.getProducts(this.categoryForProducts.id).then( res => { this.products = res; });
  }

  // getProducts(category: ICategory){
  //   this.provider.getProducts(category.id).then(res=>{
  //     this.products=res;
  //   })
  // }


}
