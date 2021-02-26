from django.db import models

# Create your models here.

class Simple(models.Model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(max_length=True)
    url = models.URLField(default='www.example.com')

    def __str__(self):
        return self.url

class DateExample(models.Model):
    the_date = models.DateTimeField()

class NullExample(models.Model):
    col = models.CharField(max_length=10, blank=True, null=True)

class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

'''
-   Should put the many to many in lower side of models in this case Characters are lower than Movies

So when the ManyToManyField is created a new table is created:
    modsr_character_movies

And its table look like:
    id   character_id    movie_id

Created First Movie in shell:
    avengers = Movie(name='Avengers')
    avengers.save()

Created First Character in shell:
    captain_america = Character(name='Captain America')
    captain_america.save()

Then to add Captain America to movies:
    captain_america.movies.add(avengers)
    (Make sure to create the movies first before trying to add characters to them)
    captain_america.movies.add(civil_war)

    - This added an:
        id=1, character_id=1, movie_id=1
        in modsr_character_movies table

Then added second, third Movie:
    civil_war = Movie(name='Civil War')
    civil_war.save()
    thor = Movie(name='Thor: Dark World')
    thor.save()
Then created second Character:
    thor_character = Character(name='Thor')
    thor_character.save()

Then add thor to movies:
    thor_character.movies.add(avengers)
    thor_character.movies.add(thor)

To create with one line use:
    captain_america.movies.create(name='Winter Soldier')

Winter Soldier was created as the fourth movie
'''

'''
    Querying many to many relationships

    Character.objects.filter(movies__name='Civil War')

    - Produces: Character: Captain America

    - To query from Character through Movie:
        Movie.objects.filter(character__name='Captain America')

    - Produces: Movie: Avengers, Movie: Civil War, Movie: Winter Soldier

    - This is how to do another way:
        captain_america.movies.all()

    - Produces: Movie: Avengers, Movie: Civil War, Movie: Winter Soldier

    - To get all characters in a movie:
        avengers = Movie.objects.get(name='Avengers')

    - avengers.character_set.all()

    - Produces: Character: Captain America, Character: Thor
'''

class Movie(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
