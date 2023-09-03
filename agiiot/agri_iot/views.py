#  i have created this file - GTA
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# import uuid, random
import json
from datetime import datetime
import requests


# from .models import Product, Contact
from .models import pricingmodel, APIKey, UserDetails, StoreData

# register
from django.contrib.auth.models import User
# login
from django.contrib.auth import authenticate, login, logout


# ========================================================================================


def index(request):
    return render(request,'agri_iot/welcomepage.html')

def line_chart(request):
    data = [
        ['day1', 30],
        ['day2', 60],
        ['day45', 90],
        ['2010', 7.0],
        ['2011', 6.9],
        ['2012', 9.5],
        ['2013', 6.5],
        ['2014', 9.2],
        ['2015', 10.5],
        ['2016', 11.2],
        ['2017', 12.5],
        ['2018', 19.3],
        ['2019', 20.1],
        ['2020', 19.9],
        ['2021', 24.6]
    ]

    context = {
        'display_data': data
    }
    return render(request, 'agri_iot/line_chart.html', context)

def cropRecommend():
    # https://agromore-api.atharvapawar.repl.co/recommend-crop/?nitrogen=100&phosphorus=300&potassium=300&humidity=300&temperature=300&soilmoisture=300&state=300&rainfall=300&season=300&ph=6.1
    base_url = 'https://agromore-api.atharvapawar.repl.co/recommend-crop/?' # Hosted

    send_data =  {
        "humidity": 300,
        "nitrogen": 100,
        "ph": 6.1,
        "phosphorus": 300,
        "potassium": 300,
        "rainfall": 300,
        "season": 300,
        "soilmoisture": 300,
        "state": 300,
        "temperature": 300,
        }

    # Create the query string for the GET request
    data = "&".join([f"{key}={value}" for key, value in send_data.items()])

    response = requests.get(f'{base_url}{data}')  # Make the GET request to the API
    data = response.json()      # Parse the JSON response
    # print("GET Response:",data) # Display the response
    return data

@login_required
def home(request,  screen_content=None):
    if screen_content == 'analytics':
        
        dataValues = [
                    ['day1', 30],
                    ['day2', 60],
                    ['day45', 90],
                    ['2010', 7.0],
                    ['2011', 6.9],
                    ['2012', 9.5],
                    ['2013', 6.5],
                    ['2014', 9.2],
                    ['2015', 10.5],
                    ['2016', 11.2],
                    ['2017', 12.5],
                    ['2018', 19.3],
                    ['2019', 20.1],
                    ['2020', 19.9],
                    ['2021', 24.6]
                ]

        Data = {
            'title' : "analytics",
            'data' : "data",
            'display_data': dataValues
        }


    elif screen_content == 'datalog':
        # user = 'gta'
        username = request.user.username
        user_data = StoreData.objects.filter(user=username)

        user_data_list = []
        for data in user_data:
            data_dict = {
                "user": data.user,
                "nitrogen": data.nitrogen,
                "phosphorus": data.phosphorus,
                "potassium": data.potassium,
                "humidity": data.humidity,
                "temperature": data.temperature,
                "soil_moisture": data.soil_moisture,
                "ph": data.ph,
                "state": data.state,
                "rainfall": data.rainfall,
                "season": data.season,
                "dateStamp": data.dateStamp,
                "timeStamp": data.timeStamp
            }
            user_data_list.append(data_dict)

        Data = {
            'title' : "datalog",
            'data' : user_data_list,
        }


    elif screen_content == 'api_key':
        all_api_key = APIKey.objects.all()
        for item in all_api_key:
            print(item)

        user = request.user
        # user_details = UserDetails.objects.get(user=user)
        # print(user_details)

        api_key, created = APIKey.objects.get_or_create(user=user)

        Data = {
            'title' : "Access Tokens",
            'apiKey' : api_key,
        }


    elif screen_content == 'documantation':
        Data = {
            'title' : "documantation",
            'data' : "data",
        }

    elif screen_content == 'account':
        # user = request.user

        user = request.user.username
        # user_details = UserDetails.objects.get(user=user)
        # print(user_details)

        try:
            user_details = UserDetails.objects.get(user=user)
            print("User Details:")
            print("Username:", user_details.user)
            print("Phone Number:", user_details.phoneNum)
            print("User Plan:", user_details.userPlan)
            print("User Plan Start Date:", user_details.userPlanStartDate)
            print("User API Key:", user_details.userApiKey)
            print("User Daily Limit Server Requests:", user_details.userDailyLimitServerRequests)
            print("User Daily Limit Chat Requests:", user_details.userDailyLimitChatRequests)
            print("User Daily Limit Rec Requests:", user_details.userDailyLimitRecRequests)
        except UserDetails.DoesNotExist:
            print("User 'gta' not found")

        Data = {
            'title' : "account",
            'data' : user_details,
        }

    else:
        data = [
                ["Nitrogen (N)", "342"],
                ["Phosphorus (P)", "50"],
                ["Potassium (K)", "21"],
                ["Humidity", "80"],
                ["Temperature", "34"],
                ["Soil Moisture", "90"],
                ["State", "Maharashtra"],
                ["Rainfall", "1251"],
                ["Season", "Kharif"]
            ]
        result = cropRecommend()
        # result = {            "RecommendedCrop": "apple",        }
        print("from view",result)
        Data = {
            'title' : "dashboard",
            'data' : data,
            'recommendedCrop' : result ,
        }



    params = {
        'content' : Data,

    }

    return render(request,'agri_iot/index.html',params)




