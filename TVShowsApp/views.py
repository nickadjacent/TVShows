from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from .models import *


# ******* intial render pages *********


def index(request):

    return render(request, 'index.html')


def allShows(request):
    context = {
        'shows': Show.objects.all(),
        'networks': Network.objects.all(),
    }
    return render(request, 'allShows.html', context)


def editShow(request, show_id):
    print(request.POST)
    context = {
        'show': Show.objects.all().get(id=show_id)

    }

    return render(request, 'editShow.html', context)


def showInfo(request, show_id):

    show = Show.objects.get(id=show_id)

    context = {
        'show': show,
    }

    print(show)

    return render(request, 'showInfo.html', context)


# ***** redirecting paths to initial renders *****

def create_new_show(request):
    print(request.POST)

    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        network_list = Network.objects.filter(name=request.POST['network'])

        if len(network_list) == 0:
            new_network = Network.objects.create(
                name=request.POST['network']
            )
        else:
            new_network = network_list[0]

        new_show = Show.objects.create(
            title=request.POST['title'],
            network=new_network,
            release_date=request.POST['release date'],
            description=request.POST['description'],
        )
        messages.success(request, 'Show successfully created')

        return redirect(f'/showInfo/{new_show.id}')


def delete_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()

    return redirect('/allShows')


def update_show(request, show_id):
    print('updating show')

    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/editShow/{show_id}')

    else:
        update = Show.objects.get(id=show_id)

        print(request.POST)

        update.title = request.POST['title']
        try:
            new_network = Network.objects.get(name=request.POST['network'])
            update.network = new_network
        except:
            new_network = Network.objects.create(
                name=request.POST['network']
            )
            update.network = new_network

        update.release_date = request.POST['release date']
        update.description = request.POST['description']

        update.save()
        messages.success(request, 'Show successfully updated')

        return redirect(f'/showInfo/{show_id}')


# def update(request, id):
#     errors = Show.objects.basic_validator(request.POST)
#     if len(errors) > 0:
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect(f'/editShow/{show_id}')
#     else:
#         show = Show.objects.get(id=id)
#         show.title = request.POST['title']
#         show.network = request.POST['network']
#         show.save()
#         messages.success(request, 'Show successfully updated')
#         return redirect('allShows')
