from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .models import MentorshipRequest, MentorshipConnection
from .forms import MentorshipRequestForm

@login_required
def dashboard(request):
    user = request.user
    mentorship_connections = MentorshipConnection.objects.filter(mentor=user) | MentorshipConnection.objects.filter(mentee=user)
    received_requests = MentorshipRequest.objects.filter(receiver=user)

    return render(request, 'dashboard.html', {
        'mentorship_connections': mentorship_connections,
        'received_requests': received_requests,
    })

@login_required
def send_request(request):
    if request.method == 'POST':
        form = MentorshipRequestForm(request.POST)
        if form.is_valid():
            mentorship_request = form.save(commit=False)
            mentorship_request.sender = request.user
            mentorship_request.save()
            return redirect('mentorship_requests')
    else:
        form = MentorshipRequestForm()

    # Handling search logic
    search_query = request.GET.get('search', '')
    mentors = Profile.objects.filter(role='mentor')

    if search_query:
        mentors = mentors.filter(
            Q(user__username__icontains=search_query) |
            Q(skills__icontains=search_query) |
            Q(interests__icontains=search_query)
        )

    return render(request, 'send_request.html', {'form': form, 'mentors': mentors, 'search_query': search_query})

@login_required
def view_requests(request):
    received_requests = MentorshipRequest.objects.filter(receiver=request.user, status='pending')
    return render(request, 'view_requests.html', {'received_requests': received_requests})

@login_required
def manage_request(request, request_id, action):
    mentorship_request = get_object_or_404(MentorshipRequest, id=request_id, receiver=request.user)
    if action == 'accept':
        mentorship_request.status = 'accepted'
        MentorshipConnection.objects.create(mentor=mentorship_request.sender, mentee=mentorship_request.receiver)
    elif action == 'decline':
        mentorship_request.status = 'declined'
    mentorship_request.save()
    return redirect('mentorship_requests')

@login_required
def mentorship_connections(request):
    connections = MentorshipConnection.objects.filter(mentor=request.user) | MentorshipConnection.objects.filter(mentee=request.user)
    return render(request, 'connections.html', {'connections': connections})