# pricing/monthly/
# pricing/annullay/
def pricing(request, data_param):
    # Retrieve all pricing models
    all_pricing_models = pricingmodel.objects.all()

    # Get a list of pri_planName values
    # plan_names = [model.pri_planName for model in all_pricing_models]

    # plan_monthly = [model.pri_Monthly_price for model in all_pricing_models]
    
    # Split pri_detailslist into lists
    details_lists = [model.pri_detailslist.split(',') for model in all_pricing_models]
    # print("Model json Lists:", all_pricing_models)

    if data_param == "annully":
        pricing_data = []
        for model in all_pricing_models:
            plan_name = model.pri_planName
            annually_price = model.pri_Annually_price
            annually_slug = model.pri_Annually_slug
            
            pricing_data.append({
                'plan_name': plan_name,
                'price': annually_price,
                'slug': annually_slug,
            })
        # print(pricing_data)

        params = {
            'plans' : pricing_data,
            'Details_list' : details_lists,
            'btn' : "annully"
                }

    elif data_param == 'monthly':
        pricing_data = []
        for model in all_pricing_models:
            plan_name = model.pri_planName
            monthly_price = model.pri_Monthly_price
            monthly_slug = model.pri_Monthly_slug
            
            pricing_data.append({
                    'plan_name': plan_name,
                    'price': monthly_price,
                    'slug': monthly_slug,
                })
        # print(pricing_data)

        params = {
            'plans' : pricing_data,
            'Details_list' : details_lists,
            'btn' : "monthly"
                }

    return render(request,'agri_iot/pricingpage.html', params)

"""
Plan Names: ['Start', 'Pro', 'Plus +']
Details Lists: [
    ['1 Month Free IoT server (20 request per day)', ' 20 Crop Recommendation', ' 10 Crop In Detail Description', ' 100 chats with Agro Chat Bot'], 
    ['IoT server (200 request per day)', ' 200 Crop Recommendation', ' 100 Crop In Detail Description', ' 1000 chats with Agro Chat Bot'], 
    ['IoT server (1000 request per day)', ' 500 Crop Recommendation', ' 250 Crop In Detail Description', ' 3000 chats with Agro Chat Bot']
    ]

"""


def recommendation(request):
    username = request.user.username
    return render(request,'agri_iot/formrecommend.html')

@login_required
def generate_api_key(request):
    user = request.user
    # msg = request.POST.get('msg', '')
    # phone = request.POST.get('phone', '')
    api_key, created = APIKey.objects.get_or_create(user=user)
    # username = User.objects.get(username="gts")
    username = request.user.username
    username = User.objects.get(username=username)

    # Update user details
    try:
        user_details = UserDetails.objects.get(user=username)
        user_details.userApiKey = str(api_key)  # Assuming 'api_key' is a variable containing the API key value
        user_details.save()
        print(username,"apiKey saved")
    except UserDetails.DoesNotExist:
        # Handle the case where UserDetails doesn't exist for the user
        print(username,"apiKey not saved")
        
        pass

    # contact = UserDetails(user="name", userApiKey=api_key)
    # contact.save()
    return HttpResponse(f'Your API Key: {api_key.key} created: {created}')

