from io import BytesIO
from typing import List

from fastapi import UploadFile
from fastapi.responses import StreamingResponse

from app.core import data_processor
from app.core.id_generator import generate_id
from app.core.image_processor import upload_image
from app.db.base.records import get_base
from app.db.drive.images import get_drive
from app.data.constants import ELEMENTS
from app.models.data.Project import Record, ProjectFull, Floor, Element
from app.models.request.Project import \
    Project as ProjectReq, \
    Floor as FloorReq, \
    Pin as PinReq


def get_project_data(project_id: str):
    db = get_base()
    res = db.get(project_id)
    return res


def get_record_data(project_id: str, floor_id: str, element_id: str):
    out_obj = {}
    project_data: ProjectFull = ProjectFull(**get_project_data(project_id))
    if project_data:
        out_obj['project_id'] = project_id
        out_obj['project_name'] = project_data.project_name
        if floor_id in project_data.floors:
            floor_data: Floor = project_data.floors[floor_id]
            out_obj['floor_id'] = floor_id
            out_obj['floor_no'] = floor_data.floor_no
            if element_id in floor_data.elements:
                element_data: Element = floor_data.elements[element_id]
                out_obj['element_id'] = element_id
                out_obj['element_name'] = element_data.element_name
                out_obj['img_name'] = element_data.img_data.img_name
                out_obj['pins'] = element_data.pins
    return Record(**out_obj)


def add_project_data(project_data: ProjectReq):
    db = get_base()
    project_data_db = db.put({
        **project_data.dict()
    })
    return project_data_db


def add_floor_data(project_id: str, floor_data: FloorReq):
    db = get_base()
    project_data = db.get(project_id)
    floor_id: str = generate_id("floor", floor_data.floor_no)
    if project_data:
        updated_data = \
            db.update(key=project_id, updates={
                f"floors.{floor_id}": floor_data.dict()
            })
        return updated_data
    else:
        return {}, 404


def add_element_data(project_id: str, floor_id: str, element_id: str, image_file: UploadFile):
    db = get_base()
    project_data = db.get(project_id)

    # Create Element Data
    # element_id: str = generate_id("element")
    element_data = ELEMENTS.get(element_id, {})

    if project_data:
        if floor_id in project_data['floors']:
            # Upload Image
            image_name = project_id + "_" + floor_id + "_" + element_id + ".png"
            image_data = upload_image(image_name, image_file)
            updated_data = \
                db.update(key=project_id, updates={
                    f"floors.{floor_id}.elements.{element_id}": {**element_data.dict(), "img_data": image_data}
                })
            return updated_data
        else:
            return {}, 404
    else:
        return {}, 404


def get_img_data(name: str):
    drive = get_drive()
    res = drive.get(name)
    print(type(res))
    return StreamingResponse(res.iter_chunks(1024), media_type="image/png")


def update_pins(project_id: str, floor_id: str, element_id: str, pins: List[PinReq]):
    db = get_base()
    project_data = db.get(project_id)

    if project_data:
        if floor_id in project_data['floors']:
            if element_id in project_data['floors'][floor_id]['elements']:
                pins_obj = {}
                for pin in pins:
                    pins_obj[pin.ref_id] = pin.dict()
                res = db.update(key=project_id, updates={
                    f"floors.{floor_id}.elements.{element_id}.pins": pins_obj
                })
                return res, 200
            else:
                return {}, 404
        else:
            return {}, 404
    else:
        return {}, 404


def get_spread_sheet(project_id: str, floor_id: str, element_id: str):
    record_data: Record = get_record_data(project_id, floor_id, element_id)
    workbook = data_processor.create_excel_sheet(record_data)

    file_stream = BytesIO()
    workbook.save(file_stream)
    file_stream.seek(0)

    return StreamingResponse(file_stream, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


# def get_test_excel():
#     wb = Workbook()
#     ws = wb.active
#     ws.append(['TDD', 'is', 'AWESOME!'])
#     ws.append(['Except', 'when', 'it', 'is', 'particularly', 'hard'])
#     ws.append(['But', 'we', 'can', 'handle', 'it'])
#
#     file_stream = BytesIO()
#     wb.save(file_stream)
#     file_stream.seek(0)
#
#     return StreamingResponse(file_stream, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
