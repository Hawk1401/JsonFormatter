Tabs = 0
OpenCurlyBracket = 0
OpenSquareBrackets = 0
OpenSingleQuotationMarks = False
OpenDoubleQuotationMarks = False

SourcFile = "C:\\Git\\Python\\JsonFormater\\Test.json"
DestinaFile = "C:\\Git\\Python\\JsonFormater\\TestNew.json"

writer = open(DestinaFile, 'w')

def WirteWithTabs(c):
    writer.write(c + "\n")
    for x in range(Tabs):
        writer.write("\t")

def WirteWithTabsBefore(c):
    writer.write("\n")
    for x in range(Tabs):
        writer.write("\t")
    writer.write(c)


with open(SourcFile) as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        if(c == "["):
            if not(OpenDoubleQuotationMarks | OpenSingleQuotationMarks):
                OpenSquareBrackets = OpenSquareBrackets + 1
                Tabs = Tabs + 1
                WirteWithTabs(c)
                continue

        if (c == "{"):
            if not (OpenDoubleQuotationMarks | OpenSingleQuotationMarks):
                OpenCurlyBracket = OpenCurlyBracket + 1
                Tabs = Tabs + 1
                WirteWithTabs(c)
                continue

        if (c == "]"):
            if not (OpenDoubleQuotationMarks | OpenSingleQuotationMarks):
                OpenSquareBrackets = OpenSquareBrackets - 1
                Tabs = Tabs - 1
                WirteWithTabsBefore(c)
                continue

        if (c == "}"):
            if not (OpenDoubleQuotationMarks | OpenSingleQuotationMarks):
                OpenCurlyBracket = OpenCurlyBracket - 1
                Tabs = Tabs - 1
                WirteWithTabsBefore(c)
                continue

        if (c == '"'):
            if not (OpenSingleQuotationMarks):
                if (OpenDoubleQuotationMarks):
                    OpenDoubleQuotationMarks = False
                else:
                    OpenDoubleQuotationMarks = True

        if (c == "'"):
            if not (OpenDoubleQuotationMarks):
                if (OpenSingleQuotationMarks):
                    OpenSingleQuotationMarks = False
                else:
                    OpenSingleQuotationMarks = True

        if (c == ","):
            if not (OpenDoubleQuotationMarks | OpenSingleQuotationMarks):
                WirteWithTabs(c)
                continue


        else:
            writer.write(c)
        print("Read a character:", c)
