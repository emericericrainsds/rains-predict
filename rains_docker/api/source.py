from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
import pprint


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
#templates = Jinja2Templates(directory='templates/')


###############################

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

#########################
#########################
#########################

#res = form_get_predict('12-12-2021:Sydney:23.8:34.9:0:13.2:12.4:NE:39:ENE:ENE:19:15:51:37:1013:1009.4:0:4:27.6:33.1:No')
#print (res)

