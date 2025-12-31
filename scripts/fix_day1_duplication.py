import os
import django
import sys

# Setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day

def fix_duplication():
    import re
    day = Day.objects.get(number=1)
    content = day.concept_content

    # 1. Define the exact strings to identify and remove
    image_markdown = "![Cloud vs On-Prem](/static/images/cloud_vs_onprem_diagram_1767030848331.png)"
    
    # 2. DEFINITIONS
    interactive_html = """
<div class="my-12">
    <h3 class="text-2xl font-bold text-slate-800 mb-6 flex items-center gap-3">
        <i class="fa-solid fa-pizza-slice text-brand-500"></i>
        Interactive Analogy: Pizza as a Service
    </h3>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- On-Premises Card -->
        <div class="group relative h-64 perspective-1000 cursor-pointer" onclick="this.classList.toggle('flipped')">
            <div class="relative w-full h-full transition-transform duration-700 transform-style-3d group-[.flipped]:rotate-y-180">
                <!-- Front -->
                <div class="absolute inset-0 backface-hidden bg-white border-2 border-slate-200 rounded-2xl p-6 flex flex-col items-center justify-center shadow-lg group-hover:border-brand-400 transition-colors">
                    <div class="w-16 h-16 bg-slate-100 rounded-full flex items-center justify-center mb-4 text-3xl">\U0001F3E0</div>
                    <h4 class="text-xl font-bold text-slate-800">On-Premises</h4>
                    <p class="text-xs text-slate-500 mt-2 uppercase tracking-widest font-bold">Made at Home</p>
                    <p class="text-sm text-brand-600 mt-4 font-bold animate-pulse">Click to Reveal</p>
                </div>
                <!-- Back -->
                <div class="absolute inset-0 backface-hidden bg-slate-900 rounded-2xl p-6 flex flex-col items-center justify-center rotate-y-180 text-white shadow-xl">
                    <h4 class="text-lg font-bold text-brand-400 mb-2">You Manage Everything</h4>
                    <ul class="text-sm space-y-2 text-slate-300">
                        <li><i class="fa-solid fa-check text-green-400 mr-2"></i>Buy Ingredients</li>
                        <li><i class="fa-solid fa-check text-green-400 mr-2"></i>Own the Oven</li>
                        <li><i class="fa-solid fa-check text-green-400 mr-2"></i>Bake & Serve</li>
                        <li><i class="fa-solid fa-check text-green-400 mr-2"></i>Clean the Kitchen</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- SaaS Card -->
        <div class="group relative h-64 perspective-1000 cursor-pointer" onclick="this.classList.toggle('flipped')">
            <div class="relative w-full h-full transition-transform duration-700 transform-style-3d group-[.flipped]:rotate-y-180">
                <!-- Front -->
                <div class="absolute inset-0 backface-hidden bg-white border-2 border-brand-100 rounded-2xl p-6 flex flex-col items-center justify-center shadow-lg group-hover:border-brand-400 transition-colors">
                    <div class="w-16 h-16 bg-brand-50 rounded-full flex items-center justify-center mb-4 text-3xl">\U0001F355</div>
                    <h4 class="text-xl font-bold text-brand-900">SaaS (Cloud)</h4>
                    <p class="text-xs text-brand-400 mt-2 uppercase tracking-widest font-bold">Dining Out</p>
                    <p class="text-sm text-brand-600 mt-4 font-bold animate-pulse">Click to Reveal</p>
                </div>
                <!-- Back -->
                <div class="absolute inset-0 backface-hidden bg-brand-600 rounded-2xl p-6 flex flex-col items-center justify-center rotate-y-180 text-white shadow-xl">
                    <h4 class="text-lg font-bold text-white mb-2">Vendor Manages All</h4>
                    <ul class="text-sm space-y-2 text-brand-100">
                        <li><i class="fa-solid fa-check text-white mr-2"></i>Just Show Up</li>
                        <li><i class="fa-solid fa-check text-white mr-2"></i>Eat the Pizza</li>
                        <li><i class="fa-solid fa-check text-white mr-2"></i>Pay the Bill</li>
                        <li><i class="fa-solid fa-xmark text-red-300 mr-2"></i>No Cleaning!</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <p class="text-center text-xs text-slate-400 mt-4 italic">Tap/Click cards to flip</p>
</div>
"""
    
    # 3. CLEAN UP
    # Remove all instances of image
    clean_content = content.replace(image_markdown, "")
    
    # Remove all instances of Pizza block (using regex to be safe about whitespace/newlines)
    # The block starts with <div class="my-12"> and contains "Pizza as a Service"
    # We'll use a regex that matches the start tag up to the "Tap/Click cards to flip</p>\n</div>" end sequence
    
    # Note: re.DOTALL makes . match newlines
    # Pattern: <div class="my-12"> ... Pizza as a Service ... </div>
    # But "</div>" is common. We know the end text is "Tap/Click cards to flip</p>\n</div>"
    
    pizza_pattern = r'<div class="my-12">.*?Pizza as a Service.*?Tap/Click cards to flip</p>\s*</div>'
    
    clean_content = re.sub(pizza_pattern, '', clean_content, flags=re.DOTALL)
    
    # Clean up excessive newlines (more than 2)
    clean_content = re.sub(r'\n{3,}', '\n\n', clean_content).strip()
    
    # 4. RE-INJECT
    final_content = f"{image_markdown}\n\n{clean_content}\n\n{interactive_html.strip()}"
    
    # 5. VERIFY
    img_count = final_content.count(image_markdown)
    # We count "Pizza as a Service" title occurrence
    pizza_title = "Interactive Analogy: Pizza as a Service"
    pizza_count = final_content.count(pizza_title)
    
    print(f"Correction Report:")
    print(f"Image Count: {img_count}")
    print(f"Pizza Block Count: {pizza_count}")
    
    if img_count == 1 and pizza_count == 1:
        day.concept_content = final_content
        day.save()
        print("SUCCESS: Day 1 content deduped and saved.")
    else:
        print("WARNING: Dedup failed logic check. Not saving.")


if __name__ == "__main__":
    fix_duplication()
