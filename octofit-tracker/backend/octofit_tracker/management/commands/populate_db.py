
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password'),
        ]

        # Create activities
        Activity.objects.create(user_email='ironman@marvel.com', activity_type='Running', duration=30)
        Activity.objects.create(user_email='cap@marvel.com', activity_type='Cycling', duration=45)
        Activity.objects.create(user_email='batman@dc.com', activity_type='Swimming', duration=60)
        Activity.objects.create(user_email='superman@dc.com', activity_type='Flying', duration=120)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=180)

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for superheroes')
        Workout.objects.create(name='Flight Training', description='Flight workout for superheroes')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
