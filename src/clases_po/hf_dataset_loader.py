from datasets import load_dataset
import pandas as pd


class HFDatasetLoader:
    """Carga un dataset de Hugging Face y lo devuelve como DataFrame de pandas."""

    def __init__(self, dataset_id, split="train"):
        # dataset_id es el identificador, por ejemplo "scikit-learn/iris"
        self.dataset_id = dataset_id
        # split es opcional: "train", "test", etc.
        self.split = split

    def load(self) -> pd.DataFrame:
        # La conexión y la descarga se hacen dentro de la clase
        if self.split is None:
            # Si no me dan split, cargo todos y tomo el primero
            dataset_dict = load_dataset(self.dataset_id)
            primer_split = list(dataset_dict.keys())[0]
            dataset = dataset_dict[primer_split]
        else:
            dataset = load_dataset(self.dataset_id, split=self.split)

        # Convierto el dataset a DataFrame
        return dataset.to_pandas() 
    