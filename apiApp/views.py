from http.client import REQUEST_URI_TOO_LONG
from typing import Union
from typing import List
from urllib import response
from fastapi import APIRouter,Body

from apiApp.models import adress_data

from apiApp.schema import addressDataCreate,addressDataDelete, addressDataGet,addressDataUpdate

app_routes = APIRouter()

'''                Note 
# data variable is used for response purpose
# body is defined for example purpose
# In this project FastApi is used for Response and Django for ORM feature'''


#-----------  Get All address --------------------------------------------
@app_routes.get("/get_all_address")
def get_all_address( ):
    data = list(adress_data.objects.all().values())
    if len(data)==0:
        data = {'Status':'Success',
                'data':'No records found'}
    return data



#-----------  Get address as per coodinates  --------------------------------------------
@app_routes.post("/get_request_address")
def get_request_address(request:addressDataGet = Body(
                                            examples={
                                                "normal": {
                                                    "summary": "A normal example",
                                                    "description": "Please enter both the coordinates to get results",
                                                    "value": {
                                                        "latitude": 51.343452,
                                                        "longitude": 21.123462,
                                                            },
                                                            }
                                                    }
                                            )
            ):
    if (request.latitude == None or request.longitude == None ):
        data = {'Status':'Failed',
                'data':'Coordinates missing'}
        return data
    else:
        data = list(adress_data.objects.filter(lat = request.latitude,long = request.longitude).values())
        
    if len(data)==0:
        data = {'Status':'Success',
                'data':'No records found'}
    return data

#-----------  creation of address --------------------------------------------
@app_routes.post('/create_address')
def create_address(request:addressDataCreate):
    try:
        cord_check = adress_data.objects.get(lat = request.latitude)
        if float(cord_check.long) == request.longitude :
            response = {
                        'Status':'Failed',
                        'Message':'coordinates already exist'
                        }
            return response
    except:
        pass
    data = adress_data(
                    add = request.address,
                    lat = request.latitude,
                    long = request.longitude,
                    contact = request.contact
                    )
    data.save()  
    data = adress_data.objects.filter(lat = request.latitude,long = request.longitude).values()
    response = {
        'Status':'Success',
        'Message':'Address Created',
        'instruction':'Note ID for further modification',
        'data':list(data)[-1]
                }
    return response

#-----------  delete address as per request --------------------------------------------
@app_routes.delete('/delete_address')
def delete_address(request:addressDataDelete):
    print(type(request.id))
    data = adress_data.objects.filter(id = request.id).values()
    if len(data) == 0:
        response = {
                    'Status':'Failed',
                    'Message':'ID does not exist'
                    }
        return response
    adress_data.objects.filter(id = request.id).delete()
    return {'Status':'Succes',
            'Message':'Address Deleted',
            'address' :list(data)[-1]
            }


#-----------  updation of address --------------------------------------------
@app_routes.put('/update_address')
def update_address(request:addressDataUpdate = Body(
                                                    examples={
                                                        "normal": {
                                                            "summary": "A normal example",
                                                            "description": "ID is mandatory filed and keep only that field which you want to update.",
                                                            "value": {
                                                                "id": "Your ID",
                                                                "address": "new address if not required please remove this field",
                                                                "latitude": "new latitude if not required please remove this field",
                                                                "longitude": "new longitude if not required please remove this field",
                                                                "contact":"new contact if not required please remove this field"
                                                                    },
                                                                  }
                                                            }
                                                    )
                  ):
    req_id = request.id
    try:
        adress_data.objects.get(id = request.id)
    except:
        response = {
                    'Status':'Failed',
                    'Message':'ID does not exist'
                    }
        return response

    data = adress_data.objects.filter(id = req_id)
    if request.address != None :
        data.update(add = request.address)
    
    if request.latitude != None :
        data.update(lat = request.latitude)
    
    if request.longitude != None :
        data.update(long = request.longitude)

    if request.longitude != None :
        data.update(contact = request.longitude)

    print('\n',data,'\n')
    data = adress_data.objects.filter(id = request.id).values()
    response = {
        'Status': 'Sucess',
        'Message': 'Updation Successfull',
        'updated_data': list(data)[-1]
    }
    return response