import const
import colorgram as cg
from typing import List
import glob
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def extract_colours(image_filepath: str) -> dict:
    """
    Extract the unique colours found in an RGB image matrix and their respective composition value
    :param image:
    :return:
    """
    colour_proportions = {}
    colour_list = cg.extract(image_filepath, 2 ** 32)
    for idx in range(len(colour_list)):
        rgb = colour_list[idx]
        hex = rgb_to_hex(rgb.rgb)
        colour_proportions[hex] = rgb.proportion
    return colour_proportions


def get_all_image_paths(folder: str = const.IMAGE_DIR) -> List[str]:
    image_filepaths = glob.glob(f'{folder}/**/*.png',
                                recursive=True)
    return image_filepaths


def analyse_images():
    file_paths = get_all_image_paths()
    image_dataset = []
    for img_path in tqdm(file_paths):
        img_colours = extract_colours(img_path)
        image_dataset.append(img_colours)
    df = pd.DataFrame(image_dataset)
    df = df.fillna(0)
    return df


def get_hex_average_weights(colour_df):
    return colour_df.mean(axis=0)


def get_rgb_values(weighted_hex_series):
    weighted_rgb_values = {hex_to_rgb(i): v for i, v in weighted_hex_series.items()}
    return np.asarray([np.asarray(t) for t in list(weighted_rgb_values.keys())])


def get_k_means_centroids(weighted_hex_series, n: int = 10000):
    weighted_rgb_values = {hex_to_rgb(i): v for i, v in weighted_hex_series.items()}
    rgb_values = np.asarray([np.asarray(t) for t in list(weighted_rgb_values.keys())])
    centroids = np.random.randint(low=0, high=255, size=(10, 3))  # 3D
    centroids_old = centroids.copy()

    K = len(centroids)
    # Train centroids
    for iter_ in range(const.ITERATIONS):
        dist = np.linalg.norm(rgb_values - centroids[0, :], axis=1).reshape(-1, 1)
        for class_ in range(1, K-1):
            dist = np.append(dist, np.linalg.norm(rgb_values - centroids[class_, :], axis=1).reshape(-1, 1), axis=1)
        classes = np.argmin(dist, axis=1)
        # Update positions
        for class_ in set(classes):
            centroids[class_, :] = np.mean(rgb_values[classes == class_, :], axis=0)
        if np.linalg.norm(centroids - centroids_old) < const.TOLERANCE:
            print('Centroid converged')
            break
    return centroids


def plot_rgb(rgb_values, centroids):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(rgb_values[:, 0], rgb_values[:, 1], rgb_values[:, 2], marker=".")
    ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], s=50, c='b', marker='+')
    ax.set_xlabel('Red')
    ax.set_ylabel('Blue')
    ax.set_zlabel('Green')


if __name__ == "__main__":
    df = analyse_images()
    weighted_hex = get_hex_average_weights(df)
    centroids = get_k_means_centroids(weighted_hex, const.CLUSTER_TOTAL)
    rgb_values = get_rgb_values(weighted_hex)
    plot_rgb(rgb_values, centroids=centroids)
