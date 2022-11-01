from fastapi import APIRouter
from app.conf import config

# Get Application Settings
from app.core import response_processor

settings = config.get_settings()

router = APIRouter(
    prefix="/app-data",
    tags=["app-data"]
)


@router.get("/list_all_projects")
async def list_all_projects():
    return response_processor.list_all_projects()


@router.get("/list_all_levels/{project_id}")
async def list_all_levels(project_id: str):
    return response_processor.list_all_levels(project_id)


@router.get("/list_all_elements/{project_id}/{floor_id}")
async def list_all_elements(project_id: str, floor_id: str):
    return response_processor.list_all_elements(project_id, floor_id)


@router.get("/get")
async def get_app_data():
    return [
        {
            "project_id": "PR001",
            "project_name": "Test1",
            "floors": [
                {
                    "floor_no": "00",
                    "elements": [
                        {
                            "element_id": "FL001",
                            "element_name": "Floor",
                        },
                        {
                            "element_id": "DR001",
                            "element_name": "Door",
                        },
                        {
                            "element_id": "WN001",
                            "element_name": "Window",
                        }
                    ]
                },
                {
                    "floor_no": "01",
                    "elements": [
                        {
                            "element_id": "FL001",
                            "element_name": "Floor",
                        },
                        {
                            "element_id": "DR001",
                            "element_name": "Door",
                        },
                        {
                            "element_id": "WN001",
                            "element_name": "Window",
                        }
                    ]
                }
            ],
        },
        {
            "project_id": "PR002",
            "project_name": "Test2",
            "floors": [
                {
                    "floor_no": "00",
                    "elements": [
                        {
                            "element_id": "FL001",
                            "element_name": "Floor",
                        },
                        {
                            "element_id": "DR001",
                            "element_name": "Door",
                        },
                        {
                            "element_id": "WN001",
                            "element_name": "Window",
                        }
                    ]
                },
                {
                    "floor_no": "01",
                    "elements": [
                        {
                            "element_id": "FL001",
                            "element_name": "Floor",
                        },
                        {
                            "element_id": "DR001",
                            "element_name": "Door",
                        },
                        {
                            "element_id": "WN001",
                            "element_name": "Window",
                        }
                    ]
                }
            ],
        }

    ]
