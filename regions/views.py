from django.shortcuts import render, get_list_or_404, get_object_or_404
import json
from cartas.models import Set1
import regions


def index(request):
    return render(request, 'index.html')


def filter_page(request):
    cards = Set1.objects.all()
    list_cards = Set1.objects.none()

    if request.method == 'POST':
        filter_tag = request.POST.getlist('regions')
        type_tag = request.POST.getlist('type')

        if type_tag != ['Unit', 'Spell'] or type_tag != []:
            if 'Unit' in type_tag:
                if filter_tag == []:
                    list_cards = cards.order_by(
                        'cost', 'name').filter(type__icontains='Unit')
                if 'Demacia' in filter_tag:
                    demaciaList = cards.filter(
                        regions__icontains='Demacia', type__icontains='Unit')
                    list_cards = list_cards.union(demaciaList)
                if 'Noxus' in filter_tag:
                    noxusList = cards.filter(
                        regions__icontains='Noxus', type__icontains='Unit')
                    list_cards = list_cards.union(noxusList)
                if 'Piltover & Zaun' in filter_tag:
                    piltoverList = cards.filter(
                        regions__icontains='Piltover & Zaun', type__icontains='Unit')
                    list_cards = list_cards.union(piltoverList)
                if 'Freljord' in filter_tag:
                    freljordList = cards.filter(
                        regions__icontains='Freljord', type__icontains='Unit')
                    list_cards = list_cards.union(freljordList)
                if 'Shadow Isles' in filter_tag:
                    shadowislesList = cards.filter(
                        regions__icontains='Shadow Isles', type__icontains='Unit')
                    list_cards = list_cards.union(shadowislesList)
                if 'Ionia' in filter_tag:
                    ioniaList = cards.filter(
                        regions__icontains='Ionia', type__icontains='Unit')
                    list_cards = list_cards.union(ioniaList)

            if 'Spell' in type_tag:
                if filter_tag == []:
                    list_cards = cards.order_by(
                        'cost', 'name').filter(type__icontains='Spell')
                if 'Demacia' in filter_tag:
                    demaciaList = cards.filter(
                        regions__icontains='Demacia', type__icontains='Spell')
                    list_cards = list_cards.union(demaciaList)
                if 'Noxus' in filter_tag:
                    noxusList = cards.filter(
                        regions__icontains='Noxus', type__icontains='Spell')
                    list_cards = list_cards.union(noxusList)
                if 'Piltover & Zaun' in filter_tag:
                    piltoverList = cards.filter(
                        regions__icontains='Piltover & Zaun', type__icontains='Spell')
                    list_cards = list_cards.union(piltoverList)
                if 'Freljord' in filter_tag:
                    freljordList = cards.filter(
                        regions__icontains='Freljord', type__icontains='Spell')
                    list_cards = list_cards.union(freljordList)
                if 'Shadow Isles' in filter_tag:
                    shadowislesList = cards.filter(
                        regions__icontains='Shadow Isles', type__icontains='Spell')
                    list_cards = list_cards.union(shadowislesList)
                if 'Ionia' in filter_tag:
                    ioniaList = cards.filter(
                        regions__icontains='Ionia', type__icontains='Spell')
                    list_cards = list_cards.union(ioniaList)

        if type_tag == ['Unit', 'Spell'] or type_tag == []:
            if filter_tag == []:
                list_cards = cards.order_by('cost', 'name')
            if 'Demacia' in filter_tag:
                demaciaList = cards.filter(regions__icontains='Demacia')
                list_cards = list_cards.union(demaciaList)
            if 'Noxus' in filter_tag:
                noxusList = cards.filter(regions__icontains='Noxus')
                list_cards = list_cards.union(noxusList)
            if 'Piltover & Zaun' in filter_tag:
                piltoverList = cards.filter(
                    regions__icontains='Piltover & Zaun')
                list_cards = list_cards.union(piltoverList)
            if 'Freljord' in filter_tag:
                freljordList = cards.filter(regions__icontains='Freljord')
                list_cards = list_cards.union(freljordList)
            if 'Shadow Isles' in filter_tag:
                shadowislesList = cards.filter(
                    regions__icontains='Shadow Isles')
                list_cards = list_cards.union(shadowislesList)
            if 'Ionia' in filter_tag:
                ioniaList = cards.filter(regions__icontains='Ionia')
                list_cards = list_cards.union(ioniaList)

        list_cards = list_cards.order_by('cost', 'name')

        context = {
            'cards': list_cards,
            'filter': filter_tag,
            'type': type_tag
        }

    return render(request, 'filter_page.html', context)


def search(request):
    cards = Set1.objects.all().order_by('cost', 'name')

    if 'search' in request.GET:
        find_card = request.GET['search']
        if search:
            byName = cards.filter(
                name__icontains=find_card)
            byDescription = cards.filter(
                descriptionraw__icontains=find_card)
            byLevelUp = cards.filter(
                levelupdescriptionraw__icontains=find_card)
            byKeywords = cards.filter(
                keywords__icontains=find_card)
            byTribe = cards.filter(
                subtypes__icontains=find_card)
            byRegion = cards.filter(
                regions__icontains=find_card)

            list_cards = byName.union(byDescription).union(
                byLevelUp).union(byKeywords).union(byTribe).union(byRegion).order_by('cost', 'name')

    searchData = {
        'cards': list_cards,
        'searchItem': find_card
    }

    return render(request, 'search.html', searchData)


def card(request, card_id):
    card = get_object_or_404(Set1, pk=card_id)
    gallery = Set1.objects.all()
    context = {
        'cardSelected': card,
        'gallery': gallery
    }
    return render(request, 'card.html', context)


def gallery(request):
    cards = Set1.objects.all().order_by('cost', 'name')
    context = {
        'cards': cards
    }

    return render(request, 'gallery.html', context)


def collection(request):
    return render(request, 'collection.html')
