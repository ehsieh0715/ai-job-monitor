"""Shared evaluation contract for pre-sync checks and Sheet planning."""
import math
from schema import SCORED_COLUMNS

NEEDS_JD = '未評分／待補 JD'


def validate_evaluations(records):
    checked, seen = [], set()
    for original in records:
        if not set(SCORED_COLUMNS) <= set(original):
            raise ValueError('Missing required evaluation columns')
        row = {k: ('' if v is None or isinstance(v, float) and math.isnan(v) else v)
               for k, v in original.items()}
        id = str(row['job_id'])
        if not id.strip() or id != id.strip() or id in seen:
            raise ValueError('Missing, padded or duplicate job_id')
        seen.add(id)
        if not isinstance(row['match_summary'], str) or not row['match_summary'].strip():
            raise ValueError('Every result needs a nonempty summary or missing-JD explanation')
        if row['recommendation'] == NEEDS_JD:
            if str(row['match_score']).strip():
                raise ValueError('Missing-JD results must have a blank score')
        else:
            if isinstance(row['match_score'], bool):
                raise ValueError('Invalid match_score')
            try: score = float(row['match_score'])
            except (ValueError, TypeError): raise ValueError('Invalid match_score') from None
            if not math.isfinite(score) or not score.is_integer() or not 0 <= score <= 100:
                raise ValueError('match_score must be an integer 0–100')
            label = 'Strong Apply' if score >= 85 else 'Apply' if score >= 70 else 'Consider' if score >= 55 else 'Skip'
            if row['recommendation'] != label:
                raise ValueError('Score/recommendation disagreement')
        checked.append(row)
    return checked
