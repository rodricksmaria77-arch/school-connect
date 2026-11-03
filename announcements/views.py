from django.shortcuts import render

def home(request):

    announcements = [
        'Annual Sports Day - 15 November',
        'Parent Teacher Meeting - 18 November',
        'School Holiday - 20 November',
        'Science Exhibition - 25 November',
        'Annual Day - 5 December',
    ]

    events = [
        'Annual Sports Day - 15 November',
        'Science Exhibition - 25 November',
        'Annual Day - 5 December',
    ]

    context = {
        'school_name': 'St. Mary\'s School',
        'announcements': announcements,
        'events': events,
    }

    return render(request, 'announcements/home.html', context)
