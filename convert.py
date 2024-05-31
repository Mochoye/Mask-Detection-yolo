import json
import os

# Paths to your JSON files and output
input_dir = 'C:/Users/sri/Desktop/Projects/internship/Medical mask/Medical mask/Medical Mask/annotations'
output_path = 'C:/Users/sri/Desktop/Projects/internship/Medical mask/Medical mask/Medical Mask/new/coco_format.json'

# Load the meta.json to map class names to IDs
with open('C:/Users/sri/Desktop/Projects/internship/Medical mask/Medical mask/meta.json', 'r') as f:
    meta = json.load(f)
    categories = [{ "id": i+1, "name": cat["title"] } for i, cat in enumerate(meta["classes"])]

# Prepare the COCO JSON structure
coco_format = {
    "images": [],
    "annotations": [],
    "categories": categories
}

annotation_id = 1  # Unique ID for each annotation
image_id = 1       # Unique ID for each image

# Process each JSON file
for file_name in os.listdir(input_dir):
    if file_name.endswith('.json'):
        json_path = os.path.join(input_dir, file_name)
        with open(json_path, 'r') as file:
            data = json.load(file)

        # Add image information
        coco_format['images'].append({
            "file_name": data['FileName'],
            "height": '640',  # Replace with actual height if available
            "width": '640',   # Replace with actual width if available
            "id": image_id
        })

        # Add annotations
        for obj in data['Annotations']:
            bbox = obj['BoundingBox']
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            category_id = next((cat["id"] for cat in categories if cat["name"] == obj["classname"]), None)

            coco_format['annotations'].append({
                "id": annotation_id,
                "image_id": image_id,
                "category_id": category_id,
                "bbox": [bbox[0], bbox[1], width, height],
                "area": width * height,
                "iscrowd": 0
            })
            annotation_id += 1

        image_id += 1

# Write the COCO formatted data to a new JSON file
with open(output_path, 'w') as f:
    json.dump(coco_format, f, indent=4)

print("Conversion to COCO format completed.")
