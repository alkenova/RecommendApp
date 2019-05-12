import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { ICategory, IProduct, IAuthResponse, IUser} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  public categoryForProducs: ICategory;
  public logged = false;

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


  login(username: string, password: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/user/login/', {
      username: username,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/user/logout/', {
    });
  }

  createUser(username:string,password:string,email:string):Promise<IUser>{
    return this.post(`http://localhost:8000/users/create/`,{
      username:username,
      password:password,
      email:email,
      isMember:true
    });
  }
}
