# React Preview

A simple Python utility that converts a snippet of React component code into an HTML file with inline CSS using the Groq API.

This tool takes hard-coded React JSX, sends it to an LLM (via the Groq client) with a prompt to generate equivalent HTML, writes the resulting HTML to `index.html`, and then opens it in the default web browser. ([GitHub][1])

## Features

* Converts React JSX to standalone HTML with inline CSS
* Uses an LLM (via the Groq API) for the conversion
* Writes the generated HTML to `index.html`
* Automatically opens the generated file in the system browser

## Prerequisites

Before using this script, ensure you have the following:

* Python 3.8 or later installed

* A valid Groq API key

* A `.env` file in the project root with the following:

  ```bash
  GROQ_API_KEY=<your_groq_api_key>
  ```

* Required Python packages (listed below)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Kashika221/react_preview.git
   cd react_preview
   ```

2. Create and activate a Python virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If there is no `requirements.txt`, install manually:

   ```bash
   pip install python-dotenv pydantic groq
   ```

## Usage

1. Ensure your `.env` file contains your `GROQ_API_KEY`.

2. Run the script:

   ```bash
   python app.py
   ```

3. Upon running, the script will:

   * Read the hard-coded React JSX
   * Convert it to HTML using Groq’s LLM
   * Write the output to `index.html`
   * Open the file in your default web browser

## How It Works

* **Environment Setup:** Loads environment variables via `dotenv`.
* **LLM Invocation:** Uses the Groq client to request a conversion prompt that instructs the model to convert React JSX into HTML with inline CSS.
* **Output:** Writes the returned HTML string to `index.html`.
* **Preview:** Automatically opens the HTML file using Python’s `webbrowser`. ([GitHub][1])

## Customization

To preview different React code:

* Replace or update the `react_code` variable in `app.py` with your own React component(s).
* Re-run the script to generate a new HTML preview.

## Troubleshooting

* **Missing API Key:** Confirm `GROQ_API_KEY` is set correctly in your `.env` file.
* **Dependency Errors:** Ensure all required packages are installed and current.

## License

This project is provided as-is. Feel free to adapt and reuse for your own JSX to HTML preview needs.

---

If you want, I can also generate a `requirements.txt` and example `.env` template.

[1]: https://raw.githubusercontent.com/Kashika221/react_preview/main/app.py "raw.githubusercontent.com"
