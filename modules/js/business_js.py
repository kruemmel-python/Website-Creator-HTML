def generate_business_js():
    js_content = '''function fadeInText() {
    const section = document.querySelector('.section');
    section.style.opacity = 0;
    section.style.transition = "opacity 2s";
    setTimeout(() => {
        section.style.opacity = 1;
    }, 10);
}

document.addEventListener("DOMContentLoaded", function() {
    fadeInText();
});'''
    return js_content
