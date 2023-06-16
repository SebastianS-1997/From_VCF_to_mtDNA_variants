import subprocess

# Define the path to the scripts
script1_path = r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis/Scripts\Step_1_VCF.py"
script2_path = r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Scripts\Step_2_VCF.py"
script3_path = r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Scripts\Step_3_VCF.py"
script4_path = r"C:\Users\sebas\OneDrive\Pulpit\mtDNA_analysis\Scripts\Step_4_VCF.py"

# Run each script using the subprocess module
subprocess.run(["python", script1_path])
subprocess.run(["python", script2_path])
subprocess.run(["python", script3_path])
subprocess.run(["python", script4_path])