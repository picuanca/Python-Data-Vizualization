suprafete = {
    
     147570,
    
     8515770,
    
     9562910,
    
     3287263,
    
     1904569,
   
     1972550,
    
     923768,
    
     881913,
   
     17098242,
   
     9831510
}

from pprint import pprint

countries = ['Bangladesh', 'Brazil', 'China', 'India', 'Indonesia', 'Mexico', 'Nigeria', 'Pakistan', 'Russia', 'United States']
population =  [170, 213, 1411, 1378, 271, 126, 211, 225, 146, 331]

populatii = { tara: population[index ] for index, tara in enumerate(countries)}
pprint(populatii)