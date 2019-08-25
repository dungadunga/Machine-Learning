from google_images_download import google_images_download
import argparse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

parser = argparse.ArgumentParser()

parser.add_argument("-keyword", "--keywords", required=True)
parser.add_argument("-path", "--paths", required=True)

arguments = parser.parse_args()

def main():
    res = google_images_download.googleimagesdownload()
    args = {
        "keywords": arguments.keywords,
        "limits": 100,
        "print_urls": True,
        "no_directory": True,
        "output_directory": arguments.paths,
        "exact_size": "640, 480"
    }

    path = res.download(args)
    print(path)

if __name__ == '__main__':
    main()