import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {}

  chat(prompt: string) {
    return this.http.post<{ reply: string }>('http://localhost:8000/api/chat', { prompt });
  }
}
