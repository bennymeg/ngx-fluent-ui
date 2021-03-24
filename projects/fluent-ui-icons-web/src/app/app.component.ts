import { Component } from '@angular/core';
import iconList from '../assets/icon_list.json';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Fluent UI Icon Library';
  iconList = iconList;
}
