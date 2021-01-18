import json,pickle
import numpy
__locations = None
__data_columns = None
__data_columns_kol = None
__data_columns_del = None
__data_columns_ban = None
__model = None
__model_kol = None
__model_del = None
__model_ban = None

def get_estimated_price(location,sqft,bhk,cp,city):
    if city=='M':
        try:
            loc_index = __data_columns.index(location.lower())
        except:
            loc_index = -1

        x = numpy.zeros(len(__data_columns))
        x[0]=sqft
        x[1]=bhk
        x[2]=cp
        if loc_index >= 0:
            x[loc_index] = 1
        return round(__model.predict([x])[0],2)
    elif city=='K':
        try:
            loc_index = __data_columns_kol.index(location.lower())
        except:
            loc_index = -1

        x = numpy.zeros(len(__data_columns_kol))
        x[0]=sqft
        x[1]=bhk
        x[2]=cp
        if loc_index >= 0:
            x[loc_index] = 1
        return round(__model_kol.predict([x])[0],2)
    elif city=='D':
        try:
            loc_index = __data_columns_del.index(location.lower())
        except:
            loc_index = -1

        x = numpy.zeros(len(__data_columns_del))
        x[0]=sqft
        x[1]=bhk
        x[2]=cp
        if loc_index >= 0:
            x[loc_index] = 1
        return round(__model_del.predict([x])[0],2)
    elif city=='B':
        try:
            loc_index = __data_columns_ban.index(location.lower())
        except:
            loc_index = -1

        x = numpy.zeros(len(__data_columns_ban))
        x[0]=sqft
        x[1]=bhk
        x[2]=cp
        if loc_index >= 0:
            x[loc_index] = 1
        return round(__model_ban.predict([x])[0],2)



def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

def load_saved_artifacts(loc1,loc2,city):#
    print("Loading saved artifacts ... start")
    global __data_columns
    global __data_columns_kol
    global __data_columns_del
    global __data_columns_ban
    global __locations
    global __model
    global __model_kol
    global __model_del
    global __model_ban
    if city=="M":
        with open(loc1,'r') as f:
            __data_columns=json.load(f)['data_columns']
            __locations = __data_columns[3:]
        #if __model is None:
        with open(loc2,'rb') as f:
            __model = pickle.load(f)
        print("Loading artifacts done....")
    elif city == "K":
        with open(loc1,'r') as f:
            __data_columns_kol=json.load(f)['data_columns']
            __locations = __data_columns_kol[3:]
        #if __model is None:
        with open(loc2,'rb') as f:
            __model_kol = pickle.load(f)
        print("Loading artifacts done....")
    elif city == "D":
        with open(loc1,'r') as f:
            __data_columns_del=json.load(f)['data_columns']
            __locations = __data_columns_del[3:]
        #if __model is None:
        with open(loc2,'rb') as f:
            __model_del = pickle.load(f)
        print("Loading artifacts done....")
    elif city == "B":
        with open(loc1,'r') as f:
            __data_columns_ban=json.load(f)['data_columns']
            __locations = __data_columns_ban[3:]
        #if __model is None:
        with open(loc2,'rb') as f:
            __model_ban = pickle.load(f)
        print("Loading artifacts done....")
    


    
    