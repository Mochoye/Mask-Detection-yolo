# Mask Detection with YOLO

This repository contains the implementation of a mask detection system using the YOLO (You Only Look Once) object detection model. This system is designed to detect whether individuals in video streams are wearing masks, which is crucial for maintaining public health safety standards, especially during health crises like the COVID-19 pandemic.

The Model is Run in 50 epochs

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- pip3
- ultralytics
- roboflow

## Installation

To install the necessary dependencies, follow these steps:

```bash
git clone https://github.com/Mochoye/Mask-Detection-yolo
cd Mask-Detection-yolo
pip install -r requirements.txt
```
## Dataset

The dataset used for training the model can be found here: [Mask Detection Dataset](https://www.kaggle.com/datasets/humansintheloop/medical-mask-detection)

The dataset is converted into Coco format using this [script](https://github.com/Mochoye/Mask-Detection-yolo/blob/main/convert.py)

## Usage

To run mask detection, use the following command:

```bash
!yolo detect predict model=best.pt source="Test_video1.mp4"
```

## Image Inferences
![0ac41a01-93b9-4125-a589-9ab3df18753c](https://github.com/Mochoye/Mask-Detection-yolo/assets/95351969/30599ee3-12f9-475b-8e5b-d86820c78413)





## Video Inference


https://github.com/Mochoye/Mask-Detection-yolo/assets/95351969/ad93aeae-ad62-4e8c-8d77-ce9d08d295dc

https://github.com/Mochoye/Mask-Detection-yolo/assets/95351969/d013e337-1790-4193-ab95-05b010a2d119



https://github.com/Mochoye/Mask-Detection-yolo/assets/95351969/1133f96f-44c6-4139-a764-644b3c6ea9b3

## Metrics
![a914c764-e878-4f56-b640-f728ac363d54](https://github.com/Mochoye/Mask-Detection-yolo/assets/95351969/2a399ad2-bc27-48f6-8e4c-39bb52748d92)
![d322dea2-138f-4ac2-895a-a420![534a97da-808a-44af-bcde-c55ba06b023e](https://github.com/Mochoye/Mask-Detection-yolo/assets/95351969/7a49af5e-51cc-4186-811e-cc9b0a1c56d1)
![d322dea2-138f-4ac2-895a-a420f3f7be55](https://github.com/Mochoye/Mask-Detection-yolo/assets/95351969/22bef6c4-9953-4f8c-ab88-0994c6c8bcc3)

## Contributing to Mask Detection with YOLO

To contribute to this project, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contributors

Thanks to the following people who have contributed to this project:

- [@Mochoye](https://github.com/Mochoye) (Archisman Ray)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.







