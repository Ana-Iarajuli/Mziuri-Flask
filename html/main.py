# class Student:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
# obj1 = Student("jasurbeki", "iaxshiboevi")
# print(obj1.name)
# print(obj1.surname)

# with open("data.txt", "r", encoding="utf-8") as f:
#     for i in f:
#         x = i.split()
#         print(len(x))

class Movie:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def get_title(self):
        return self.title

    def __str__(self):
        return f"title: {self.title},rating: {self.rating}"

movie1 = Movie("whiplash", "drama", 2011, 7.7)
movie2 = Movie("detachment", "drama", 2011, 7.8)
# print(movie1)

class MovieDatabase(Movie):
    def __init__(self, movie_list):
        self.movie_list = movie_list

    def add_movie(self, new_movie):
        self.movie_list.append(new_movie)

    def display_movies(self):
        for movie in self.movie_list:
            print(movie)

movies = [movie1, movie2]
database = MovieDatabase(movies)
database.display_movies()