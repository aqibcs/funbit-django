from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Submission, Like
from .forms import SubmissionForm


@login_required
def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    user_liked = False

    if request.user.is_authenticated:
        user_liked = Like.objects.filter(user=request.user,
                                         submission=submission).exists()

    return render(request, 'submissions/submission_detail.html', {
        'submission': submission,
        'user_liked': user_liked,
    })


@login_required
def like_submission(request, pk):
    submission = get_object_or_404(Submission, pk=pk)

    # Check if user already liked this submission
    like, created = Like.objects.get_or_create(user=request.user,
                                               submission=submission)

    if not created:
        # User already liked, so unlike
        like.delete()
        liked = False
    else:
        liked = True

    # Return JSON for AJAX requests
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'liked': liked,
            'likes_count': submission.likes_count()
        })

    # Redirect for non-AJAX requests
    return redirect('submission_detail', pk=submission.pk)
