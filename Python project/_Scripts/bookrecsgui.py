from breezypythongui import EasyFrame
import bookrecs


class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Book Recommendations", background="#B0E0E6")
        self.name_list = []
        self.report_list = []

        self.addButton(text="Friends", row=0, column=0, command=self.friend_action)
        self.addButton(text="Recommend", row=0, column=1, command=self.recommend_action)
        self.addButton(text="Report", row=0, column=2, command=self.report_action)

    def friend_action(self):
        value = self.prompterBox(title="Friends", promptString="Enter Reader Name.")
        try:
            self.messageBox(title=f"Friends of {value}", message=f"{bookrecs.friends(value)[0]}\n{bookrecs.friends(value)[1]}")
        except KeyError:
            self.messageBox(title="Error", message="Incorrect name inserted.")

    def recommend_action(self):
        value = self.prompterBox(title="Recommend", promptString="Enter Reader Name.")
        try:
            self.name_list.append(value)
            self.messageBox(title=f"Recommendations for {value}", message=f"{bookrecs.recommend(value)}")
        except KeyError:
            self.messageBox(title="Error", message="Incorrect name inserted.")

    def report_action(self):
        try:
            self.name_list.sort()
            report_string = ""
            for item in self.name_list:
                self.report_list.append(f"{bookrecs.recommend(item)}")

            for i in range(len(self.report_list)):
                report_string += f"{self.report_list[i][0]}, {self.report_list[i][1]}\n"
            self.messageBox(title="Report", message=f"{self.report_list}", width=50, height=25)
        except KeyError:
            self.messageBox(title="Error", message="No names to report.")


def main():
    BookRecsGui().mainloop()


if __name__ == "__main__":
    main()
