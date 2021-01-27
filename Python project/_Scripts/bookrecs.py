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

def dot_product(x, y):
    first_name_values = ratings_dict[x]
    second_name_values = ratings_dict[y]
    dot_list = [int(first_name_values[i]) * int(second_name_values[i]) for i in range(len(second_name_values))]
    return sum(dot_list)

def friends(target_name):
    affinity_score = {}
    friend_dict = {}
    # number_tuple = ()
    # friend_tuple = ()
    for keys in ratings_dict.keys():
        if keys == target_name:
            affinity_score[-(dot_product(target_name, keys))] = None
        else:
            affinity_score[(dot_product(target_name, keys))] = keys
    friend_dict[affinity_score.get(sorted(affinity_score.keys())[-2])] = sorted(affinity_score.keys())[-2]
    friend_dict[affinity_score.get(sorted(affinity_score.keys())[-1])] = sorted(affinity_score.keys())[-1]
    #return sorted(friend_dict.items()) #this returns key and value sorted by key
    return sorted(friend_dict.keys())




def main():
    """add stuff"""
    print(book_list)
    # print(ratings_list)
    print(ratings_dict)
    # print(ratings_lyst)
    print(dot_product("ben", "moose"))
    print(friends("ben"))

if __name__ == "__main__":
    main()
