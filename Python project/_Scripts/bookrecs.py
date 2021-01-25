book_file = open("booklist.txt", "r")
ratings_file = open("ratings.txt", "r")

book_list = []
for lines in book_file:
    line = (lines.strip().split(","))
    book_list.append(line)

ratings_dict = {}
ratings_list = [x.strip() for x in ratings_file.readlines()]
for ratings_value in ratings_list:
    i = 0
    if i == 0:
        ratings_key = ratings_value
    else:
        ratings_dict[ratings_key] = ratings_value
    i += 1




book_file.close()
ratings_file.close()

def main():
    """add stuff"""
    print(book_list)
    print(ratings_dict.items())

if __name__ == "__main__":
    main()
