# VaxLab

<img src="https://github.com/ChangLabSNU/VaxLab/blob/main/logo/VaxLab_octopus.png?raw=true" height="240" align="right">

**VaxLab** is an integrated platform for designing optimized mRNA vaccine candidates. This user-friendly tool guides researchers through the complete process of mRNA vaccine design, from antigen input to generating optimized sequences and evaluation.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ChangLabSNU/VaxLab/blob/main/VaxLab.ipynb)

## 🎯 Key Features

- **Multiple Optimization Strategies**: Choose from LinearDesign, CodonBERT, Simple Codon Optimizer, or tissue-specific CUSTOM optimization
- **Comprehensive UTR Library**: Pre-validated 5' and 3' UTRs from successful commercial vaccines (Pfizer/BioNTech, Moderna)
- **Custom UTR Generation**: Generate optimized 5' UTRs using Optimus 5-Prime
- **Interactive Visualization**: Explore your mRNA construct with an integrated sequence editor and structure viewer
- **Quality Assessment**: Automated generation of comprehensive optimization reports
- **No Coding Required**: User-friendly interface accessible to researchers without programming experience

## 🚀 Quick Start
1. Click the "[Open in Colab](https://colab.research.google.com/github/ChangLabSNU/VaxLab/blob/main/VaxLab.ipynb)" badge above
2. Check the "Example Run" box to test with sample data
3. Click `Runtime` → `Run all`
4. Observe the optimization process with NanoLuciferase sequence (~1 minute)

## 📋 Workflow Overview

VaxLab guides you through four simple steps:

### 1️⃣ **Name Your Sequence**
Enter a unique identifier for your mRNA construct (e.g., `SARS-CoV-2_Spike`, `mGFP`)

### 2️⃣ **Input Your Antigen**
- **Protein sequences**: Single-letter amino acid code (ACDEFGHIKLMNPQRSTVWY)
- **DNA/RNA sequences**: Nucleotide sequences (automatically translated)

### 3️⃣ **Choose CDS Optimization Strategy**
- **LinearDesign**: Balances mRNA structure and codon optimization
- **CodonBERT**: AI-based deep learning approach
- **Simple Codon Optimizer**: Frequency-based codon optimization
- **CUSTOM**: Tissue-specific optimization (36 human tissues available)

### 4️⃣ **Select UTR Sequences**
- **5' UTR**: Choose from proven vaccine UTRs or generate custom sequences by using Optimus 5-Prime
- **3' UTR**: Choose from proven vaccine UTRs
- Option to input your own custom UTR sequences


## 📊 Output and Analysis

### Interactive Results
- **Sequence Editor**: Color-coded visualization of 5' UTR, CDS, and 3' UTR regions
- **Structure Viewer**: Interactive RNA secondary structure with folding energy
- **Quality Report**: Comprehensive analysis with optimization metrics

### Key Metrics in Quality Report
- **Codon Adaptation Index (CAI)**: Codon usage optimization score
- **GC Content**: Sequence composition analysis
- **Minimum Free Energy (MFE)**: RNA structure stability
- **DegScore**: Predicted mRNA degradation score ([Leppek et al., 2022](https://doi.org/10.1038/s41467-022-28776-w))
- **Repeat Analysis**: Detection of problematic sequences

### Downloadable Files
- **FASTA/GenBank**: Optimized sequence
- **HTML**: Quality report
- **XLSX**: Ready-to-use synthesis order form

## ⏱️ Performance

- **Typical runtime**: 1-3 minutes for average proteins (300-500 amino acids)

## 🎯 Applications

- **mRNA Vaccines**: SARS-CoV-2, influenza, cancer antigens
- **Therapeutic Proteins**: Antibodies, enzymes, hormones
- **Research Tools**: Reporter proteins, research antigens
- **Comparative Studies**: Multiple optimization strategy evaluation

## 📚 Citation

If you use VaxLab in your research, please cite:

```
A pre-print is going to be uploaded soon.
```


## 📞 Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/ChangLabSNU/VaxLab/issues)
- **Documentation**: Full user guide and FAQ available in the notebook
- **Contact**: [Chang Lab](https://qbio.io/), Seoul National University

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

VaxLab integrates several outstanding tools:
- [LinearDesign](https://github.com/LinearDesignSoftware/LinearDesign) - RNA structure and codon optimization
- [CodonBERT](https://github.com/FPPGroup/CodonBERT) - AI-based codon optimization
- [Simple Codon Optimizer](https://github.com/tdseher/simple-codon-optimizer) - Basic frequency-based codon optimization
- [CUSTOM](https://github.com/hexavier/CUSTOM) - Tissue-specific optimization for targeted expression
- [Optimus-5-Prime](https://github.com/castillohair/paper-5utr-design) - 5' UTR design
- [ViennaRNA](https://www.tbi.univie.ac.at/RNA/) - RNA structure prediction
- [OVE](https://github.com/TeselaGen/tg-oss/tree/master/packages/ove) - Teselagen's Open Source Vector Editor

---

**Developed by [Chang Lab](https://qbio.io/), Seoul National University** 