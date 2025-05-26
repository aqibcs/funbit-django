import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funbit.settings')
django.setup()

from challenges.models import Challenge

# Sample challenges
challenges = [
    {
        'title': 'Take a Funny Selfie',
        'description': 'Make a silly face and take a selfie.',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Draw a Cat',
        'description': 'Draw a cat, even if it looks funny!',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Say Hello in 3 Languages',
        'description': 'Write how to say "Hello" in three different languages.',
        'points': 10,
        'requires_image': False,
        'requires_text': True,
    },
    {
        'title': 'Make a Sock Puppet',
        'description': 'Make a quick sock puppet and show it.',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Describe Your Mood with an Emoji',
        'description': 'Use just emojis to show how you feel today.',
        'points': 10,
        'requires_image': False,
        'requires_text': True,
    },
    {
        'title': 'Take a Picture of Your Shoes',
        'description': 'Snap a photo of whatever shoes you’re wearing.',
        'points': 5,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Write a 2-line Poem',
        'description': 'Make a short and simple 2-line poem.',
        'points': 10,
        'requires_image': False,
        'requires_text': True,
    },
    {
        'title': 'Show Your Favorite Mug',
        'description': 'Take a picture of your favorite mug or cup.',
        'points': 5,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'What’s for Lunch?',
        'description': 'Take a photo of your lunch today.',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'One Word to Describe Today',
        'description': 'Write one word that sums up your day.',
        'points': 5,
        'requires_image': False,
        'requires_text': True,
    },
    {
        'title': 'Take a Picture of the Sky',
        'description': 'Look up! Take a photo of the sky where you are.',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Make a Face with Food',
        'description': 'Arrange food to look like a face and take a photo.',
        'points': 15,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Favorite Color',
        'description': 'Show something that’s your favorite color.',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Write a Joke',
        'description': 'Make up a simple joke and write it down.',
        'points': 10,
        'requires_image': False,
        'requires_text': True,
    },
    {
        'title': 'Pretend You’re a Superhero',
        'description': 'What would your superhero name and power be?',
        'points': 10,
        'requires_image': False,
        'requires_text': True,
    },
    {
        'title': 'Show Your Pet (or a Toy)',
        'description': 'Take a photo of your pet. No pet? Use a toy!',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Dance Pose!',
        'description': 'Strike a dance pose and snap a picture.',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Draw a Happy Face',
        'description': 'Draw a smiley face however you like!',
        'points': 5,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Write Your Name Backwards',
        'description': 'Can you write your name backwards?',
        'points': 5,
        'requires_image': False,
        'requires_text': True,
    },
    {
        'title': 'Show a Book You Like',
        'description': 'Take a picture of a book you enjoy or want to read.',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
    {
        'title': 'Draw a House',
        'description': 'Draw a simple house—stick figures welcome!',
        'points': 10,
        'requires_image': True,
        'requires_text': False,
    },
]



# Create challenges
for challenge_data in challenges:
    Challenge.objects.get_or_create(
        title=challenge_data['title'],
        defaults={
            'description': challenge_data['description'],
            'points': challenge_data['points'],
            'requires_image': challenge_data['requires_image'],
            'requires_text': challenge_data['requires_text'],
        }
    )

print(f"Added {len(challenges)} challenges to the database!")
