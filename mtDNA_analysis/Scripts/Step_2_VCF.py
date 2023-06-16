import pandas as pd

# Read the first Excel file
df1 = pd.read_excel(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Out_step_1/Step_1.xlsx")

# Read the second Excel file
df2 = pd.read_excel(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis/Database/MITOMAP.xlsx")

# Merge the two dataframes on the "Pos_ref_alt" column, keeping only the common values
merged_df = pd.merge(df1, df2, on="Pos_ref_alt", how="inner")

# Save the merged dataframe to a new Excel file
merged_df.to_excel(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Out_step_2/step_2.xlsx", index=False)