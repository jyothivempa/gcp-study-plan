document.addEventListener("DOMContentLoaded", () => {
    // 1. Syntax Highlighting
    if (window.hljs) {
        hljs.highlightAll();
    }

    // 2. Mermaid Diagram Support
    // Markdown renders: <pre><code class="language-mermaid">
    // Mermaid needs: <div class="mermaid">
    const mermaidBlocks = document.querySelectorAll('pre code.language-mermaid');
    mermaidBlocks.forEach(block => {
        const pre = block.parentElement;
        const div = document.createElement('div');
        div.className = 'mermaid';
        div.textContent = block.textContent;
        // Replace pre with div
        pre.replaceWith(div);
    });

    // 3. Premium Table Enhancement
    // Wrap tables in a responsive div to prevent overflow
    const tables = document.querySelectorAll('.prose table');
    tables.forEach(table => {
        const wrapper = document.createElement('div');
        wrapper.className = 'overflow-x-auto rounded-xl border border-slate-200 shadow-sm my-8';
        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);

        // Add styling classes to table
        table.classList.add('w-full', 'text-left', 'border-collapse');
    });

    // 4. GitHub-Style Admonitions (Alerts)
    // Converts > [!TIP] into a styled div
    const blockquotes = document.querySelectorAll('.prose blockquote');
    blockquotes.forEach(bq => {
        const p = bq.querySelector('p');
        if (!p) return;

        const content = p.innerHTML;
        let type = 'NOTE';
        let alertClass = 'bg-slate-50 border-l-4 border-slate-400 text-slate-700';
        let icon = '<i class="fa-solid fa-circle-info mr-2"></i>';
        let title = 'Note';

        // Detect Type
        if (content.includes('[!TIP]')) {
            type = 'TIP';
            alertClass = 'bg-emerald-50 border-l-4 border-emerald-500 text-emerald-800';
            icon = '<i class="fa-solid fa-lightbulb mr-2"></i>';
            title = 'Pro Tip';
        } else if (content.includes('[!WARNING]') || content.includes('[!IMPORTANT]')) {
            type = 'WARNING';
            alertClass = 'bg-amber-50 border-l-4 border-amber-500 text-amber-800';
            icon = '<i class="fa-solid fa-triangle-exclamation mr-2"></i>';
            title = 'Important';
        } else if (content.includes('[!CAUTION]')) {
            type = 'CAUTION';
            alertClass = 'bg-red-50 border-l-4 border-red-500 text-red-800';
            icon = '<i class="fa-solid fa-ban mr-2"></i>';
            title = 'Caution';
        } else if (content.includes('**Critical Exam Rule**') || content.includes('**Exam Watch**')) {
            // Custom detection for our content style
            type = 'EXAM';
            alertClass = 'bg-violet-50 border-l-4 border-violet-500 text-violet-800';
            icon = '<i class="fa-solid fa-graduation-cap mr-2"></i>';
            title = 'Exam Strategy';
        }

        if (type !== 'NOTE' || content.includes('[!NOTE]')) {
            // Clean content (remove the tag)
            let newContent = content
                .replace('[!TIP]', '')
                .replace('[!WARNING]', '')
                .replace('[!IMPORTANT]', '')
                .replace('[!CAUTION]', '')
                .replace('[!NOTE]', '');

            // Create Alert Box
            const alertBox = document.createElement('div');
            alertBox.className = `p-4 my-6 rounded-r-lg shadow-sm ${alertClass}`;
            alertBox.innerHTML = `
                <div class="flex items-center font-bold mb-1 text-sm uppercase tracking-wide opacity-80">
                    ${icon} ${title}
                </div>
                <div class="text-sm font-medium leading-relaxed opacity-90">
                    ${newContent}
                </div>
            `;

            bq.replaceWith(alertBox);
        } else {
            // Standard Blockquote Styling (if not an explicit alert)
            bq.classList.add('not-italic', 'bg-slate-50', 'p-6', 'rounded-xl', 'border-l-4', 'border-slate-300', 'shadow-sm', 'my-8');
        }
    });

});
