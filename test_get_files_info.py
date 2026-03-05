from functions.get_files_info import get_files_info

def test_access():
    current_dir = get_files_info("calculator", ".")
    pkg_dir = get_files_info("calculator", "pkg")
    bin_dir = get_files_info("calculator", "/bin")
    prev_dir = get_files_info("calculator", "../")

    print("Result for current directory:\n" + current_dir + "\n")
    print("Result for 'pkg' directory:\n" + pkg_dir + "\n")
    print("Result for '/bin' directory:\n" + bin_dir + "\n")
    print("Result for '../' directory:\n" + prev_dir)

if __name__ == "__main__":
    test_access()