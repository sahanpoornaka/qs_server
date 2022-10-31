from typing import List

from fastapi import APIRouter
from app.conf import config

# Get Application Settings
from app.core import data_processor
from app.models.request.Project import Project, Floor, Element, Pin

settings = config.get_settings()

router = APIRouter(
    prefix="/project",
    tags=["project"]
)


@router.get("/get-project")
async def get_project(project_id: str):
    project_data = data_processor.get_project_data(project_id=project_id)
    return project_data


@router.post("/add-project")
async def add_project(project_data: Project):
    res = data_processor.add_project_data(project_data)
    return res


@router.put("/update-project")
async def update_project():
    return {
        "Project Updated Successfully!"
    }


@router.delete("/remove-project")
async def remove_project():
    return {
        "Project Removed Successfully!"
    }


@router.post("/add-floor")
async def add_floor(project_id: str, floor_data: Floor):
    res = data_processor.add_floor_data(project_id, floor_data)
    return res


@router.put("/update-floor")
async def update_floor():
    return {
        "Floor Updated Successfully!"
    }


@router.delete("/remove-floor")
async def remove_floor():
    return {
        "Floor Removed Successfully!"
    }


@router.post("/add-element")
async def add_element(project_id: str, floor_id: str, element_data: Element):
    res = data_processor.add_element_data(project_id, floor_id, element_data)
    return res


@router.put("/update-element")
async def update_element():
    return {
        "Element Updated Successfully!"
    }


@router.delete("/remove-element")
async def remove_element():
    return {
        "Element Removed Successfully!"
    }


@router.put("/update-pins")
async def update_pins(project_id: str, floor_id: str, element_id: str, pins: List[Pin]):
    res = data_processor.update_pins(project_id, floor_id, element_id, pins)
    return res
