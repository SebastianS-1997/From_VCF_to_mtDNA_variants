import pandas as pd

# Read the first file into a DataFrame
df1 = pd.read_excel(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Out_step_3\step_3_non_matching.xlsx")

# Read the second file into a DataFrame
df2 = pd.read_excel(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis/Database\MitImpact_db_3.1.0.xlsx")

# Merge the two DataFrames on the 'Pos_ref_alt' column
merged_df = pd.merge(df1, df2, on='Pos_ref_alt', how='left')

# Filter the merged DataFrame to find the unmatched rows from the first file
unmatched_df = merged_df[merged_df['Gene_symbol'].isnull()]

# Filter the merged DataFrame to find the matched rows from the first file
matched_df = merged_df[merged_df['Gene_symbol'].notnull()]

# Write both DataFrames to the same Excel file
with pd.ExcelWriter(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Out_step_4/out_step_4.xlsx") as writer:
    matched_df.to_excel(writer, sheet_name='matched', index=False)
    unmatched_df.to_excel(writer, sheet_name='unmatched', index=False)