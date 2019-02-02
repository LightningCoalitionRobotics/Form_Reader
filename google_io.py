import OpenSSL
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from pylatex import Document, Section, Subsection, Command
import pylatex as pyl

json_key = json.load(open('creds.json'))
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
file = gspread.authorize(credentials)
sheet = file.open("Notebook Form Responses").sheet1

date = {}
author = {}
accomplished_bul = {}
accomplished_par = {}
wanted_bul = {}
wanted_par = {}
next_par = {}
next_bul = {}
didnt_do_bul = {}
improve_par = {}

for i in range(2, 5):
    if sheet.acell('A{}'.format(i)).value != "Stop":
        v = i-1
        date[v] = sheet.cell(i, 3)
        author[v] = sheet.cell(i, 4)
        wanted_bul[v] = sheet.cell(i, 5)
        wanted_par[v] = sheet.cell(i, 6)
        accomplished_bul[v] = sheet.cell(i, 7)
        accomplished_par[v] = sheet.cell(i, 8)
        didnt_do_bul[v] = sheet.cell(i, 9)
        improve_par[v] = sheet.cell(i, 10)
        next_bul[v] = sheet.cell(i, 11)
        next_par[v] = sheet.cell(i , 12)

        print("Finished parsing row {}".format(v))

    elif sheet.acell('A{}'.format(i)).value == "Stop":
        print("Finished parsing")

'''
Latex Section Begins:
'''

for i in range(2, 5):
    if __name__ == '__main__':
        v = i - 1

        doc = Document()
        doc.documentclass = Command('documentclass', options=['12pt'], arguments=['article'])
        doc.packages.append(pyl.Package('graphicx'))
        doc.packages.append(pyl.Package('fancyhdr'))
        doc.packages.append(pyl.Package('float'))

        doc.preamble.append(pyl.Command('pagestyle', 'fancy'))
        doc.preamble.append(pyl.Command('title', 'Notebook'))
        doc.append(date[v] + " - " + author[v]) #or preamble.append?

        with doc.create(Section('Our Plan')):
            # remove [] from all strings
            with doc.create(Itemize()) as itemize:
                for v in wanted_bul:
                    itemize.add_item(wanted_bul[v])
                itemize.append(Command("ldots"))
            doc.append(wanted_par[v])
        with doc.create(Section('What We Got Done')):
            with doc.create(Itemize()) as itemize:
                for v in accomplished_bul:
                    itemize.add_item(accomplished_bul[v])
                itemize.append(Command("ldots"))
            doc.append(accomplished_par[v])
        with doc.create(Section('What We Can Improve On For Next Time')):
            with doc.create(Itemize()) as itemize:
                for v in improve_bul:
                    itemize.add_item(improve_bul[v])
                itemize.append(Command("ldots"))
            doc.append(improve_par[v])
        with doc.create(Section('Next Practice')):
            with doc.create(Itemize()) as itemize:
                for v in next_bul:
                    itemize.add_item(next_bul[v])
                itemize.append(Command("ldots"))
            doc.append(next_par[v])
        doc.generate_pdf("notebook{}".format(v), clean_tex=False)



#     #cd C:\Users\chris\Desktop\Coding\Python\Form Reader
#
#     # redo form with author
