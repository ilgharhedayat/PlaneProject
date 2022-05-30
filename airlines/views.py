import json
import requests
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from .models import Airline
from .utils import city_name, Persian


class SearchListView(View):
    template_name = "airlines/search.html"

    def get(self, request):
        airlines_list = Airline.objects.all()
        flight_count = 0
        trip_list_final = []
        fly_date = request.GET.get('date')
        print(fly_date)
        new_fly_date = Persian(fly_date).gregorian_string()
        for airline in airlines_list:
            trips = requests.get(
                f"http://zv.nirasoftware.com:882/AvailabilityJS.jsp?AirLine={airline.symbol}&cbSource={request.GET.get('source')}&cbTarget={request.GET.get('target')}&cbDay1=_&cbMonth1=_&DepartureDate={str(new_fly_date)}&cbAdultQty={request.GET.get('adult', 0)}&cbChil%20dQty={request.GET.get('child', 0)}&cbInfantQty={request.GET.get('infant', 0)}&OfficeUser={airline.username}&OfficePass={airline.password}"
            )

            a = json.loads(trips.content)
            trip_list = a["AvailableFlights"]

            for i in trip_list:
                adultTotalPrices = i['AdultTotalPrices']
                adultTotalPrices = str(adultTotalPrices).split(' ')
                for adultTotalPrice in adultTotalPrices:
                    print(adultTotalPrice)
                    split = str(adultTotalPrice).split(':')
                    last = split[len(split) - 1]
                    if last != '-':
                        i['AdultTotalPrices'] = last
                        i["image"] = airline.logo.url
                        i["airline_id"] = airline.id
                        i["airline_name"] = airline.name
                        i["DepartureTime"] = i["DepartureDateTime"][11:]
                        i["ArrivalTime"] = i["ArrivalDateTime"][11:]
                        i['persian_date'] = i['DepartureDateTime'][:10]
                        i['origin_city_name'] = city_name.get(i['Origin'])
                        i['destination_city_name'] = city_name.get(i['Destination'])
                        flight_count += 1
                        trip_list_final.append(i)

        request.session["passenger_info"] = {
            "adult": request.GET.get("adult", 0),
            "child": request.GET.get("child", 0),
            "infant": request.GET.get("infant", 0),
        }
        print(request.session["passenger_info"])

        return render(
            request,
            self.template_name,
            {"trip_list": trip_list_final, "flight_count": flight_count, 'airline_list': airlines_list},
        )
