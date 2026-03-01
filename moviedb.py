#PA - 385.2.1 - Practice Assignment - Dictionary
movies = {}

# User Interface
while True:
    print("\nMovie Database")
    print("1. Add Movie")
    print("2. Edit Movie")
    print("3. Delete Movie")
    print("4. View Movies")
    print("5. Search Movie")
    print("6. Exit")

    choice = input("Choose an option: ")
# Add a new movie
    if choice == "1":
        title = input("Enter movie title: ")

# Data validation (check empty input)
        if title == "":
            print("Title cannot be empty.")
            continue

        genre = input("Enter genre: ")
        year = input("Enter year: ")

        movies[title] = {
            "genre": genre,
            "year": year
        }

        print("Movie added!")

#Edit a movie
    elif choice == "2":
        title = input("Enter movie title to edit: ")

#Error handling (check if movie exists)
        if title in movies:
            new_genre = input("Enter new genre: ")
            new_year = input("Enter new year: ")

            movies[title]["genre"] = new_genre
            movies[title]["year"] = new_year

            print("Movie updated!")
        else:
            print("Movie not found.")

#Delete a movie
    elif choice == "3":
        title = input("Enter movie title to delete: ")

        if title in movies:
            del movies[title]
            print("Movie deleted.")
        else:
            print("Movie not found.")

#View all movies
    elif choice == "4":
        if not movies:
            print("No movies in database.")
        else:
            for title, info in movies.items():
                print(f"{title} - {info}")

#Search movies
    elif choice == "5":
        title = input("Enter movie title to search: ")

        if title in movies:
            print(movies[title])
        else:
            print("Movie not found.")

#Exit program
    elif choice == "6":
        break

    else:
        print("Invalid choice.")
