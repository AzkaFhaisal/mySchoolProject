from reportlab.pdfgen import canvas

dataSiswa = {
	"nama" : "Anas",
	"kelas" : "VII-1",
	"laporan" : "Rapor Kelas 7 Semester 2"
}


class Data:

	def __init__(self, filename, documentTitle, heading):
		self.filename = filename
		self.documentTitle = documentTitle
		self.heading = heading
		self.info = """
		Anas Azhar
		Kelas 7.2
		"""
myData = Data(str(dataSiswa['nama']+dataSiswa["kelas"]+".pdf"), "Hasil Ujian", dataSiswa['laporan'])
myPdf = canvas.Canvas(myData.filename)
myPdf.setTitle(myData.documentTitle)

#myPdf.drawString(220,810,myData.heading) #x, y,heading

myPdf.setFont("Helvetica", 30)
myPdf.setFillColorRGB(0,0,255)
myPdf.drawCentredString(300, 770,"Biodata Kucing")
myPdf.line(30, 760, 560, 760)
#			x1	y1	x2		y2
myText = myPdf.beginText(40,700)
myText.setFont("Helvetica", 18)

Lines = ["Berikut data Kucing", "Nama: Pupu", "Tahun lahir: 2019", "Jenis Kelamin: Perempuan", "Jenis Kucing: Persia", "Warna Bulu: Coklat mudah dengan pola coklat tua"]
for line in Lines:
	myText.textLine(line)
myPdf.drawText(myText)

myPdf.drawInlineImage("pic1.JPG", 220, 500)

myPdf.save()

#print("OK")