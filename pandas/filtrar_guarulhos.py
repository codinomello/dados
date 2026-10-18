import pandas as pd

INPUT_FILE = "data/perfil_eleitorado_ATUAL.csv"
OUTPUT_FILE = "eleitores_guarulhos.txt"

CHUNK_SIZE = 100_000

def main():

    print("🚀 Starting processing...")

    chunks = pd.read_csv(
        INPUT_FILE,
        sep=";",
        encoding="latin1",
        chunksize=CHUNK_SIZE,
        dtype=str
    )

    total = 0

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:

        for i, chunk in enumerate(chunks):

            print(f"📦 Processing chunk {i + 1}...")

            # Filter only Guarulhos
            filtered = chunk[chunk["NM_MUNICIPIO"] == "GUARULHOS"]

            if not filtered.empty:

                # Write to file
                filtered.to_csv(
                    out_file,
                    index=False,
                    header=(total == 0),  # write header only once
                    sep=";"
                )

                total += len(filtered)

    print("✅ Done!")
    print(f"📊 Total voters from Guarulhos: {total}")
    print(f"📄 Output file: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()