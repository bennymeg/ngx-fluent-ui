import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { LazyLoadImageModule } from 'ng-lazyload-image';
import { IconsFilterPipe } from './pipes/icons-filter.pipe';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    IconsFilterPipe
  ],
  imports: [
    BrowserModule,
    LazyLoadImageModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
