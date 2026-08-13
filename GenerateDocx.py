from docx import Document
from docx.oxml.shared import OxmlElement, qn
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt



def constructFile(student_name, start_date, mandatories, seminar, electives):
    doc = Document()

    title = doc.add_paragraph()
    addRun(title,'בדיקת השלמת חובות שמיעה בחטיבה לניהול וישוב סכסוכים',True,True,alignment= WD_PARAGRAPH_ALIGNMENT.CENTER,size=16)

    smallTitle = doc.add_paragraph()
    addRun(smallTitle,'סה"כ יש להשלים 28 נק"ז',True,alignment= WD_PARAGRAPH_ALIGNMENT.CENTER)

    nameP = doc.add_paragraph()
    addRun(nameP,'שם הסטודנט/ית: ',True)
    addRun(nameP,f'       {student_name}       ',underline=True)

    dateP = doc.add_paragraph()
    addRun(dateP,'תחילת לימודים בחטיבה: ',True)
    addRun(dateP,f'       {start_date}       ',underline=True)

    
    
    
    


    doc.save('demo.docx')

def addRun(paragraph, text, bold=False, underline=False,alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT,size=12,font="David"):
    paragraph.alignment = alignment
    run = paragraph.add_run(text)
    make_run_rtl(run,bold,underline,size,font)
    

def make_run_rtl(run, bold=False, underline=False,size=None,font="David"):
    r = run._element
    rPr = r.get_or_add_rPr()

    # RTL
    rtl = OxmlElement('w:rtl')
    rtl.set(qn('w:val'), '1')
    rPr.append(rtl)

    # Bold
    if bold:
        b = OxmlElement('w:b')
        rPr.append(b)

        bCs = OxmlElement('w:bCs')
        rPr.append(bCs)

    # Underline
    if underline:
        u = OxmlElement('w:u')
        u.set(qn('w:val'), 'single')
        rPr.append(u)

    # Font size
    if size is not None:
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), str(size * 2))
        rPr.append(sz)

        szCs = OxmlElement('w:szCs')
        szCs.set(qn('w:val'), str(size * 2))
        rPr.append(szCs)

    # Font
    if font is not None:
        rFonts = OxmlElement('w:rFonts')
        rFonts.set(qn('w:ascii'), font)
        rFonts.set(qn('w:hAnsi'), font)
        rFonts.set(qn('w:cs'), font)
        rPr.append(rFonts)

constructFile("גיא אברהם","23.8.2024","","","")
