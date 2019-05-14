import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { ICategory, IProduct, IAuthResponse, IUser, IComment} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  public categoryForProducts: ICategory;
  public productForComments: IProduct;
  public logged = false;

  constructor(http: HttpClient) {
    super(http);
   }

   getCategories(): Promise<ICategory[]>{
     return this.get('http://localhost:8000/categories/', {});
   }  

   setCategoryForProducts(category: ICategory){
      this.categoryForProducts = category;
   }

   getCategoryForProducts(){
    return this.categoryForProducts;
   }


   getProductForComments(){
    return this.productForComments;
   }

   setProductForComments(product: IProduct){
    this.productForComments = product;
    }

   getProducts(id:number):Promise<IProduct[]>{
    return this.get(`http://localhost:8000/categories/${id}/products/`, {});
   } 

   getComments(id:number):Promise<IComment[]>{
    return this.get(`http://localhost:8000/products/${id}/comments/`, {});
   } 

  searchProductByName(name:string): Promise<IProduct[]>{
    return this.get(`http://localhost:8000/products/?search=${name}/`, {name})
  }

  login(username: string, password: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/login/', {
      username: username,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/user/logout/', {
    });
  }

  createUser(username:string,password:string,email:string, name:string, surname:string):Promise<IUser>{
    return this.post(`http://localhost:8000/users/create/`,{
      username:username,
      password:password,
      email:email,
      name:name,
      surname:surname,
    });
  }
}
