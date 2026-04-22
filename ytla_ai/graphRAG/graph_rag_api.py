from pathlib import Path

from graphrag.cli import initialize

path = Path("")
force = False
model = "model"
embedding_model = "embedding"

def init():
    initialize.initialize_project_at(path=path, force=force, model=model, embedding_model=embedding_model)