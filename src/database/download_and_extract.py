import pathlib, logging, tarfile, requests

import database.config as db_config
import context

def _download_large_file(url: str, destination: pathlib.Path):
    """
    Downloads a large file from the given URL to the given destination.
    """
    CHUNK_SIZE = 8192
    response = requests.get(url, stream=True)
    response.raise_for_status()
    nr_chunks = 0
    logging.info(f"Downloading {url} to {destination}...")
    print(f"Downloading {url}...")
    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            f.write(chunk)
            nr_chunks += 1
            if nr_chunks % 10000 == 0:
                logging.debug(f"Downloaded {nr_chunks * CHUNK_SIZE // 2**20} MB...")
                print(".", end='', flush=True)
    print("")
    # sanity check
    if nr_chunks <= 100:
        logging.error(f"Downloaded file is too small: {nr_chunks * CHUNK_SIZE // 2**20} MB.")
        raise ValueError(f"Downloaded file is too small: {nr_chunks * CHUNK_SIZE // 2**20} MB.")
        
    print(f"Downloaded {nr_chunks * CHUNK_SIZE // 2**20} MB.")
    logging.info(f"Downloaded {nr_chunks * CHUNK_SIZE // 2**20} MB.")


def _possible_download_urls(db_and_version: db_config.DatabaseTypeAndVersion):
    """
    Returns the possible paths for the database binaries.
    """
    if db_and_version.database_type == db_config.DatabaseType.MYSQL:
        return [
            f"https://dev.mysql.com/get/Downloads/MySQL-{db_and_version.version}/mysql-{db_and_version.version}-linux-glibc2.12-x86_64.tar.xz",
            f"https://dev.mysql.com/get/Downloads/MySQL-{db_and_version.version}/mysql-{db_and_version.version}-linux-glibc2.12-x86_64.tar.gz"
        ]
    else:
        raise ValueError(f"Unsupported database type: {db_and_version.database_type}")
    


def download_and_extract_db_binaries(db: db_config.DatabaseTypeAndVersion) -> pathlib.Path:
    """
    Downloads and extracts the necessary binaries for the database.
    """
    # get the cache location
    cache_location = context.Context.get_context().cache_folder / f"databases/{db}"
    
    # # if we already have the binaries, we don't need to download them again
    if cache_location.exists() and (cache_location / "binaries").exists():
        logging.info(f"Binaries for {db} already exist at {cache_location}. Skipping download.")
        return cache_location / "binaries"
    
    # download the binaries
    cache_location.mkdir(exist_ok=True, parents=True)
    urls = _possible_download_urls(db)
    downloaded = False
    for url in urls:
        compression = url.split(".")[-1]
        try:
            _download_large_file(url, cache_location / f"binaries.tar.{compression}")
            downloaded = True
            break
        except Exception as e:
            logging.error(f"Could not download the database from {url}: {e}")
            continue
    if not downloaded:
        logging.error(f"Could not download the database binaries for {db}.")
        raise ValueError(f"Could not download the database binaries for {db}.")

    # extract the binaries
    print("Extracting the binaries...")
    with tarfile.open(cache_location / f"binaries.tar.{compression}", f"r:{compression}") as tar:
        # Extract all contents to the destination folder
        tar.extractall(cache_location)
    
    # change the extracted folder name to "binaries"
    extracted_folder = [i for i in cache_location.iterdir() if i.is_dir()][0]
    extracted_folder.rename(cache_location / "binaries")
    logging.info(f"Extracted the binaries for {db} to {cache_location / 'binaries'}.")
    return cache_location / "binaries"
