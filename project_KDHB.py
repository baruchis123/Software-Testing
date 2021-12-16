import sys
import csv
import pytesseract as pst

HEADER = "Test#   Command          Result\n"


def generate_config(row):
    name = str("test_" + row[0] + "_config.txt")
    f = open(name, "w+")
    for i in range(5, 10):
        if row[i]:
            f.write(str(row[i] + "\n"))
    f.close()
    return name


def test_automation(path, debug=None):
    """
    A test of font sizes read by the tesseract prog.
    :param path: A file path to the csv file that holds all test cases.
    :return: None
    """
    with open(path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            # accept tesseract output
            config = row[5] + row[6] + row[7] + row[8] + row[9]
            if config:
                name = generate_config(row)
                string = pst.image_to_string(row[2] + row[3], lang=row[12], config=name).strip()
            else:
                string = pst.image_to_string(row[2] + row[3], lang=row[12]).strip()
            result = string == row[11]
            print(HEADER)
            if not config:
                print(row[0] + "       tesseract " + sys.argv[0] + " -l " + row[12] + "       " + str(result))
            else:
                configs = row[5] + " " + row[6] + " " + row[7] + " " + " " + row[8] + " " + row[9]
                print(row[0] + "       tesseract " + sys.argv[0] + " -l " + row[12] + " -c " + configs + "         " + str(result))
            if debug == "--debug":
                print("expected: " + row[11] + "\n" + "actual: " + string + "\n")


if __name__ == '__main__':
    if len(sys.argv) > 2:
        test_automation(sys.argv[1], sys.argv[2])
    else:
        test_automation(sys.argv[1])