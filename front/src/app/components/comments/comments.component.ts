import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/services/provider.service';
import { IProduct, IComment } from 'src/app/models/models';
import { ThrowStmt } from '@angular/compiler';

@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrls: ['./comments.component.css']
})
export class CommentsComponent implements OnInit {

  constructor(private provider: ProviderService) { }
  public productForComments: IProduct;
  public comments: IComment[]=[];



  ngOnInit() {
    this.productForComments = this.provider.getProductForComments();
    this.provider.getComments(this.productForComments.id).then( res => { this.comments = res; });
  }

  getCom(prodList: IProduct){
    this.provider.getComments(prodList.id).then( res =>{
      this.comments=res;
    })
  }

}
