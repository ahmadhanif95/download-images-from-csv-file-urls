import csv
import requests
import os

def download_images_from_csv(csv_file_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(csv_file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            url = row['URL'].strip()
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    # Extract filename from URL
                    filename = os.path.join(output_folder, os.path.basename(url))
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded: {filename}")
                else:
                    print(f"Failed to download image from {url}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error downloading image from {url}: {str(e)}")

if __name__ == "__main__":
    csv_file_path = "urls.csv"  # Specify the path to your CSV file
    output_folder = "images"  # Specify the output folder where images will be saved
    download_images_from_csv(csv_file_path, output_folder)

