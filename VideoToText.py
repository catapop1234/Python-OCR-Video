import cv2
import pytesseract

# Path to the video file
video_path = 'VideoToText/S.mp4'

# Initialize video capture
video = cv2.VideoCapture(video_path)

# Initialize frame count
frame_count = 0

# List to hold extracted questions and answers
questions_and_answers = []

# Process the video frame by frame
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    frame_count += 1

    # Convert frame to grayscale for better OCR results
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Use OCR to extract text from the frame
    text = pytesseract.image_to_string(gray_frame)
    
    # Extract questions and answers if any text is detected
    if text.strip():
        questions_and_answers.append((frame_count, text.strip()))

# Release the video capture object
video.release()

# Save the extracted questions and answers to a text file
with open('VideoToText/extracted_text_from_video.txt', 'w') as file:
    for frame_number, text in questions_and_answers:
        file.write(f'Frame {frame_number}:\n{text}\n\n')

print("Text extraction complete. Check 'extracted_text.txt' for results.")
