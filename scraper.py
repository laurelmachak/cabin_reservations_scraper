'''
source env/bin/activate

deactivate
'''

import requests
from bs4 import BeautifulSoup
import json
from credentials import PIN, EMAIL

LOGIN_URL = 'https://rentals.riverhomes.com/RNS/ownerservices/OwnerLogin.aspx'
RESERVATIONS_URL = 'https://rentals.riverhomes.com/RNS/ownerservices/UnitReservations.aspx'


payload = {
    "ctl00_toolkitscriptmanager1_HiddenField": "",
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__VIEWSTATE": "/wEPDwUJMjU1NDYzNTk3D2QWAmYPZBYEAgEPZBYCAgEPFgIeBFRleHQF7QM8bWV0YSBuYW1lPSJrZXl3b3JkcyIgY29udGVudD0iUnVzc2lhbiBSaXZlciwgU29ub21hIENvdW50eSwgTm9ydGhlcm4gQ2FsaWZvcm5pYSwgdmFjYXRpb24gcmVudGFscywgd2luZSB0YXN0aW5nLCBnZXRhd2F5cywgR3Vlcm5ldmlsbGUsIFJpbyBOaWRvLCBNb250ZSBSaW8sIEZvcmVzdHZpbGxlLCBDYXphZGVybywgcmVkd29vZHMsIEphenogRmVzdGl2YWwsIEJsdWVzIEZlc3RpdmFsIj48bWV0YSBuYW1lPSJkZXNjcmlwdGlvbiIgY29udGVudD0iUnVzc2lhbiBSaXZlciBWYWNhdGlvbiBIb21lcyB2YWNhdGlvbiByZW50YWxzIGluIEd1ZXJuZXZpbGxlIEZvcmVzdHZpbGxlIE1vbnRlIFJpbyBDYXphZGVybyBhbmQgUmlvIE5pZG8gd2l0aCB3aW5lIGNvdW50cnkgYWN0aXZpdGllcyBpbmNsdWRpbmcgZmlzaGluZyBzaWdodHNlZWluZyByZWR3b29kcyBjYW5vZWluZyBvbiB0aGUgUnVzc2lhbiBSaXZlciBhbmQgcmVsYXhpbmcgYXQgc3BhcyBhbmQgcmVzb3J0cyI+ZAIDD2QWAgIBD2QWAgIFD2QWAmYPDxYCHwAFHFJ1c3NpYW4gUml2ZXIgVmFjYXRpb24gSG9tZXNkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAgUaY3RsMDAkcGFnZWNvbnRlbnQkYnRuTG9naW4FHWN0bDAwJHBhZ2Vjb250ZW50JGJ0bkVtYWlsUElO10VARP9ATJwfqmF6L21NPLERirmxAkBtzE5Se+/oBig=",
    "__VIEWSTATEGENERATOR": "7E676602",
    "ctl00$pagecontent$txtEmail": EMAIL,
    "ctl00$pagecontent$txtPIN": PIN,
    "ctl00$pagecontent$btnLogin.x": "45",
    "ctl00$pagecontent$btnLogin.y": "11"
}


# LOGGED IN SUCCESSSSSSSSSSSS & ABLE TO GET RESERVATION TABLE WOOOOOO
# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(LOGIN_URL, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    

    # An authorised request.
    r = s.get(RESERVATIONS_URL)
    # print(r.text)

# print("================BEGIN RESERVATIONS PAGE HTML ========================")
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)
res_table = soup.find(id="ctl00_pagecontent_grdReservations")
rows = res_table.find_all('tr')
# print(res_table.prettify())
print("=========================")
# print(rows)
print("=========================")

table_headers = ['Code', 'Guest', 'Description', 'Arrive', 'Nights', 'Depart', 'Resv Date', 'Rental Rate']

unit_reservations = []


for row in rows[1:len(rows)-1]:
    cells = row.find_all('td')
    
    reservation = {}
    for i in range(len(table_headers)):
        
        key = table_headers[i]
        val = cells[i].string
        # print(cells[i])
        reservation[key] = val
    unit_reservations.append(reservation)


print(unit_reservations)

with open('reservations.json', 'w') as f:
    json.dump(unit_reservations, f)