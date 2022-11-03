from typing import List

from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse

from app.conf import config

# Get Application Settings
from app.core import request_processor
from app.models.request.Project import Project, Floor, Element, Pin

settings = config.get_settings()

router = APIRouter(
    prefix="/project",
    tags=["project"]
)


@router.get("/get-project")
async def get_project(project_id: str):
    return request_processor.get_project_data(project_id=project_id)


@router.post("/add-project")
async def add_project(project_data: Project):
    return request_processor.add_project_data(project_data)


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
    return request_processor.add_floor_data(project_id, floor_data)


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
def add_element(project_id: str = Form(), floor_id: str = Form(), element_name: str = Form(),
                image_file: UploadFile = File()):
    return request_processor.add_element_data(project_id, floor_id, element_name, image_file)


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


@router.get("/get-record")
async def get_project(project_id: str, floor_id: str, element_id: str):
    return request_processor.get_record_data(project_id, floor_id, element_id)


@router.get("/get-image/{name}")
def download_img(name: str):
    return request_processor.get_img_data(name)


@router.post("/upload-image")
def upload_img(image_name: str = Form(), image_file: UploadFile = File()):
    return request_processor.upload_img(image_name, image_file)


@router.put("/update-pins")
async def update_pins(project_id: str, floor_id: str, element_id: str, pins: List[Pin]):
    return request_processor.update_pins(project_id, floor_id, element_id, pins)


@router.get("/get-spread-sheet")
async def get_spread_sheet(project_id: str, floor_id: str, element_id: str):
    return request_processor.get_spread_sheet(project_id, floor_id, element_id)



