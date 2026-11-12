import csv
import matplotlib.pyplot as plt
import numpy as np
# comma separated value

row_title = np.array(["Little Women", "Forever...","Code Talker", "Feed", "Tyrel", "Stamped"])
colum_rate = np.array([4.18, 3.75, 3.95, 3.52, 4.02, 4.39])

plt.bar(row_title ,colum_rate, color = "grey")
plt.show()

with open("YA_Books.csv", mode = "r") as bookfile:
    # mode "r" means read 

    books = csv.reader(bookfile)

    #skip header row:
    next(books)

    most_recent_published = 0 # bc we dont know so we have to starting low num so that we actually caputer the first book

    worst_rating = 5.0

    highest_rating = 0.0

    highest_pages = 0


    for book in books:
        title = book[0]
        author = book[1]

        # print all the authors that begin with "M"
        if author.startswith("M"):
            print(author)

        #get most recently published book 
        year = int(book[2])

        if year > most_recent_published:
            most_recent_published = year 
            most_recent_book = book 


        # get book with worst rating
        rate = float(book[6])
        if rate < worst_rating:
            worst_rating = rate
            worst_rating_star = book

        # get highest rating for any book in dataset
        rate = float(book[6])
        if rate > highest_rating:
            highest_rating = rate
            highest_rating_star = book

        # get highest pages before the 2000s
        pages = int(book[5])
        if year <= 2000:
            if pages > highest_pages:
                highest_pages = pages
                highest_count = book


    print(f"Most recetly published: {most_recent_book}]")

    # print book with worst rating: 
    print(f"Worst star rating: {worst_rating_star}")

    #print the book has highest rating
    print(f"Highest star rating: {highest_rating_star}")

    # print the highest pages before 2000s
    print(f"Book highest pages: {highest_count}")






       