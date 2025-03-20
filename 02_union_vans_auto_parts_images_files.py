# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:45:44 2025

@author: LKOSINSKI
"""

import pandas as pd
import glob
import os

# Set file directory
directory = 'C:/Users/lkosinski/OneDrive - Bentley University/Documents/My MSBA/MA 795 Spring 2025/Vans Auto Parts Images'

def union_csv_files(directory, output_filename="vans_auto_parts_images.csv"):
    all_filenames = glob.glob(os.path.join(directory, "*.csv"))
    all_df = []
    for f in all_filenames:
        df = pd.read_csv(f)
        all_df.append(df)
    
    combined_df = pd.concat(all_df, ignore_index=True)
    combined_df.to_csv(output_filename, index=False)
    print(f"Successfully combined all CSV files in '{directory}' to '{output_filename}'")

# Example usage:
directory_path = directory
union_csv_files(directory_path)