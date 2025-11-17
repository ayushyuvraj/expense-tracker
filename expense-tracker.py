import streamlit as st
import pandas as pd

# Initialize session state for expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Function to add an expense
def add_expense(date, category, amount, description):
    expense = {
        'Date': date,
        'Category': category,
        'Amount': amount,
        'Description': description
    }
    st.session_state.expenses.append(expense)

# Function to display expenses
def display_expenses():
    if st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        st.write(df)
        st.write("Total Expenses: ", df['Amount'].sum())
    else:
        st.write("No expenses recorded yet.")

# Streamlit app layout
st.title("Expense Tracker")

# Input form for adding expenses
with st.form(key='expense_form'):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Other"])
    amount = st.number_input("Amount", min_value=0.01, format="%.2f")
    description = st.text_input("Description")
    submit_button = st.form_submit_button(label='Add Expense')

    if submit_button:
        add_expense(date, category, amount, description)
        st.success("Expense added!")

# Display the expenses
st.subheader("Recorded Expenses")
display_expenses()