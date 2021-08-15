import sys
import csv
import pytesseract as pst

HEADER = "Test#   Command          Result"


def test_automation(path):
    """
    A test of font sizes read by the tesseract prog.
    :param path: A file path to the csv file that holds all test cases.
    :return: None
    """
    with open(path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[3] == "":
                continue
            # accept tesseract output
            config = row[10]
            print(row[2] + row[3])
            if config:
                print(row[2] + config)
                string = pst.image_to_string(row[2] + row[3], lang=row[12], config=row[2]+config).strip()

            else:
                string = pst.image_to_string(row[2] + row[3], lang=row[12]).strip()
            result = string == row[11]
            print(HEADER)
            if not config:
                print(row[0] + "       tesseract " + sys.argv[0] + " -l " + row[12] + "       " + str(result))
            else:
                configs = row[5] + " " + row[6] + " " + row[7] + " " + " " + row[8] + " " + row[9]
                print(row[0] + "       tesseract " + sys.argv[0] + " -l " + row[12] + " -c " + configs + "         " + str(result))
            print("expected: " + row[11] + "\n" + "actual: " + string + "\n")


if __name__ == '__main__':
    test_automation(sys.argv[1])
