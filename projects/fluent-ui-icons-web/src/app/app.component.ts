import { Component } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { faGithub, faNpm, faAngular } from '@fortawesome/free-brands-svg-icons';
import iconList from '../assets/icon_list.json';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Fluent UI Icon Library';
  iconList = Object.values(iconList);
  searchValue = '';
  filter = '';
  faGithub = faGithub;
  faNpm = faNpm;
  faAngular = faAngular;

  constructor(private _snackBar: MatSnackBar) {}

  applyFilter() {
    this.filter = this.searchValue;
  }

  clearFilter() {
    this.searchValue = '';
    this.applyFilter();
  }

  getIconName(name: string, style: string, size: any) {
    const snakeCaseIconName = name.replace(/[A-Z]/g, (letter, index) => { 
      return index == 0 ? letter.toLowerCase() : '_' + letter.toLowerCase();
    }).replace(/\s+/, '');

    return `${snakeCaseIconName}_${size.key}_${style.toLowerCase()}`;
  }

  showCopiesBanner(size?: any) {
    this._snackBar.open("Copied!", size ? size.value : '', { duration: 3000 });
  }
}
