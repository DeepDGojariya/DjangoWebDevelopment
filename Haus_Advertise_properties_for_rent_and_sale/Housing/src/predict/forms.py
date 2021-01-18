from .import util 
from django import forms

util.load_saved_artifacts('C:/Users/deepg/Desktop/Hotel_website/Model/Datasets/mumbai_columns.json',
                        'C:/Users/deepg/Desktop/Hotel_website/Model/Datasets/mumbai_model.pickle','M')
location_names_mumbai = util.get_location_names()
MUM_LOC = [("0","")]
count=1
for i in range(len(location_names_mumbai)):
    MUM_LOC.append((str(count),location_names_mumbai[i]))
    count+=1
MUM_LOC = tuple(MUM_LOC)


class MumbaiPredictForm(forms.Form):
    location = forms.ChoiceField(choices = MUM_LOC)
    area = forms.FloatField()
    Number_of_bedrooms = forms.IntegerField()
    parking_available = forms.ChoiceField(choices=(("1","Yes"),("2","No")))

#######################################################################################

util.load_saved_artifacts('C:/Users/deepg/Desktop/Hotel_website/Model/Datasets/kolkata_columns.json',
                        'C:/Users/deepg/Desktop/Hotel_website/Model/Datasets/kolkata_model.pickle','K')
location_names_kolkata = util.get_location_names()
KOL_LOC = [("0","")]
count=1
for i in range(len(location_names_kolkata)):
    KOL_LOC.append((str(count),location_names_kolkata[i]))
    count+=1
KOL_LOC = tuple(KOL_LOC)

class KolkataPredictForm(forms.Form):
    location = forms.ChoiceField(choices = KOL_LOC)
    area = forms.FloatField()
    Number_of_bedrooms = forms.IntegerField()
    parking_available = forms.ChoiceField(choices=(("1","Yes"),("2","No")))

#######################################################################################

util.load_saved_artifacts('C:/Users/deepg/Desktop/Hotel_website/Model/Datasets/delhi_columns.json',
                        'C:/Users/deepg/Desktop/Hotel_website/Model/Datasets/delhi_model.pickle','D')
location_names_delhi = util.get_location_names()
DEL_LOC = [("0","")]
count=1
for i in range(len(location_names_delhi)):
    DEL_LOC.append((str(count),location_names_delhi[i]))
    count+=1
DEL_LOC = tuple(DEL_LOC)

class DelhiPredictForm(forms.Form):
    location = forms.ChoiceField(choices = DEL_LOC)
    area = forms.FloatField()
    Number_of_bedrooms = forms.IntegerField()
    parking_available = forms.ChoiceField(choices=(("1","Yes"),("2","No")))


#######################################################################################

util.load_saved_artifacts('C:/Users/deepg/Desktop/Hotel_website/Model/Datasets/bangalore_columns.json',
                        'C:/Users/deepg/Desktop/Hotel_website/Model/Datasets/bangalore_model.pickle','B')
location_names_bangalore = util.get_location_names()
BAN_LOC = [("0","")]
count=1
for i in range(len(location_names_bangalore)):
    BAN_LOC.append((str(count),location_names_bangalore[i]))
    count+=1
BAN_LOC = tuple(BAN_LOC)

class BangalorePredictForm(forms.Form):
    location = forms.ChoiceField(choices = BAN_LOC)
    area = forms.FloatField()
    Number_of_bedrooms = forms.IntegerField()
    parking_available = forms.ChoiceField(choices=(("1","Yes"),("2","No")))


class City(forms.Form):
    CITIES = (("0",""),("1","Mumbai"),("2","Kolkata"),("3","Delhi"),("4","Bangalore"))
    city = forms.ChoiceField(choices=CITIES)

