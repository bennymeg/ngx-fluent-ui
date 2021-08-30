import { Component, ElementRef, Input, Inject, ChangeDetectorRef, OnChanges, SimpleChanges } from '@angular/core';
import { Icons } from "./fluent-ui-icons.provider";

@Component({
  selector: 'fluent-ui-icon, fui',
  template: `<ng-content></ng-content>`,
  styles: [
    `:host {
      display: inline-block;
      width: 24px;
      height: 24px;
      fill: none;
      stroke-linecap: round;
      stroke-linejoin: round;
      svg{
        width: 100% !important;
        height: 100% !important;
      }
    }`
  ]
})
export class FluentUiIconsComponent implements OnChanges  {
  @Input() name!: string;

  constructor(
    private element: ElementRef,
    private changeDetector: ChangeDetectorRef,
    @Inject(Icons) private icons: Icons
  ) {}

  ngOnChanges(changes: SimpleChanges) {
    // icons are provided as an array of objects because of "multi: true"
    const icons = Object.assign({}, ...(this.icons as any as object[]));
    const svg = icons[changes.name.currentValue] || '';

    if (!svg) {
      console.warn(`Icon not found: ${changes.name.currentValue}\n`);
    }

    this.element.nativeElement.innerHTML = svg;
    this.changeDetector.markForCheck();
  }
}
