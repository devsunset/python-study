from docx import Document
import docx
from docx.oxml.ns import qn

doc = Document(r'3.수료증 자동생성 후 PDF 변환\수료증양식.docx')

for i, paragraph in enumerate(doc.paragraphs):
    print(str(i) + ": " + paragraph.text)