from pydantic import Field, validator
from typing import List, Optional, Union, Literal,Tuple
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"

class InputDetection(Input):
    name: Literal["InputDetection"] = "InputDetection"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Detection"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Union[List[Image],Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"

class OutputDetection(Output):
    name: Literal["outputDetection"] = "outputDetection"
    value: Union[List[Image],Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "detection"





class KeepSideFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"


class KeepSideTrue(Config):
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class KeepSideBBox(Config):
    """
        Rotate image without catting off sides.
    """
    name: Literal["KeepSide"] = "KeepSide"
    value: Union[KeepSideTrue, KeepSideFalse]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Keep Sides"



class Degree(Config):
    """
        Positive angles specify counterclockwise rotation while negative angles indicate clockwise rotation.
    """
    name: Literal["Degree"] = "Degree"
    value: int = Field(ge=-359.0, le=359.0,default=0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[-359, 359]"] = "[-359, 359]"

    class Config:
        title = "Angleee"



class KSize3x3(Config):
    name: Literal["KSize3x3"] = "KSize3x3"
    value: Tuple[int, int] = Field(default=(3, 3))
    type: Literal["tuple"] = "tuple"
    field: Literal["option"] = "option"

    class Config:
        title = "KSize3x3"

class KSize5x5(Config):
    name: Literal["KSize5x5"] = "KSize5x5"
    value: Tuple[int, int] = Field(default=(5, 5))
    type: Literal["tuple"] = "tuple"
    field: Literal["option"] = "option"

    class Config:
        title = "KSize5x5"

class KSize7x7(Config):
    name: Literal["KSize7x7"] = "KSize7x7"
    value: Tuple[int, int] = Field(default=(7, 7))
    type: Literal["tuple"] = "tuple"
    field: Literal["option"] = "option"

    class Config:
        title = "KSize7x7"


class SizeTrue(Config):
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class SizeFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"

class KSize(Config):
    """
            bulanıklaştırmada kullanılacak pencere büyüklüğüdür.
    """
    name: Literal["KSize"] = "KSize"
    value: Union[SizeTrue,SizeFalse]
    type: Literal["bool"] = "bool"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "KSize"


class SigmaX(Config):
    """
            X ekseni (yatay) için standart sapma değeri.
    """
    name: Literal["SigmaX"] = "SigmaX"
    value:int = Field(ge=0, le=10,default=4)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["Tek sayı, 0-10 arası"] = "Tek sayı, 0-10 arası"

    class Config:
        title = "sigmax"



class MinRadius1(Config):
    name: Literal["MinRadius1"] = "MinRadius1"
    value: string = 1
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"

    class Config:
        title = "MinRadius1"


class MinRadius2(Config):
    name: Literal["MinRadius2"] = "MinRadius2"
    value: string=2
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"

    class Config:
        title = "MinRadius2"

class MinRadius3(Config):
    name: Literal["MinRadius3"] = "MinRadius3"
    value: string=3
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"

    class Config:
        title = "MinRadius3"



class MinRadiusTrue(Config):
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class MinRadiusFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"

class MinRadius(Config):
    """
             Tespit edilecek minimum daire yarıçapı
    """
    name: Literal["MinRadius"] = "MinRadius"
    value: Union[MinRadius1, MinRadius2,MinRadius3]
    type: Literal["option"] = "option"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Min Radius"

class MaxRadius(Config):
    """
            Tespit edilecek maksimum daire yarıçapı
    """
    name: Literal["MaxRadius"] = "MaxRadius"
    value:int
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["Tek sayı, 5-10 arası"] = "Tek sayı, 5-10 arası"

    class Config:
        title = "Max Radius"




class HoughCircleExecutorInputs(Inputs):
    inputImage: InputImage
    inputDetection: InputDetection


class GaussianBlurExecutorInputs(Inputs):
    inputImage: InputImage


class MScaleExecutorInputs(Inputs):
    inputImage: InputImage




class HoughCircleExecutorConfigs(Configs):

    minRadius: MinRadius
    maxRadius: MaxRadius

class GaussianBlurExecutorConfigs(Configs):
    kSize:KSize
    sigmaX:SigmaX

class MScaleExecutorConfigs(Configs):
    degree: Degree
    drawBBox: KeepSideBBox




class HoughCircleExecutorRequest(Request):
    inputs: Optional[HoughCircleExecutorInputs]
    configs: HoughCircleExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class GaussianBlurExecutorRequest(Request):
    inputs: Optional[GaussianBlurExecutorInputs]
    configs: GaussianBlurExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class MScaleExecutorRequest(Request):
    inputs: Optional[MScaleExecutorInputs]
    configs: MScaleExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }




class HoughCircleExecutorOutputs(Outputs):
    outputImage: OutputImage
    outputDetection: OutputDetection

class GaussianBlurExecutorOutputs(Outputs):
    outputImage: OutputImage


class MScaleExecutorOutputs(Outputs):
    outputImage: OutputImage





class HoughCircleExecutorResponse(Response):
    outputs: HoughCircleExecutorOutputs


class GaussianBlurExecutorResponse(Response):
    outputs: GaussianBlurExecutorOutputs

class MScaleExecutorResponse(Response):
    outputs: MScaleExecutorOutputs




class HoughCircleExecutor(Config):
    name: Literal["HoughCircleExecutor"] = "HoughCircleExecutor"
    value: Union[HoughCircleExecutorRequest, HoughCircleExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "HoughCircle"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class GaussianBlurExecutor(Config):
    name: Literal["GaussianBlurExecutor"] = "GaussianBlurExecutor"
    value: Union[GaussianBlurExecutorRequest, GaussianBlurExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "GaussianBlur"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class MScaleExecutor(Config):
    name: Literal["MScaleExecutor"] = "MScaleExecutor"
    value: Union[MScaleExecutorRequest, MScaleExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Rotate"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }




class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[MScaleExecutor,GaussianBlurExecutor,HoughCircleExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    restart: Literal[True] = True

    class Config:
        title = "Type"


class PackageConfigs(Configs):
    executor: ConfigExecutor

class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["MScaling"] = "MScaling"




