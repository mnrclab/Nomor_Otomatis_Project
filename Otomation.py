import xlsxwriter

file = xlsxwriter.Workbook('DataWarga.xlsx')
sheet = file.add_worksheet('DataWarga')

sheet.write(0, 0, 'No') 
sheet.write(0, 1, 'Nama') 
sheet.write(0, 2, 'Profesi') 

gate = input('Apakah Anda ingin memasukkan data? (Y/N) ').lower()

row = 1
n = 1
while gate == 'y':
    col = 0
    nama = input('Ketik nama warga: ')
    profesi = input('Ketik profesinya: ')
    hasil = [n, nama, profesi]
    for i in range(len(hasil)):
        sheet.write(row, col, hasil[col])
        col += 1
    row += 1
    n += 1
    gate = input('Apakah Anda ingin memasukkan data? (Y/N) ').lower()
else:
    file.close()