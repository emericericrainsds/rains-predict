curl -X GET -i http://127.0.0.1:8002/test
curl -X GET -i http://127.0.0.1:8002/RainsPredict/2012-01-13:Perth:23.8:34.9:0:13.2:12.4:NE:39:ENE:ENE:19:15:51:37:1013:1009.4:0:4:27.6:33.1:No

# http://localhost:8002/docs

# 1) creation de la table image du fichier 'rains.csv'
#    http://localhost:8002/db_init_table

# 2) verification que la tables existe & vide  
#    'select * from RAINS_PREDICT limit 10'
#    http://localhost:8002/db_request/select%20%2A%20from%20RAINS_PREDICT%20limit%2010

# 3) population de la table
#    http://localhost:8002/db_load_csv/

# 4) verification que la tables existe & contient des records 
#    'select * from RAINS_PREDICT limit 10'
#    http://localhost:8002/db_request/select%20%2A%20from%20RAINS_PREDICT%20limit%2010

# 5) test insertion row (GET)
#    init/reinit table RAINS_PREDICT
#    http://localhost:8002/db_init_table
#    insertion one row:
#    '2012-01-13','Perth',23.8,34.9,0,13.2,12.4,'NE',39,'ENE','ENE',19,15,51,37,1013,1009.4,0,4,27.6,33.1,'No','No'
#    http://localhost:8002/db_insert/%272012-01-13%27%2C%27Perth%27%2C23.8%2C34.9%2C0%2C13.2%2C12.4%2C%27NE%27%2C39%2C%27ENE%27%2C%27ENE%27%2C19%2C15%2C51%2C37%2C1013%2C1009.4%2C0%2C4%2C27.6%2C33.1%2C%27No%27%2C%27No%27
#    verification
#    http://localhost:8002/db_request/select%20%2A%20from%20RAINS_PREDICT%20limit%2010


#  6) test insertion rom (POST)
#    init/reinit table RAINS_PREDICT
#    http://localhost:8002/db_init_table
#    insertion one row:
#    http://localhost:8002/db_insert/
#     Date         Location  MinTemp  MaxTemp  Rainfall  Evaporation   Sunshine      WindGustDir  WindGustSpeed  WindDir9am   WindDir3pm  WindSpeed9am  WindSpeed3pm  Humidity9am  Humidity3pm  Pressure9am Pressure3pm  Cloud9am Cloud3pm  Temp9am  Temp3pm  RainToday  RainTomorrow                        
#    2012-01-13,   Perth,    23.8,    34.9,    0,        13.2,         12.4,         NE,          39,            ENE,         ENE,        19,           15,           51,          37,          1013,       1009.4,      0,       4,        27.6,    33.1,    No,        No

