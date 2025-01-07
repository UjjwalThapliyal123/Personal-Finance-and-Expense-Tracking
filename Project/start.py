import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_chat import message
from datetime import datetime

# message("Hello bot!", is_user=True)  

# st.title("Personal Finance and Expense Tracking")
# # file_name='combined_expense.xls'
# df=pd.read_csv("combined_expense.csv")
conn=pymysql.connect(host='localhost',user='root',password='789456ujjwal@',database='TRACKER_EXPENSE')

def home_page():

   # Page Title
    st.title("Welcome to Personal Finance Tracker")

    # Description
    st.write("""
    This application helps you manage your personal finances by tracking your income, 
    expenses, and savings. It provides a simple interface to log your daily expenses and 
    visualize your financial health with graphs and summaries.

    #### Features:
    - **Track Expenses and Income:** Easily record all your transactions.
    - **View Summary:** Get an overview of your income, expenses, and balance.
    - **Analyze Spending:** Visualize your expenses by category with graphs.
    - **Save for the Future:** Plan and monitor your savings goals.
    
    Take control of your finances and start budgeting smarter today!
    """)
    # Page Title
    st.title("Welcome to Personal Finance Tracker")

    # Description
    st.write("""
    This application helps you manage your personal finances by tracking your income, 
    expenses, and savings. It provides a simple interface to log your daily expenses and 
    visualize your financial health with graphs and summaries.
    """)

    # Sample User Financial Overview
    st.write("### Your Financial Overview")
    total_income = 5000
    total_expenses = 3000
    savings_goal = 2000
    current_balance = total_income - total_expenses

    # Display financial stats
    st.write(f"**Total Income:** ${total_income}")
    st.write(f"**Total Expenses:** ${total_expenses}")
    st.write(f"**Current Balance:** ${current_balance}")
    st.write(f"**Savings Goal:** ${savings_goal}")

    # Display progress towards savings goal
    st.progress(current_balance / savings_goal)

    # Sample Transaction History
    st.write("### Recent Transactions")
    data = {
        'Date': [datetime(2024, 8, 1), datetime(2024, 8, 5), datetime(2024, 8, 10), datetime(2024, 8, 12)],
        'Category': ['Food', 'Transport', 'Entertainment', 'Utilities'],
        'Amount': [150, 50, 200, 100],
        'Type': ['Expense', 'Expense', 'Expense', 'Expense']
    }
    df = pd.DataFrame(data)
    st.table(df)

    # Sample Expense Breakdown (Pie Chart or Graph)
    st.write("### Expense Breakdown")
    expense_data = df.groupby('Category')['Amount'].sum()
    
    st.bar_chart(expense_data)

    # Financial Tips
    st.write("### Financial Tips")
    st.write("""
    - **Track All Expenses**: Even small purchases can add up over time.
    - **Set Realistic Savings Goals**: Start with small, achievable goals.
    - **Avoid Impulse Buying**: Plan your purchases and stick to your budget.
    - **Review Your Spending Regularly**: Adjust your budget based on actual spending.
    """)





# message("Hello") 
# message("Hello bot!", is_user=True)
  
