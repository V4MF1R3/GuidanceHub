from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .models import MentorshipRequest, MentorshipConnection
from .forms import MentorshipRequestForm

@login_required
def dashboard(request):
    user = request.user
    # Fetch mentorship connections
    mentorship_connections = MentorshipConnection.objects.filter(
        Q(mentor=user) | Q(mentee=user)
    )
    
    # Fetch received requests for mentors
    received_requests = MentorshipRequest.objects.filter(
        receiver=user, status='pending'
    )
    
    # Fetch sent requests for mentees
    sent_requests = MentorshipRequest.objects.filter(sender=user).order_by('-timestamp')

    return render(request, 'dashboard.html', {
        'mentorship_connections': mentorship_connections,
        'received_requests': received_requests,
        'sent_requests': sent_requests,  # Pass sent requests to the template
    })

@login_required
def send_request(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        receiver = get_object_or_404(Profile, id=receiver_id, role='mentor').user
        
        # Prevent mentees from sending duplicate requests to the same mentor
        existing_request = MentorshipRequest.objects.filter(sender=request.user, receiver=receiver).first()
        if existing_request:
            return render(request, 'send_request.html', {
                'error': 'You have already sent a request to this mentor.',
                'mentors': Profile.objects.filter(role='mentor'),
            })

        # Create a new mentorship request
        MentorshipRequest.objects.create(sender=request.user, receiver=receiver)
        return redirect('dashboard')

    # Display mentors for searching
    search_query = request.GET.get('search', '')
    mentors = Profile.objects.filter(role='mentor')
    if search_query:
        mentors = mentors.filter(
            Q(user__username__icontains=search_query) |
            Q(skills__icontains=search_query) |
            Q(interests__icontains=search_query)
        )

    return render(request, 'send_request.html', {'mentors': mentors})


@login_required
def view_requests(request):
    # Show requests received by the current user
    received_requests = MentorshipRequest.objects.filter(receiver=request.user, status='pending')
    return render(request, 'view_requests.html', {'received_requests': received_requests})


@login_required
def manage_request(request, request_id, action):
    mentorship_request = get_object_or_404(MentorshipRequest, id=request_id, receiver=request.user)

    if action == 'accept':
        mentorship_request.status = 'accepted'
        MentorshipConnection.objects.create(mentor=mentorship_request.receiver, mentee=mentorship_request.sender)
    elif action == 'decline':
        mentorship_request.status = 'declined'
    
    mentorship_request.save()
    return redirect('mentorship_requests')


@login_required
def mentorship_connections(request):
    # Show all connections of the current user
    connections = MentorshipConnection.objects.filter(
        Q(mentor=request.user) | Q(mentee=request.user)
    )
    return render(request, 'connections.html', {'connections': connections})