# Expense Tracker

A simple, local-first expense tracker built with Python and Streamlit. The project is intentionally delivered as three files for an easy open-source release:

- `expense-tracker.py` — the single-file Streamlit app
- `requirements.txt` — pinned dependencies
- `README.md` — this document

## Features

- Add new expenses with date, amount, currency, category, merchant, notes, and optional receipt attachment.
- Local SQLite storage (`expenses.db`) with timestamped backups.
- Import from CSV and export to CSV/JSON. Optional password-protected encrypted backups using `cryptography`.
- Overview charts (monthly trend and category breakdown) using Altair.
- Full ISO currency support and optional automatic rate fetching (exchangerate.host).

## Installation (Windows PowerShell)

1. Clone the repository and change directory:

```powershell
git clone https://github.com/ayushyuvraj/expense-tracker.git
cd expense-tracker
```

2. Create and activate a virtual environment (recommended):

```powershell
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run the app

Start Streamlit with:

```powershell
streamlit run expense-tracker.py
```

The app runs locally and opens in your default browser. Data is stored in `expenses.db` in the same folder by default.

## Import / Export / Backups

- Import: use the **Import/Export** tab to upload a CSV with headers `date,amount,currency,category,merchant,notes`.
- Export: download CSV or JSON from the **Transactions** tab.
- Backup: download a JSON backup or create an encrypted backup (requires `cryptography`).

## Privacy & Security

- Data is stored locally by default and the app does not phone home.
- Automatic currency-rate fetching uses `exchangerate.host` (no API key); you can disable auto-fetch in Settings to be fully offline.
- Encrypted backups are optional and protected by a password you choose (the repo does not store passwords).

## Receipts

- Receipt files uploaded via the app are saved to a local `receipts/` folder and referenced by path in the DB. Keep `receipts/` together with `expenses.db` when moving files.

## Contributing

Contributions are welcome. For this minimal three-file project, please open issues or submit small PRs. Describe the platform and Python version when reporting bugs.

## Troubleshooting

- If Streamlit crashes on import, ensure your Python version is supported and `pip install -r requirements.txt` completed successfully.
- If the DB file is locked, close other apps using `expenses.db` or restart Streamlit.

## License

This project is released under the MIT License.
