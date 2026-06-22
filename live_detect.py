from ultralytics import YOLO
import cv2
import csv
import os
import time
from datetime import datetime

# =========================
# SETTINGS
# =========================

SHOW_WINDOW = False

# =========================
# LOAD MODEL
# =========================

model = YOLO("training/weights/best.pt")

print("=================================")
print("🦺 SAFETYEYE AI MONITORING")
print("=================================")

# =========================
# CREATE FOLDERS
# =========================

os.makedirs("alerts", exist_ok=True)
os.makedirs("alerts/screenshots", exist_ok=True)

# =========================
# ALERT CSV
# =========================

alert_file = "alerts/alerts.csv"

if not os.path.exists(alert_file):

    with open(alert_file, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Time",
            "Alert"
        ])

# =========================
# OCCUPANCY LOG
# =========================

if not os.path.exists(
    "occupancy_log.csv"
):

    with open(
        "occupancy_log.csv",
        "w"
    ) as f:

        f.write(
            "Time,Occupancy\n"
        )

# =========================
# CAMERA
# =========================

cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("❌ Camera Not Found")

    exit()

last_alert_time = 0
last_occ_log = 0

print("✅ SafetyEye Started")
# =========================
# MAIN LOOP
# =========================

while True:

    ret, frame = cap.read()

    if not ret:

        print("❌ Camera Error")

        break

    # =========================
    # YOLO DETECTION
    # =========================

    results = model(
        frame,
        conf=0.4
    )

    annotated_frame = (
        results[0].plot()
    )

    # =========================
    # PERSON COUNT
    # =========================

    person_count = 0

    for box in results[0].boxes:

        cls = int(
            box.cls[0]
        )

        label = model.names[
            cls
        ]

        if label == "Person":

            person_count += 1

    worker_count = (
        person_count
    )

    # =========================
    # SAVE OCCUPANCY
    # =========================

    with open(
        "occupancy.txt",
        "w"
    ) as f:

        f.write(
            str(worker_count)
        )

    # =========================
    # OCCUPANCY LOG
    # =========================

    if (
        time.time()
        - last_occ_log
        > 5
    ):

        with open(
            "occupancy_log.csv",
            "a"
        ) as f:

            f.write(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{worker_count}\n"
            )

        print(
            f"Occupancy Logged: {worker_count}"
        )

        last_occ_log = (
            time.time()
        )

    # =========================
    # LIVE DASHBOARD FRAME
    # =========================

    cv2.imwrite(
        "latest_frame.jpg",
        annotated_frame
    )
        # =========================
    # VIOLATION DETECTION
    # =========================

    current_time = time.time()

    for box in results[0].boxes:

        cls = int(
            box.cls[0]
        )

        label = model.names[
            cls
        ]

        if label in [

            "NO-Hardhat",

            "NO-Safety Vest",

            "NO-Mask"

        ]:

            if (
                current_time
                - last_alert_time
                > 5
            ):

                if (
                    label
                    == "NO-Hardhat"
                ):

                    alert = (
                        "Worker without Helmet"
                    )

                elif (
                    label
                    == "NO-Safety Vest"
                ):

                    alert = (
                        "Worker without Safety Vest"
                    )

                else:

                    alert = (
                        "Worker without Mask"
                    )

                print(
                    "⚠",
                    alert
                )

                # =========================
                # SAVE ALERT CSV
                # =========================

                with open(

                    alert_file,

                    "a",

                    newline=""

                ) as f:

                    writer = csv.writer(f)

                    writer.writerow([

                        datetime.now()
                        .strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),

                        alert

                    ])

                # =========================
                # SAVE SCREENSHOT
                # =========================

                screenshot_name = (

                    "alerts/screenshots/"

                    + str(
                        int(
                            time.time()
                        )
                    )

                    + ".jpg"

                )

                cv2.imwrite(

                    screenshot_name,

                    annotated_frame

                )

                last_alert_time = (
                    current_time
                )
                    # =========================
    # OPTIONAL CAMERA WINDOW
    # =========================

    if SHOW_WINDOW:

        cv2.imshow(
            "SafetyEye Live Detection",
            annotated_frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):

            print(
                "Stopping SafetyEye..."
            )

            break

# =========================
# CLEANUP
# =========================

cap.release()

if SHOW_WINDOW:

    cv2.destroyAllWindows()

print(
    "✅ Detection Stopped"
)