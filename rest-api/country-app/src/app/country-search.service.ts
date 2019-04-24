import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CountrySearchService {

  // public static endpoint = 'https://restcountries.eu/rest/v2/name/';
  public static endpoint = '/api/name';

  public static httpHeaders = new HttpHeaders({
      'Content-Type':  'application/json',
      'Accept': 'application/json'
    });

  constructor(private http: HttpClient) { }

  public searchCountries(searchTerm: String): Observable<any> {
    return this.http.get(CountrySearchService.endpoint + '/' + searchTerm, { headers: CountrySearchService.httpHeaders });
  }

}
