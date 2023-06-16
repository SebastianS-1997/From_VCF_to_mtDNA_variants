# From VCF file to mtDNA variants analysis 


From VCF to mtDNA Variants is a simple Python project designed to extract mtDNA variants from a VCF file and filter them based on frequency in HelixMTdb (https://www.helix.com/pages/mitochondrial-variant-database), MITOMAP (https://www.mitomap.org/MITOMAP) and Mitimpact 3D (https://mitimpact.css-mendel.it/). The scripts provides an efficient way to analyse and process genetic variant data, allowing to focus on specific variants of interest.

# Features:
- Variant extraction: The script reads a VCF file and extracts relevant variant information including chromosome, position, reference allele, alternative allele, VAF and coverage.
- Frequency filtering: The extracted variants are filtered based on their frequency in the HelixMTdb database. The script uses this information to prioritise variants based on their prevalence in the population.
- Filtering for deleterious characters: Variants are filtered based on their confirmed pathogenic character based on Mitomap's Confirmed Pathogenic Mutations (https://www.mitomap.org/foswiki/bin/view/MITOMAP/ConfirmedMutations) and only for protein-coding gene prediction from Mitimpact 3D.
- Output: The filtered variants are saved in .xslx format.

# Dependencies:

This project depends on the following:

- Python (version 3.11)

Library for Python: 
- subprocess32 3.5.4
- pandas 2.0.1
- PyVCF 0.6.8 
- os3 0.1.2
- XlsxWriter 3.1.0

Please make sure you have these dependencies installed before running the script.

VCF file requirements

Reference genome: VCF files refer to a specific reference genome assembly. It is essential to ensure that the reference genome is:
- rCRS (NC_012920, https://www.ncbi.nlm.nih.gov/nuccore/251831106)
- hg38
- hs37d5
- hg19 Not acceptable

Versions: 
-	VCF 4.1, and VCF 4.2

# Limitation 

If you are not routinely analysing variants of mtDNA, we recommend using merged VCF files from a few samples to avoid sequencing artefacts or other problems.
