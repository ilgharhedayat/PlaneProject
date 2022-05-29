from django.shortcuts import render

import json

import requests

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
    def get(self, request):
        f = requests.Session()
        headers = {'content-type': 'application/json'}
        my_data = {
            "availabilityRq": {'hotelsId': [request.GET.get('')]},
            'form': '2022-5-26',
            'to': '2022-5-30',
        }
        get_data = f.post('https://api.vhotel.ir/api/V4/availability', auth=('admin', "iEol5iBJjFCRKIBA"),
                          data=json.dumps(my_data), timeout=30, headers=headers)
        rooms = json.loads(get_data.content)
        print(rooms)
        return render(request, 'hotels/search.html', {'hotels_list': rooms})


class ReserveRoomView(View):
    def get(self, ):
        pass
