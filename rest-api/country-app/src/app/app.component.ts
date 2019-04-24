import { Component, OnInit } from '@angular/core';
import { CountrySearchService } from './country-search.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  title = 'Search country app';

  protected results: any;
  protected searchText: String;

  constructor(private service: CountrySearchService) {}

  public ngOnInit() {
    this.results = {};
  }

  protected performSearch() {
    console.log('SEARCH :' + this.searchText);
    this.searchCountries(this.searchText);
  }

  protected searchCountries(searchTerm: String): void {
    this.service.searchCountries(searchTerm).subscribe((result) => {
      console.log('RESULTS: ' + JSON.stringify(result));
      this.results = result;
    });
  }
}
