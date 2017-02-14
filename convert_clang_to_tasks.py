import os
import sys

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

filenamew = "clang-tidy-check-converted.tasks"
filetowrite = open(filenamew, 'w')

for check in tidy_check_report:
    if check.startswith('/') and "note:" not in check:
        try:
            # print check
            error = check.split(":")[0]
            line = check.split(":")[1]
            id = check.split(':')[-1].split('[')[1].strip(']\n')
            msgtype = check.split(':')[3].replace("error", "err").replace("warning", "warn").strip(" ")
            msg = check.split(':')[4].split('[')[0]
            # print error
            # print line
            # print id
            # print msg
            filetowrite.write(error+"\t"+line+"\t"+msgtype+"\t"+msg+"\n")
        except:
            pass
    else:
        filetowrite.write(check)

filetowrite.close()
