from typing import Dict
from pydantic import BaseModel


# class ImageDims(BaseModel):
#     height: float
#     width: float
#
#
# class ImageData(BaseModel):
#     img_name: str
#     img_dims: ImageDims


class Pin(BaseModel):
    ref_id: str
    measure_unit: str
    height: float
    width: float
    breadth: float
    times: int
    x_coord: float
    y_coord: float
    remarks: str


class Element(BaseModel):
    element_id: str
    element_description: str = ""
    element_remarks: str = ""
    # img_data: ImageData
    # pins: Dict[str, Pin] = {}


class Floor(BaseModel):
    floor_no: int
    floor_remarks: str = ""
    elements: Dict[str, Element] = {}


class Project(BaseModel):
    # project_id: str
    project_name: str
    project_description: str = ""
    project_remarks: str = ""
    num_floors: int = 0
    floors: Dict[str, Floor] = {}
