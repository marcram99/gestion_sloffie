from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime, date, timedelta

from . import schema

def generate_pdf(client: schema.Client,
                 facture: schema.Facture):
    print(f'DEBUG-Wellcome to PDF generator')
    w, h = A4
    step = 13
    # Données facture
    no_fact = f"FSMCC_{facture.id:0>4}"
    date_fact = facture.timestamp
    # Entête (ligne 1)
    c = canvas.Canvas(f"facture_{no_fact}.pdf", pagesize=A4)
    c.drawImage("logo.jpg", 30, h - 70, width=100, height=45)
    c.line(135, h-56, w-30, h-56)
    c.setFont("Times-Roman", 20)
    c.drawString(w-225, h-45,f"Facture: {no_fact}")
    # Entête (ligne 2)
    c.setFont("Times-Bold", 12)
    haut = h-92
    c.drawString(50, haut + 1, "Sloffiemusic-Coaching vocal")
    c.setFont("Times-Roman", 12)
    c.drawString(50, haut - 1 * step, "@My FunMusic School")
    c.drawString(50, haut - 2 * step, "Route de Chêne 78")
    c.drawString(50, haut - 3 * step, "1224 Chêne-Bougerie")
    c.drawString(50, haut - 4 * step, "tel: +4176 313 0193")
    c.setFont("Times-Roman", 12)
    c.drawString(w-190, haut, f"date facture:         {date_fact}")
    c.drawString(w-190, haut - 1 * step, f"échéance facture: {date_fact}")
    c.setStrokeGray(0.8)
    c.line(50, h-165, w-50, h-165)
    # Infos client
    haut = h-190
    c.setFont("Times-Bold", 12)
    c.drawString(50, haut, "Informations client")
    c.setFont("Times-Roman", 12)
    c.drawString(50, haut - 1 * step, f"{client.prenom} {client.nom}")
    c.drawString(50, haut - 2 * step, f"{client.adresse}")
    c.drawString(50, haut - 3 * step, f"{client.code_postal} {client.code_postal}")
    c.drawString(50, haut - 4 * step, f"{client.mail}")
    c.drawString(50, haut - 5 * step, f"tel: {client.no_tel}")
    """
    c.drawString(50, haut - 1 * step, f"{client['prenom']} {client['nom']}")
    c.drawString(50, haut - 2 * step, f"{client['adresse']}")
    c.drawString(50, haut - 3 * step, f"{client['code_postal']} {client['ville']}")
    c.drawString(50, haut - 4 * step, f"{client['mail']}")
    c.drawString(50, haut - 5 * step, f"{client['no_tel']}")
    """
    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.rect(30, h-280, w-60, -36, fill=1)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(50, h-302, f"Article ou service")
    c.drawString(290, h-302, f"Prix")
    c.drawString(390, h-302, f"Quantité")
    c.drawString(500, h-302, f"Total")
#-----------------------------------------------------
    h_item = h-342
    rabais = 20
    acompte = 0
    total = 0
    panier =[ 
                ["formule 5 cours", 1, 350],
                ["formule 10 cours", 1,650],
                ["formule 5 cours", 2, 350],
                ["formule 10 cours", 1,650],
            ]
    for count, items in enumerate(panier):
        article, quantite, prix = items
        c.drawString(50, h_item - count * 18, f"{article}")
        c.drawString(280, h_item - count * 18, f"{prix} CHF")
        c.drawString(400, h_item - count * 18, f"{quantite}x")
        c.drawString(490, h_item - count * 18, f"{prix * quantite:>5n}")
        c.drawString(522, h_item - count * 18, f"CHF")
        total += prix * quantite
#-----------------------------------------------------
    h_total = h_item - 60  - (count + 1) * 18
    c.drawString(280, h_total - 20, f"Total de la facture:")
    c.drawString(490, h_total - 20, f"{total: >5n}")
    c.drawString(522, h_total - 20, f"CHF")
    c.drawString(280, h_total - 40, f"Rabais:")
    c.drawString(490, h_total - 40, f"{rabais: >5n}")
    c.drawString(522, h_total - 40, f"CHF")
    c.drawString(280, h_total - 60, f"Montant déjà payé:")
    c.drawString(490, h_total - 60, f"{acompte: >5n}")
    c.drawString(522, h_total - 60, f"CHF")
    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.rect(270, h_total - 75 , 295, -36, fill=1)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(280, h_total - 96, f"Reste à payer:")
    c.drawString(490, h_total - 96, f"{(total - rabais): >5n}")
    c.drawString(522, h_total - 96, f"CHF")

    c.line(50, h_total, w-50, h_total)

    """ Gabarit
    c.line(w-30, 0, w-30, h)
    c.line(30, 0, 30, h)
    c.line(50, 0, 50, h)
    c.line(w-50, 0, w-50, h)
    c.line(w-80, 0, w-80, h)
    """
    c.showPage()
    c.save()

if __name__ == '__main__':
    now = datetime.now()
    today = date.today()
    print(f'{now=: %Y-%m-%d}')
    print(f'{today}')
    client = {'nom': 'Wanner',
            'prenom':'Marc',
            'adresse':"141 ch. de l'Eau Belle",
            'code_postal':'74100',
            'ville': 'Etrembières',
            'mail': 'marcram@proton.me',
            'no_tel': '+4176 615 6408'
            }
    generate_pdf(client)
    print('generate')
