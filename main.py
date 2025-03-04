from dotenv import load_dotenv

load_dotenv()

from pprint import pprint
from app.common.pdf_text_extractor import extract_text_from_pdf
from app.use_cases.document_field import DocumentField
from app.use_cases.document_identify import DocumentIdentify
from app.use_cases.local_id_pattern_loader import LocalIdPatternLoader
from app.use_cases.local_field_pattern_loader import LocalFieldsPatternLoader


document = DocumentIdentify(LocalIdPatternLoader('./infra/local_patterns/ids.txt'))

text = extract_text_from_pdf('./pdf_2.pdf')

# print(text)
doc_type = document.get_classification(text)
print(f"Tipo do documento: {doc_type}")

doc_fields = DocumentField(LocalFieldsPatternLoader('./infra/local_patterns/fields.txt'))

json_data = doc_fields.get_fields(doc_type, text)
pprint(json_data, width=160)