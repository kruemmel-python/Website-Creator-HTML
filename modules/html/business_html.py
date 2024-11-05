def generate_business_html():
    html_content = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Template</title>
    <link rel="stylesheet" href="business_styles.css">
    <script src="animations.js"></script>
</head>
<body>

    <header class="header">Professional business solutions</header>
    
    <section class="section">
        <h1>We help local businesses grow</h1>
        <p>Our team of experts provides innovative solutions to boost your business.</p>
        <button class="button" onclick="fadeInText()">Learn more</button>
    </section>

</body>
</html>'''
    return html_content
