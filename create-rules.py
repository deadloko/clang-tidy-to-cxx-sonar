import yaml

filenamew = "clang-tidy-rules.xml"
filetowrite = open(filenamew, 'w')
filetowrite.write("<?xml version=\"1.0\" encoding=\"ASCII\"?>\n")
filetowrite.write("<rules>\n")

unformatted_checks_file = open('checks.txt', 'r')
unformatted_checks = unformatted_checks_file.read()
unformatted_checks_file.close()

appended_rules = []

for check in unformatted_checks.split('    '):
    if not check.startswith('Enabled'):
        name = check.strip('\n')
        key = 'clang-tidy/' + name
        category = 'clang-tidy'
        if name.startswith('clang-analyzer-'):
            descr = 'https://clang-analyzer.llvm.org/available_checks.html'
        else:
            descr = 'http://clang.llvm.org/extra/clang-tidy/checks/' + name + '.html'

        if key not in appended_rules:
            appended_rules.append(key)
            filetowrite.write("    <rule key=\"" + key + "\">\n")
            filetowrite.write("        <name><![CDATA[" + name + "]]></name>\n")
            filetowrite.write("        <configKey><![CDATA[" + key + "@CLANG_TIDY]]></configKey>\n")
            filetowrite.write("        <category name=\"" + category + "\" />\n")
            filetowrite.write("        <description><![CDATA[ " + descr + " ]]></description>\n")
            filetowrite.write("    </rule>\n")
        else:
            pass

#append diagnostics error

name = 'Clang diagnostics error'
key = 'clang-tidy/clang-diagnostic-error'
category = 'clang-tidy'
descr = 'Clang diagnostics error'


filetowrite.write("    <rule key=\"" + key + "\">\n")
filetowrite.write("        <name><![CDATA[" + name + "]]></name>\n")
filetowrite.write("        <configKey><![CDATA[" + key + "@CLANG_TIDY]]></configKey>\n")
filetowrite.write("        <category name=\"" + category + "\" />\n")
filetowrite.write("        <description><![CDATA[ " + descr + " ]]></description>\n")
filetowrite.write("    </rule>\n")


filetowrite.write("</rules>\n")
filetowrite.close()