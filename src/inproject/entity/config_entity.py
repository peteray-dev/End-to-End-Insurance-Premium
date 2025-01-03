from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionCOnfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path
    comp_name: str

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE:str
    all_schema: str 

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    n_estimators: int
    learning_rate: float
    target_column: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    train_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str