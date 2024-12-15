from django.shortcuts import render
from t3app.models import course
from django.db.models import Q

def search(request):
    context = {}
    query = request.GET.get('query', '')  # Get query parameter
    location = request.GET.get('location', None)  # Get location filter parameter
    category = request.GET.get('category', None)  # Get category filter parameter

    # Start with an empty queryset
    products = course.objects.all()

    # Apply filters if query is provided
    if query:
        pname = products.filter(name__icontains=query)
        pdetail = products.filter(cdetail__icontains=query)
        pcat = products.filter(cat__icontains=query)
        products = pname.union(pdetail, pcat)

    # Apply location filter if selected
    if location:
        products = products.filter(lc=location)

    # Apply category filter if selected
    if category:
        products = products.filter(cat=category)

    # Handle the case where no products match
    if products.count() == 0:
        context['errmsg'] = 'Products Not Found'
    
    context['data'] = products
    return render(request, 'base.html', context)


def all(request):
    p = course.objects.filter(is_active=True)
    context = {'data': p}
    return render(request, 'base.html', context)


def catfilter(request, cv):
    location_filter = request.GET.get('location', None)  # Get location from request
    q1 = Q(cat=cv)
    q2 = Q(is_active=True)

    # Apply category and location filter dynamically
    p = course.objects.filter(q1 & q2)

    if location_filter:
        p = p.filter(lc=location_filter)

    context = {'data': p}
    return render(request, 'base.html', context)


def locfilter(request, vc):
    category_filter = request.GET.get('category', None)  # Get category from request
    q1 = Q(lc=vc)
    q2 = Q(is_active=True)

    # Apply location and category filter dynamically
    p = course.objects.filter(q1 & q2)

    if category_filter:
        p = p.filter(cat=category_filter)

    context = {'data': p}
    return render(request, 'base.html', context)


def filter_courses(request):
    # Get category and location filters from the GET parameters
    category_filter = request.GET.get('category', None)
    location_filter = request.GET.get('location', None)

    # Initialize the query for active courses
    q1 = Q(is_active=True)  # Ensure we only get active courses

    # Handle the category filter if provided
    if category_filter:
        q1 &= Q(cat=category_filter)  # Filter by the selected category

    # Handle the location filter if provided
    if location_filter:
        q1 &= Q(lc=location_filter)  # Filter by the selected location

    # Fetch the filtered courses
    filtered_courses = course.objects.filter(q1)

    # Return the filtered courses to the template
    return render(request, 'base.html', {'data': filtered_courses})
