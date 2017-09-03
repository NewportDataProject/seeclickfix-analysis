# SeeClickFix Utilities and Analysis

Code for accessing [SeeClickFix](http://seeclickfix.com) data, manipulating the data, and running associated analyses.

### API call notes
* Issues - issues that have been closed for 7 days change status to archived, and are not returned in api calls by 
default. This can be overridden by using `status=archived`

SeeClickFix data is licensed under a Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License.
Attribution should be to seeclickfix.com.