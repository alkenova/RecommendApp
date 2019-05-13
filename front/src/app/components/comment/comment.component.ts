import { Component, OnInit, Input } from '@angular/core';
import { IComment } from 'src/app/models/models';
import { ProviderService } from 'src/app/services/provider.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.css']
})
export class CommentComponent implements OnInit {

  constructor(private provider: ProviderService) { }

  @Input()
  public comment: IComment;

  ngOnInit() {
  }

}
