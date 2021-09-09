<br/>
<p align="center">
  <a href="https://github.com/bennymeg/ngx-fluent-ui">
    <img src="https://github.com/bennymeg/ngx-fluent-ui/blob/master/docs/assets/logo.png?raw=true" width="128px" alt="Logo">
  </a>

  <h3 align="center">NGX Fluent UI</h3>

  <p align="center">
    Microsoft's Fluent UI icons library for Angular applications
    <br/>
    <br/>
    <img src="https://github.com/bennymeg/ngx-fluent-ui/blob/master/docs/assets/fluent.png?raw=true" width="10px" alt="LIVE Demo">
    <a href="https://bennymeg.github.io/ngx-fluent-ui/">View Demo</a>
    .
    <a href="https://github.com/bennymeg/ngx-fluent-ui/issues">Report Bug</a>
    .
    <a href="https://github.com/bennymeg/ngx-fluent-ui/issues">Request Feature</a>
  </p>

  <br/>

  <div align="center">

  [![licence](https://img.shields.io/github/license/bennymeg/ngx-fluent-ui.svg)](https://github.com/bennymeg/ngx-fluent-ui/blob/master/LICENSE)
  [![npm version](https://img.shields.io/npm/v/ngx-fluent-ui.svg)](https://www.npmjs.com/package/ngx-fluent-ui-icons)
  
  </div>
</p>

<hr></br>

## Installation

```bash
npm install ngx-fluent-ui-icons
```

<!-- https://www.chrisjmendez.com/2017/06/17/angular-dynamically-inserting-svg-into-an-element/ -->

## Usage

1. Import Fluent UI icon module

```ts  
import { NgModule } from '@angular/core';

import { FluentUiIconsModule } from 'ngx-fluent-ui-icons';
import { heart_24_filled, heart_24_regular } from 'ngx-fluent-ui-icons';

@NgModule({
  imports: [
    FluentUiIconsModule.pick({ heart_24_filled, heart_24_regular })
  ]
})
export class AppModule { }
```
> **Note:** Only the icons you pick will be bundled in the final build

2. Use it in the html template

```html
<fluent-ui-icon name="heart_24_filled" class="beat" style="fill: red;"></fluent-ui-icon>
<!-- OR -->
<fui name="heart_24_regular" class="beat" style="color: red;"></fui>
```

## Roadmap

See the [open issues](https://github.com/bennymeg/ngx-fluent-ui/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/bennymeg/ngx-fluent-ui/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/bennymeg/ngx-fluent-ui/blob/master/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the Apache 2.0 License. See [LICENSE](https://github.com/bennymeg/ngx-fluent-ui/blob/master/LICENSE.md) for more information.

## Authors

* **[Benny Megidish](https://github.com/bennymeg/)**
