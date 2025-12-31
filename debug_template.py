
import django
from django.conf import settings
from django.template import Template, Context, Engine

# Minimal Django settings configuration
if not settings.configured:
    settings.configure(
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
        }],
        INSTALLED_APPS=['django.contrib.staticfiles'],
    )
    django.setup()

# The proposed template content
template_content = """
{% block content %}
<div class="min-h-screen w-full flex bg-white font-sans">
    
    <!-- LEFT SIDE: Form & Function -->
    <div class="w-full lg:w-1/2 flex flex-col p-8 lg:p-16 xl:p-24 relative z-10">
        <!-- Header (Logo + Login Link) -->
        <div class="flex items-center justify-between mb-12">
            <a href="{% url 'home' %}" class="flex items-center gap-2 group">
                <div class="w-8 h-8 bg-brand-600 text-white rounded-lg flex items-center justify-center font-bold text-xl">
                    <i class="fa-brands fa-google"></i>
                </div>
                <span class="text-xl font-bold text-slate-900 tracking-tight">GCP<span class="text-brand-600">Mastery</span></span>
            </a>
            <div class="text-sm font-medium text-slate-600">
                Already a member? <a href="{% url 'login' %}" class="text-brand-600 font-bold hover:underline ml-1">Log in</a>
            </div>
        </div>

        <!-- Main Form Content -->
        <div class="flex-1 flex flex-col justify-center max-w-md mx-auto w-full">
            <div class="mb-10">
                <h1 class="text-3xl lg:text-4xl font-extrabold text-slate-900 mb-3 tracking-tight">Create your account</h1>
                <p class="text-slate-500 text-base">Start your 30-day roadmap to Google Cloud certification.</p>
            </div>

            <form method="post" class="space-y-6">
                {% csrf_token %}

                {% if form.non_field_errors %}
                <div class="bg-red-50 border border-red-100 text-red-600 px-4 py-3 rounded-xl text-sm font-medium animate-pulse">
                    {% for error in form.non_field_errors %}
                    <p class="flex items-center gap-2">
                        <i class="fa-solid fa-circle-exclamation"></i> {{ error }}
                    </p>
                    {% endfor %}
                </div>
                {% endif %}

                {% for field in form %}
                <div class="space-y-2 group/field">
                    <label for="{{ field.id_for_label }}" class="block text-xs font-bold text-slate-700 uppercase tracking-wide group-focus-within/field:text-brand-600 transition-colors">
                        {{ field.label }}
                    </label>
                    
                    <div class="relative">
                        <input type="{{ field.field.widget.input_type }}" name="{{ field.name }}" id="{{ field.id_for_label }}" 
                               class="w-full px-4 py-3.5 rounded-xl bg-slate-50 border border-slate-200 text-slate-900 text-sm font-medium focus:bg-white focus:ring-4 focus:ring-brand-500/10 focus:border-brand-500 outline-none transition-all duration-200 placeholder:text-slate-400" 
                               placeholder=" " 
                               {% if field.field.required %}required{% endif %} 
                               {% if field.help_text %}aria-describedby="{{ field.id_for_label }}_help"{% endif %}>
                    </div>

                    {% if field.help_text and not field.errors %}
                    <p id="{{ field.id_for_label }}_help" class="text-xs text-slate-400 font-medium">
                        {{ field.help_text }}
                    </p>
                    {% endif %}

                    {% if field.errors %}
                    <div class="text-red-500 text-xs mt-1 space-y-1 font-medium">
                        {% for error in field.errors %}
                        <p class="flex items-center gap-1">
                            <i class="fa-solid fa-xmark"></i> {{ error }}
                        </p>
                        {% endfor %}
                    </div>
                    {% endif %}
                </div>
                {% endfor %}

                <button type="submit" 
                        class="w-full bg-brand-600 hover:bg-brand-700 text-white font-bold py-4 px-6 rounded-xl shadow-lg shadow-brand-600/20 hover:shadow-xl hover:shadow-brand-600/30 hover:-translate-y-0.5 transition-all duration-200 flex items-center justify-center gap-2 text-sm uppercase tracking-wider mt-4">
                    <span>Get Started</span>
                    <i class="fa-solid fa-arrow-right"></i>
                </button>
            </form>

            <p class="mt-8 text-xs text-slate-400 text-center leading-relaxed">
                By clicking "Get Started", you agree to our 
                <a href="#" class="text-slate-600 hover:text-brand-600 font-medium underline">Terms</a> and 
                <a href="#" class="text-slate-600 hover:text-brand-600 font-medium underline">Privacy Policy</a>.
            </p>
        </div>
    </div>

    <!-- RIGHT SIDE: Visual/Brand -->
    <div class="hidden lg:flex w-1/2 bg-slate-900 relative overflow-hidden items-center justify-center p-12">
        <!-- Abstract Background -->
        <div class="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20 mix-blend-soft-light"></div>
        <div class="absolute inset-0 bg-gradient-to-br from-brand-900 via-slate-900 to-slate-900"></div>
        <div class="absolute top-0 right-0 w-[600px] h-[600px] bg-brand-600/20 rounded-full blur-[120px] -translate-y-1/2 translate-x-1/2"></div>
        <div class="absolute bottom-0 left-0 w-[600px] h-[600px] bg-indigo-600/20 rounded-full blur-[120px] translate-y-1/2 -translate-x-1/2"></div>

        <!-- Content Content -->
        <div class="relative z-10 max-w-lg">
            <div class="bg-white/10 backdrop-blur-xl border border-white/10 p-8 rounded-3xl shadow-2xl mb-8 transform rotate-1 hover:rotate-0 transition-transform duration-500">
                <div class="flex items-center gap-4 mb-6">
                    <div class="w-12 h-12 rounded-full bg-gradient-to-r from-brand-500 to-indigo-500 flex items-center justify-center text-white font-bold text-lg shadow-lg">
                        <i class="fa-solid fa-trophy"></i>
                    </div>
                    <div>
                        <h3 class="text-white font-bold text-lg">Goal: Google Cloud Architect</h3>
                        <p class="text-brand-200 text-sm">30 Day Zero-to-Hero Plan</p>
                    </div>
                </div>
                <div class="space-y-4">
                    <div class="flex items-center gap-3">
                        <div class="w-6 h-6 rounded-full bg-green-500/20 text-green-400 flex items-center justify-center text-xs"><i class="fa-solid fa-check"></i></div>
                        <span class="text-slate-200 text-sm font-medium">Structured Curriculum</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-6 h-6 rounded-full bg-green-500/20 text-green-400 flex items-center justify-center text-xs"><i class="fa-solid fa-check"></i></div>
                        <span class="text-slate-200 text-sm font-medium">Practice Quizzes</span>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="w-6 h-6 rounded-full bg-green-500/20 text-green-400 flex items-center justify-center text-xs"><i class="fa-solid fa-check"></i></div>
                        <span class="text-slate-200 text-sm font-medium">Mermaid Diagrams</span>
                    </div>
                </div>
            </div>
            
            <blockquote class="text-slate-300 font-medium italic text-lg leading-relaxed">
                "The structured approach of GCP Mastery helped me pass my ACE exam in just 4 weeks. The daily breakdown is a game changer."
            </blockquote>
            <div class="mt-4 flex items-center gap-3">
                <div class="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center text-xs text-slate-300 font-bold">JD</div>
                <span class="text-slate-400 text-sm font-semibold">Jane Doe, Cloud Engineer</span>
            </div>
        </div>
    </div>
</div>
{% endblock %}
"""

print("Attempting to parse template...")
try:
    # We only care about syntax validation here
    t = Template(template_content)
    print("SUCCESS: Template syntax is valid.")
except Exception as e:
    print(f"ERROR: Template syntax invalid.\n{e}")
