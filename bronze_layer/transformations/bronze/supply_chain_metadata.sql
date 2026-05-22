CREATE OR REFRESH STREAMING TABLE supply_chain.bronze.raw_access_metadata
COMMENT "Raw metadata for DataCo" AS
SELECT
* FROM
STREAM read_files("/Volumes/supply_chain/default/raw/metadata",
format => "csv",
header => true,
inferSchema => true
)