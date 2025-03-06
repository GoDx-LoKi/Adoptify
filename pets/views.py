from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Pet
from .choices import STATES

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pets/pet_detail.html', {'pet': pet})


def pets(request):
    pets_list = Pet.objects.filter(is_adopted=False).order_by('-list_date')

    # Mandatory filter for pet_type (if provided)
    pet_type = request.GET.get('pet_type')
    if pet_type:
        pets_list = pets_list.filter(pet_type__iexact=pet_type)
    else:
        # Option: if no pet type is provided, you might want to show all results
        # or display a message. For now, let's show all:
        pass

    # Optional filters
    gender = request.GET.get('gender')
    if gender:
        pets_list = pets_list.filter(gender__iexact=gender)

    age = request.GET.get('age')
    if age:
        pets_list = pets_list.filter(age=age)

    size = request.GET.get('size')
    if size:
        pets_list = pets_list.filter(size__iexact=size)

    state = request.GET.get('state')
    if state:
        pets_list = pets_list.filter(state=state)

    paginator = Paginator(pets_list, 6)  # 6 pets per page
    page = request.GET.get('page')
    paged_pets = paginator.get_page(page)

    context = {
        'pets': paged_pets,
        'values': request.GET,  # This helps repopulate the search fields in your template
        'STATES': STATES,
    }
    return render(request, 'pets/pets.html', context)

