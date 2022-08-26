from datetime import datetime

# From: https://github.com/vagabond-systems/forage-lyft-task-2-model-answer/blob/main/utils.py
def add_years_to_date(original_date: datetime, years_to_add: int) -> datetime:
    result = original_date.replace(year=original_date.year + years_to_add)
    return result
