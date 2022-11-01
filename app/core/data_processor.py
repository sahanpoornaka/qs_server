from typing import Dict

from openpyxl import Workbook

from app.models.data.Project import Record, Pin


def create_excel_sheet(record_data: Record):
    workbook = Workbook()
    sheet = workbook.active
    # Header
    sheet["A1"] = "Project Name:"
    sheet["B1"] = record_data.project_name
    sheet["A2"] = "Level No:"
    sheet["B2"] = record_data.floor_id
    sheet["A3"] = "Element Name:"
    sheet["B3"] = record_data.element_name

    # Table Headers
    sheet["A5"] = "Ref ID"
    sheet["B5"] = "Height"
    sheet["C5"] = "Width"
    sheet["D5"] = "Breadth"
    sheet["E5"] = "Volume"
    sheet["F5"] = "Times"
    sheet["G5"] = "Total"
    sheet["H5"] = "Remarks"

    # Add Pin Data
    pins: Dict[str, Pin] = record_data.pins
    for idx, (ref_id, pin) in enumerate(pins.items()):
        sheet[f"A{idx + 6}"] = ref_id
        sheet[f"B{idx + 6}"] = pin.height
        sheet[f"C{idx + 6}"] = pin.width
        sheet[f"D{idx + 6}"] = pin.breadth
        sheet[f"E{idx + 6}"] = pin.height * pin.width * pin.breadth
        sheet[f"F{idx + 6}"] = pin.times
        sheet[f"G{idx + 6}"] = pin.height * pin.width * pin.breadth * pin.times
        sheet[f"H{idx + 6}"] = pin.remarks

    return workbook
