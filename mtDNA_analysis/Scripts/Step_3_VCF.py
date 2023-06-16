import pandas as pd
import xlsxwriter

# Read the first Excel file
df1 = pd.read_excel(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Out_step_1\Step_1.xlsx")

# Read the second Excel file
df2 = pd.read_excel(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis/Database\HelixMTdb.xlsx")

# Merge the two dataframes on the "Pos_ref_alt" column, keeping only the common values
merged_df = pd.merge(df1, df2, on="Pos_ref_alt", how="inner")

# Find the "Pos_ref_alt" values that occur only once in the data
non_matching_df_unique = df1[~df1["Pos_ref_alt"].isin(df2["Pos_ref_alt"])].copy()
non_matching_df_unique.drop_duplicates(subset="Pos_ref_alt", keep=False, inplace=True)

# Find the "Pos_ref_alt" values that occur more than once in the data
non_matching_df_multi = df1[~df1["Pos_ref_alt"].isin(df2["Pos_ref_alt"])].copy()
non_matching_df_multi = non_matching_df_multi[non_matching_df_multi["Pos_ref_alt"].duplicated(keep=False)]

# Select the columns to include in the non-matching dataframes
non_matching_cols = ["Pos_ref_alt", "SampleID", "Variant-Level", "Coverage-Total"]

# Filter the non-matching dataframes to only include the selected columns
non_matching_df_unique = non_matching_df_unique[non_matching_cols]
non_matching_df_multi = non_matching_df_multi[non_matching_cols]

# Rename the "Coverage-Total" column to "Coverage-Total for Pos_ref_alt" for both dataframes
non_matching_df_unique = non_matching_df_unique.rename(columns={"Coverage-Total": "Coverage-Total for Pos_ref_alt"})
non_matching_df_multi = non_matching_df_multi.rename(columns={"Coverage-Total": "Coverage-Total for Pos_ref_alt"})

# Create a Pandas Excel writer object
writer = pd.ExcelWriter(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Out_step_3\step_3_non_matching.xlsx", engine="xlsxwriter")

# Write the "Unique" sheet to the Excel file
non_matching_df_unique.to_excel(writer, sheet_name="Unique", index=False)

# Write the "Multi" sheet to the Excel file
non_matching_df_multi.to_excel(writer, sheet_name="Multi", index=False)

# Save the merged dataframe and the non-matching dataframe to separate Excel files
merged_df.to_excel(r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Out_step_3\step_3_matching.xlsx", index=False)

# Close the Excel writer object to save the Excel file
writer.close()
