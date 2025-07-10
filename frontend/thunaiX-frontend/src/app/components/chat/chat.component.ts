import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-chat',
  imports: [FormsModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.scss'
})
export class ChatComponent {

   prompt: string = '';
  reply: string = '';

  constructor(private apiService: ApiService) {}

  send() {
    this.apiService.chat(this.prompt).subscribe(
      res => {
        this.reply = res.reply;
      },
      err => {
        console.error(err);
        this.reply = "Oops! ThunaiX couldn't reply.";
      }
    );
  }
  clear(){
    this.reply='';
  } 
  ReturnToHome(){

  }
}
