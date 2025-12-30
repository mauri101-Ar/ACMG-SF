# ACMG Secondary Findings (ACMG-SF) Repository

This repository maintains machine-readable (TSV) versions of the **American College of Medical Genetics and Genomics (ACMG)** recommendations for reporting of secondary findings in clinical exome and genome sequencing.

The goal is to provide structured data for bioinformatics pipelines, ensuring reproducibility and easy integration.

## Available Versions & References

The following table tracks the history of ACMG Secondary Findings (SF) lists, linking to the original policy statements and their respective machine-readable datasets in this repository.

| Version | Year | PubMed | TSV Data |
| :--- | :---: | :--- | :--- |
| **v3.3** | 2025 | [PMID: 37347242](https://pubmed.ncbi.nlm.nih.gov/40568962/) | [Download](./data/ACMG_SF_3.3.tsv) |
| **v3.2** | 2023 | [PMID: 37347242](https://pubmed.ncbi.nlm.nih.gov/37347242/) | [Download](./data/ACMG_SF_3.2.tsv) |
| **v3.1** | 2022 | [PMID: 35802134](https://pubmed.ncbi.nlm.nih.gov/35802134/) | [Download](./data/ACMG_SF_3.1.tsv) |
| **v3.0** | 2021 | [PMID: 34345026](https://pubmed.ncbi.nlm.nih.gov/34345026/) | [Download](./data/ACMG_SF_3.0.tsv) |
| **v2.0** | 2016 | [PMID: 28383573](https://pubmed.ncbi.nlm.nih.gov/28383573/) | [Download](./data/ACMG_SF_2.0.tsv) |
| **v1.0** | 2013 | [PMID: 23788249](https://pubmed.ncbi.nlm.nih.gov/23788249/) | [Download](./data/ACMG_SF_1.0.tsv) |

## Column Description

The TSV files follow this schema:

* **Phenotype:** The specific clinical condition or disease associated with the gene (e.g., "Familial Hypercholesterolemia", "Lynch Syndrome").
* **ACMG SF List Version:** Version of the guideline.
* **MIM Disorder:** OMIM ID for the associated phenotype.  
* **Gene:** Official HUGO Gene Symbol.  
* **HGNC_ID:** Stable identifier from HGNC (Essential for mapping).  
* **Inheritance:** Mode of inheritance (AD: Autosomal Dominant, AR: Autosomal Recessive, etc.).  
* **Variants to Report:** Specific criteria for variant reporting (e.g., "LP/P", "Truncating only").  

## Usage in Pipelines

You can pull a specific version using `wget` or `curl` pointing to the raw file:

```bash
# Example: Pulling v3.3
wget https://raw.githubusercontent.com/mauri101-Ar/ACMG-SF/main/data/ACMG_SF_3.3.tsv
```

## Data Curation Methodology

To ensure interoperability and stability within bioinformatics pipelines, this repository does not only provide information extracted from original publications; it also enriches the datasets with stable identifiers.

### HGNC ID Enrichment

Gene symbols are volatile and change over time. To mitigate this and ensure data longevity, each list is programmatically processed using the internal `enrich_acmg.py` script.

**Enrichment Process:**  

1. **Source of Truth:** We use the official **HGNC REST API** (genenames.org) to map each symbol to its unique and permanent `HGNC_ID`.
2. **Symbol Validation:** The process ensures that the symbol provided in the TSV matches the current *Approved Symbol* designated by HGNC.
3. **Automation:** The script reads the Gene Symbol (extracted from the ACMG policy statements) and generates the final enriched TSV by inserting the `HGNC_ID` column specifically between the `Gene` and `Inheritance` columns.

### Internal Script Usage

While the TSV files in the `data/` directory are already processed and ready for use, the script is included for auditing purposes or to process future updates (e.g., v3.4, v4.0):

```bash
# Syntax
python scripts/enrich_acmg.py <raw_input.tsv> <enriched_output.tsv>
```

## Citation

Please cite the original ACMG publications listed in the table above when using these lists in clinical reports.
