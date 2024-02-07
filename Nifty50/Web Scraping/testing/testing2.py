import csv
import json

# Read JSON file
with open("indicesHistory.json", "r") as file:
    json_data = file.read()

# Convert JSON to CSV
csv_data = []
index_close_records = json.loads(json_data)["data"]["indexCloseOnlineRecords"]
index_turnover_records = json.loads(json_data)["data"]["indexTurnoverRecords"]

for i in range(len(index_close_records)):
    close_record = index_close_records[i]
    records = index_turnover_records[i]
    timestamp = close_record["EOD_TIMESTAMP"]
    open_val = close_record["EOD_OPEN_INDEX_VAL"]
    high_val = close_record["EOD_HIGH_INDEX_VAL"]
    low_val = close_record["EOD_LOW_INDEX_VAL"]
    close_val = close_record["EOD_CLOSE_INDEX_VAL"]
    traded_qty = records["HIT_TRADED_QTY"]
    turnover = records["HIT_TURN_OVER"]
    csv_data.append([timestamp, open_val, high_val, low_val, close_val, traded_qty, turnover])

# Write CSV file
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "open", "high", "low", "close", "shares trades", "turnover in Cr"])
    writer.writerows(csv_data)
