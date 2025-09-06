import os
import requests
from urllib.parse import urlparse
import sys
import uuid
import hashlib

def get_file_hash(file_bytes):
    """Return MD5 hash of given file content for duplicate detection."""
    return hashlib.md5(file_bytes).hexdigest()

def fetch_images():
    print("🌍 The Wisdom of Ubuntu: 'I am because we are'")
    print("Let's fetch and share images with the community!\n")
    
    # Prompt the user for multiple URLs
    print("Enter image URLs (comma-separated or newline-separated).")
    print("When done, just press Enter on a blank line.\n")
    
    urls = []
    while True:
        url = input("Image URL: ").strip()
        if url == "":
            break
        urls.extend([u.strip() for u in url.split(",") if u.strip()])
    
    if not urls:
        print("❌ No URLs provided. Exiting.")
        sys.exit(0)
    
    # Directory for fetched images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)
    
    # Track downloaded hashes to prevent duplicates
    downloaded_hashes = set()
    
    for idx, url in enumerate(urls, 1):
        try:
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()
            
            # ✅ Check Content-Type header
            content_type = response.headers.get("Content-Type", "").lower()
            if not content_type.startswith("image/"):
                print(f"⚠️ [{idx}] Skipped (not an image): {url} ({content_type})")
                continue
            
            # ✅ Check Content-Length to avoid huge files
            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > 10 * 1024 * 1024:  # >10MB
                print(f"⚠️ [{idx}] Skipped (file too large): {url}")
                continue
            
            # Read file content
            file_bytes = response.content
            
            # ✅ Check for duplicate via hash
            file_hash = get_file_hash(file_bytes)
            if file_hash in downloaded_hashes:
                print(f"⚠️ [{idx}] Duplicate skipped: {url}")
                continue
            downloaded_hashes.add(file_hash)
            
            # Extract filename or generate unique one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename or "." not in filename:
                ext = content_type.split("/")[-1] if "/" in content_type else "jpg"
                filename = f"image_{uuid.uuid4().hex[:8]}.{ext}"
            
            filepath = os.path.join(save_dir, filename)
            
            # Save file
            with open(filepath, "wb") as f:
                f.write(file_bytes)
            
            print(f"✅ [{idx}/{len(urls)}] Saved: {filepath}")
        
        except requests.exceptions.MissingSchema:
            print(f"❌ [{idx}] Invalid URL format: {url}")
        except requests.exceptions.HTTPError as e:
            print(f"❌ [{idx}] HTTP Error for {url}: {e}")
        except requests.exceptions.ConnectionError:
            print(f"❌ [{idx}] Connection failed for {url}")
        except requests.exceptions.Timeout:
            print(f"❌ [{idx}] Timeout for {url}")
        except Exception as e:
            print(f"❌ [{idx}] Unexpected error for {url}: {e}")

    print("\n🎉 All done! Check your 'Fetched_Images' folder for saved images.")

if __name__ == "__main__":
    fetch_images()
