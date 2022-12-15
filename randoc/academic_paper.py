import random
from typing import List

from faker import Faker
from faker.providers import lorem
from pylatex import Command
from pylatex import Document
from pylatex import NoEscape
from pylatex import Section
from pylatex import Subsection


class AcademicPaper(Document):
    def __init__(
        self,
        title: str = None,
        authors: List[str] = None,
        date: str = None,
        random_text: bool = False,
    ):
        super().__init__()
        self.random_text = random_text
        self.preamble.append(Command("title", title))

        for author in authors:
            self.preamble.append(Command("author", author))

        if date is None:
            self.preamble.append(Command("date", NoEscape(r"\today")))
        else:
            self.preamble.append(Command("date", date))

        self.append(NoEscape(r"\maketitle"))

        self.fake = Faker()
        self.fake.add_provider(lorem)

    def fill_document(
        self,
        section_title: str = None,
        section_text: str = None,
        subsection_title: str = None,
        subsection_text: str = None,
    ):
        """Add a section, a subsection and some text to the document."""

        if not self.random_text:
            with self.create(Section(section_title)):
                self.append(section_text)

                with self.create(Subsection(subsection_title)):
                    self.append(subsection_text)

        else:
            with self.create(Section(self.fake.sentence())):
                num_paragraphs = random.randint(3, 5)
                for _ in range(num_paragraphs):
                    self.append(self.fake.paragraph())
                    self.append(NoEscape(r"\newline\newline"))

                with self.create(Subsection(self.fake.sentence())):
                    num_paragraphs = random.randint(3, 5)
                    for _ in range(num_paragraphs):
                        self.append(self.fake.paragraph())
                        self.append(NoEscape(r"\newline\newline"))
