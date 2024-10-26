import yt_dlp
import cv2
import os
import img2pdf

# Input for YouTube link
link = input('Enter your YouTube link: ')

# Download the video using yt-dlp
ydl_opts = {
    'format': 'best',
    'outtmpl': 'downloaded_video.%(ext)s',  # Save as 'downloaded_video.mp4' or similar
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
    # Get the path of the downloaded video
    info_dict = ydl.extract_info(link, download=False)
    video_path = ydl.prepare_filename(info_dict)

# Output the video path for confirmation
print("Video downloaded and saved at:", video_path)

# Function to convert timestamp to seconds
def timestamp_to_seconds(timestamp):
    minutes, seconds = map(int, timestamp.split(':'))
    return minutes * 60 + seconds

# Input for timestamps
timestamps_input = input("Enter the timestamps (separated by comma, format: MM:SS): ")
timestamps = [ts.strip() for ts in timestamps_input.split(',')]

# Create VideoCapture object
vid = cv2.VideoCapture(video_path)

# Check if the video file is opened successfully
if not vid.isOpened():
    print("Error: Unable to open video file.")
    exit()

# Create directory to save frames
output_directory = 'data'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Extract frames at specified timestamps
for timestamp in timestamps:
    # Set the frame position based on timestamp
    seconds = timestamp_to_seconds(timestamp)
    vid.set(cv2.CAP_PROP_POS_MSEC, seconds * 1000)
    # Read the frame
    success, frame = vid.read()
    if not success:
        print(f"Error: Unable to read frame at timestamp {timestamp}.")
        continue
    # Save the frame as an image
    output_path = os.path.join(output_directory, f'frame_{timestamp.replace(":", "_")}.jpg')
    cv2.imwrite(output_path, frame)
    print(f"Frame at timestamp {timestamp} saved.")

# Release the video capture object and close windows
vid.release()
cv2.destroyAllWindows()
print("Frames extraction completed.")

# Convert images to PDF
pdf_path = os.path.join(output_directory, "file.pdf")

# Get a list of image files in the directory
image_files = [os.path.join(output_directory, f) for f in os.listdir(output_directory) if f.endswith('.jpg')]
# Sort the files by name to maintain the order
image_files.sort()

# Convert images to PDF using img2pdf
with open(pdf_path, "wb") as pdf_file:
    pdf_file.write(img2pdf.convert(image_files))

# Output the PDF path
print("Successfully created PDF file:", pdf_path)

# Clean up: delete the downloaded video and extracted frames
if os.path.exists(video_path):
    os.remove(video_path)
    print(f"Deleted video file: {video_path}")

# Delete the extracted frames
for frame in image_files:
    os.remove(frame)
    print(f"Deleted frame file: {frame}")



