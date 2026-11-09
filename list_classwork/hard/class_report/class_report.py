def letter(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
def ranking(records):
    ordered = sorted(records, key=lambda r: (-r[1], r[0]))
    return [name for name, score in ordered]


def report(records):
    ordered = sorted(records, key=lambda r: (-r[1], r[0]))
    lines = []
    for name, score in ordered:
        place = 1 + sum(other_score > score for _, other_score in records)
        lines.append(f"{place}. {name} - {score} ({letter(score)})")

    return "\n".join(lines)
def failed(records):
    return [name for name, score in records if letter(score) == "F"]