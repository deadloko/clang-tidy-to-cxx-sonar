import os
import sys
from xml.sax.saxutils import escape

def usage():
    return 'Usage: %s <cpplint.py> .... txt file can be obtain by running python cpplint.py --filter=' % sys.argv[0]

if len(sys.argv) != 2:
    print usage()
    exit()

tidy_check_report_path = os.path.abspath(sys.argv[1])
tidy_check_report_file = open(os.path.abspath(tidy_check_report_path), "r")
tidy_check_report = tidy_check_report_file.readlines()
tidy_check_report_file.close()

# print tidy_check_report

filenamew = "clang-tidy-check-converted.xml"
filetowrite = open(filenamew, 'w')
filetowrite.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
filetowrite.write("<results>\n")

for check in tidy_check_report:
    if check.startswith('/') and "note:" not in check:
        try:
            # print check
            error = check.split(":")[0]
            line = check.split(":")[1]
            id = check.split(':')[-1].split('[')[1].strip(']\n')
            msg = escape(check.split(':')[4].split('[')[0], {"\"": "&quot;"})
            # print error
            # print line
            # print id
            # print msg
            filetowrite.write(" <error file=\"" + error + "\" line=\""+ line + "\" id=\"clang-tidy/" + id + "\" msg=\"" + msg + "\"/>\n")
        except:
            pass


filetowrite.write("</results>\n")

filetowrite.close()
