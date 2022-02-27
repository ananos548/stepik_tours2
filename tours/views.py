from django.shortcuts import render
from random import sample
from tours import data
from tours.data import title, description, subtitle, departures, tours


def main_view(request):
    tours_random = dict(sample(data.tours.items(), 6))
    context = {'departure': departures,
               'title': title,
               'description': description,
               'subtitle': subtitle,
               'tour': tours,
               'tours_random': tours_random
               }
    return render(request, 'tours/index.html', context=context)


def departure_view(request, departure):
    tour_departure = {key: j for key, j in tours.items() if j['departure'] == departure}
    # tour_departure = {}
    # for key, j in tours.items():
    # if key == tours_departures:
    # tours_departures = values

    price = [i['price'] for i in tour_departure.values()]  # [выражения, for значение(i) in коллекция]
    nights = [j['nights'] for j in tour_departure.values()]

    context = {
        'departure': departures,
        'title': title,
        'description': description,
        'subtitle': subtitle,
        'tour': tours,
        'departures': departures[departure],  # взять нужный тур и положить в него имя направления
        'tour_departure': tour_departure,
        'num_tours': len(tour_departure),
        'min_price': min(price),
        'max_price': max(price),
        'min_night': min(nights),
        'max_night': max(nights)
    }
    return render(request, 'tours/departure.html', context)


def tour_view(request, id):
    tour_id = data.tours.get(id)
    dep_title = data.departures[tour_id['departure']]
    context = {'id': tour_id,
               'title': title,
               'departure': departures,
               'description': description,
               'subtitle': subtitle,
               'tour': tours,
               'dep_title': dep_title,
               }
    return render(request, 'tours/tour.html', context)