# /store-data/?user=gta&api_key=f8792900-8ffe-4892-83ae-8ac6785f8e49
# /store-data/?user=gta&api_key=f8792900-8ffe-4892-83ae-8ac6785f8e49&nitrogen=100&phosphorus=300&potassium=300&humidity=300&temperature=300&soilmoisture=300&state=300&rainfall=300&season=300&ph=6.1
def store_data(request):
    if request.method == 'GET':
        username = request.GET.get('user')
        api_key = request.GET.get('api_key')
        
        try:
            user_details = UserDetails.objects.get(user=username)
            if (user_details.userApiKey == api_key):
                # print("apiKey: ", user_details.userApiKey,api_key)

                nitrogen = request.GET.get('nitrogen')
                phosphorus = request.GET.get('phosphorus')
                potassium = request.GET.get('potassium')
                humidity = request.GET.get('humidity')
                temperature = request.GET.get('temperature')
                soil_moisture = request.GET.get('soilmoisture')
                ph = request.GET.get('ph')
                state = request.GET.get('state')
                rainfall = request.GET.get('rainfall')
                season = request.GET.get('season')

                current_time = datetime.now().time()
                formatted_time = current_time.strftime('%H:%M:%S')

                current_date = datetime.now().date()
                formatted_date = current_date.strftime('%d/%m/%Y')


                # Create and save the StoreData instance
                store_data = StoreData(
                    user=username,
                    nitrogen=nitrogen,
                    phosphorus=phosphorus,
                    potassium=potassium,
                    humidity=humidity,
                    temperature=temperature,
                    soil_moisture=soil_moisture,
                    ph=ph,
                    state=state,
                    rainfall=rainfall,
                    season=season,
                    dateStamp= formatted_date,
                    timeStamp= formatted_time,
                )
                store_data.save()
                
                return HttpResponse('Data stored successfully.')

        except APIKey.DoesNotExist:
            return HttpResponse('Invalid API key or Unauthorized.', status=401)

    return HttpResponse('Invalid request method.', status=400)



# /recommend-data/?api_key=YOUR_API_KEY
# /recommend-data/?api_key=286ae6c3-bb25-4f6f-8cc4-c06e6004cbe2
# @login_required
# def recommend_data(request):
#     api_key = request.GET.get('api_key')  # Assuming the user provides the API key as a parameter in the request
#     try:
#         api_key_obj = APIKey.objects.get(key=api_key, user=request.user)
#         return HttpResponse(f'Your api_key_obj: {api_key_obj} u got the data')

#     except APIKey.DoesNotExist:
#         return HttpResponse('Invalid API key or Unauthorized.', status=401)

#     # Your logic to recommend data based on the valid API key
#     # ...

#     return HttpResponse('Data recommended based on API key.')

# http://127.0.0.1:8000/recommend-data/?api_key=286ae6c3-bb25-4f6f-8cc4-c06e6004cbe2
# http://127.0.0.1:8000/recommend-data/?api_key=286ae6c3-bb25-4f6f-8cc4-c06e6004cbe2&nitrogen=100&phosphorus=300&potassium=300&humidity=300&temperature=300&soilmoisture=300&state=300&rainfall=300&season=300&ph=6.1

# /recommend-data/?nitrogen=100&phosphorus=300&potassium=300&humidity=300&temperature=300&soilmoisture=300&state=300&rainfall=300&season=300&ph=6.1

@login_required
def recommend_data(request):
    if request.method == 'POST':
        api_key = request.POST.get('api_key')  # Assuming the user provides the API key as a parameter in the request
        try:
            api_key_obj = APIKey.objects.get(key=api_key, user=request.user)

            # Get the JSON data from the request body
            data = request.body.decode('utf-8')
            data_dict = json.loads(data)

            # Your logic to process the data here
            # For example, you can access individual items using data_dict["key"]

            response_data = {
                "message": "Data processed successfully based on the API key (POST Query Type).",
                "data": data_dict,
            }

            return JsonResponse(response_data)

        except APIKey.DoesNotExist:
            return JsonResponse({"error": "Invalid API key or Unauthorized."}, status=401)

    elif request.method == 'GET':
        api_key = request.GET.get('api_key')
        try:
            api_key_obj = APIKey.objects.get(key=api_key, user=request.user)
            username = request.user.username

            data = {
                "Nitrogen (N)": request.GET.get('nitrogen'),
                "Phosphorus (P)": request.GET.get('phosphorus'),
                "Potassium (K)": request.GET.get('potassium'),
                "Humidity": request.GET.get('humidity'),
                "Temperature": request.GET.get('temperature'),
                "Soil Moisture": request.GET.get('soilmoisture'),
                "State": request.GET.get('state'),
                "Rainfall": request.GET.get('rainfall'),
                "Season": request.GET.get('season'),
                "ph": request.GET.get('ph'),
                "apiKey": api_key,
                "username": username,
            }
            prepdata = {
                    "K": int(request.GET.get('potassium')),
                    "N": int(request.GET.get('nitrogen')),
                    "P": int(request.GET.get('phosphorus')),
                    "temperature": int(request.GET.get('temperature')),
                    "humidity": int(request.GET.get('humidity')),
                    "ph": int(request.GET.get('phosphorus')),
                    "rainfall": int(request.GET.get('rainfall')),
                    }
            # recData = recommendCropModel(prepdata)

            response_data = {
                "message": "GET request processed successfully based on the API key. (GET Query Type)",
                "data" : data,
                # "recData" : recData,
            }

            return JsonResponse(response_data)

        except APIKey.DoesNotExist:
            return JsonResponse({"error": "Invalid API key or Unauthorized."}, status=401)

    return JsonResponse({"error": "Invalid request method."}, status=400)

    # if api_key != '92376236751273657162':
        # return JsonResponse({"error": "Invalid API key or Unauthorized."}, status=401)









