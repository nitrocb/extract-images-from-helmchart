# extract-images-from-helmchart

this small python tool creates a list of images from a given helmchart

# Usage

```bash
usage: get_images_from_helmchart.py [-h] --chartname CHARTNAME --repo REPO [--version VERSION]

tool for extracting images from a helm chart

optional arguments:
  -h, --help            show this help message and exit
  --chartname CHARTNAME
                        Helm Chart Name
  --repo REPO           Helm Chart Repository
  --version VERSION     Helm Chart Version (optional)
```