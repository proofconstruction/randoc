from academic import AcademicPaper
from faker import Faker
import random

fake = Faker()

title = fake.sentence(nb_words = random.randint(3,7))
authors = []
for _ in range(random.randint(1,3)):
    authors.append(fake.name())

doc = AcademicPaper(title, authors, random_text = True)
doc.fill_document()

doc.generate_pdf('academic_paper', clean_tex=False)
