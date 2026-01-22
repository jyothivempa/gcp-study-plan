import os
import re
import markdown
import datetime

CONTENT_DIR = r"d:\GCP\gcp-study-plan\curriculum\content"
OUTPUT_MD = r"d:\GCP\gcp-study-plan\GCP_Course_Complete.md"
OUTPUT_HTML = r"d:\GCP\gcp-study-plan\GCP_Course_Complete.html"

def get_file_order():
    files = [f for f in os.listdir(CONTENT_DIR) if f.endswith(".md") and f.startswith("section_")]
    
    # Sort key: extract the first number found in the filename
    def sort_key(filename):
        match = re.search(r"section_(\d+)_", filename)
        if match:
            return int(match.group(1))
        return 9999
    
    sorted_files = sorted(files, key=sort_key)
    
    # Prepend Index if exists
    if os.path.exists(os.path.join(CONTENT_DIR, "MODULE_INDEX.md")):
        sorted_files.insert(0, "MODULE_INDEX.md")
    
    # Append standalone resources including new Capstones and Reference Guides
    extras = [
        "mini_projects.md",
        "capstone_1_static_website.md",
        "capstone_2_serverless_api.md",
        "capstone_3_enterprise_network.md",
        "decision_tables.md",
        "production_checklists.md",
        "interview_question_bank.md",
        "interview_guide.md"
    ]
    final_list = sorted_files + [x for x in extras if os.path.exists(os.path.join(CONTENT_DIR, x))]
    
    return final_list

