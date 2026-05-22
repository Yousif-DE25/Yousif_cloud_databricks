from pyspark import pipelines as dp

BASE_DIR = "/Volumes/supply_chain/default/raw"

schema = (
    spark.read.format("csv")
    .options(header=True, inferSchema=True)
    .load(f"{BASE_DIR}/data/DataCoSupplyChainDataset.csv")
    .schema
)


@dp.table(
    name="supply_chain.bronze.raw_supply_chain",
    comment="Raw data from the DataCoSupplyChainDataset.csv file",
    table_properties={
        "delta.columnMapping.mode": "name"
    })

def raw_supply_chain():
    return (
        spark.readStream.format("csv")
        .options(header=True, encoding="UTF-8")
        .schema(schema)
        .load(f"{BASE_DIR}/data")
    )
