# Projekt pri predmetu progamiranje1

Za projekt sem analizirala prosta delovna mesta iz spletne strani študentskega servisa:
https://www.studentski-servis.com/studenti/delo/prosta-dela

Za posamezno delovno mesto sem zajela
- vrsto dela,
- identifikacijsko številko dela,
- vrsto delovnika, 
- opis dela, 
- plačilo, 
- kraj dela in
- število prostih mest.
Podatki so shranjeni v datoteki izhodni_podatki.csv.
Nekoliko preurejeni pa se nahajajo v datotei precisceni.csv. V teh sem uskladila velike in male začetnice, odstranila enote za plačilo in izločila ponudbe za delo z opisno obliko plačila. (Kjer so namesto urne postavke pisali npr. po projektu, po dogovoru...)

Delovne hipoteze:
- Ali so v Ljubljani dela bolje plačana kot drugje po Sloveniji?
- Katera dela so najbolje plačana?
- Ali so dela z izmenskim delovnim časom bolje plačana?

Podatki so analizirani v datoteki analiza_podatkov.ipynb.

Datoteki skripta shrani spletno stran in naloga.py pa sta namenjeni shranjevanju spletne strani in izločevanju podatkov, ki se zberejo v csv datoteko.
