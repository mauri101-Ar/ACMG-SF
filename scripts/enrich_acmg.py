"""
ACMG-SF TSV Enriched: HGNC ID Fetcher
This script adds the HGNC_ID to an ACMG Secondary Findings TSV file.
Usage: python enrich_acmg.py input.tsv output.tsv
"""

import argparse
import sys
import time
import pandas as pd
import requests
from tqdm import tqdm


def get_hgnc_id(gene_symbol: str) -> str:
    """
    Query the HGNC REST API to retrieve the unique HGNC ID for a gene.

    Args:
        gene_symbol: The official gene symbol to search for.

    Returns:
        The HGNC ID (e.g., 'HGNC:1100') if a unique approved match
        is found, otherwise returns 'NOT_FOUND'.
    """
    url = f"https://rest.genenames.org/fetch/symbol/{gene_symbol}"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        docs = data.get('response', {}).get('docs', [])

        if not docs:
            return "na"  # No matches found

        # Ensure we only pick the record that matches the symbol exactly
        for doc in docs:
            if doc.get('symbol') == gene_symbol:
                return doc.get('hgnc_id')
        return "na"

    except requests.exceptions.RequestException as err:
        print(f"Error connecting to HGNC API for {gene_symbol}: {err}")
        return "API_ERROR"


def enrich_acmg_tsv(input_path: str, output_path: str):
    """
    Reads the ACMG TSV, fetches HGNC IDs, and inserts them into the
    specified column position between 'Gene' and 'Inheritance'.
    """
    try:
        # Load the TSV file
        df = pd.read_csv(input_path, sep='\t')

        # Validate required columns exist
        if 'Gene' not in df.columns or 'Inheritance' not in df.columns:
            print("Error: Input TSV must contain 'Gene' and 'Inheritance' columns.")
            sys.exit(1)

        print(f"Processing {len(df)} genes from {input_path}...")

        hgnc_ids = []
        for symbol in tqdm(df['Gene'], desc="Fetching HGNC IDs", unit="gene"):
            clean_symbol = str(symbol).strip()
            tqdm.write(f"Fetching ID for: {clean_symbol}...")
            hgnc_id = get_hgnc_id(clean_symbol)
            if hgnc_id == "na":
                tqdm.write(f"WARNING: No HGNC ID found for: {clean_symbol}")
            else:
                tqdm.write(f"Found HGNC ID for {clean_symbol}: {hgnc_id}")
            hgnc_ids.append(hgnc_id)
            time.sleep(0.2)  # Rate limiting

        # Resolve column index safely for Pylance/Type Checking
        gene_loc = df.columns.get_loc('Gene')

        if isinstance(gene_loc, int):
            insertion_idx = gene_loc + 1
        else:
            # If multiple columns match, get_loc returns a slice or array
            # We take the start of the first occurrence
            insertion_idx = getattr(gene_loc, 'start', 0) + 1

        df.insert(loc=insertion_idx, column='HGNC_ID', value=hgnc_ids)

        # Sort by 'Gene' column
        df.sort_values(by='Gene', inplace=True)

        # Save the enriched file
        df.to_csv(output_path, sep='\t', index=False)
        print(f"\nSuccess! Enriched file saved to: {output_path}")

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """Entry point for the script using terminal arguments."""
    parser = argparse.ArgumentParser(
        description="Enrich ACMG-SF TSV files with HGNC IDs."
    )
    parser.add_argument(
        "input",
        help="Path to the source TSV file (e.g., ACMG_SF_3.2.tsv)"
    )
    parser.add_argument(
        "output",
        help="Path where the enriched TSV will be saved"
    )

    args = parser.parse_args()
    enrich_acmg_tsv(args.input, args.output)


if __name__ == "__main__":
    main()
