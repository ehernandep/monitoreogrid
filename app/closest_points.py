from app import open_dataframes
from sklearn.neighbors import BallTree, KDTree
import pandas as pd


class Trees:
    station_tree = KDTree(open_dataframes.get_stations()[['latitude', 'longitude']].values, leaf_size=2)
    zones_tree = BallTree(open_dataframes.get_zones()[['latitude', 'longitude']].values, leaf_size=2)
    # df_out['distance_nearest'], df_out['id_nearest'] = station_tree.query(df_out[['latitude', 'longitude']].values, k=1)


if __name__ == '__main__':
    stations = open_dataframes.get_stations()
    # zones = open_dataframes.get_zones()
    stations = stations[["name"]]
    rutas = open_dataframes.alturas_df("elevation", 1)
    # rutas = rutas.iloc[1:2]
    _, rutas['id_nearest'] = Trees.station_tree.query(rutas[['latitude', 'longitude']].values, k=1)
    rutas["closest_stations"] = stations["name"].reindex(index=rutas['id_nearest']).tolist()
    # string = b.item()