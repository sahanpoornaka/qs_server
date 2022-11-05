from app.core.request_processor import get_project_data
from app.data import constants
from app.db.base.records import get_base
from app.models.data.Project import ProjectFull, Floor, Element


def list_all_projects():
    db = get_base()
    res = db.fetch(query=None, limit=1000, last=None)
    return [{'project_id': item['key'], 'project_name': item['project_name']} for item in res.items]


def list_all_levels(project_id: str):
    out_obj = {}
    project_data: ProjectFull = get_project_data(project_id)
    if project_data:
        out_obj['project_id'] = project_id
        out_obj['project_name'] = project_data.project_name
        if project_data.floors:
            floors = []
            for floor_id, floor in project_data.floors.items():
                floors = floors + [{"floor_id": floor_id, "floor_no": floor.floor_no}]
            out_obj['floors'] = floors
    return out_obj


def list_all_elements(project_id: str, floor_id: str):
    out_obj = {}
    project_data: ProjectFull = get_project_data(project_id)
    if project_data:
        out_obj['project_id'] = project_id
        out_obj['project_name'] = project_data.project_name
        if floor_id in project_data.floors:
            floor_data: Floor = project_data.floors[floor_id]
            out_obj['floor_id'] = floor_id
            out_obj['floor_no'] = floor_data.floor_no
            if floor_data.elements:
                elements = []
                for element_id, element in floor_data.elements.items():
                    elements = elements + [{"element_id": element_id, "element_name": element.element_name}]
                out_obj['elements'] = elements
    return out_obj


def list_all_add_elements():
    out_list = []
    elements_data: dict = constants.ELEMENTS
    for elem in elements_data.values():
        out_list = out_list + [{"element_id": elem.element_id, "element_name": elem.element_name}]
    return out_list
