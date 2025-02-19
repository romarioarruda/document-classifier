from pprint import pprint
from core.document_field import DocumentField
from core.document_identify import DocumentIdentify
from utils.pdf_text_extractor import extract_text_from_pdf
from database.local_id_pattern_loader import LocalIdPatternLoader
from database.local_field_pattern_loader import LocalFieldsPatternLoader


document = DocumentIdentify(LocalIdPatternLoader('./patterns/ids.txt'))

text = extract_text_from_pdf('./pdf_2.pdf')

# print(text)
doc_type = document.get_classification(text)
print(f"Tipo do documento: {doc_type}")

doc_fields = DocumentField(LocalFieldsPatternLoader('./patterns/fields.txt'))

json_data = doc_fields.get_fields(doc_type, text)
pprint(json_data, width=160)