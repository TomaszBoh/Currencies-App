import yaml

def load_config(file_path="config.yaml"):
    with open("config.yaml", "r", encoding="utf-8") as fp:
        config = yaml.safe_load(fp)
    return config