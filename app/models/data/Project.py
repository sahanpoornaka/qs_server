from typing import Dict, Union
from pydantic import BaseModel


class ImageDims(BaseModel):
    height: float
    width: float


class ImageData(BaseModel):
    img_name: str
    img_dims: ImageDims


class Pin(BaseModel):
    ref_id: str
    measure_unit: str = "meter"
    height: float = 1.0
    width: float = 1.0
    breadth: float = 1.0
    times: int = 1
    x_coord: float = 0.0
    y_coord: float = 0.0
    remarks: Union[str, None] = ""


class Element(BaseModel):
    element_id: str
    element_name: str
    element_description: Union[str, None] = ""
    element_remarks: Union[str, None] = ""
    img_data: Union[ImageData, None] = None
    pins: Dict[str, Pin] = {}


class Floor(BaseModel):
    floor_no: int
    floor_remarks: Union[str, None] = ""
    elements: Dict[str, Element] = {}


class Project(BaseModel):
    # project_id: str
    project_name: str
    project_description: str = ""
    project_remarks: str = ""
    num_floors: int = 0
    floors: Dict[str, Floor] = {}


class ProjectFull(BaseModel):
    # project_id: str
    project_name: str
    project_description: Union[str, None] = ""
    project_remarks: Union[str, None] = ""
    num_floors: int = 0
    floors: Dict[str, Floor] = {}


class Record(BaseModel):
    project_id: str
    project_name: str
    floor_id: str
    floor_no: int
    element_id: str
    element_name: str
    img_name: str
    pins: Dict[str, Pin] = {}
