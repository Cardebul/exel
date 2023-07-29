from docx import Document


def word_gen(data, project_name):
    document = Document('exelgen/utils/xxx.docx')
    mul = 8 if data.get('data1').get('Дни/Недели') == 'дням' else 40
    price = int(data.get('data1').get('Тариф'))
    count = sum(list(map(int, data.get('data2').get('Количество'))))
    total_price = price*count*mul
    total_hours = count*mul
    temp = [r'%price%', r"%hour%"]
    for paragraph in document.paragraphs:
        if temp[0] in paragraph.text:
            paragraph.text = paragraph.text.replace(temp[0], str(total_price))
        elif temp[1] in paragraph.text:
            paragraph.text = paragraph.text.replace(temp[1], str(total_hours))

    file_path = f'wordfiles/{project_name}.docx'
    document.save(file_path)
    return file_path
