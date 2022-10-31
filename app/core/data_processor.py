from typing import List

from app.core.id_generator import generate_id
from app.db.base.records import get_base
from app.db.drive.images import get_drive
from app.models.request.Project import \
    Project as ProjectReq, \
    Floor as FloorReq, \
    Element as ElementReq, \
    Pin as PinReq


def get_project_data(project_id: str):
    db = get_base()
    res = db.get(project_id)
    return res


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


def add_element_data(project_id: str, floor_id: str, element_data: ElementReq):
    db = get_base()
    project_data = db.get(project_id)
    element_id: str = generate_id("element")

    if project_data:
        if floor_id in project_data['floors']:
            updated_data = \
                db.update(key=project_id, updates={
                    f"floors.{floor_id}.elements.{element_id}": element_data.dict()
                })
            return updated_data
        else:
            return {}, 404
    else:
        return {}, 404


def update_pins(project_id: str, floor_id: str, element_id: str, pins: List[PinReq]):
    db = get_base()
    project_data = db.get(project_id)

    if project_data:
        if floor_id in project_data['floors']:
            if element_id in project_data['floors'][floor_id]['elements']:
                for pin in pins:
                    db.update(key=project_id, updates={
                        f"floors.{floor_id}.elements.{element_id}.pins.{pin.ref_id}": pin.dict()
                    })
                return {}, 200
            else:
                return {}, 404
        else:
            return {}, 404
    else:
        return {}, 404
