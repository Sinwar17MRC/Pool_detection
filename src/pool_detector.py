import cv2
import numpy as np
import argparse
import os

def process_image(img_path):
    image = cv2.imread(img_path)
    if image is None:
        return
        
    h, w = image.shape[:2]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Range tuned to capture pool water while ignoring gray roofs/asphalt
    lower_val = np.array([85, 70, 75]) 
    upper_val = np.array([135, 255, 255])
    mask = cv2.inRange(hsv, lower_val, upper_val)

    # Cleaning noise and bridging small gaps (small things like a palm branch over the pool or an object in general)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    results = []
    min_area = (h * w) * 0.005 # Dynamic threshold to ignore small objects/clutter

    for c in contours:
        area = cv2.contourArea(c)
        if area > min_area:
            hull = cv2.convexHull(c)
            solidity = float(area)/cv2.contourArea(hull) if cv2.contourArea(hull) > 0 else 0
            
            if solidity > 0.75:
                # Smoothing the edges while keeping high point density
                epsilon = 0.0015 * cv2.arcLength(c, True)
                poly = cv2.approxPolyDP(c, epsilon, True)
                results.append({'area': area, 'poly': poly})

    # Sort by area descending
    results.sort(key=lambda x: x['area'], reverse=True)

    final_img = image.copy()
    with open("coordinates.txt", "w") as f:
        for i, item in enumerate(results):
            pool_id = i + 1
            pts = item['poly']
            
            # Draw outline
            cv2.drawContours(final_img, [pts], -1, (0, 0, 255), 1, lineType=cv2.LINE_AA)

            # Edge-aware labels
            bx, by, bw, bh = cv2.boundingRect(pts)
            tx = max(10, min(bx, w - 150))
            ty = by - 10 if by > 40 else by + bh + 25
            
            txt = f"Pool {pool_id} (Area: {int(item['area'])})"
            cv2.putText(final_img, txt, (tx, ty), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            cv2.putText(final_img, txt, (tx, ty), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

            # Save coordinates
            f.write(f"--- Pool {pool_id} ---\n")
            for p_idx, p in enumerate(pts.reshape(-1, 2)):
                f.write(f"pt{p_idx+1}: {p[0]},{p[1]}\n")
            f.write("\n")

    cv2.imwrite("output_image.jpg", final_img)
    print(f"Detected {len(results)} pools.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Image path")
    args = parser.parse_args()
    process_image(args.input)
