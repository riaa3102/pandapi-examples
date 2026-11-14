# PDF tables to one Excel file

Send a list of PDF links, get back `tables.xlsx`: an index sheet plus one sheet per table, numbers stored as numbers, tables that run over several pages joined into one sheet.

Tested 2026-11-14 on three US government reports (Fed H.8, Census new residential construction, Census retail sales): 17 tables in about 45 seconds, cost under one cent.

## Run it

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=...   # free account at apify.com, Settings > API & Integrations
python pdf_tables_to_excel.py
```

Edit `PDF_LINKS` in the script to use your own files.

## How it works

The script calls the [PDF to Excel, Markdown & Text](https://apify.com/blueberry_rainstorm/pdf-to-text-markdown) actor, prints one line per PDF and saves the combined workbook from the run's key-value store. Each PDF also gets its own workbook (`excelUrl` in the dataset), plus Markdown and plain text.

Price: $3 per 1,000 PDFs (failed PDFs free), OCR for scanned pages $5 per 1,000 pages.

## Free alternative

For a few PDFs with ruled tables, `pdfplumber` (`page.extract_tables()`) or `camelot` (`flavor="lattice"`) are free and work well. Borderless tables, multi-page tables and mixed layouts are where they need tuning. Walkthrough: see the blog post linked from the repo description.
