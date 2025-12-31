import os
import django
import sys

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcp_study_plan.settings')
django.setup()

from curriculum.models import Day

# 1. Define the new content assets
image_path = "/static/images/cloud_vs_onprem_diagram_1767030848331.png"

# Interactive "Flip Card" Style HTML Component
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

# Existing content (we'll prepend/append to this or just set it fresh if we want to be clean)
# Ideally, we want to keep the text but add these visuals
current_day = Day.objects.get(number=1)

# Prepend Image
new_content = f"![Cloud vs On-Prem]({image_path})\n\n" + current_day.concept_content

# Append Interactive HTML (using safe filter in template allows this)
new_content += "\n\n" + interactive_html

# Save
current_day.concept_content = new_content
current_day.save()

print("Successfully updated Day 1 content with visuals and interactivity.")