def contact(request):
    return HttpResponse('agri_iot    |      contact Page')

    # coreMem = Contact.objects.filter(mem_tag="core")
    # teamMem = Contact.objects.filter(mem_tag="team")
    # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

    # return render(request, 'agri_iot/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
    
    # # Fetch the product using the id
    # product = Product.objects.filter(slug=myslug)
    # prodCat = product[0].category
    # # print(prodCat)
    # recproduct = Product.objects.filter(category=prodCat)
    # # print(recproduct)

    # # randomObjects = random.sample(recproduct, 2)
    # randomObjects = random.sample(list(recproduct), 2)


    # return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })


# def index(request):
#     return HttpResponse('Teamzeffort    |      index Page')

def saveUserDetails(username,user_type,phoneNumber):
    # Assuming you have obtained these values from your form or some other source
    # username = "example_username"
    # phoneNumber = "1234567890"
    # accountPlan = "basic"
    # dailyServerReq = 100
    # dailyChatReq = 50
    # dailyRecRequest = 200

    if user_type == 'free':
        accountPlan = "free"
        dailyServerReq = 20
        dailyChatReq = 20
        dailyRecRequest = 20
    elif user_type == 'pro':
        accountPlan = "pro"
        dailyServerReq = 100
        dailyChatReq = 100
        dailyRecRequest = 100
    elif user_type == 'ultrapro':
        accountPlan = "ultrapro"
        dailyServerReq = 200
        dailyChatReq = 200
        dailyRecRequest = 200

    current_date = datetime.now().date()

    userRegisterDetails = UserDetails(
        user=username,
        phoneNum=phoneNumber,
        userPlan=accountPlan,
        userPlanStartDate=current_date,
        userDailyLimitServerRequests=dailyServerReq,
        userDailyLimitChatRequests=dailyChatReq,
        userDailyLimitRecRequests=dailyRecRequest
    )
    userRegisterDetails.save()


# == Register =======================================
def register(request,  user_type=None):
    if request.method == 'POST':
        username = request.POST['username']
        phoneNumber = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                print("user: ", user)
                messages.success(request, 'Registration successful. You can now log in.')

                saveUserDetails(username,user_type,phoneNumber)
                return redirect('user_login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    
    return render(request, 'agri_iot/register.html')

# def register(request, user_type=None):
    # if user_type == 'free':
    #     return HttpResponse("free")
    # elif user_type == 'pro':
    #     return HttpResponse("pro")
    # elif user_type == 'ultrapro':
    #     return HttpResponse("ultrapro")
    # else:
    #     return HttpResponse("simple login")

# == Login =======================================
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to your app's user account | home page
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    
    return render(request, 'agri_iot/login.html')






# == Logout =======================================

def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to your login page or any other page after logout

# == Edit User Profile =======================================
from .forms import MyDataForm

# def edit_profile(request):
    # return render(request, 'agri_iot/edit_profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = MyDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = MyDataForm()

    return render(request, 'agri_iot/edit_profile.html', {'form': form})



# == ML: Crop Recommend =======================================

# http://127.0.0.1:8000/apikey/data/?nitrogen=100&phosphorus=300&potassium=300&humidity=300&temperature=300&soilmoisture=300&state=300&rainfall=300&season=300

# http://127.0.0.1:8000/apikey/data/?

# http://localhost:8000/apikey/data/?apikey=92376236751273657162&nitrogen=100&phosphorus=300&potassium=300&humidity=300&temperature=300&soilmoisture=300&state=300&rainfall=300&season=300



# API

# get field data 

def getfielddata(request):
# Create a dictionary to store the parameter values
    parameter_values = {}

    # Get the parameters from the request's GET query parameters
    for param_name, param_value in request.GET.items():
        # Convert the parameter name to lowercase
        param_name = param_name.lower()

        # Store the lowercase parameter name and its value in the dictionary
        parameter_values[param_name] = int(param_value)

    # Process the values as needed (e.g., store them in the database or use them in calculations)
    # For this example, we'll just display the parameter values as a response
    response = ", ".join(f"{param}: {value}" for param, value in parameter_values.items())
    return HttpResponse(response)