# message("Welcome to Personal Finance and Expense Tracking Project") 
def page1():
                
                st.title("Page 1: Overview and Expenses")
                st.image("imagenew.png.webp",caption="The expense tracker")
                st.write("The Dataframe/Tables containing the full table")
                sql1="select * from combined_expenses"
                df=pd.read_sql(sql1,conn)
                st.dataframe(df)
                
              

                cursor=conn.cursor()

                st.write("")

                # Query to fetch data for August 2024
                sql2 = """ SELECT * 
                    FROM combined_expenses
                    WHERE date BETWEEN '2024-08-1' AND '2024-08-31';
                        """
                data = pd.read_sql(sql2, conn)

                    # Display the filtered data in the Streamlit app
                st.write("Filtered Data for August 2024:")
                st.dataframe(data)

                    # Optional: Count rows in the filtered data
                st.write(f"Total rows in the filtered data: {len(data)}")


                sql3 = """select sum(amount) as total_amount_of_month,extract(month from date) as month
                        from combined_expenses
                        where date  between '2024-08-1' and '2024-08-31'
                        group by month
                        order by total_amount_of_month desc
                        limit 1;
                            """
                query3= pd.read_sql(sql3,conn)
                st.dataframe(query3)            
                            
                if not query3.empty:
                        fig, ax = plt.subplots(figsize=(8, 5))
                        ax.plot(query3['month'], query3['total_amount_of_month'], marker='o', linestyle='-', color='b', label='Total Amount')
                        
                        # Add labels and title
                        ax.set_title("Total Expenses by Month for August 2024", fontsize=16)
                        ax.set_xlabel("Month", fontsize=12)
                        ax.set_ylabel("Total Amount (INR)", fontsize=12)
                        ax.legend()
                        ax.grid(True, linestyle='--', alpha=0.9)

                        # Render the chart in Streamlit
                        st.pyplot(fig)
                else:
                        st.warning("No data found for the specified date range.")        
                        

                sql4="""select amount,date
                            from combined_expenses
                            where amount between 3000 and 7000;
                            """
                data4= pd.read_sql(sql4,conn)
                top10=data4.head(10)
                st.dataframe(top10)


                st.write("This contains all the values which is in 3000 and 7000")
                if not data4.empty:
                        # Convert 'date' column to datetime for proper plotting
                        data4['date'] = pd.to_datetime(data4['date'])

                        # Create the plot
                        fig, ax = plt.subplots(figsize=(10, 6))
                        ax.plot(data4['date'], data4['amount'], marker='o', linestyle='-', color='g', label='Expense Amount')

                        # Add labels, title, and grid
                        ax.set_title("Expenses Between 3000 and 7000", fontsize=16)
                        ax.set_xlabel("Date", fontsize=12)
                        ax.set_ylabel("Amount (INR)", fontsize=12)
                        ax.legend()
                        ax.grid(True, linestyle='--', alpha=0.6)

                        # Rotate x-axis labels for better readability
                        plt.xticks(rotation=45)

                        # Render the chart in Streamlit
                        st.pyplot(fig)
                else:
                        st.warning("No data found for the specified range of amounts.")


                st.write("FIRST 10 VALUES")

                if not top10.empty:
                        # Convert 'date' column to datetime for proper plotting
                        top10['date'] = pd.to_datetime(top10['date'])

                        # Create the plot
                        fig, ax = plt.subplots(figsize=(10, 6))
                        ax.bar(top10['date'].dt.strftime('%Y-%m-%d'), top10['amount'], color='skyblue')

                        # Add labels and title
                        ax.set_title("Top 10 Expenses (Amount Between 3000 and 7000)", fontsize=16)
                        ax.set_xlabel("Date", fontsize=12)
                        ax.set_ylabel("Amount (INR)", fontsize=12)
                        ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for readability
                        ax.grid(True, linestyle='--', alpha=0.6)

                        # Render the chart in Streamlit
                        st.pyplot(fig)
                else:
                        st.warning("No data found for the specified range of amounts.")
                        
                st.write("  Amount between 4000 and 5000 with cashback more than average")



                sql5="""SELECT COUNT(amount) AS total_amount, AVG(cashback) 
                FROM combined_expenses
                WHERE amount BETWEEN 4000 AND 5000 
                AND cashback > (SELECT AVG(cashback) FROM combined_expenses);
                """
                data5=pd.read_sql(sql5,conn)
                st.dataframe(data5)
 
    # SQL query to fetch data
                query_new = """
                    SELECT amount, date 
                    FROM combined_expenses
                    WHERE date BETWEEN '2024-08-01' AND '2024-08-31';
                """
                
                # Execute the SQL query and load data into a DataFrame
                query = pd.read_sql(query_new, conn)
                
                # Fetch the top 15 rows from the query result
                top15 = query.head(15)
                
                # Display the top 15 rows as a table in Streamlit
                st.write("Top 15 expenses for August 2024")
                st.table(top15)
                
                # Convert the 'date' column to datetime format
                query['date'] = pd.to_datetime(query['date'])
                
                # Plotting the 'amount' against 'date'
                plt.figure(figsize=(10, 6))
                plt.plot(query['date'], query['amount'], marker='o', color='b', label='Expense Amount')

                # Adding labels and title
                plt.title('Expense Amount Over Time (August 2024)', fontsize=14)
                plt.xlabel('Date', fontsize=12)
                plt.ylabel('Amount', fontsize=12)
                plt.xticks(rotation=45)  # Rotate x-axis labels for readability
                plt.grid(True)
                plt.legend()

                # Display the plot in Streamlit
                st.pyplot(plt)
                
                
    
def last_page():
    st.title(" Summary and Feedback")
    
    # Simple introduction text
    st.write("Thank you for using the Personal Finance and Expense Tracker!")
    st.write("We hope the app helped you track your expenses efficiently.")

    # Display key statistics (placeholder values)
    st.write("### Key Statistics:")
    st.write("- **Total Expenses**: ₹ X")
    st.write("- **Average Monthly Expenses**: ₹ Y")
    st.write("- **Highest Expense**: ₹ Z")

    # User feedback section
    st.write("### We Value Your Feedback!")
    feedback = st.text_area("Please share your feedback:")
    
    if feedback:
        st.write("Thank you for your feedback!")
    
    # Contact details
    st.write("### Contact Us:")
    st.write("Email: support@financeapp.com")

    st.write("Thank you for using our tracker!")

 
def main():
    # Define the `page` variable using a selectbox
    page = st.sidebar.selectbox(
        "Navigate to:",
        ["Home", "Page 1: Overview and Expenses","Last Page"]
    )

    # Render the correct page based on the selected value
    if page == "Home":
        home_page()
    elif page == "Page 1: Overview and Expenses":
        page1()
    else:
        last_page()

# Run the app
if __name__ == "__main__":
    main()
    

