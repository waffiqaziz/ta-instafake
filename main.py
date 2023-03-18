from utils import import_data

dataset_path = "data"
dataset_version = "fake-v1.0"

fake_dataset = import_data(dataset_path, dataset_version)

# show info dataset
print(fake_dataset.T.info())
