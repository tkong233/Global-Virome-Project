import xlsxwriter

workbook = xlsxwriter.Workbook('test_workbook.xlsx')
worksheet = workbook.add_worksheet()

Ecotypes = (
	['Ecotype 1', 100],
	['Ecotype 2', 200],
	['Ecotype 3', 300]
	)

row = 0
col = 0

for Ecotype, count in Ecotypes:
	worksheet.write(row, col, Ecotype)
	worksheet.write(row + 1, col, count)
	col += 1

workbook.close()