def create_merged_documents():
    files = get_file_order()
    print(f"Merging {len(files)} files...")
    
    full_md = "# GCP Associate Cloud Engineer - Complete Course Curriculum\n\n"
    
    # CSS for printing
    # Premium CSS with Printing Support
    css = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #1a73e8;
            --secondary: #ea4335;
            --success: #34a853;
            --text-main: #202124;
            --text-muted: #5f6368;
            --bg-body: #f8f9fa;
            --bg-card: #ffffff;
            --code-bg: #2d2d2d;
            --border: #e0e0e0;
        }
        
        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            line-height: 1.7;
            color: var(--text-main);
            background-color: var(--bg-body);
            margin: 0;
            padding: 40px;
        }

        /* Container for readability */
        article {
            max-width: 800px;
            margin: 0 auto 60px auto;
            background: var(--bg-card);
            padding: 60px;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        /* Typography */
        h1, h2, h3, h4 { color: #202124; font-weight: 700; letter-spacing: -0.02em; margin-top: 1.5em; }
        h1 { 
            text-align: center; font-size: 2.5rem; 
            border-bottom: 3px solid var(--primary); padding-bottom: 20px; color: var(--primary); 
            margin-top: 0;
        }
        h2 { font-size: 1.8rem; border-left: 5px solid var(--primary); padding-left: 15px; margin-top: 2.5em; }
        h3 { font-size: 1.4rem; color: #444; margin-top: 2em; }
        p, li { font-size: 1.05rem; color: #374151; }
        strong { color: #111; font-weight: 600; }

        /* Code Blocks */
        pre {
            background-color: var(--code-bg);
            color: #f8f8f2;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 1px solid #444;
        }
        code {
            font-family: 'JetBrains Mono', monospace;
            background-color: #f1f3f4;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.9em;
            color: #d63384;
        }
        pre code { background: none; color: inherit; padding: 0; }

        /* Tables */
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 30px 0;
            font-size: 0.95rem;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        th { background-color: var(--primary); color: white; padding: 15px; text-align: left; font-weight: 600; }
        td { padding: 12px 15px; border-bottom: 1px solid var(--border); }
        tr:nth-child(even) { background-color: #f8f9fa; }
        tr:hover { background-color: #f1f5f9; }

        /* Blockquotes / Alerts */
        blockquote {
            background: #f0f7ff;
            border-left: 6px solid var(--primary);
            margin: 30px 0;
            padding: 20px 25px;
            border-radius: 0 8px 8px 0;
            color: #2c3e50;
            font-style: normal;
        }
        
        /* Links */
        a { color: var(--primary); text-decoration: none; border-bottom: 1px solid transparent; transition: all 0.2s; }
        a:hover { border-bottom-color: var(--primary); opacity: 0.8; }

        /* Divider & Page Breaks */
        hr { border: 0; height: 1px; background: #e5e7eb; margin: 50px 0; }
        .page-break { page-break-after: always; display: block; height: 0; margin: 0; }

        /* Print Optimization */
        @media print {
            body { background: white; padding: 0; }
            article { box-shadow: none; padding: 0; margin: 0; max-width: 100%; }
            h1, h2 { color: black !important; border-color: #000 !important; }
            pre { background: #f5f5f5; color: black; border: 1px solid #ccc; }
            code { color: #000; }
            a { color: #000; text-decoration: underline; }
            .page-break { page-break-after: always; }
            /* Hide nav links in print */
            a[href^="#"] { display: none; } 
        }

        /* Progress Bar */
        .progress-container {
            padding: 0 20px 20px 20px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 20px;
        }
        .progress-text {
            display: flex; justify-content: space-between;
            font-size: 0.85rem; color: var(--text); opacity: 0.8; margin-bottom: 8px;
        }
        .progress-bar-bg {
            background: var(--border); height: 8px; border-radius: 4px; overflow: hidden;
        }
        .progress-bar-fill {
            height: 100%; background: var(--success); width: 0%;
            transition: width 0.5s ease-in-out;
        }

        /* Scroll Behavior */
        html { scroll-behavior: smooth; }

        /* Mobile & Responsive */
        .mobile-toggle {
            display: none; position: fixed; top: 15px; left: 15px; z-index: 200;
            background: var(--card-bg); border: 1px solid var(--border);
            padding: 8px; border-radius: 6px; cursor: pointer; color: var(--text);
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        @media (max-width: 768px) {
            #sidebar { transform: translateX(-100%); transition: transform 0.3s; box-shadow: 2px 0 10px rgba(0,0,0,0.1); }
            #sidebar.open { transform: translateX(0); }
            main { margin-left: 0; padding: 20px 15px; margin-top: 40px; }
            article { padding: 20px; }
            .mobile-toggle { display: block; }
            h1 { font-size: 1.75rem; }
        }

        /* Back to Top */
        .back-to-top {
            position: fixed; bottom: 30px; right: 30px;
            background: var(--primary); color: white;
            width: 45px; height: 45px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; opacity: 0; pointer-events: none;
            transition: all 0.3s; z-index: 90;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: none; font-size: 1.2rem;
        }
        .back-to-top.visible { opacity: 1; pointer-events: auto; }
        .back-to-top:hover { transform: translateY(-2px); background: var(--primary-dark); }

        /* Print Optimization */
        @media print {
            #sidebar, .copy-btn, .mobile-toggle, .back-to-top { display: none; }
            main { margin: 0; padding: 0; max-width: 100%; }
            article { box-shadow: none; border: none; margin-bottom: 2rem; page-break-inside: avoid; }
            a { text-decoration: none; color: #000; }
            body { background: #fff; color: #000; }
            pre { border: 1px solid #ccc; }
        }
    </style>
    """
    
    # HTML Header with "Ultimate Feature Pack"
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GCP Course Complete</title>
        
        <!-- Fonts & Icons -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
        
        <!-- Syntax Highlighting -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/atom-one-dark.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>
        
    {css}
    </head>
    <body onload="initApp()">
    
    <!-- Mobile Toggle -->
    <button class="mobile-toggle" onclick="toggleSidebar()">☰</button>

    <nav id="sidebar">
        <div class="sidebar-header">
            <input type="text" id="search-input" placeholder="Search modules... (/)" onkeyup="filterModules()">
        </div>
        
        <!-- Progress Stats -->
        <div class="progress-container">
            <div class="progress-text">
                <span id="progress-count">0/0 Completed</span>
                <span id="progress-percent">0%</span>
            </div>
            <div class="progress-bar-bg">
                <div id="progress-fill" class="progress-bar-fill"></div>
            </div>
        </div>

        <div id="toc-container">
            <ul id="toc"></ul>
        </div>
        <div class="controls">
            <button class="btn" onclick="toggleTheme()">🌗 Theme</button>
            <button class="btn" onclick="resetProgress()">↺ Reset</button>
        </div>
    </nav>

    <main>
    """
    
    for filename in files:
        path = os.path.join(CONTENT_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            html_fragment = markdown.markdown(content, extensions=['tables', 'fenced_code'])
            module_id = filename.replace(".md", "")
            
            # Estimate Read Time (200 wpm)
            word_count = len(content.split())
            read_time = max(1, round(word_count / 200))
            
            # Inject Read Time Badge
            meta_html = f'<div style="margin-bottom: 20px; font-size: 0.85rem; color: var(--text); opacity: 0.7;">⏱️ {read_time} min read</div>'
            
            html_content += f'<article id="{module_id}">\n{meta_html}\n{html_fragment}\n</article>\n'

    html_content += """
    </main>
    
    <button class="back-to-top" onclick="scrollToTop()">↑</button>
    
    <script>
        function initApp() {
            hljs.highlightAll();
            setupIntersectionObserver();
            setupKeyboardShortcuts();
            generateTOC();
            loadProgress();
            loadTheme();
            addCopyButtons();
        }

        // 1. Generate TOC with Checkboxes
        function generateTOC() {
            const articles = document.querySelectorAll('article');
            const toc = document.getElementById('toc');
            
            articles.forEach(article => {
                const h1 = article.querySelector('h1');
                if (h1) {
                    const li = document.createElement('li');
                    
                    // Checkbox
                    const check = document.createElement('input');
                    check.type = 'checkbox';
                    check.className = 'progress-check';
                    check.dataset.id = article.id;
                    check.onclick = (e) => saveProgress(article.id, e.target.checked);
                    
                    // Link
                    const a = document.createElement('a');
                    a.textContent = h1.textContent.replace('# ', '').replace('Module ', '');
                    a.href = '#' + article.id;
                    a.title = h1.textContent;
                    
                    li.appendChild(check);
                    li.appendChild(a);
                    toc.appendChild(li);
                }
            });
        }

        // 2. Progress Tracking (LocalStorage)
        function saveProgress(id, isChecked) {
            let progress = JSON.parse(localStorage.getItem('gcp_progress') || '{}');
            progress[id] = isChecked;
            localStorage.setItem('gcp_progress', JSON.stringify(progress));
            updateProgressUI();
        }

        function loadProgress() {
            let progress = JSON.parse(localStorage.getItem('gcp_progress') || '{}');
            document.querySelectorAll('.progress-check').forEach(box => {
                if (progress[box.dataset.id]) box.checked = true;
            });
            updateProgressUI();
        }
        
        function updateProgressUI() {
            const total = document.querySelectorAll('.progress-check').length;
            const checked = document.querySelectorAll('.progress-check:checked').length;
            const percent = total === 0 ? 0 : Math.round((checked / total) * 100);
            
            document.title = `GCP Course (${percent}%)`;
            
            // Update Sidebar Stats
            const countEl = document.getElementById('progress-count');
            const percentEl = document.getElementById('progress-percent');
            const fillEl = document.getElementById('progress-fill');
            
            if(countEl) countEl.textContent = `${checked}/${total} Modules`;
            if(percentEl) percentEl.textContent = `${percent}%`;
            if(fillEl) fillEl.style.width = `${percent}%`;
        }
        
        function resetProgress() {
            if(confirm('Reset all progress?')) {
                localStorage.removeItem('gcp_progress');
                location.reload();
            }
        }

        // 3. Dark Mode
        function toggleTheme() {
            document.body.classList.toggle('dark');
            localStorage.setItem('theme', document.body.classList.contains('dark') ? 'dark' : 'light');
        }

        function loadTheme() {
            if (localStorage.getItem('theme') === 'dark') {
                document.body.classList.add('dark');
            }
        }

        // 4. Search
        function filterModules() {
            const query = document.getElementById('search-input').value.toLowerCase();
            const items = document.querySelectorAll('#toc li');
            
            items.forEach(li => {
                const text = li.querySelector('a').textContent.toLowerCase();
                li.style.display = text.includes(query) ? 'flex' : 'none';
            });
        }

        // 5. Copy Buttons
        function addCopyButtons() {
            document.querySelectorAll('pre').forEach(pre => {
                const btn = document.createElement('button');
                btn.className = 'copy-btn';
                btn.textContent = 'Copy';
                btn.onclick = () => {
                    navigator.clipboard.writeText(pre.innerText);
                    btn.textContent = 'Copied!';
                    setTimeout(() => btn.textContent = 'Copy', 2000);
                };
                pre.appendChild(btn);
            });
        }
    </script>
    <script>
        // 6. Intersection Observer for Active TOC
        function setupIntersectionObserver() {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        // Remove active class from all
                        document.querySelectorAll('#toc a').forEach(a => a.classList.remove('active'));
                        
                        // Add to current
                        const id = entry.target.id;
                        const link = document.querySelector(`#toc a[href="#${id}"]`);
                        if (link) {
                            link.classList.add('active');
                            // Auto-scroll TOC if needed
                            link.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                        }
                    }
                });
            }, { threshold: 0.1, rootMargin: "-100px 0px -60% 0px" });

            document.querySelectorAll('article').forEach(section => observer.observe(section));
        }

        // 7. Back to Top
        window.onscroll = () => {
            const btn = document.querySelector('.back-to-top');
            if (btn) {
                if (document.documentElement.scrollTop > 300) {
                    btn.classList.add('visible');
                } else {
                    btn.classList.remove('visible');
                }
            }
        };

        function scrollToTop() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // 8. Mobile Sidebar
        function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('open');
        }
        
        // Close sidebar when clicking a link on mobile
        document.addEventListener('click', (e) => {
            if (window.innerWidth < 768 && e.target.closest('#toc a')) {
                document.getElementById('sidebar').classList.remove('open');
            }
        });

        // 9. Keyboard Shortcuts
        function setupKeyboardShortcuts() {
            document.addEventListener('keydown', (e) => {
                // Search: /
                if (e.key === '/' && document.activeElement !== document.getElementById('search-input')) {
                    e.preventDefault();
                    document.getElementById('search-input').focus();
                }
                
                // Escape to blur
                if (e.key === 'Escape') {
                    if(document.activeElement === document.getElementById('search-input')) {
                        document.activeElement.blur();
                    }
                }
                
                // Theme: t
                if (e.key === 't' && document.activeElement.tagName !== 'INPUT') {
                    toggleTheme();
                }

                // Next/Prev: n / p
                if ((e.key === 'n' || e.key === 'p') && document.activeElement.tagName !== 'INPUT') {
                    // Find active active article or first visible
                    const articles = Array.from(document.querySelectorAll('article'));
                    let currentIdx = 0;
                    
                    // Simple heuristic: top of element is near top of viewport
                    for(let i=0; i<articles.length; i++) {
                        const rect = articles[i].getBoundingClientRect();
                        if(rect.top >= -100 && rect.top < 500) {
                            currentIdx = i;
                            break;
                        }
                    }

                    if (e.key === 'n' && currentIdx < articles.length - 1) {
                         const next = articles[currentIdx + 1];
                         // Offset for padding
                         const y = next.getBoundingClientRect().top + window.pageYOffset - 20;
                         window.scrollTo({top: y, behavior: 'smooth'});
                    }
                    if (e.key === 'p' && currentIdx > 0) {
                         const prev = articles[currentIdx - 1];
                         const y = prev.getBoundingClientRect().top + window.pageYOffset - 20;
                         window.scrollTo({top: y, behavior: 'smooth'});
                    }
                }
            });
        }
    </script>
    </body></html>
    """
    
    # Write MD
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(full_md)
        
    # Write HTML
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Created {OUTPUT_MD}")
    print(f"Created {OUTPUT_HTML}")

if __name__ == "__main__":
    import datetime
    create_merged_documents()
