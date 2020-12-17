import os
from src.pipeline.create_pipeline import create_pipeline


if __name__ == "__main__":
    pipeline = create_pipeline()
    print(pipeline.pipe_names)
