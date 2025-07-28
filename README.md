<<<<<<< HEAD
# AdobeRound1A
=======
## Adobe Hackathon 2025 – Round 1A Submission
Challenge: "Connecting the Dots Through Docs"

This solution extracts a structured outline (Title, H1, H2, H3) from input PDF files. The output is saved in a hierarchical JSON format.

---

Directory Structure

- `/app/input` – Place your PDF files here.
- `/app/output` – The corresponding `.json` output files will be saved here.
- `extract_outline.py` – Main Python script for outline extraction.
- `Dockerfile` – Docker configuration for building and running the solution.

---

Approach

1. We use `pdfplumber` to extract individual character and font-size data from each PDF.
2. Headings are identified using a combination of:
   - Font size (relative ranking, not absolute)
   - Line segmentation via vertical position
   - Text length (short lines likely indicate headings)
3. The largest font on the first page is assumed to be the document title.
4. All extracted headings are tagged as H1, H2, or H3 based on font-size thresholds.

This avoids hardcoded rules and works on a variety of PDF layouts.

---

Docker Usage

Build the Image:

```bash
docker build --platform linux/amd64 -t adobe-outline-extractor .

