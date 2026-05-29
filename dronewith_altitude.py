import airsim
import cv2
import numpy as np
import time

vehicle_name = "Drone1"

client = airsim.MultirotorClient()
client.confirmConnection()

client.enableApiControl(True, vehicle_name)
client.armDisarm(True, vehicle_name)

print("Taking off...")
client.takeoffAsync(vehicle_name=vehicle_name).join()

altitude = -5
client.moveToZAsync(altitude, 2, vehicle_name=vehicle_name).join()

print("Drone flying.")
print("Click Drone Camera window.")
print("W/A/S/D = move, R = up, F = down, Q = quit")

while True:
    responses = client.simGetImages([
        airsim.ImageRequest("bottom_center", airsim.ImageType.Scene, False, False)
    ], vehicle_name=vehicle_name)

    response = responses[0]

    if response.height == 0 or response.width == 0:
        print("No camera image received")
        continue

    img1d = np.frombuffer(response.image_data_uint8, dtype=np.uint8)
    img_rgb = img1d.reshape(response.height, response.width, 3)

    hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

    lower_yellow = np.array([10, 80, 80])
    upper_yellow = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    yellow_pixels = cv2.countNonZero(yellow_mask)

    lower_green = np.array([50, 150, 150])
    upper_green = np.array([70, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green_pixels = cv2.countNonZero(green_mask)

    print("Yellow pixels:", yellow_pixels, "| Green pixels:", green_pixels, "| Altitude:", altitude)

    if yellow_pixels > 2:
        print("WEED DETECTED - SPRAY REQUIRED")
        client.simPrintLogMessage("WEED DETECTED - SPRAY REQUIRED")

    elif green_pixels > 5000:
        print("GOOD PLANTS DETECTED - NO SPRAY")
        client.simPrintLogMessage("GOOD PLANTS - NO SPRAY")

    else:
        print("NO PLANTS DETECTED")

    if yellow_pixels > 50:
        print("SPRAYING WEEDS")
        client.simPrintLogMessage("SPRAYING WEEDS")
        time.sleep(0.5)

    cv2.imshow("Drone Camera", img_rgb)
    cv2.imshow("Yellow Weed Mask", yellow_mask)
    cv2.imshow("Green Plant Mask", green_mask)

    key = cv2.waitKey(1) & 0xFF

    client.enableApiControl(True, vehicle_name)

    speed = 1
    duration = 0.5

    if key == ord('w'):
        print("Moving forward")
        client.moveByVelocityZAsync(speed, 0, altitude, duration, vehicle_name=vehicle_name)

    elif key == ord('s'):
        print("Moving backward")
        client.moveByVelocityZAsync(-speed, 0, altitude, duration, vehicle_name=vehicle_name)

    elif key == ord('a'):
        print("Moving left")
        client.moveByVelocityZAsync(0, -speed, altitude, duration, vehicle_name=vehicle_name)

    elif key == ord('d'):
        print("Moving right")
        client.moveByVelocityZAsync(0, speed, altitude, duration, vehicle_name=vehicle_name)

    elif key == ord('r'):
        altitude -= 0.5
        altitude = max(-10, min(-1, altitude))
        print("Moving up. Altitude:", altitude)
        client.moveByVelocityZAsync(0, 0, altitude, duration, vehicle_name=vehicle_name)

    elif key == ord('f'):
        altitude += 0.5
        altitude = max(-10, min(-1, altitude))
        print("Moving down. Altitude:", altitude)
        client.moveByVelocityZAsync(0, 0, altitude, duration, vehicle_name=vehicle_name)

    elif key == ord('q'):
        break

print("Landing...")
client.landAsync(vehicle_name=vehicle_name).join()
client.armDisarm(False, vehicle_name)
client.enableApiControl(False, vehicle_name)
cv2.destroyAllWindows()