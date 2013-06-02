rhok-nasa
=========

Random Hacks of Kindness Nasa Team project

Light pollution data. 

#Live database:  
        mysql -h rhoknasa.cr5o3gwscupd.us-east-1.rds.amazonaws.com -P3306 -urhoknasa -prhoknasa -Drhoknasa  

##prerequisites
sudo apt-get update
sudo apt-get install python-mysqldb
sudo apt-get install python-pip
sudo pip install web.py

#start server locally  
        python rhoknasa.py  

#deploy server remotely
        scp -i aws/rhok-nasa.pem src/python/rhoknasa.py ubuntu@ec2-23-22-78-214.compute-1.amazonaws.com:rhok-nasa/

#start server remotely
        ssh -f -i aws/rhok-nasa.pem ubuntu@ec2-23-22-78-214.compute-1.amazonaws.com "python /home/ubuntu/rhok-nasa/rhoknasa.py"


#test get  
        curl -X GET localhost:8080  
        curl -X GET ec2-23-22-78-214.compute-1.amazonaws.com:8080

#test post  
        curl -H "Accept: application/json" -X POST localhost:8080 -d '{"country": "xx", "limiting_magnitude": -99, "comments": "", "latitude": "40.4558", "date": "0012-10-19 16:30:00", "constellation": "Cygnus", "longitud": "-79.91068"}'  
        curl -H "Accept: application/json" -X POST ec2-23-22-78-214.compute-1.amazonaws.com:8080 -d '{"country": "xx", "limiting_magnitude": -99, "comments": "", "latitude": "40.4558", "date": "0012-10-19 16:30:00", "constellation": "Cygnus", "longitud": "-79.91068"}'  

#TODO:  
Check the hackpad  

