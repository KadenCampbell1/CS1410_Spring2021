from breezypythongui import EasyFrame
import bookrecs


class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Book Recommendations", background="#B0E0E6")
        self.name_list = []

        self.addButton(text="Friends", row=0, column=0, command=self.friend_action)
        self.addButton(text="Recommend", row=0, column=1, command=self.recommend_action)
        self.addButton(text="Report", row=0, column=2, command=self.report_action)

    def friend_action(self):
        value = self.prompterBox(title="Friends", promptString="Enter Reader Name.")
        try:
            self.messageBox(title=f"Friends of {value}", message=f"{bookrecs.friends(value)[0]}\n{bookrecs.friends(value)[1]}")
        except KeyError:
            self.messageBox(title="Error", message="No such reader.")

    def recommend_action(self):
        value = self.prompterBox(title="Recommend", promptString="Enter Reader Name.")
        try:
            self.name_list.append(value)
            report_string = ""
            for books in bookrecs.recommend(value):
                report_string += f"{books[0]}, {books[1]}\n"

            self.messageBox(title=f"Recommendations for {value}", message=f"{report_string}", width=60, height=25)
        except KeyError:
            self.messageBox(title="Error", message="No such reader.")

    def report_action(self):
        try:
            self.name_list.sort()
            report_string = ""
            for item in self.name_list:
                if item in bookrecs.ratings_dict.keys():
                    report_string += f"Recommendations for {item} from {bookrecs.friends(item)[0]} and {bookrecs.friends(item)[1]}:\n"
                    for books in bookrecs.recommend(item):
                        report_string += f"\t{books[0]}, {books[1]}\n"
                    report_string += "\n"
                
            if len(self.name_list) == 0:
                report_string = "No readers to report."

            self.messageBox(title="Report", message=f"{report_string}", width=60, height=25)
        except KeyError:
            self.messageBox(title="Error", message="No such reader.")


def main():
    BookRecsGui().mainloop()


if __name__ == "__main__":
    main()
