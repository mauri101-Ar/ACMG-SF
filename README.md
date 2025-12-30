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
| **v3.0** | 2021 | [PMID: 34012068](https://pubmed.ncbi.nlm.nih.gov/34012068/) | [Download](./data/ACMG_SF_3.0.tsv) |
| **v2.0** | 2016 | [PMID: 27854360](https://pubmed.ncbi.nlm.nih.gov/27854360/) | [Download](./data/ACMG_SF_2.0.tsv) |
| **v1.0** | 2013 | [PMID: 23788249](https://pubmed.ncbi.nlm.nih.gov/23788249/) | [Download](./data/ACMG_SF_1.0.tsv) |

## Column Description

The TSV files follow this schema:

* **Phenotype:** The specific clinical condition or disease associated with the gene (e.g., "Familial Hypercholesterolemia", "Lynch Syndrome").  
* **Gene:** Official HUGO Gene Symbol.  
* **HGNC_ID:** Stable identifier from HGNC (Essential for mapping).  
* **MIM Disorder:** OMIM ID for the associated phenotype.  
* **Inheritance:** Mode of inheritance (AD: Autosomal Dominant, AR: Autosomal Recessive, etc.).  
* **Variants to Report:** Specific criteria for variant reporting (e.g., "LP/P", "Truncating only").  
* **ACMG SF List Version:** Version of the guideline.  

## Usage in Pipelines

You can pull a specific version using `wget` or `curl` pointing to the raw file:

```bash
# Example: Pulling v3.2
wget [https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/v3.2/data/ACMG_SF_v3.2.tsv](https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/v3.2/data/ACMG_SF_v3.2.tsv)
```

## Citation
Please cite the original ACMG publications listed in the table above when using these lists in clinical reports.
