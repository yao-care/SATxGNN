# SATxGNN - Saudi Arabia: Drug Repurposing

[![Website](https://img.shields.io/badge/Website-satxgnn.yao.care-blue)](https://satxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Drug repurposing predictions for Saudi Arabia SFDA-approved drugs using the TxGNN model.

## Disclaimer

- The results of this project are for research purposes only and do not constitute medical advice.
- Drug repurposing candidates require clinical validation before application.

## Project Overview

### Report Statistics

| Item | Count |
|------|------|
| **Drug Reports** | 808 |
| **Total Predictions** | 12,123,340 |
| **Unique Drugs** | 1,102 |
| **Unique Indications** | 17,041 |
| **DDI Data** | 302,516 |
| **DFI Data** | 857 |
| **DHI Data** | 35 |
| **DDSI Data** | 8,359 |
| **FHIR Resources** | 808 MK / 5,659 CUD |

### Evidence Level Distribution

| Evidence Level | Report Count | Description |
|---------|-------|------|
| **L1** | 0 | Multiple Phase 3 RCTs |
| **L2** | 0 | Single RCT or multiple Phase 2 |
| **L3** | 0 | Observational studies |
| **L4** | 0 | Preclinical / mechanistic studies |
| **L5** | 808 | Computational prediction only |

### By Source

| Source | Predictions |
|------|------|
| DL | 12,117,681 |
| KG + DL | 4,874 |
| KG | 785 |

### By Confidence

| Confidence | Predictions |
|------|------|
| very_high | 3,627 |
| high | 527,905 |
| medium | 1,008,316 |
| low | 10,583,492 |

---

## Prediction Methods

| Method | Speed | Accuracy | Requirements |
|------|------|--------|----------|
| Knowledge Graph | Fast (seconds) | Lower | No special requirements |
| Deep Learning | Slow (hours) | Higher | Conda + PyTorch + DGL |

### Knowledge Graph Method

```bash
uv run python scripts/run_kg_prediction.py
```

| Metric | Value |
|------|------|
| SFDA Total Drugs | 9,650 |
| Mapped to DrugBank | 6,904 (71.5%) |
| Repurposing Candidates | 5,659 |

### Deep Learning Method

```bash
conda activate txgnn
PYTHONPATH=src python -m satxgnn.predict.txgnn_model
```

| Metric | Value |
|------|------|
| Total DL Predictions | 2,169,966 |
| Unique Drugs | 1,102 |
| Unique Indications | 17,041 |

### Score Interpretation

The TxGNN score represents the model's confidence in a drug-disease pair, ranging from 0 to 1.

| Threshold | Meaning |
|-----|------|
| >= 0.9 | Very high confidence |
| >= 0.7 | High confidence |
| >= 0.5 | Moderate confidence |

#### Score Distribution

| Threshold | Meaning |
|-----|------|
| ≥ 0.9999 | Extremely high confidence, model's most confident predictions |
| ≥ 0.99 | Very high confidence, worth prioritizing for validation |
| ≥ 0.9 | High confidence |
| ≥ 0.5 | Moderate confidence (sigmoid decision boundary) |

#### Evidence Level Definitions

| Level | Definition | Clinical Significance |
|-----|------|---------|
| L1 | Phase 3 RCT or systematic review | Can support clinical use |
| L2 | Phase 2 RCT | Can consider for use |
| L3 | Phase 1 or observational study | Requires further evaluation |
| L4 | Case report or preclinical research | Not recommended yet |
| L5 | Computational prediction only, no clinical evidence | Requires further research |

#### Important Reminders

1. **High scores do not guarantee clinical efficacy: TxGNN scores are knowledge graph-based predictions that require clinical trial validation.**
2. **Low scores do not mean ineffective: The model may not have learned certain associations.**
3. **Recommended to use with validation pipeline: Use this project's tools to review clinical trials, literature, and other evidence.**

### Validation Pipeline

```mermaid
flowchart TD
    A["TxGNN Prediction Results"] --> B
    subgraph B["Step 1: DrugBundle Collector"]
        B1["Drug-level: SFDA, DDI, DrugBank"]
        B2["Indication-level: ClinicalTrials, PubMed, ICTRP"]
    end
    B --> |"drug_bundle.json"| C
    subgraph C["Step 2: Evidence Pack Generator"]
        C1["Programmatic data transfer (100%)"]
        C2["+ LLM Analysis (L1-L5)"]
    end
    C --> |"drug_evidence_pack.json/md"| D
    subgraph D["Step 3: Notes Writer"]
        D1["drug_pharmacist_notes.md"]
        D2["drug_sponsor_notes.md"]
    end
```

---

## Quick Start

### Step 1: Download Data

| File | Download |
|------|------|
| SFDA Data | [SFDA Open Data - Registered Human Drugs List](https://www.sfda.gov.sa/en/open-data) |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) |

### Step 2: Install Dependencies

```bash
uv sync
```

### Step 3: Process Drug Data

```bash
uv run python scripts/process_fda_data.py
```

### Step 4: Prepare Vocabulary Data

```bash
uv run python scripts/prepare_external_data.py
```

### Step 5: Run Knowledge Graph Prediction

```bash
uv run python scripts/run_kg_prediction.py
```

### Step 6: Set Up Deep Learning Environment

```bash
conda create -n txgnn python=3.11 -y
conda activate txgnn
pip install torch==2.2.2 torchvision==0.17.2
pip install dgl==1.1.3
pip install git+https://github.com/mims-harvard/TxGNN.git
pip install pandas tqdm pyyaml pydantic ogb
```

### Step 7: Run Deep Learning Prediction

```bash
conda activate txgnn
PYTHONPATH=src python -m satxgnn.predict.txgnn_model
```

---

## Resources

### TxGNN Core

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine, 2024
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org)

### Data Sources

| Category | Data | Source | Note |
|------|------|------|------|
| **Drug Data** | SFDA | [SFDA Open Data - Registered Human Drugs List](https://www.sfda.gov.sa/en/open-data) | Saudi Arabia |
| **Knowledge Graph** | TxGNN KG | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) | 17,080 diseases, 7,957 drugs |
| **Drug Database** | DrugBank | [DrugBank](https://go.drugbank.com/) | Drug ingredient mapping |
| **Drug Interactions** | DDInter 2.0 | [DDInter](https://ddinter2.scbdd.com/) | DDI pairs |
| **Drug Interactions** | Guide to PHARMACOLOGY | [IUPHAR/BPS](https://www.guidetopharmacology.org/) | Approved drug interactions |
| **Clinical Trials** | ClinicalTrials.gov | [CT.gov API v2](https://clinicaltrials.gov/data-api/api) | Clinical trials registry |
| **Clinical Trials** | WHO ICTRP | [ICTRP API](https://apps.who.int/trialsearch/api/v1/search) | International clinical trials platform |
| **Literature** | PubMed | [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/) | Medical literature search |
| **Name Mapping** | RxNorm | [RxNav API](https://rxnav.nlm.nih.gov/REST) | Drug name standardization bridge |
| **Name Mapping** | PubChem | [PUG-REST API](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | Chemical substance synonym lookup |
| **Name Mapping** | ChEMBL | [ChEMBL API](https://www.ebi.ac.uk/chembl/api/data) | Bioactivity database mapping |
| **Standards** | FHIR R4 | [HL7 FHIR](http://hl7.org/fhir/) | MedicationKnowledge, ClinicalUseDefinition |
| **Standards** | SMART on FHIR | [SMART Health IT](https://smarthealthit.org/) | EHR integration, OAuth 2.0 + PKCE |

### Model Downloads

| File | Download | Note |
|------|------|------|
| Pretrained Model | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | model_ckpt.zip |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | Node Data |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | Knowledge Graph Data |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | Edge Data (DL) |

## Project Introduction

### Directory Structure

```
SATxGNN/
├── README.md
├── CLAUDE.md
├── pyproject.toml
│
├── config/
│   └── fields.yaml
│
├── data/
│   ├── kg.csv
│   ├── node.csv
│   ├── edges.csv
│   ├── raw/
│   ├── external/
│   ├── processed/
│   │   ├── drug_mapping.csv
│   │   ├── repurposing_candidates.csv
│   │   ├── txgnn_dl_predictions.csv.gz
│   │   └── integration_stats.json
│   ├── bundles/
│   └── collected/
│
├── src/satxgnn/
│   ├── data/
│   │   └── loader.py
│   ├── mapping/
│   │   ├── normalizer.py
│   │   ├── drugbank_mapper.py
│   │   └── disease_mapper.py
│   ├── predict/
│   │   ├── repurposing.py
│   │   └── txgnn_model.py
│   ├── collectors/
│   └── paths.py
│
├── scripts/
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   └── integrate_predictions.py
│
├── docs/
│   ├── _drugs/
│   ├── fhir/
│   │   ├── MedicationKnowledge/
│   │   └── ClinicalUseDefinition/
│   └── smart/
│
├── model_ckpt/
└── tests/
```

**Legend**: 🔵 Project development | 🟢 Local data | 🟡 TxGNN data | 🟠 Validation pipeline

### Data Flow

```mermaid
flowchart TD
    FDA["SFDA Data"] --> proc["process_fda_data.py"]
    TxGNN["TxGNN Data"] --> prep["prepare_external_data.py"]

    proc --> json["sa_fda_drugs.json"]
    prep --> ext["data/external/"]

    json --> norm["normalizer.py"]
    ext --> norm

    norm --> drug_map["drug_mapping.csv"]
    drug_map --> ind_map["indication_mapping.csv"]

    ind_map --> KG["Knowledge Graph"]
    ind_map --> DL["Deep Learning"]

    KG --> kg_out["repurposing_candidates.csv"]
    DL --> dl_out["txgnn_dl_predictions.csv"]
```

---

## Citation

If you use this dataset or software, please cite:

```bibtex
@software{satxgnn2026,
  author       = {Yao.Care},
  title        = {SATxGNN: Drug Repurposing Validation Reports for Saudi Arabia SFDA Drugs},
  year         = 2026,
  publisher    = {GitHub},
  url          = {https://github.com/yao-care/SATxGNN}
}
```

Also cite the original TxGNN paper:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and Chandak, Payal and Wang, Qianwen and Haber, Shreyas and Zitnik, Marinka},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```
