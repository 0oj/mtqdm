from fontTools.ttLib import TTFont
from collections import defaultdict

def generate_html(width_to_chars):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>San Francisco Font Character Widths</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text"; }
            .width-group {
                margin: 20px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            .width-label {
                font-weight: bold;
                margin-bottom: 10px;
            }
            .char-group {
                font-size: 24px;
                line-height: 1.5;
                word-wrap: break-word;
            }
            .char {
                display: inline-block;
                margin: 5px;
                padding: 5px;
                border: 1px solid #eee;
                border-radius: 3px;
            }
            .char:hover {
                background-color: #f0f0f0;
            }
            .char-info {
                font-size: 12px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <h1>San Francisco Font Character Groups by Width</h1>
    """
    
    # Sort widths for consistent display
    for width in sorted(width_to_chars.keys()):
        chars = width_to_chars[width]
        if len(chars) > 1:
            html += f"""
            <div class="width-group">
                <div class="width-label">Width: {width}</div>
                <div class="char-group">
            """
            for char in chars:
                html += f"""
                    <span class="char">
                        {char}
                        <div class="char-info">U+{ord(char):04X}</div>
                    </span>
                """
            html += """
                </div>
            </div>
            """
    
    html += """
    </body>
    </html>
    """
    
    return html

# Load the font file
font = TTFont("/System/Library/Fonts/SFNS.ttf")

# Get the horizontal metrics table
hmtx = font['hmtx']

# Create a dictionary to store characters by width
width_to_chars = defaultdict(list)

# Iterate through all characters
for char_code in range(32, 65536):  # Start from space (32) to cover most Unicode characters
    try:
        char = chr(char_code)
        glyph_name = font.getBestCmap().get(char_code)
        if glyph_name:
            width = hmtx[glyph_name][0]
            width_to_chars[width].append(char)
    except:
        pass  # Skip characters that cause errors

# Generate and save HTML
html_content = generate_html(width_to_chars)
with open('sf_font_widths.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML file generated as 'sf_font_widths.html'")