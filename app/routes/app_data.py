from fastapi import APIRouter
from app.conf import config

# Get Application Settings
settings = config.get_settings()

router = APIRouter(
    prefix="/app-data",
    tags=["app-data"]
)


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

