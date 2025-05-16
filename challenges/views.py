from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Challenge
from submissions.models import Submission, Like
from submissions.forms import SubmissionForm
from accounts.models import Profile
from django.utils import timezone


def home(request):
    daily_challenge = Challenge.get_random_challenge()
    recent_submissions = Submission.objects.order_by('-created_at')[:5]

    # Check if user has already completed today's challenge
    user_completed = False
    if request.user.is_authenticated and daily_challenge:
        user_completed = Submission.objects.filter(
            user=request.user,
            challenge=daily_challenge,
            created_at__date=timezone.now().date()).exists()

    return render(
        request, 'challenges/home.html', {
            'challenge': daily_challenge,
            'recent_submissions': recent_submissions,
            'user_completed': user_completed,
        })


def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    submissions = Submission.objects.filter(
        challenge=challenge).order_by('-created_at')

    # Check if user has already completed this challenge today
    user_completed = False
    user_liked_submissions = []

    if request.user.is_authenticated:
        user_completed = Submission.objects.filter(
            user=request.user,
            challenge=challenge,
            created_at__date=timezone.now().date()).exists()

        # Get list of submission IDs that the user has liked
        user_liked_submissions = Like.objects.filter(
            user=request.user,
            submission__in=submissions).values_list('submission_id', flat=True)

    # Handle submission form
    if request.method == 'POST' and request.user.is_authenticated and not user_completed:
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.challenge = challenge
            submission.save()

            # Update user points
            profile = request.user.profile
            profile.points += challenge.points
            profile.save()

            messages.success(
                request,
                f'Your submission was successful! You earned {challenge.points} points.'
            )
            return redirect('challenge_detail', pk=challenge.pk)
    else:
        form = SubmissionForm()

    return render(
        request, 'challenges/challenge_detail.html', {
            'challenge': challenge,
            'submissions': submissions,
            'form': form,
            'user_completed': user_completed,
            'user_liked_submissions': user_liked_submissions,
        })


def leaderboard(request):
    top_users = Profile.objects.order_by('-points')[:20]
    return render(request, 'challenges/leaderboard.html',
                  {'top_users': top_users})
