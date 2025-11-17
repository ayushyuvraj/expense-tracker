# Expense Tracker

This is a simple expense tracker application built using Python and Streamlit. The application allows users to input, view, and manage their expenses through an intuitive web interface.

## Features

- Add new expenses with descriptions and amounts.
- View a summary of all expenses.
- Visualize spending trends over time.

## Installation

To run this application, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the expense tracker application, run the following command:
```
streamlit run expense-tracker.py
```

This will open a new tab in your web browser where you can start adding and managing your expenses.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is open source and available under the MIT License.

# (Expanded README)

This repository now contains a single-file Streamlit app `expense-tracker.py` plus `requirements.txt` and this `README.md`. Follow the Quick Start below to run the app locally.

## Quick Start (Windows PowerShell)

```powershell
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run expense-tracker.py
```

See the app's `Import/Export` tab for CSV import and encrypted backup options.