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

myData = Data(str(dataSiswa['nama']+dataSiswa["kelas"]+".pdf"), "Hasil Ujian", dataSiswa['laporan'])
myPdf = canvas.Canvas(myData.filename)
myPdf.setTitle(myData.documentTitle)

myPdf.drawString(190,750,myData.heading) #x, y,heading

myPdf.save()

#print("OK")