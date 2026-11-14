"""Pull every table out of a list of PDFs into one Excel file.

pip install "apify-client>=3"
APIFY_TOKEN=... python pdf_tables_to_excel.py
"""
import os
from apify_client import ApifyClient

PDF_LINKS = [
    "https://www.federalreserve.gov/releases/h8/current/h8.pdf",
    "https://www.census.gov/construction/nrc/pdf/newresconst.pdf",
    "https://www.census.gov/retail/marts/www/marts_current.pdf",
]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("blueberry_rainstorm/pdf-to-text-markdown").call(
    run_input={"urls": [{"url": u} for u in PDF_LINKS]}
)

# One row per PDF: status, page count, table count, link to its own workbook
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["fileName"], item["status"], item.get("tableCount"), "tables")

# Every table from every PDF in one workbook (one sheet per table + an index sheet)
record = client.key_value_store(run.default_key_value_store_id).get_record("tables.xlsx")
with open("tables.xlsx", "wb") as f:
    f.write(record["value"])
print("Saved tables.xlsx")
