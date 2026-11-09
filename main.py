import csv
# comma separated value

with open("YA_Books.csv", mode = "r") as bookfile:
    # mode "r" means read 

    books = csv.reader(bookfile)

    #skip header row:
    next(books)

    most_recent_published = 0 # bc we dont know so we have to starting low num so that we actually caputer the first book

    worst_rating = 5.0

    highest_rating = 5.0


    for book in books:
        title = book[0]
        author = book[1]
        # print all the authors that begin with "M"
        if author.startswith("M"):
            print(author)

        #get most recently published book 
        # year = int(book[2])
        # if year > most_recent_published:
        #     most_recent_published = year 
        #     most_recent_book = book 

        # get book with worst rating
        # rate = float(book[6])
        # if rate < worst_rating:
        #     worst_rating = rate
        #     worst_rating_star = book

        # get highest rating for any book in dataset
        rate = float(book[6])
        if rate < highest_rating:
            highest_rating = rate
            highest_rating_star = book



    # print(f"Most recetly published: {most_recent_book}]")

    # print book with worst rating: 
    # print(f"Worst star rating: {worst_rating_star}")

    #print the book has highest rating
    print(f"Highest star rating: {highest_rating_star}")






       