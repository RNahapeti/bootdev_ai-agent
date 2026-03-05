from functions.get_file_content import get_file_content

def test_file_read():
    test_read = get_file_content("calculator", "lorem.txt")
    print(f"Lorem length: {len(test_read)}\nLorem ending text: \n{test_read[-100:]}\n")

    test_read = get_file_content("calculator", "main.py")
    print("Result for main.py:\n" + test_read + "\n")

    test_read = get_file_content("calculator", "pkg/calculator.py")
    print("Result for calculator.py:\n" + test_read + "\n")

    test_read = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin/cat':\n" + test_read + "\n")

    test_read = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for 'pkg/does_not_exist.py':\n" + test_read + "\n")

if __name__ == "__main__":
    test_file_read()