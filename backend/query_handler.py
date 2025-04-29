import json
from nlp_utils import extract_region_and_month

def handle_query(query):
    region, month = extract_region_and_month(query)
    if not region or not month:
        return "Sorry, I couldn't understand your question. Please mention region and month."

    with open('sales_data.json') as f:

        data = json.load(f)

    for record in data:
        if record['region'] == region and record['month'] == month:
            sales = record['sales']
            target = record['target']
            diff = sales - target
            status = "above" if diff > 0 else "below"
            return f"In {month}, the {region} region had sales of ${sales:,}, which is ${abs(diff):,} {status} the target of ${target:,}."

    return f"No data found for {region} region in {month}."
