import { TestBed } from '@angular/core/testing';

import { FluentUiIconsService } from './fluent-ui-icons.service';

describe('FluentUiIconsService', () => {
  let service: FluentUiIconsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FluentUiIconsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
