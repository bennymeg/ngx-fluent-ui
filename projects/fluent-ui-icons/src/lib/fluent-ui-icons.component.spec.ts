import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FluentUiIconsComponent } from './fluent-ui-icons.component';

describe('FluentUiIconsComponent', () => {
  let component: FluentUiIconsComponent;
  let fixture: ComponentFixture<FluentUiIconsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FluentUiIconsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FluentUiIconsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
