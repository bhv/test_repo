# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "polars>=1.41.2",
# ]
# ///
import polars as pl

def main():
    df = pl.DataFrame(
    {
        "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
        "birthdate": [
            "2004-09-15",
            "2004-09-15",
            "2004-09-15",
            "2004-09-15",
        ],
        "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
        "height": [1.56, 1.77, 1.65, 1.75],  # (m)
    }
)

    print(df)

if __name__ == '__main__':
    main()