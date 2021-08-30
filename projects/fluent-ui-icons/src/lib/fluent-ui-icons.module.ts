import { NgModule, ModuleWithProviders, Optional } from "@angular/core";
import { FluentUiIconsComponent } from './fluent-ui-icons.component';
import { Icons } from "./fluent-ui-icons.provider";

@NgModule({
  declarations: [FluentUiIconsComponent],
  imports: [],
  exports: [FluentUiIconsComponent],
})
export class FluentUiIconsModule {
  constructor(@Optional() private icons: Icons) {
    if (!this.icons) {
      throw new Error(
        `No icon provided. Make sure to use 'FluentUiIconsModule.pick({ ... })' when importing the module\n`
      );
    }
  }

  static pick(icons: { [key: string]: string; }): ModuleWithProviders<FluentUiIconsModule> {
    return {
      ngModule: FluentUiIconsModule,
      providers: [{ provide: Icons, multi: true, useValue: icons }],
    };
  }
}