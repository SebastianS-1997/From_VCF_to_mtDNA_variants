import pandas as pd
import vcf
import os

# set the paths to the input VCF file and the output Excel file
input_vcf_path = r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis/Input/input.vcf"
output_excel_path = r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis/Out_step_1\Step_1.xlsx"

# open the VCF file
vcf_reader = vcf.Reader(open(input_vcf_path, 'r'))

# create empty lists to hold the variant data
variant_data = []

# iterate over each variant in the VCF file
for record in vcf_reader:
    # check if the variant is on the MT chromosome
    if record.CHROM == "MT":
        # extract the variant data for each sample
        for sample in record.samples:
            pos_ref_alt = f"{record.POS}:{record.REF}:{','.join(map(str, record.ALT))}"
            sample_id = sample.sample
            vaf = sample.data.VAF
            dp = sample.data.DP
            # add the variant data to the list only if Coverage-Total value exists
            if dp is not None:
                variant_data.append([pos_ref_alt, sample_id, vaf, dp])

# create a DataFrame from the variant data
df = pd.DataFrame(variant_data, columns=["Pos_ref_alt", "SampleID", "Variant-Level", "Coverage-Total"])

# create the output directory if it doesn't exist
output_dir = os.path.dirname(output_excel_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# write the DataFrame to the output Excel file
df.to_excel(output_excel_path, index=False)

