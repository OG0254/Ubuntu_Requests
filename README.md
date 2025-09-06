# Ubuntu-Inspired Image Fetcher

🌍 **The Wisdom of Ubuntu: "I am because we are"**

This project is a simple Python script that fetches images from the internet, inspired by the Ubuntu philosophy of **community, respect, sharing, and practicality**.

---

## ✨ Features
- Fetch **multiple images at once** from given URLs
- **Validate safety**: only downloads valid images (JPEG, PNG, etc.)
- **Avoids large files**: skips files larger than 10 MB
- **Duplicate detection**: prevents saving the same image twice using MD5 hash
- **Error handling**: gracefully handles invalid URLs, timeouts, or connection errors
- Saves all images into a **Fetched_Images/** directory

---

## 🚀 How to Use

1. Clone or download this project.
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   fetch_images.py
   ```
4. Enter one or more image URLs (comma-separated or line by line). Press Enter on a blank line to finish.

All images will be saved inside the `Fetched_Images` folder.

---

## 🛡 Precautions Implemented
- Checks `Content-Type` header to ensure only images are downloaded.
- Skips files larger than **10MB**.
- Prevents **duplicate downloads** by checking file hashes.
- Handles common network errors (invalid URL, timeout, HTTP errors, etc.).

---

## 🧩 Example Run

```text
🌍 The Wisdom of Ubuntu: 'I am because we are'
Let's fetch and share images with the community!

Enter image URLs (comma-separated or newline-separated).
When done, just press Enter on a blank line.

Image URL: https://example.com/image1.jpg
Image URL: https://example.com/photo.png
Image URL:

✅ [1/2] Saved: Fetched_Images/image1.jpg
✅ [2/2] Saved: Fetched_Images/photo.png

🎉 All done! Check your 'Fetched_Images' folder for saved images.
```

---

## 🧭 Ubuntu Principles in Action
- **Community**: Connects with the global web community to fetch resources.  
- **Respect**: Handles errors politely, validates sources, and avoids unsafe downloads.  
- **Sharing**: Saves and organizes images for later use.  
- **Practicality**: Simple, safe, and useful in real-world contexts.  

---

## 📜 License
This project is provided for educational purposes and community sharing under the Ubuntu spirit.
