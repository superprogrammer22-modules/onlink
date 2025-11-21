import os
import sys
# Import all public functions from the onlink package
from onlink import Url, Open, Read, Search, Image, Fetch, Show, __version__

# --- Configuration ---
SEARCH_TERM = "latest trends in AI deep learning"
WEB_PAGE_URL = "https://en.wikipedia.org/wiki/Artificial_intelligence"
IMAGE_QUERY = "futuristic robot concept art"
IMAGE_SIZE = "800x600" # Target size for image display/resize

# Check for OpenCV (cv2) display compatibility
# Image display functions (Fetch and Show) require an interactive environment
# that supports cv2.imshow(). We'll wrap these in a check.
def is_interactive_cv2_available():
    """Checks if we can likely run cv2.imshow/waitKey without crashing."""
    # This is a basic check. Real environment compatibility may vary.
    return 'cv2' in sys.modules and os.environ.get('DISPLAY') is not None


# --- 1. Basic Utility Functions ---
print(f"--- ONLINK Package Demo (Version {__version__}) ---")
print("\n[1. URL Helper & Browser Opener]")
print(f"Original input: 'google.com/maps'")
# Demonstrate Url normalization
normalized_url = Url("google.com/maps")
print(f"Normalized URL (Url()): {normalized_url}")
print("If you uncomment the line below, it will open the URL in your default browser.")
# Open(normalized_url)
# print("Browser opened (uncommented).")


# --- 2. Content Reader ---
print("\n[2. Webpage Content Reader (Read)]")
print(f"Fetching and processing text from: {WEB_PAGE_URL}")
try:
    # Read text with a line break target around 100 characters (80-130 range)
    content = Read(WEB_PAGE_URL, line_break=100)
    
    if content:
        # Display the first 1000 characters of the structured text
        print("--- Extracted Text Preview (First 1000 chars) ---")
        print(content[:1000] + "...")
        print(f"Total characters extracted: {len(content)}")
    else:
        print("READ FAILED: Could not extract content from the URL.")
except Exception as e:
    print(f"An error occurred during Read operation: {e}")


# --- 3. Search Functions ---
print("\n[3. Search Functionality]")

# A. Text Search (Search)
print(f"\n--- Text Search: '{SEARCH_TERM}' ---")
text_urls = Search(search=SEARCH_TERM, results=3)
if text_urls:
    print(f"Found {len(text_urls)} result URLs:")
    for i, url in enumerate(text_urls):
        print(f"  {i+1}: {url}")
else:
    print("Text search returned no results.")

# B. Image Search (Image)
print(f"\n--- Image Search: '{IMAGE_QUERY}' ---")
image_urls = Image(search=IMAGE_QUERY, results=2)
if image_urls:
    print(f"Found {len(image_urls)} image URLs:")
    for i, url in enumerate(image_urls):
        print(f"  {i+1}: {url}")
else:
    print("Image search returned no image URLs.")


# --- 4. Image Display Functions (Requires Interactive Environment) ---
print("\n[4. Image Display (Fetch & Show)]")

if not is_interactive_cv2_available():
    print("WARNING: OpenCV image display functions (Fetch/Show) are skipped.")
    print("These require an active graphical environment supporting cv2.imshow/waitKey.")
    print("To run, execute the commented code blocks below on a machine with a display server.")
else:
    print(f"OpenCV environment detected. Testing image display at size: {IMAGE_SIZE}...")
    
    # A. Display Images from a Search (Show)
    if image_urls:
        print("\nAttempting to open images found via Image() search (Show())...")
        # NOTE: This call will block until you close the opened image window(s).
        # loaded_search_images = Show(image_urls, size=IMAGE_SIZE)
        # print(f"Successfully loaded and displayed {len(loaded_search_images)} search images.")
        print("--> Show() demo skipped. Uncomment line 79 to run.")


    # B. Display Images from a Webpage (Fetch)
    print(f"\nAttempting to fetch and display images from: {WEB_PAGE_URL} (Fetch())...")
    # NOTE: This call will block until you close the opened image window(s).
    # loaded_page_images = Fetch(WEB_PAGE_URL, max_images=2, size=IMAGE_SIZE)
    # print(f"Successfully loaded and displayed {len(loaded_page_images)} images from the webpage.")
    print("--> Fetch() demo skipped. Uncomment line 86 to run.")

print("\n--- Demo Complete ---")