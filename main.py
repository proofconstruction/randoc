from randoc import AcademicPaper
from faker import Faker
import random
from pdf2image import convert_from_path

fake = Faker()

title = fake.sentence(nb_words = random.randint(3,7))
authors = []
for _ in range(random.randint(1,3)):
    authors.append(fake.name())

doc = AcademicPaper(title, authors, random_text = True)
doc.fill_document()

doc.generate_pdf('academic_paper', clean_tex=False)

filename = 'academic_paper'

pages = convert_from_path(f'{filename}.pdf')
for i, page in enumerate(pages):
    page.save(f'{filename}-{i}.jpg', 'JPEG')
