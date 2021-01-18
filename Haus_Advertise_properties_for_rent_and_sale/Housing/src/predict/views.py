from django.shortcuts import render,redirect
from .forms import City,MumbaiPredictForm,KolkataPredictForm,DelhiPredictForm,BangalorePredictForm
from .import util
from django.contrib import messages
'''
# Create your views here.
def predict(request):
    predicted_price=''
    if request.method == 'POST':
        predict_form = PredictForm(request.POST)
        if predict_form.is_valid():
            city = predict_form.cleaned_data['city']
            
            location = mumbai_form.cleaned_data['location']
            sqft = mumbai_form.cleaned_data['area']
            bhk = mumbai_form.cleaned_data['Number_of_bedrooms']
            cp = mumbai_form.cleaned_data['parking_available']
            if cp == "Yes":
                cp=1
            else:
                cp=0
            predicted_price = util.get_estimated_price(location,sqft,bhk,cp)
            mumbai_form = MumbaiForm()
            messages.add_message(request, messages.SUCCESS, 'As Per Our Predictions Price will be INR '+str(predicted_price)+' Lakhs')
    else:
        mumbai_form = MumbaiForm()


    context = {'mum_form':mumbai_form}
    return render(request,'predict/predict.html',context)
    '''
selected_city = ''
def city_select(request):
    
    if request.method == 'POST':
        print("in if")
        select_city = City(request.POST)
        if select_city.is_valid():
            print('imvalid')
            global selected_city
            selected_city = select_city.cleaned_data['city']
            select_city = City()
            context = {'city':selected_city}
            print(context['city'])
            return redirect('http://127.0.0.1:8000/predict/price/')
    else:
        print("in else")
        select_city = City()
        context = {'select_city_form':select_city,'city':''}
        return render(request,'predict/predict.html',context)
    
    

def predict(request):
    print("In predict")
    print(selected_city)
    if selected_city == '1':
        predicted_price=''
        if request.method == 'POST':
            mumbai_form = MumbaiPredictForm(request.POST)
            if mumbai_form.is_valid():
                location = mumbai_form.cleaned_data['location']
                sqft = mumbai_form.cleaned_data['area']
                bhk = mumbai_form.cleaned_data['Number_of_bedrooms']
                cp = mumbai_form.cleaned_data['parking_available']
                if cp == "Yes":
                    cp=1
                else:
                    cp=0
                predicted_price = util.get_estimated_price(location,sqft,bhk,cp,'M')
                mumbai_form = MumbaiPredictForm()
                messages.add_message(request, messages.SUCCESS, 'As Per Our Predictions Price will be INR '+str(predicted_price)+' Lakhs')
        else:
            mumbai_form = MumbaiPredictForm()
        context = {'predict_form':mumbai_form,'city':selected_city}
        return render(request,'predict/predict.html',context)

    elif selected_city == '2':
        predicted_price=''
        if request.method == 'POST':
            kolkata_form = KolkataPredictForm(request.POST)
            if kolkata_form.is_valid():
                location = kolkata_form.cleaned_data['location']
                sqft = kolkata_form.cleaned_data['area']
                bhk = kolkata_form.cleaned_data['Number_of_bedrooms']
                cp = kolkata_form.cleaned_data['parking_available']
                if cp == "Yes":
                    cp=1
                else:
                    cp=0
                predicted_price = util.get_estimated_price(location,sqft,bhk,cp,'K')
                kolkata_form = KolkataPredictForm()
                messages.add_message(request, messages.SUCCESS, 'As Per Our Predictions Price will be INR '+str(predicted_price)+' Lakhs')
        else:
            kolkata_form = KolkataPredictForm()
        context = {'predict_form':kolkata_form,'city':selected_city}
        return render(request,'predict/predict.html',context)

    elif selected_city == '3':
        predicted_price=''
        if request.method == 'POST':
            delhi_form = DelhiPredictForm(request.POST)
            if delhi_form.is_valid():
                location =delhi_form.cleaned_data['location']
                sqft = delhi_form.cleaned_data['area']
                bhk =  delhi_form.cleaned_data['Number_of_bedrooms']
                cp = delhi_form.cleaned_data['parking_available']
                if cp == "Yes":
                    cp=1
                else:
                    cp=0
                predicted_price = util.get_estimated_price(location,sqft,bhk,cp,'D')
                delhi_form = DelhiPredictForm()
                messages.add_message(request, messages.SUCCESS, 'As Per Our Predictions Price will be INR '+str(predicted_price)+' Lakhs')
        else:
            delhi_form = DelhiPredictForm()
        context = {'predict_form':delhi_form,'city':selected_city}
        return render(request,'predict/predict.html',context)

    elif selected_city == '4':
        predicted_price=''
        if request.method == 'POST':
            bangalore_form = BangalorePredictForm(request.POST)
            if bangalore_form.is_valid():
                location =bangalore_form.cleaned_data['location']
                sqft = bangalore_form.cleaned_data['area']
                bhk =  bangalore_form.cleaned_data['Number_of_bedrooms']
                cp = bangalore_form.cleaned_data['parking_available']
                if cp == "Yes":
                    cp=1
                else:
                    cp=0
                predicted_price = util.get_estimated_price(location,sqft,bhk,cp,'B')
                bangalore_form = BangalorePredictForm()
                messages.add_message(request, messages.SUCCESS, 'As Per Our Predictions Price will be INR '+str(predicted_price)+' Lakhs')
        else:
            bangalore_form = BangalorePredictForm()
        context = {'predict_form':bangalore_form,'city':selected_city}
        return render(request,'predict/predict.html',context)



