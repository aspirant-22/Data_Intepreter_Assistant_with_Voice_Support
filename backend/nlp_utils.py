def extract_region_and_month(text):
    regions = ['north', 'south', 'east', 'west']
    months = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']

    text = text.lower()
    region = next((r for r in regions if r in text), None)
    month = next((m for m in months if m in text), None)

    return region.capitalize() if region else None, month.capitalize() if month else None
