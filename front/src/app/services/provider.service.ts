import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { ICategory, IProduct} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  public categoryForProducs: ICategory;
  constructor(http: HttpClient) {
    super(http);
   }

   getCategories(): Promise<ICategory[]>{
     return this.get('http://localhost:8000/categories/', {});
   }  

   setCategoryForProducts(category: ICategory){
      this.categoryForProducs = category;
   }

   getCategoryForProducts(){
    return this.categoryForProducs;
   }

   getProducts(id:number):Promise<IProduct[]>{
    return this.get(`http://localhost:8000/categories/${id}/products/`, {});
   } 
}
