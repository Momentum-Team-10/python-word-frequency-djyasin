import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        line = text.read()
        print(f"{len(line)} lines in the file.")
        for text in line: 
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("-", "")
            line = line.replace("?", "")
            line = line.replace(":", "")
            line = line.replace("'", "")
            line = line.replace("'", "")
            line = line.lower()
            line = line.split(" ")
            print(line)
#"""can't figure out how to remove the STOP_WORDS so want to write an if else statement to omit them from the word count"""
#"""pass over STOP_WORDS"""
#def word_pass(file):
#   with open(file) as text:
#        lines = text.readlines()
#        print(f"{len(lines)} lines in the file.")
#           if word in STOP_WORDS:
#                 pass
#   else:
#"""somehow count words"""
#Are we trying to get thee exact words from the stop list, OR get the top frequencies



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

""""this calls the file to run"""
file = Path(args.file)
if file.is_file():
        print_word_freq(file)
else:
        print(f"{file} does not exist!")
        exit(1)
