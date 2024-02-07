import csv
import json
import json

# JSON data
# Read JSON file
with open("indicesHistory.json", "r") as file:
    json_data = file.read()

    # Convert JSON to CSV
    csv_data = []
    for record in json.loads(json_data)["data"]["indexCloseOnlineRecords"]:
        csv_data.append([
            record["EOD_TIMESTAMP"],
            record["EOD_OPEN_INDEX_VAL"],
            record["EOD_HIGH_INDEX_VAL"],
            record["EOD_LOW_INDEX_VAL"],
            record["EOD_CLOSE_INDEX_VAL"],
            record["HIT_TRADED_QTY"],
            record["HIT_TURN_OVER"]
        ])
    for record in json.loads(json_data)["data"]["indexCloseOnlineRecords"]:
        csv_data.append([
            record["EOD_TIMESTAMP"],
            record["EOD_OPEN_INDEX_VAL"],
            record["EOD_HIGH_INDEX_VAL"],
            record["EOD_LOW_INDEX_VAL"],
            record["EOD_CLOSE_INDEX_VAL"],
            record["HIT_TRADED_QTY"],
            record["HIT_TURN_OVER"]
        ])

    # Write CSV file
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "open", "high", "low", "close", "shares trades", "turnover in Cr"])
        writer.writerows(csv_data)