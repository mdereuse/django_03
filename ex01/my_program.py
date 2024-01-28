from path import Path


def main():
    new_directory = Path("my_new_directory")
    if not new_directory.exists():
        new_directory.makedirs()
    new_file = new_directory/"my_new_file"
    new_file.touch()
    new_file.write_text("Hello world.")
    print(new_file.read_text())


if __name__ == "__main__":
    main()
