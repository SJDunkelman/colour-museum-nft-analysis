import os

# Paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = f'{ROOT_DIR}/images/'

# Web driver
CHROME_DRIVER_PATH = "/Users/simondunkelman/GitHub/colour-museum-nft-analysis/chromedriver"
CHROME_BINARY_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# Dataset constants
COLLECTION_INDEX_URL = 'https://opensea.io/rankings?category=art&sortBy=total_volume'


# K Means parameters
CLUSTER_TOTAL = 10
ITERATIONS = 100
TOLERANCE = 1E-3
