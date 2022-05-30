from django.shortcuts import render

import json

import requests
from airlines.utils import Persian
from django.views.generic import View


# Create your views here.
class HotelView(View):
    def get(self, request):
        response = requests.get('https://api.vhotel.ir/api/V4/hotels', auth=('admin', "iEol5iBJjFCRKIBA"))
        hotel_list = json.loads(response.content)
        print(hotel_list)
        print('asdk')
        count = range(0, 2)
        return render(request, 'hotels/list.html', {'hotels_list': hotel_list, 'count': count})


# parsa
# https://api.vhotel.ir/api/V4/cities

class HotelSearchView(View):
    def get(self, request):
        f = requests.Session()
        headers = {'content-type': 'application/json'}
        my_data = {
            "getRoomsRq": {'hotelsId': [request.GET.get('city_id')]}
        }

        get_data = f.post('https://api.vhotel.ir/api/V4/availabilityByCity/', auth=('admin', "iEol5iBJjFCRKIBA"),
                          data=json.dumps(my_data), timeout=30, headers=headers)
        hotel_list = json.loads(get_data.content)
        return render(request, 'hotels/list.html', {'hotels_list': hotel_list})


class HotelRoomsView(View):
    def get(self, request, city_id):
        go = Persian(request.GET.get('go')).gregorian_string()
        come = Persian(request.GET.get('come')).gregorian_string()
        f = requests.Session()
        headers = {'content-type': 'application/json'}
        my_data = {
            "availabilityRq": {'hotelsId': [city_id]},
            'form': go,
            'to': come,
        }
        get_data = f.post('https://api.vhotel.ir/api/V4/availability', auth=('admin', "iEol5iBJjFCRKIBA"),
                          data=json.dumps(my_data), timeout=30, headers=headers)
        rooms = json.loads(get_data.content)
        print('*' * 99)
        print(rooms)
        return render(request, 'hotels/search.html', {'hotels_list': rooms})


class ReserveRoomView(View):
    def get(self, ):
        pass
