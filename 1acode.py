import os
import json
import pdfplumber

def assign_heading_level(size, sorted_sizes):
    if size >= sorted_sizes[0]:
        return "H1"
    elif len(sorted_sizes) > 1 and size >= sorted_sizes[1]:
        return "H2"
    else:
        return "H3"

def extract_outline_from_pdf(pdf_path):
    outline = []
    font_sizes = set()
    text_items = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            chars = page.chars
            if not chars:
                continue
            line_map = {}
            for char in chars:
                text = char.get("text", "").strip()
                if not text or text in "\n\r\t":
                    continue
                size = round(char.get("size", 0), 1)
                top = round(char.get("top", 0), 1)
                font_sizes.add(size)
                if top not in line_map:
                    line_map[top] = {
                        "text": text,
                        "size": size,
                        "page": page_num
                    }
                else:
                    line_map[top]["text"] += text
            for line in line_map.values():
                combined_text = line["text"].strip()
                if combined_text:
                    text_items.append((line["size"], combined_text, line["page"]))

    if not font_sizes:
        return {"title": "", "outline": []}
    
    sorted_sizes = sorted(font_sizes, reverse=True)


    title = ""
    for size, text, page in text_items:
        if page == 1 and size == sorted_sizes[0]:
            title = text
            break

    for size, text, page in text_items:
        if len(text.split()) <= 15:
            level = assign_heading_level(size, sorted_sizes)
            outline.append({
                "level": level,
                "text": text,
                "page": page
            })

    return {
        "title": title,
        "outline": outline
    }

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            output_json = extract_outline_from_pdf(pdf_path)

            out_file = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(output_json, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
