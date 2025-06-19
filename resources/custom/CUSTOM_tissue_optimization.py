import argparse
from custom import TissueOptimizer

# Tissue list for validation
tissue_list = [
    "Lung", "Breast", "Skin", "Spleen", "Heart", "Liver", "Salivarygland",
    "Muscle", "Tonsil", "Smallintestine", "Placenta", "Appendices", "Testis",
    "Rectum", "Urinarybladder", "Prostate", "Esophagus", "Kidney", "Thyroid",
    "Lymphnode", "Artery", "Brain", "Nerve", "Gallbladder", "Uterus",
    "Pituitary", "Colon", "Vagina", "Duodenum", "Fat", "Stomach", "Adrenal",
    "Fallopiantube", "Smoothmuscle", "Pancreas", "Ovary"
]

def main():
    parser = argparse.ArgumentParser(description="Tissue-specific codon optimizer using CUSTOM")
    parser.add_argument("--seq", type=str, required=True, help="Amino acid sequence (e.g., eGFP)")
    parser.add_argument("--tissue", type=str, required=True, help="Target tissue name")
    args = parser.parse_args()

    egfp = args.seq.strip()
    tissue = args.tissue.strip()

    if tissue not in tissue_list:
        print(f"\nError: '{tissue}' is not in the supported tissue list.")
        return

    print(f"\nOptimizing for tissue: {tissue}...\n")

    # Run optimization
    opt = TissueOptimizer(tissue, n_pool=100)
    opt.optimize(egfp)

    # Select top optimized sequence
    best_seq = opt.select_best(
        by={"MFE": "min", "MFEini": "max", "CAI": "max", "CPB": "max", "ENC": "min"},
        homopolymers=7,
        top=1
    )
    print(f"Generated {len(opt.pool)} candidate sequences")
    print("\nTop optimized sequence:")
    if not best_seq.empty and "Sequence" in best_seq.columns:
        print(best_seq.iloc[0]["Sequence"])
    else:
        print("No optimized sequence found.")

if __name__ == "__main__":
    main()
