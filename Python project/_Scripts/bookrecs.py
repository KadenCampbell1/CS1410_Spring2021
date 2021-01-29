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
        name = str(ratings_list[ratings_value]).strip("\'[").strip("\']").replace('\', \'', " ")
        # print(name)
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


def recommend(name_for_rec):
    rec_list = []
    t_index = 0
    index_values = []
    compare_list1 = []
    compare_list2 = []

    target_list = [int(target_number) for target_number in ratings_dict[name_for_rec]]

    for names_rec in friends(name_for_rec):
        rec_list.append(ratings_dict[names_rec])

    for list1_values in rec_list[0]:
        compare_list1.append(int(list1_values))

    for list2_values in rec_list[1]:
        compare_list2.append(int(list2_values))

    # for t_value in target_list:
    #     t_index = t_index + 1
    #     if t_value == 0:
    #         if compare_list1[t_index - 1] >= 3 or compare_list2[t_index - 1] >= 3:
    #             index_values.append(t_index - 1)
    #             print(f"\t{str(book_list[t_index - 1])}")
    recommended = []
    for i in range(len(target_list)):
        if target_list[i] == 0:
            if compare_list1[i] >= 3 or compare_list2[i] >= 3:
                recommended.append(tuple(book_list[i]))

    r = sorted(recommended, key=lambda k: (k[0][k[0].rfind(" ") + 1:], k[0][:k[0].rfind(" ")], k[1]))

    print(f"Recommendations for {name_for_rec} from {friends(name_for_rec)[0]} and {friends(name_for_rec)[1]}:")
    for i_string_num in r:
        author_string = i_string_num[0]
        book_string = i_string_num[1]
        print(f"\t{author_string}, {book_string}")

    return r


            # print(f"index: {t_index} number: {str(target_list[t_index - 1])}")
            # if compare_list1[target_list.index(t_value)] >= 3:
            #     print(str(compare_list1[target_list.index(t_value)]) + " " + str(target_list.index(t_value)))
            # if compare_list2[compare_list1.index(l1_value)] == 0:
            #     print(None)
            # print(l1_value, compare_list2[compare_list1.index(l1_value)])







def main():
    """add stuff"""
    name = input("Enter a reader's name: ").lower()
    if name in ratings_dict:
        recommend(name)
    else:
        print(f"No such reader as {name}")

    # print(friends(name))
    # print(recommend(name))
    # print(book_list)
    # print(ratings_list)
    # print(ratings_dict)
    # print(ratings_lyst)
    # print(dot_product("ben", "moose"))
    # print(friends("ben"))
    # print(recommend('albus dumbledore'))
    # print(ratings_dict.keys())
    # print(ratings_lyst)




if __name__ == "__main__":
    main()
