from curriculum.models import Course

def remove_azure():
    print("--- Removing Azure Content ---")
    try:
        azure = Course.objects.get(slug='azure')
        print(f"Found Azure Course: {azure.title}")
        
        # This cascades to Weeks and Days because of on_delete=models.CASCADE
        azure.delete() 
        print("✅ Azure Course and all related content deleted.")
        
    except Course.DoesNotExist:
        print("🆗 Azure Course not found (already deleted).")

if __name__ == '__main__':
    pass
