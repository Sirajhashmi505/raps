import cv2

def capture_image():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    # Capture a single frame
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Error: Could not read frame.")
        return None

    return frame

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h))

def crop_image(image, start_x, start_y, width, height):
    return image[start_y:start_y + height, start_x:start_x + width]

def display_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Capture an image from the camera
    image = capture_image()
    if image is None:
        return

    # Resize the image
    resized_image = resize_image(image, 300, 300)

    # Rotate the image
    rotated_image = rotate_image(resized_image, 45)

    # Crop the image
    cropped_image = crop_image(rotated_image, 50, 50, 200, 200)

    # Display the manipulated image
    display_image('Manipulated Image', cropped_image)

if __name__ == "__main__":
    main()
