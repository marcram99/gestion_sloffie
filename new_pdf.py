from fpdf import FPDF
from datetime import datetime, date, timedelta
from os import path

from . import schema

def generate_pdf(client: schema.Client,
                 facture: schema.Facture):
    # -- Info facture ------------------------------------
    no_fact = f"SM_{facture.id:0>4}"
    panier =[ 
    #            ["formule  5 cours", 1, 350],
                ["formule 10 cours", 1,800],
    #            ["formule  5 cours", 2, 350],
    #            ["formule 10 cours", 1,650],
            ]
    date_fact = datetime.strptime(facture.timestamp, '%Y-%m-%d')
    echeance = (date_fact + timedelta(days=30)).strftime('%Y-%m-%d')
    # -- Info facture ------------------------------------

    pdf_file = path.join('/Users/mcwa/Marc-perso/code/python/gestion_sloffie/static/fichiers/',f'facture_{no_fact}.pdf')
    logo = path.join('/Users/mcwa/Marc-perso/code/python/gestion_sloffie/static/images/','logo.jpg')

    pdf = FPDF()
    pdf.add_page()
    # -- Entête
    pdf.image(logo, x=8, y=8, h=17)
    pdf.set_line_width(0.5)
    pdf.set_draw_color(1)
    pdf.line(x1=48, y1=20, x2=197, y2=20)
    pdf.set_font(family="Times", style="", size=16)
    pdf.set_text_color(00)
    pdf.cell(190, 10, align='R', txt=f'Facture: {no_fact}') 
    # -- Cartouche Sloffie 
    x, y = 16, 29
    pdf.set_draw_color(180)
    pdf.set_line_width(0.3)
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_xy(x, y)
    pdf.cell(txt='Sloffiemusic-Coaching vocal')
    pdf.set_font(family="Times", style="", size=12)
    pdf.set_xy(x, y+5)
    pdf.cell(txt='@My FunMusic School')
    pdf.set_xy(x, y+10)
    pdf.cell(txt='Route de Chêne 78')
    pdf.set_xy(x, y+15)
    pdf.cell(txt='1224 Chêne-Bougerie')
    pdf.set_xy(x, y+20)
    pdf.cell(txt='tel: +4176 313 9103')
    pdf.line(x1=17, y1=60, x2=197, y2=60)
    # -- information date facture
    pdf.set_xy(x + 136, y + 5)
    pdf.cell(txt='Date facture:')
    pdf.set_xy(x + 161, y + 5)
    pdf.cell(txt=facture.timestamp)
    pdf.set_xy(x + 128, y+10)
    pdf.cell(txt='Echéance facture:')
    pdf.set_xy(x + 161, y+10)
    pdf.cell(txt=echeance)
    # -- Informations client
    y = y + 37
    pdf.set_xy(x, y)
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(txt='Information client:')
    pdf.set_font(family="Times", style="", size=12)
    pdf.set_xy(x, y+5)
    pdf.cell(txt=f'{client.prenom} {client.nom}')
    pdf.set_xy(x, y+10)
    pdf.cell(txt=f'{client.adresse}')
    pdf.set_xy(x, y+15)
    pdf.cell(txt=f'{client.code_postal} {client.ville}')
    pdf.set_xy(x, y+20)
    pdf.cell(txt=f'{client.mail}')
    pdf.set_xy(x, y+25)
    pdf.cell(txt=f'{client.no_tel}')
    # -- Information facture
    pdf.set_fill_color(230)
    y = y + 41
    pdf.rect(8, y-5, 193, 14, round_corners=True, style="F")
    pdf.set_xy(x, y)
    pdf.cell(txt='Article ou service')
    pdf.set_xy(x+80, y)
    pdf.cell(txt='Prix')
    pdf.set_xy(x+110, y)
    pdf.cell(txt='Quantité')
    pdf.set_xy(x+152, y)
    pdf.cell(txt='Total')
    # -- détails
    y = y + 16
    total = 0
    for count, items in enumerate(panier):
        article, quantite, prix = items
        pdf.set_xy(x, y)
        pdf.cell(txt=article)
        pdf.set_xy(x+80, y)
        pdf.cell(txt=str(prix))
        pdf.set_xy(x+120, y)
        pdf.cell(txt=str(quantite))
        pdf.set_xy(x+155, y)
        pdf.cell(txt=str(prix*quantite))
        pdf.set_xy(x+172, y)
        pdf.cell(txt='CHF')
        y += 7
        total += prix*quantite
    pdf.set_line_width(0.5)
    pdf.line(x1=92, y1=y+5, x2=197, y2=y+5)
    # -- Information total
    x, y = 96, y + 12
    pdf.set_xy(x, y)
    pdf.cell(txt='Total de la facture:')
    pdf.set_xy(x + 71, y)
    pdf.cell(w=12, align='R', txt=f'{total}')
    pdf.set_xy(x + 92, y)
    pdf.cell(txt='CHF')
    pdf.set_xy(x, y + 7)
    pdf.cell(txt='Rabais:')
    pdf.set_xy(x + 71, y + 7 )
    rabais= 000
    pdf.cell(w=12, align='R', txt=f'{rabais}')
    pdf.set_xy(x + 92, y + 7)
    pdf.cell(txt='CHF')
    pdf.set_xy(x, y + 14)
    pdf.cell(txt='Montant déjà payé:')
    pdf.set_xy(x + 71, y + 14)
    acompte = 00
    pdf.cell(w=12, align='R', txt=f'{acompte} ')
    pdf.set_xy(x + 92, y + 14)
    pdf.cell(txt='CHF')

    pdf.rect(92, y + 25, 109, 14, round_corners=True, style="DF")
    pdf.set_xy(x, y + 29)
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(txt='Reste à payer:')
    pdf.set_xy(x + 70, y + 29)
    reste = total - rabais - acompte
    pdf.cell(w=15, align='R', txt=f'{reste} ')
    pdf.set_xy(x + 88, y + 29)
    pdf.cell(txt='CHF')

    pdf.line(x1=17, y1=240, x2=197, y2=240)
    x, y = 16, 245
    pdf.set_draw_color(180)
    pdf.set_line_width(0.3)
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_xy(x, y)
    pdf.cell(txt='Contact:')
    pdf.set_font(family="Times", style="", size=12)
    pdf.set_xy(x, y+5)
    pdf.cell(txt='Sophie Martin')
    pdf.set_xy(x, y+10)
    pdf.cell(txt='Téléphone: +4176 313 9103')
    pdf.set_xy(x, y+15)
    pdf.cell(txt='Email: sloffiemusic@gmail.com')
    pdf.set_xy(x, y+20)
    pdf.cell(txt='www.sloffiemusic.com')
    
    x, y = 107, 245
    pdf.set_draw_color(180)
    pdf.set_line_width(0.3)
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_xy(x, y)
    pdf.cell(txt='Coordonnées bancaires:')
    pdf.set_font(family="Times", style="", size=12)
    pdf.set_xy(x, y+5)
    pdf.cell(txt='Banque:')
    pdf.set_xy(x, y+10)
    pdf.cell(txt='Code Banque:')
    pdf.set_xy(x, y+15)
    pdf.cell(txt='No de compte:')
    pdf.set_xy(x, y+20)
    pdf.cell(txt='IBAN: ')
    pdf.set_xy(x, y+25)
    pdf.cell(txt='SWIFT/BIC: ')
    x, y = 137, 245
    pdf.set_draw_color(180)
    pdf.set_line_width(0.3)
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_font(family="Times", style="", size=12)
    pdf.set_xy(x, y+5)
    pdf.cell(txt='BCGE ')
    pdf.set_xy(x, y+10)
    pdf.cell(txt='Code Banque:')
    pdf.set_xy(x, y+15)
    pdf.cell(txt='GE-1234')
    pdf.set_xy(x, y+20)
    pdf.cell(txt='CH12-1234-1234-123-12')
    pdf.set_xy(x, y+25)
    pdf.cell(txt='SWIFT/BIC: ')
    """
    # -- GABARIT pour CORRECTION
    pdf.set_draw_color(180,0,0)
    pdf.line(x1=8, y1=1, x2=8, y2=252)
    pdf.line(x1=17, y1=1, x2=17, y2=252)
    pdf.line(x1=92, y1=1, x2=92, y2=252)
    pdf.line(x1=97, y1=1, x2=97, y2=252)
    pdf.line(x1=178, y1=1, x2=178, y2=252)
    pdf.line(x1=197, y1=1, x2=197, y2=252)
    pdf.line(x1=201, y1=1, x2=201, y2=252)
    #"""
    pdf.output(pdf_file)


if __name__ == '__main__':
    facture = schema.Facture(id=125,
                            timestamp='06-07-2023',
                            produit='cours de chant',
                            user_id=123)
    client = schema.Client(nom='Wanner',
                        prenom='Marc',
                        adresse='144 impasse de la Touvières',
                        code_postal='74100',
                        ville='Etrembières',
                        no_tel='+4176 615 6408',
                        mail='marcram@proton.me',
                        id= 666,
                        )
    generate_pdf(client, facture)
    print('generate')
