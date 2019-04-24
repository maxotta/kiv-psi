import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ModuleWithProviders } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { CountrySearchService } from './country-search.service';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
    /**
   * Keep services as singletons
   */
  static forRoot(): ModuleWithProviders {
    return {
      ngModule: HttpClientModule,
      providers: [
        CountrySearchService
      ]
    };
  }
}
