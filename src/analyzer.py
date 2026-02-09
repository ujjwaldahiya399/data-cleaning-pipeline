from __future__ import annotations


def build_report_row(filename: str, before: dict, after: dict) -> dict:
    """
    Builds a single report row (dictionary)
    for one csv file.    :param filename: str
    :param before: dict
    :param after: dict
    :return: dict
    """
    return {
        "file":filename,
        # Before cleaning
        "rows_before":before.get("rows"),
        "columns_before":before.get("columns"),
        "missing_cells_before":before.get("missing_cells"),
        "duplicate_rows_before":before.get("duplicate_rows"),

        # After cleaning
        "rows_after":after.get("rows"),
        "columns_after":after.get("columns"),
        "missing_cells_after":after.get("missing_cells"),
        "duplicate_rows_after":after.get("duplicate_rows"),
        "cells_missing_removed": (before.get("missing_cells") or 0) - (after.get("missing_cells") or 0),
        "duplicate_rows_removed":(before.get("duplicate_rows") or 0) - (after.get("duplicate_rows") or 0),
    }