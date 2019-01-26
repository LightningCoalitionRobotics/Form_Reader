import OpenSSL
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from pylatex import Document, Section, Subsection, Command

json_key = json.load(open('creds.json'))
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
file = gspread.authorize(credentials)
sheet = file.open("Form Reader Thing").sheet1

# down, right
date = {}
team_growth = {}
accomplished = {}
wanted = {}
plan_for_next = {}
not_accomplished = {}

for i in range(2, 7):
    if sheet.acell('A{}'.format(i)).value != "Stop":
        v = i-1

        date[v] = sheet.cell(i, 3).value

        if len(sheet.cell(i, 4).value) > 0:
            is_team_growth = True
            team_growth[v] = sheet.cell(i,4).value

        elif len(sheet.cell(i, 4).value) == 0:
            is_team_growth = False

        accomplished[v] = sheet.cell(i, 5).value.split(',')
        not_accomplished[v] = sheet.cell(i, 6).value.split(',')
        wanted[v] = sheet.cell(i, 7).value.split(',')
        plan_for_next[v] = sheet.cell(i, 8).value.split(',')

        # if "https" in sheet.cell(i, 9).value:
        #     images = True
        #     image_links = sheet.cell(i,9).value.split(',')
        # else:
        #     images = False
        print("Finished parsing row {}".format(v))

    elif sheet.acell('A{}'.format(i)).value == "Stop":
        print("Finished parsing, data:")
        print(wanted)

'''
Latex Section Begins:
'''

for i in range(2, 7):
    if __name__ == '__main__':
        v = i - 1

        doc = Document()
        doc.preamble.append(Command('title', 'title eeeee')) # what should the tile be???
        doc.preamble.append(Command('author', sheet.cell(i, 9))) # create dict with emails to authors
        doc.preamble.append(Command('date', "date lol"))
        # doc.append(NoEscape(r'\maketitle'))

        with doc.create(Section('Our Plan')):
            doc.append(wanted[v]) # format this all
        with doc.create(Section('What We Got Done')):
            doc.append(accomplished[v])
        with doc.create(Section('What We Did Not Get Done')):
            doc.append(not_accomplished[v])
        with doc.create(Section('Next Practice')):
            doc.append(plan_for_next[v])
        doc.generate_pdf("test", clean_tex=False) # based On October 13, 2019 or whatever
        tex = doc.dumps()

#     #cd C:\Users\chris\Desktop\Coding\Python\Form Reader
#
#     # redo form with author and also with the correct seperators (,)
