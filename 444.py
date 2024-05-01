import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming the data has already been loaded somewhere in the script
# For example:
def load_csv_file(file_path, encoding='utf-8'):
    try:
        return pd.read_csv(file_path, encoding=encoding)
    except UnicodeDecodeError as e:
        st.error(f"Failed to load file {file_path} with encoding {encoding}: {e}")
        return None

# Example usage in your app
salary_df = load_csv_file(r'C:\Users\user\Desktop\Ziyi_Wang_Proj2\nba_2022-23_all_stats_with_salary.csv', 'ISO-8859-1')
final_df = load_csv_file(r'C:\Users\user\Desktop\Ziyi_Wang_Proj2\final_merged_data.csv', 'ISO-8859-1')
def load_csv_file(file_path):
    encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            return pd.read_csv(file_path, encoding=encoding)
        except UnicodeDecodeError:
            continue
    st.error(f"All encodings failed for file {file_path}. Check the file encoding.")
    return None



def display_correlation():
    # Ensure 'final_df' is the DataFrame you are referring to
    if 'PTS_x' in final_df.columns:
        corr = final_df[['PTS_x', 'TRB_x', 'AST_x', 'FG%_x', 'WS_x', 'WS/48_x', 'Salary']].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation between Performance Metrics and Salary')
        st.pyplot(plt)
    else:
        st.error('Required columns are not present in the DataFrame.')


def display_violin_plot():
        #print(final_df.columns)
    # Define bins and labels for the points per game categories
        bins = [0, 10, 20, 30, 40]
        labels = ['0-10', '11-20', '21-30', '31-40']
        #final_df.iloc[:, 0] #yes
        print(type(final_df))

        print('FUCKKKKKKK')
        print(final_df['PTS_x'])
        temp = final_df.iloc[:,10]
        print('this is still good')
        final_df['PTS_x_category'] = pd.cut(temp, bins=bins, labels=labels, include_lowest=True)
        print('fuck222222222222222222')
        plt.figure(figsize=(12, 8))
        sns.violinplot(x='PTS_x_category', y='Salary', data=final_df)
        plt.title('Violin Plot of Salary Distribution Across Points Per Game Categories')
        plt.xlabel('Points Per Game')
        plt.ylabel('Salary')

        st.pyplot(plt)



def main():
    st.sidebar.title("Analysis Part")
    selected_page = st.sidebar.radio("Go to", ["Home", "NBA Player salary VS NBA player performance",
                                               "LeBron James' Three-Pointers vs Total Points Analysis"])

    if selected_page == "Home":
        home_page()
    elif selected_page == "NBA Player salary VS NBA player performance":
        display_violin_plot()
        display_correlation()


def home_page():
    st.title("Welcome to NBA Analysis App")
    st.write("Select an option from the sidebar to analyze NBA basketball.")


if __name__ == "__main__":
    main()

