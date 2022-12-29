from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

import psycopg2
import pandas as pd
import numpy as np

from sklearn.metrics import confusion_matrix

from os import listdir
from os.path import isfile, join

from joblib import dump, load

###############################


app = FastAPI()
#    openapi_tags = [
#    {
#        'name':'rainspredict',
#        'description': 'entry point'
#    }
#])
templates = Jinja2Templates(directory='templates/')

##################################
##################################
# api
##################################
##################################


g_ = {} # global dict
g_['modeles'] = {}
g_['modeles']['dir'] = './modeles/'
g_['modeles']['load'] = {}

g_['current_vars'] = {}
g_['current_vars']['Date'] = None
g_['current_vars']['Location'] = None
g_['current_vars']['MinTemp'] = None
g_['current_vars']['MaxTemp'] = None
g_['current_vars']['Rainfall'] = None
g_['current_vars']['Evaporation'] = None
g_['current_vars']['Sunshine'] = None
g_['current_vars']['WindGustSpeed'] = None
g_['current_vars']['WindSpeed9am'] = None
g_['current_vars']['WindSpeed3pm'] = None
g_['current_vars']['Humidity9am'] = None
g_['current_vars']['Humidity3pm'] = None
g_['current_vars']['Pressure9am'] = None
g_['current_vars']['Pressure3pm'] = None
g_['current_vars']['Cloud9am'] = None
g_['current_vars']['Cloud3pm'] = None
g_['current_vars']['Temp9am'] = None
g_['current_vars']['Temp3pm'] = None
g_['current_vars']['WindDir3pm'] = None
g_['current_vars']['WindDir9am'] = None
g_['current_vars']['WindGustDir'] = None
g_['current_vars']['RainToday'] = None
#g_['current_vars']['RainTomorrow'] = None

g_['y_var_name'] = 'RainTomorrow'

  # order is important
g_['windcat'] = ['WindDir3pm','WindDir9am','WindGustDir']
  # order is important
