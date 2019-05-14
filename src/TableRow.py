def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


class TableRow:
    def __init__(self, isHeader=False, rno=-1, elementsPerRow=9999999999):
        self.isHeader = isHeader
        self.elements = []
        self.rno = rno
        self.elementsPerRow = elementsPerRow

    def addElement(self, element):
        self.elements.append(element)

    def getHTML(self):
        html = ''
        for elements in chunks(self.elements, self.elementsPerRow):
            html += '<tr>'
            if self.rno >= 0:
                html += '<td><a href="#' + \
                        str(self.rno) + '">' + str(self.rno) + '</a>'
                html += '<a name=' + str(self.rno) + '></a></td>'
            for e in elements:
                if self.isHeader or e.isHeader:
                    elTag = 'th'
                else:
                    elTag = 'td'
                html += '<%s>' % elTag + e.getHTML() + '</%s>' % elTag
            html += '</tr>\n'
        return html
