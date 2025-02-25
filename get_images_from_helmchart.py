import yaml
import subprocess
import argparse
import re

# Parser erstellen
parser = argparse.ArgumentParser(description="tool for extracting images from a helm chart")
parser.add_argument("--chartname", type=str,required=True, help="Helm Chart Name")
parser.add_argument("--repo", type=str ,required=True, help="Helm Chart Repository")
parser.add_argument("--version", type=str, help="Helm Chart version (optional)")
parser.add_argument("--values", type=str, help="Helm Chart values (optional)")


# Argumente parsen
args = parser.parse_args()

imageList = []
helmCommand = ""

if "oci:" in args.repo:
  helmCommand = f"helm template {args.chartname} {args.repo}"
else:
  helmCommand = f"helm template {args.chartname} --repo {args.repo}"

if args.version:
  helmCommand += f" --version {args.version}"

if args.values:
  helmCommand += f" --values {args.values}"

renderedCharts = subprocess.run(helmCommand, shell=True, capture_output=True).stdout.decode().strip()
resources = re.split(r'^\s*---\s*$', renderedCharts, flags=re.MULTILINE)[1:]

for resource in resources:

  if resource == "":
    continue

  resourceObj = yaml.safe_load(resource)
  
  try: 
    containerList = resourceObj["spec"]["template"]["spec"]["containers"]
  except (KeyError):
    continue

  try:
    containerList.extend(resourceObj["spec"]["template"]["spec"]["initContainers"])
  except (KeyError):
    pass

  try:
    containerList.extend(resourceObj["spec"]["template"]["spec"]["ephemeralContainers"])
  except (KeyError):
    pass

  for container in containerList:
    if container["image"] not in imageList:
      imageList.append(container["image"])

print("\n".join(imageList))