g_['windir'] = ['E', 'ENE', 'ESE', 'N', 'NE', 'NNE', 'NNW', 'NW', 'S', 'SE', 'SSE', 'SSW', 'SW', 'W', 'WNW', 'WSW']
g_['windirnum'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

g_['drop_var'] = ['Date','Location','RainToday']#,'RainTomorrow']

g_['X'] = pd.core.frame.DataFrame()
g_['y'] = pd.core.series.Series(dtype='object')


g_['vp'] = g_['fp'] = g_['vn'] = g_['fn'] = 0

###################################
def create_popule_X():

  global g_
  # order is important
  g_['X']['MinTemp'] = [g_['current_vars']['MinTemp']]
  g_['X']['MaxTemp'] = [g_['current_vars']['MaxTemp']]
  g_['X']['Rainfall'] = [g_['current_vars']['Rainfall']]
  g_['X']['Evaporation'] = [g_['current_vars']['Evaporation']]
  g_['X']['Sunshine'] = [g_['current_vars']['Sunshine']]
  g_['X']['WindGustSpeed'] = [g_['current_vars']['WindGustSpeed']]
  g_['X']['WindSpeed9am'] = [g_['current_vars']['WindSpeed9am']]
  g_['X']['WindSpeed3pm'] = [g_['current_vars']['WindSpeed3pm']]
  g_['X']['Humidity9am'] = [g_['current_vars']['Humidity9am']]
  g_['X']['Humidity3pm'] = [g_['current_vars']['Humidity3pm']]
  g_['X']['Pressure9am'] = [g_['current_vars']['Pressure9am']]
  g_['X']['Pressure3pm'] = [g_['current_vars']['Pressure3pm']]
  g_['X']['Cloud9am'] = [g_['current_vars']['Cloud9am']]
  g_['X']['Cloud3pm'] = [g_['current_vars']['Cloud3pm']]
  g_['X']['Temp9am'] = [g_['current_vars']['Temp9am']]
  g_['X']['Temp3pm'] = [g_['current_vars']['Temp3pm']]
  for wc in g_['windcat']:
    for wd in g_['windir']:
      var_0 = wc+'_'+wd
      g_['X'][var_0] = [0]
    var_1 = wc+'_'+g_['current_vars'][wc]
    g_['X'][var_1] = [1]

###################################

def load_modeles():

  global g_
  fichiers = [f for f in listdir(g_['modeles']['dir']) if isfile(join(g_['modeles']['dir'], f))]
  for f in fichiers:
    name = f[:-4]
    g_['modeles']['load'][name] = load(g_['modeles']['dir']+'/'+f)

##################################
def replace_yn(df = None):

  global g_
  if type(df).__name__ == 'NoneType':
    df = g_['X']
  vars = df.select_dtypes("O").columns.tolist()
  for v in vars:
    df[v]= df[v].replace(['Yes','No'],[1, 0])

##################################
def prepare_df():

  global g_
  create_popule_X()
  replace_yn()

##################################
def apply_modeles():

  global g_
  g_['y']= g_['modeles']['load'][g_['current_vars']['Location']].predict(g_['X'])

##################################
def set_g_vars(datas):

  global g_
  #order is important
  g_['current_vars']['Date'],\
  g_['current_vars']['Location'],\
  g_['current_vars']['MinTemp'],\
  g_['current_vars']['MaxTemp'],\
  g_['current_vars']['Rainfall'],\
  g_['current_vars']['Evaporation'],\
  g_['current_vars']['Sunshine'],\
  g_['current_vars']['WindGustDir'],\
  g_['current_vars']['WindGustSpeed'],\
  g_['current_vars']['WindDir9am'],\
  g_['current_vars']['WindDir3pm'],\
  g_['current_vars']['WindSpeed9am'],\
  g_['current_vars']['WindSpeed3pm'],\
  g_['current_vars']['Humidity9am'],\
  g_['current_vars']['Humidity3pm'],\
  g_['current_vars']['Pressure9am'],\
  g_['current_vars']['Pressure3pm'],\
  g_['current_vars']['Cloud9am'],\
  g_['current_vars']['Cloud3pm'],\
  g_['current_vars']['Temp9am'],\
  g_['current_vars']['Temp3pm'],\
  g_['current_vars']['RainToday'] = datas.split(':')
  
  g_['current_vars']['MinTemp'] = float(g_['current_vars']['MinTemp'])
  g_['current_vars']['MaxTemp'] = float(g_['current_vars']['MaxTemp'])
  g_['current_vars']['Rainfall'] = int(g_['current_vars']['Rainfall'])
  g_['current_vars']['Evaporation'] = float(g_['current_vars']['Evaporation'])
  g_['current_vars']['Sunshine'] = float(g_['current_vars']['Sunshine'])
  g_['current_vars']['WindGustSpeed'] = int(g_['current_vars']['WindGustSpeed'])
  g_['current_vars']['WindSpeed9am'] = int(g_['current_vars']['WindSpeed9am'])
  g_['current_vars']['WindSpeed3pm'] = int(g_['current_vars']['WindSpeed3pm'])
  g_['current_vars']['Humidity9am'] = int(g_['current_vars']['Humidity9am'])
  g_['current_vars']['Pressure9am'] = float(g_['current_vars']['Pressure9am'])
  g_['current_vars']['Pressure3pm'] = float(g_['current_vars']['Pressure3pm'])
  g_['current_vars']['Cloud9am'] = int(g_['current_vars']['Cloud9am'])
  g_['current_vars']['Cloud3pm'] = int(g_['current_vars']['Cloud3pm'])
  g_['current_vars']['Temp9am'] = float(g_['current_vars']['Temp9am'])
  g_['current_vars']['Temp3pm'] = float(g_['current_vars']['Temp3pm'])
  
  #print (g_['current_vars'])

  #g_['X'] = pd.DataFrame(g_['current_vars'], index=[0])
  
##################################
def apply():

  global g_
  load_modeles()
  prepare_df()
  apply_modeles()
##################################

##################################

##################################

##################################

@app.get('/RainsPredict/{datas}')#, tags=['RainsPredict'])
def form_get_predict(datas):
 
  global g_
  set_g_vars(datas)
  apply()
  res = g_['y'][0]
  return {'prediction' : int(res) }

##################################

# Requête pour tester l'API
@app.get('/test')
def form_get():


  return 'OK'

##################################
##################################
# db
##################################
##################################

g_['HOST'] = "database" # from container 
#g_['HOST'] = "localhost" # from host (test)
g_['PORT']="5432"
g_['USER'] = "postgres"
g_['PASSWORD'] = "postgres"
g_['DATABASE'] = "postgres"

g_['VARS'] = \
    'Date VARCHAR(10),\
    Location VARCHAR(20),\
    MinTemp FLOAT,\
    MaxTemp FLOAT,\
    Rainfall FLOAT,\
    Evaporation FLOAT,\
    Sunshine FLOAT,\
    WindGustDir VARCHAR(6),\
    WindGustSpeed FLOAT,\
    WindDir9am VARCHAR(6),\
    WindDir3pm VARCHAR(6),\
    WindSpeed9am FLOAT,\
    WindSpeed3pm FLOAT,\
    Humidity9am FLOAT,\
    Humidity3pm FLOAT,\
    Pressure9am FLOAT,\
    Pressure3pm FLOAT,\
    Cloud9am FLOAT,\
    Cloud3pm FLOAT,\
    Temp9am FLOAT,\
    Temp3pm FLOAT,\
    RainToday VARCHAR(3),\
    RainTomorrow VARCHAR(3)'

##################################

def db_connect():
  
  global g_
  # Open connection
  conn = psycopg2.connect("host=%s port=%s dbname=%s user=%s password=%s"\
   % (g_['HOST'], g_['PORT'], g_['DATABASE'], g_['USER'], g_['PASSWORD']))
  return conn

##################################

def db_close(conn):
  
  conn.close()
  
##################################

@app.get('/db_request/{request}')
def db_request(request):
  
  global g_
  print (request)

  conn = db_connect()
  cur = conn.cursor()

  cur.execute(request)
  conn.commit()
 
  res = ''
  try:
    res = cur.fetchall()
    print(res)
  except:
    pass

  db_close(conn)

  return res

##################################

@app.get('/db_init_table')
def db_init_table():

  db_request('DROP TABLE IF EXISTS RAINS_PREDICT;')
  return db_request('CREATE TABLE RAINS_PREDICT ('+g_['VARS']+');')

##################################

@app.get('/db_load_csv/')
def db_load_csv():

  #db_request('COPY RAINS_PREDICT FROM \''+file_csv+'\' DELIMITER \',\' CSV HEADER;')
  return db_request('COPY RAINS_PREDICT FROM \'/home/rains_docker/input/rains.csv\' DELIMITER \',\' CSV HEADER;')


##################################

@app.get('/db_insert/{row}')
def db_insert(row):

  return db_request('INSERT INTO RAINS_PREDICT VALUES ('+row+')')

##################################

# html get
@app.get('/db_insert/')
def form_get(request:Request):
  global g_
  result = 'Fill all the fields ...'
  return templates.TemplateResponse('insert.html', context={'request': request, 'questions': 'questions', 'result': result})

##################################

@app.post('/db_insert/')
def form_post(request:Request,
              Date:str = Form(...),
              Location:str = Form(...),
              MinTemp:float = Form(...),
              MaxTemp:float = Form(...),
              Rainfall:float = Form(...),
              Evaporation:float = Form(...),
              Sunshine:float = Form(...),
              WindGustDir:str = Form(...),
              WindGustSpeed:float = Form(...),
              WindDir9am:str = Form(...),
              WindDir3pm:str = Form(...),
              WindSpeed9am:float = Form(...),
              WindSpeed3pm:float = Form(...),
              Humidity9am:float = Form(...),
              Humidity3pm:float = Form(...),
              Pressure9am:float = Form(...),
              Pressure3pm:float = Form(...),
              Cloud9am:float = Form(...),
              Cloud3pm:float = Form(...),
              Temp9am:float = Form(...),
              Temp3pm:float = Form(...),
              RainToday:str = Form(...),
              RainTomorrow:str = Form(...)
            ):
    
  global g_
  row = '\''+Date+'\',\''+Location+'\','+str(MinTemp)+','+str(MaxTemp)+','+str(Rainfall)+','+str(Evaporation)+\
        ','+str(Sunshine)+',\''+WindGustDir+'\','+str(WindGustSpeed)+','+\
        '\''+WindDir9am+'\',\''+WindDir3pm+'\','+str(WindSpeed9am)+','+str(WindSpeed3pm)+','+str(Humidity9am)+','+\
        str(Humidity3pm)+','+str(Pressure9am)+','+str(Pressure3pm)+','+str(Cloud9am)+','+\
        str(Cloud3pm)+','+str(Temp9am)+','+str(Temp3pm)+',\''+RainToday+'\',\''+RainTomorrow+'\'' 


  print (row)
  db_insert(row)

  result = ''#get_current_choice()
  return templates.TemplateResponse('insert.html', context={'request': request, 'questions': 'questions', 'result': result})


##################################

@app.get('/db_test')
def db_test():

  return db_request('SHOW ALL')

#########################
######### TEST ##########
#########################

#res = form_get_predict('12-12-2021:Sydney:23.8:34.9:0:13.2:12.4:NE:39:ENE:ENE:19:15:51:37:1013:1009.4:0:4:27.6:33.1:No')
#print (res)

#db_test()
#db_init_table()

#db_load_csv('/home/rains_docker/input/rains.csv') #from server point of view
#db_load_csv()

#db_request('SELECT * FROM RAINS_PREDICT WHERE Location = \'Melbourne\';')
#db_request('SELECT * FROM RAINS_PREDICT;')

