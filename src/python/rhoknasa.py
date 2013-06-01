import web
import simplejson as json
from itertools import izip

urls = ('/', 'index')

db = web.database(dbn='mysql', user='rhoknasa', pw='rhoknasa', db='rhoknasa', host='rhoknasa.cr5o3gwscupd.us-east-1.rds.amazonaws.com')

class index:
    def GET(self):
        obs = db.select('stargazing_observations')
        #, where="id={0}".format(i))
        web.header('Content-Type', 'application/json')
        result=[]
        for o in obs:
            result.append({"date":str(o.date), "latitude":o.latitude, "longitud": o.longitud, "country":o.country,"constellation":o.constellation,"limiting_magnitude":o.limiting_magnitude, "comments":o.comments})
        d=json.dumps(result)
        return d

    def POST(self):

        i=web.input()
        n=db.insert('stargazing_observations',date=i.date,latitude=i.latitude,longitud=i.longitud,country=i.country,constellation=i.constellation,limiting_magnitude=i.limiting_magnitude,comments=i.comments)
        raise web.seeother('/')
    

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
