from fontTools.ttLib import TTFont
import os

# List of common macOS system font locations
font_paths = [
    "/System/Library/Fonts/SFNS.ttf",
    "/System/Library/Fonts/Menlo.ttc",
    "/System/Library/Fonts/Monaco.ttf",
    "/System/Library/Fonts/AppleSymbols.ttf",
    "/System/Library/Fonts/LastResort.ttf",
    "/System/Library/Fonts/LucidaGrande.ttc",
]

test_char = '█'  # U+2588 FULL BLOCK
test_char_code = ord(test_char)

for font_path in font_paths:
    if os.path.exists(font_path):
        try:
            # Handle TTC (TrueType Collection) files
            if font_path.endswith('.ttc'):
                for font_number in range(4):  # Check fonts 0-3 in the collection
                    try:
                        font = TTFont(font_path, fontNumber=font_number)
                        cmap = font.getBestCmap()
                        
                        if test_char_code in cmap:
                            glyph_name = cmap[test_char_code]
                            width = font['hmtx'][glyph_name][0]
                            print(f"Found '{test_char}' in {os.path.basename(font_path)} (font #{font_number})")
                            print(f"Glyph name: {glyph_name}")
                            print(f"Width: {width}")
                            print()
                    except Exception as e:
                        print(f"Error reading font #{font_number} in {font_path}: {e}")
            else:
                # Handle regular TTF files
                font = TTFont(font_path)
                cmap = font.getBestCmap()
                
                if test_char_code in cmap:
                    glyph_name = cmap[test_char_code]
                    width = font['hmtx'][glyph_name][0]
                    print(f"Found '{test_char}' in {os.path.basename(font_path)}")
                    print(f"Glyph name: {glyph_name}")
                    print(f"Width: {width}")
                    print()
        except Exception as e:
            print(f"Error reading {font_path}: {e}")
