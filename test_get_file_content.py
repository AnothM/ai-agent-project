from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test_lorem_truncation():
    result = get_file_content("calculator", "lorem.txt")

    # at least MAX_CHARS of content (plus maybe the truncation message)
    assert len(result) >= MAX_CHARS

    # ends with the same truncation message you add in get_file_content
    assert result.endswith(f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]')


def main():
    test_lorem_truncation()

    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()