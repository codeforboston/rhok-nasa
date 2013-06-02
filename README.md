rhok-nasa
=========

Random Hacks of Kindness Nasa Team project

Light pollution data. 

#Live database:  
        mysql -h rhoknasa.cr5o3gwscupd.us-east-1.rds.amazonaws.com -P3306 -urhoknasa -prhoknasa -Drhoknasa  

#start server locally  
        python rhoknasa.py  

#test get  
        curl -X GET localhost:8080  

#test post  
        curl -H "Accept: application/json" -X POST localhost:8080 -d '{"country": "xx", "limiting_magnitude": -99, "comments": "", "latitude": "40.4558", "date": "0012-10-19 16:30:00", "constellation": "Cygnus", "longitud": "-79.91068"}'  

#TODO:  
Check the hackpad  

