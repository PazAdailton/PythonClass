MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []
def add_movies():
    title = input("Enter title movie: ")
    autor = input("Enter autor: ")
    year = input("Enter year movie: ")
    movies.append({
        "title": title,
        "autor": autor,
        "ano": year
    })

def get_movies():
    for movie in movies:
        print("You have this movies : ",movie)

def find_movies():
    #ano_busca = input("Enter year: ")
    title_busca = input("Enter title: ")
    #autor_busca = input("Enter autor: ")
    results = [movie for movie in movies if (movie["title"] == title_busca) ]#| (movie["title"] == title_busca) | (movie["autor"] == autor_busca)]
    if results:
        for m in results:
            print(f"{m["title"]} - {m["autor"]} {m["ano"]}")
    else:
        print("nobody movies find!")

user_options = {
    "a": add_movies,
    "l": get_movies,
    "f": find_movies,
}

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            select_function = user_options[selection]
            select_function()
        else:
            print("Unknow command. Please try again")
        selection = input(MENU_PROMPT)
menu()


