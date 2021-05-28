from files_operations import Word, Excel
from folder_operations import Folder
from mixin import breakline


def main():
    cv = Word("python-cv", ".docx")
    breakline()
    cv.show_fileinfo()
    breakline()

    emps = Excel(filename="employees", file_extension=".xlsx", usages="reports", sizeondisk=12, created="2019-09-01")
    emps.show_fileinfo()

    # generalfile = File(
    #     "test", ""
    # )  # error TypeError: Can't instantiate abstract class File with abstract methods show_fileinfo

    breakline()
    for f in [emps, cv]:
        f.show_fileinfo()
        breakline(char="*")

    breakline()

    personal_data = Folder("Personal Data")

    personal_data.add(emps)
    personal_data.add(cv)

    personal_data.list()

    breakline()
    personal_data.list()

    print(emps in personal_data)
    print(cv in personal_data)

    print(len(personal_data))

    breakline()
    for file in personal_data:
        print(file)

    breakline()
    Word("test", ".py", 2010)
    # Word("test?", ".docx", 2010)
    # movies = Folder("movies:")


if __name__ == "__main__":
    main()
