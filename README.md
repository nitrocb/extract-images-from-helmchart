# extract-images-from-helmchart

this small python tool creates a list of images from a given helmchart

# Usage

```
usage: get_images_from_helmchart.py [-h] --chartname CHARTNAME --repo REPO [--version VERSION] [--values VALUES]

tool for extracting images from a helm chart

optional arguments:
  -h, --help            show this help message and exit
  --chartname CHARTNAME
                        Helm Chart Name
  --repo REPO           Helm Chart Repository
  --version VERSION     Helm Chart version (optional)
  --values VALUES       Helm Chart values (optional)
```