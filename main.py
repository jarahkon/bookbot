def get_book_text(book_path) -> str:
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        book_path (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(book_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents

def main():
    """
    Main function to execute the script.
    """
    book_path = 'books/frankenstein.txt'  # Replace with your book file path
    book_text = get_book_text(book_path)
    print(book_text)
if __name__ == "__main__":
    main()