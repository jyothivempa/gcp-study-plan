import requests
import concurrent.futures
import re
import os
import time

BASE_URL = "http://127.0.0.1:8000"
CONTENT_DIR = r"d:\GCP\gcp-study-plan\curriculum\content"

def get_urls():
    urls = [
        "/",
        "/admin/",
        f"/static/GCP_Course_Complete.html"
    ]
    # Parse MODULE_INDEX.md to find all content pages
    index_path = os.path.join(CONTENT_DIR, "MODULE_INDEX.md")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Find links like [Link Name](filename.md)
            links = re.findall(r'\]\((.*?\.md)\)', content)
            for link in links:
                # Assuming the Django app serves markdown files at /curriculum/content/<filename>
                # or similar. Based on "curriculum" directory structure, let's guessing the URL pattern.
                # If these are just static files served by Django, we might need adjustments.
                # STARTING ASSUMPTION: The user has a Django app that renders these MD files.
                # If not, we just check if they are accessible as static or if the app has routes.
                # Let's assume a generic route pattern based on file administration.
                # OR, given the "gcp-study-plan" name, maybe /course/<filename>?
                
                # Let's try to find the urls from the urls.py if possible, but for now 
                # we will test generic patterns + the known HTML export.
                
                # Cleaning link
                clean_link = link.split("/")[-1]
                urls.append(f"/curriculum/{clean_link}") 
                urls.append(f"/content/{clean_link}")
                
    # Also add the new capstones and checklists
    urls.extend([
        "/curriculum/capstone_1_static_website.md",
        "/curriculum/capstone_2_serverless_api.md",
        "/curriculum/capstone_3_enterprise_network.md",
        "/curriculum/production_checklists.md",
        "/curriculum/decision_tables.md",
        "/curriculum/MODULE_INDEX.md"
    ])
    
    return list(set(urls)) # Deduplicate

def check_url(url):
    full_url = f"{BASE_URL}{url}"
    try:
        start = time.time()
        response = requests.get(full_url, timeout=5)
        duration = time.time() - start
        
        status = response.status_code
        size = len(response.content)
        
        if status == 200:
            return f"✅ {url.ljust(40)} | 200 OK | {size} bytes | {duration:.2f}s"
        elif status == 404:
            return f"❌ {url.ljust(40)} | 404 Not Found"
        else:
            return f"⚠️ {url.ljust(40)} | {status}"
            
    except requests.exceptions.ConnectionError:
        return f"💀 {url.ljust(40)} | Connection Refused (Is server running?)"
    except Exception as e:
        return f"⚠️ {url.ljust(40)} | Error: {str(e)}"

def run_parallel_tests():
    print(f"Testing URLs against {BASE_URL}...")
    urls = get_urls()
    print(f"Found {len(urls)} potential endpoints to test.")
    
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            results.append(future.result())
            
    # Sort results for readability (Failures first)
    results.sort(key=lambda x: "✅" in x)
    
    print("\n" + "="*60)
    print("TEST RESULTS")
    print("="*60)
    for res in results:
        print(res)
    print("="*60)

if __name__ == "__main__":
    run_parallel_tests()
