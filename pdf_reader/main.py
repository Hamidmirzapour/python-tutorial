# pip install pypdf2
import re
from collections import Counter
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open('pdf_reader/' + pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)
    
        print(f'Pages: {len(reader.pages)}')
        print('-' * 10) # Divider
        text_list: list[str] = [page.extract_text() for page in reader.pages]
        return text_list
    
def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower()) # Remove punctuations

        all_words += [word for word in split_text if word] # Remove spaces

    return Counter(all_words)

def main():
    extracted_text: list[str] = extract_text_from_pdf('sample.pdf')
    counter: Counter = count_words(extracted_text)

    for page in extracted_text:
        print(page)

    for word, mentions in counter.most_common(5):
        print(f'{word:10} {mentions}')



if __name__ == '__main__':
    main()