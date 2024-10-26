#YouTube Frame Extractor 
This Python project extracts frames from Youtube videos at specified timestamps and compiles them into a PDF document for easy sharing and viewing.

##Features
-Extracts specified frames from Youtube videos based on user-defined timestamps.
-Compiles the extracted frames into a single PDF file.
-User-friendly command-line interface for inputting video URLs and timestamps.

##Technologies Used 
-Python
-OpenCV(cv2) for frame extraction
-img2pdf for generating PDFs
-yt_dlp for downloading videos

##Installation Instructions
1. Clone the repository:
   bash
   git clone
https://github.com/bhavesh1309/YOUTUBE-FRAME-EXTRACTOR.git
2. Navigate to the project directory:
   cd YouTube-Frame-Extractor
3. Install the required dependencies:
   pip install -r requirements.txt
4. Run the script:
   python extractor.py

##Usage Example
1. After running the script, enter the YouTube video URL when prompted.
2. Specify the timestamps in MM:SS fromat for the frames you want to extract.
3. The output will be a PDF file containing thw selected frames.

##Contributing
Contributions are welcome! Please see the CONTRIBUTING.md file for guidelines on how to contribute to this project.

##License
This project is licnesed under the MIT License.
