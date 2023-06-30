from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def generate_pdf(nom):
    w, h = A4
    step = 13
    # Données facture
    no_fact = "FSMCC_00001"
    date_fact = "31.12.2023"
    client = {'nom': nom,
            'prenom':'Marc',
            'adresse':"141 ch. de l'Eau Belle",
            'code_postal':'74100',
            'ville': 'Etrembières',
            'mail': 'marcram@proton.me',
            'no_tel': '+4176 615 6408'
            }
    # Entête (ligne 1)
    c = canvas.Canvas("facture_sloffiemusic.pdf", pagesize=A4)
    c.drawImage("logo.jpg", 30, h - 70, width=100, height=45)
    c.line(135, h-56, w-25, h-56)
    c.setFont("Times-Roman", 20)
    c.drawString(w-220, h-45,f"Facture: {no_fact}")
    # Entête (ligne 2)
    c.setFont("Times-Bold", 12)
    haut = h-88
    c.drawString(30, haut + 1, "Sloffiemusic-Coaching vocal")
    c.setFont("Times-Roman", 12)
    c.drawString(30, haut - 1 * step, "@My FunMusic School")
    c.drawString(30, haut - 2 * step, "Route de Chêne 78")
    c.drawString(30, haut - 3 * step, "1224 Chêne-Bougerie")
    c.drawString(30, haut - 4 * step, "tel: +4176 313 0193")
    c.setFont("Times-Roman", 12)
    c.drawString(w-167, haut, f"date facture:         {date_fact}")
    c.drawString(w-167, haut - 1 * step, f"échéance facture: {date_fact}")
    c.setStrokeGray(0.8)
    c.line(30, h-160, w-30, h-160)
    # Infos client
    haut = h-190
    c.setFont("Times-Bold", 12)
    c.drawString(30, haut, "Facture à:")
    c.setFont("Times-Roman", 12)
    c.drawString(30, haut - 1 * step, f"{client['prenom']} {client['nom']}")
    c.drawString(30, haut - 2 * step, f"{client['adresse']}")
    c.drawString(30, haut - 3 * step, f"{client['code_postal']} {client['ville']}")
    c.drawString(30, haut - 4 * step, f"{client['mail']}")
    c.drawString(30, haut - 5 * step, f"{client['no_tel']}")
    c.line(30, h-280, w-30, h-280)
    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.rect(30, h-280, w-60, -40, fill=1)
    c.showPage()
    c.save()
    print('function pdf')
if __name__ == '__main__':
    generate_pdf('Marc_test')
    print('generate')
