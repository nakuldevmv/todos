Yo Nakul, I’ve swapped out PrismJS for Highlight.js so you get dope auto-language detection, way more themes, and zero hassle with that components path. I’ve kept your dark/light toggle, color picker, fonts and styling intact. Peep the changes:

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Markdown Viewer</title>

  <!-- Inter font for a clean look -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">

  <!-- Highlight.js GitHub Dark theme -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github-dark.min.css">

  <link rel="icon" href="ico/icon.png" type="image/png">

  <style>
    /* your existing :root, scrollbar, body, typography, tables, images, blockquote,
       toggle button, color picker, etc. all stays the same */
  </style>
</head>

<body>
  <div class="wrapper">
    <input type="color" id="colorPicker" class="round-color-picker" value="#9673ff" />
    <input type="checkbox" id="hide-checkbox">
    <label for="hide-checkbox" class="toggle">…</label>
  </div>

  <div id="content" aria-live="polite">Loading markdown...</div>
  <h4 style="font-size:small; text-align:center; margin-top:2rem; color:var(--accent);">
    Made with ❤️ by <a style="text-decoration:none;" href="https://github.com/nakuldevmv">Nakul</a>
  </h4>

  <!-- core scripts -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/lib/common.min.js"></script>

  <script>
    // fetch + render with auto syntax highlighting
    const markdownUrl = `https://nakuldevmv.github.io/todos/oose.md?cb=${Date.now()}`;
    const contentDiv = document.getElementById('content');

    async function loadMarkdown() {
      try {
        const res = await fetch(markdownUrl, { cache: 'no-cache' });
        if (!res.ok) throw new Error('File not found: ' + res.status);

        const md = await res.text();
        const html = marked.parse(md, {
          breaks: true,
          smartypants: true,
          highlight: (code, lang) => {
            if (hljs.getLanguage(lang)) {
              return hljs.highlight(code, { language: lang }).value;
            }
            return hljs.highlightAuto(code).value;
          }
        });

        contentDiv.innerHTML = html;
      } catch (e) {
        contentDiv.innerHTML = `<div id="error">⚠️ Failed to load Markdown file: ${e.message}</div>`;
      }
    }

    loadMarkdown();
  </script>

  <script>
    // dark/light toggle logic
    const toggleCheckbox = document.getElementById('hide-checkbox');
    function applyTheme(light) {
      document.body.style.backgroundColor = light ? 'var(--light-bg)' : 'var(--bg)';
      document.body.style.color = light ? 'var(--light-fg)' : 'var(--fg)';
      localStorage.setItem('theme', light ? 'light' : 'dark');
    }
    toggleCheckbox.addEventListener('change', e => applyTheme(e.target.checked));
    window.addEventListener('DOMContentLoaded', () => {
      const saved = localStorage.getItem('theme');
      const useLight = saved === 'light';
      toggleCheckbox.checked = useLight;
      applyTheme(useLight);
    });

    // accent color picker
    const colorPicker = document.getElementById('colorPicker');
    colorPicker.addEventListener('input', () => {
      document.documentElement.style.setProperty('--accent', colorPicker.value);
    });
  </script>

  <!-- vercel analytics -->
  <script defer src="/_vercel/insights/script.js"></script>
</body>

</html>
```

**What changed?**

* Ditch PrismJS CSS/JS + autoloader
* Add Highlight.js core + GitHub Dark CSS
* Use `marked`’s `highlight` callback so code blocks get auto-detected + styled
* No more messing with that `components/` path

If you wanna try a different style just swap the CDN stylesheet to any of the themes at [https://highlightjs.org/static/demo](https://highlightjs.org/static/demo) . Enjoy your fresh-pressed markdown viewer!
