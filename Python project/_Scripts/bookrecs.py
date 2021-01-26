book_file = open("booklist.txt", "r")
ratings_file = open("ratings.txt", "r")

book_list = []
for lines in book_file:
    line = (lines.strip().split(","))
    book_list.append(line)


ratings_list = [x.strip().split() for x in ratings_file.readlines()]
ratings_lyst = []
ratings_dict = {}

for ratings_value in range(0, len(ratings_list)):
    if ratings_value % 2 == 0:
        name = ratings_list[ratings_value]
    if ratings_value % 2 == 1:
        rating = ratings_list[ratings_value]
        ratings_lyst.append((name, rating))

for key, lock in ratings_lyst:
    ratings_dict[str(key).strip("\'[").strip("\']").lower()] = lock

book_file.close()
ratings_file.close()

def main():
    """add stuff"""
    print(book_list)
    # print(ratings_list)
    print(ratings_dict)
    # print(ratings_lyst)

if __name__ == "__main__":
    main()
