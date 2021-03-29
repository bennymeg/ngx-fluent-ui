import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
    name: 'iconsfilter',
    pure: false
})
export class IconsFilterPipe implements PipeTransform {
    transform(items: any[], filter: string): any {
        if (!items || !filter) {
            return items;
        }

        // filter items array, items which match and return true will be
        // kept, false will be filtered out
        console.log(items.filter(item => item.name.toLowerCase().includes(filter.toLowerCase())));
        
        // return Object.assign({}, ...Object.entries(items).filter(([k,v]) => v.name.toLowerCase().includes(filter.toLowerCase())).map(([k,v]) => ({[k]:v})));
        return items.filter(item => item.name.toLowerCase().includes(filter.toLowerCase()));
    }
}