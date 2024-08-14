# Parking Pixels

**Parking Pixels** is a smart parking space detection system that utilizes computer vision techniques to detect vacant parking slots in real-time using video input. This project leverages YOLOv9 for object detection and provides an intuitive interface for users to select regions of interest in the video.

## Features

- Real-time detection of vacant parking slots.
- Easy-to-use interface for selecting parking regions in video footage.
- Support for multiple video formats (.mp4, .avi, .mkv).
- Runs efficiently on both local machines and cloud environments.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher.
- Git installed on your local machine.
- Optional: Conda installed for environment management.

## Installation

Follow the steps below to set up the Parking Pixels project on your local machine:

### 1. Clone the Repository

First, clone the GitHub repository to your local machine using the following command:

```
git clone https://github.com/yourusername/parking-pixels.git
cd parking-pixels
```
Set Up the Environment
You can set up a Python virtual environment or a Conda environment to manage dependencies.

Option 1: Using Python Virtual Environment
```
python3 -m venv parking-env
source parking-env/bin/activate  # On Windows: parking-env\Scripts\activate
```

Option 2: Using Conda
```
conda create --name parking-env python=3.9
conda activate parking-env
```
3. Install Required Packages
With your environment activated, install the required Python packages using pip:

```
pip install -r requirements.txt
```

Running the Application
After setting up the environment and installing the necessary packages, you can run the application as follows:

```
python MyApp.py
```

This will start the Parking Pixels application, where you can select video files, define parking regions, and detect vacant slots in real-time.

## Usage
- Select Video: Choose a video file that contains the parking area.
- Set Region: Define the parking slots within the video frame.
- Detect: Start the detection process to identify vacant parking spots.
- Reset: Reset the application to select a new video or region.
