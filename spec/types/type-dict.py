from typing import TypedDict

class Config(TypedDict):
    export_show_error: bool
    export_timeout: float
    # 添加其他配置项
    export_show_error_bad: bool

config: Config = {
    "export_show_error": True,
    "export_timeout": 0.001,
    "export_show_error_bad": False,
    # 初始化其他配置项
}
