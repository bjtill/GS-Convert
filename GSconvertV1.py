#!/usr/bin/env python3
#BT November 25, 2025
#Built as a module for downstream analysis
"""
Convert GenomeStudio Full Data Table Format into a three column genotype format
Output format: MarkerName SampleName Genotype 
"""

import sys

def convert_genotypes(input_file, output_file):
    """
    Convert genotype data to three-column format.
    
    Args:
        input_file: Path to input tab-delimited file
        output_file: Path to output file
    """
    with open(input_file, 'r') as infile:
        # Read header line
        header = infile.readline().strip().split('\t')
        
        # Find marker name column (column 2, index 1)
        marker_col_idx = 1
        
        # Find all .GType columns and extract sample names
        gtype_columns = []
        for idx, col_name in enumerate(header):
            if col_name.endswith('.GType'):
                # Extract sample name by removing .GType suffix
                sample_name = col_name.replace('.GType', '')
                gtype_columns.append((idx, sample_name))
        
        print(f"Found {len(gtype_columns)} samples with genotype data")
        
        # Process data rows
        with open(output_file, 'w') as outfile:
            for line in infile:
                if not line.strip():
                    continue
                    
                fields = line.strip().split('\t')
                marker_name = fields[marker_col_idx]
                
                # Extract genotype for each sample
                for gtype_idx, sample_name in gtype_columns:
                    if gtype_idx < len(fields):
                        genotype = fields[gtype_idx]
                        outfile.write(f"{marker_name}\t{sample_name}\t{genotype}\n")
    
    print(f"Conversion complete. Output written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 convert_genotypes.py <input_file> <output_file>")
        print("Example: python3 convert_genotypes.py example.text output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_genotypes(input_file, output_file)
