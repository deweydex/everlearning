/* Article import runs entirely in the browser. No proxy or extraction API. */
"use strict";
(() => {
  const byId = id => document.getElementById(id);
  const urlInput = byId("articleUrl");
  const loadButton = byId("loadArticle");
  const fileInput = byId("articleFile");
  const preview = byId("articlePreview");
  const previewText = byId("articleText");
  const status = byId("articleStatus");
  const maxBytes = 5 * 1024 * 1024;
  let request = 0;
  let controller = null;

  function normalizeUrl(value) {
    const url = new URL(value.trim());
    if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password) {
      throw new Error("Use a public http:// or https:// article link without login details.");
    }
    if (location.protocol === 'https:' && url.protocol === 'http:') {
      throw new Error("This page can only load HTTPS links. Try an HTTPS address or import saved HTML.");
    }
    url.hash = '';
    return url;
  }

  function extractHtml(html) {
    if (typeof Readability !== 'function') throw new Error("Article extractor did not load. Refresh the page.");
    // Template content is inert: its scripts do not run and its images do not load.
    // Remove active elements and resource attributes before copying to a detached document.
    const template = document.createElement('template');
    template.innerHTML = html;
    template.content.querySelectorAll('script,style,link,iframe,object,embed,img,audio,video,source,track,svg,math,template,noscript').forEach(node => node.remove());
    for (const node of template.content.querySelectorAll('*')) {
      for (const attr of [...node.attributes]) {
        const keep = ['class', 'id', 'lang', 'dir'].includes(attr.name)
          || (node.tagName === 'A' && attr.name === 'href')
          || (node.tagName === 'META' && ['name', 'property', 'content'].includes(attr.name));
        if (!keep) node.removeAttribute(attr.name);
      }
    }
    const doc = document.implementation.createHTMLDocument('');
    doc.head.replaceChildren();
    for (const node of template.content.querySelectorAll('title,meta')) doc.head.appendChild(node);
    doc.body.replaceChildren(template.content);
    const article = new Readability(doc, { maxElemsToParse: 30000, serializer: el => el }).parse();
    if (!article || !article.textContent.trim()) {
      throw new Error("No readable article was found. The page may need JavaScript, a login, or a different layout. Copy its text instead.");
    }
    // Preserve paragraph boundaries without inserting article HTML into our page.
    const blockTags = new Set(['P','DIV','SECTION','ARTICLE','H1','H2','H3','H4','H5','H6','LI','BLOCKQUOTE','PRE','TR']);
    function textOf(node) {
      if (node.nodeType === 3) return node.textContent;
      if (node.nodeType !== 1) return '';
      if (node.tagName === 'BR') return '\n';
      const text = [...node.childNodes].map(textOf).join('');
      return blockTags.has(node.tagName) ? '\n\n' + text + '\n\n' : text;
    }
    const text = textOf(article.content).replace(/[ \t]+/g, ' ').replace(/ *\n */g, '\n').replace(/\n{3,}/g, '\n\n').trim();
    return { title: article.title || 'Imported article', text };
  }

  async function readResponse(response) {
    const length = Number(response.headers.get('content-length'));
    if (length > maxBytes) throw new Error("This page is larger than the 5 MB import limit. Copy the article text instead.");
    const reader = response.body?.getReader();
    if (!reader) throw new Error("This browser cannot stream the article response. Import saved HTML instead.");
    const decoder = new TextDecoder();
    let bytes = 0, text = '';
    try {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        bytes += value.byteLength;
        if (bytes > maxBytes) {
          await reader.cancel();
          throw new Error("This page is larger than the 5 MB import limit. Copy the article text instead.");
        }
        text += decoder.decode(value, { stream: true });
      }
      return text + decoder.decode();
    } finally { reader.releaseLock(); }
  }

  function begin() {
    controller?.abort();
    controller = null;
    preview.hidden = true;
    loadButton.disabled = true;
    return ++request;
  }
  function show(result, source, id) {
    if (id !== request) return;
    byId('articleTitle').textContent = result.title;
    byId('articleSource').textContent = source;
    previewText.value = result.text;
    preview.hidden = false;
    status.textContent = "Text extracted. Let's review it below, then use it in the reader.";
  }
  function fail(error, id) {
    if (id !== request) return;
    status.textContent = error instanceof TypeError
      ? "The link could not be loaded directly. The site may block browser access (CORS), or the connection failed. Import saved HTML or copy the article text instead."
      : error.name === 'AbortError'
        ? "Article loading timed out. Try again, import saved HTML, or copy the text."
        : error.message;
  }

  loadButton.addEventListener('click', async () => {
    let url;
    try { url = normalizeUrl(urlInput.value); }
    catch (error) { status.textContent = error instanceof TypeError ? 'Please enter a complete article URL, starting with https://.' : error.message; return; }
    const id = begin();
    const abort = controller = new AbortController();
    const timer = setTimeout(() => abort.abort(), 20000);
    status.textContent = 'Loading the article directly from its website…';
    try {
      const response = await fetch(url.href, { mode: 'cors', credentials: 'omit', referrerPolicy: 'no-referrer', signal: abort.signal });
      if (!response.ok) throw new Error('The website returned HTTP ' + response.status + '. Import saved HTML or copy the text instead.');
      const type = response.headers.get('content-type') || '';
      if (!/text\/html|application\/xhtml\+xml|text\/plain/i.test(type)) throw new Error('This link is not an HTML article or plain text. PDFs and other document formats are not supported here.');
      const text = await readResponse(response);
      const result = /text\/plain/i.test(type) ? { title: 'Imported text', text: text.trim() } : extractHtml(text);
      if (!result.text) throw new Error('The article contains no readable text.');
      show(result, response.url || url.href, id);
    } catch (error) { fail(error, id); }
    finally { clearTimeout(timer); if (id === request) { controller = null; loadButton.disabled = false; } }
  });

  fileInput.addEventListener('change', async () => {
    const file = fileInput.files[0];
    if (!file) return;
    const id = begin();
    status.textContent = 'Reading the file on this device…';
    try {
      if (file.size > maxBytes) throw new Error('Choose a file smaller than 5 MB.');
      if (!/\.(html?|txt)$/i.test(file.name)) throw new Error('Choose a saved .html, .htm, or .txt file.');
      const text = await file.text();
      const result = /\.txt$/i.test(file.name) ? { title: file.name, text: text.trim() } : extractHtml(text);
      if (!result.text) throw new Error('This file contains no readable text.');
      show(result, 'Local file: ' + file.name + ' (not uploaded)', id);
    } catch (error) { fail(error, id); }
    finally { if (id === request) loadButton.disabled = false; fileInput.value = ''; }
  });

  byId('useArticle').addEventListener('click', () => {
    if (!previewText.value.trim()) { status.textContent = 'The preview is empty. Add some text first.'; return; }
    byId('text').value = previewText.value.trim();
    byId('text').dispatchEvent(new Event('input', { bubbles: true }));
    byId('status').textContent = 'Article text ready. Choose Generate & play when ready.';
    byId('text').focus();
  });
})();
