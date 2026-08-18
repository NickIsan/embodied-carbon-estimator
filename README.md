Embodied Carbon & Cost Estimator (Python)
A simple Python tool built to compute total material costs and embodied carbon intensity (kgCO2/m²) for construction projects, exporting a summary report in PDF format.

💡 Overview
As sustainable construction becomes an industry priority, tracking carbon emissions alongside financial metrics is essential. This CLI-based tool helps civil engineering students and builders quickly evaluate the environmental footprint and budget of small-to-medium structural projects.

✨ Features
Project Metadata Input: Captures project title, owner, engineer, location, and total area (m²).

Material Database: Pre-defined unit costs and carbon emission factors for common structural materials (Concrete, Steel, Masonry, Insulation, Fenestration).

Eco-Score Rating: Calculates embodied carbon density (kgCO2/m²) and assigns a sustainability grade (A+, A, B, or C).

PDF Generation: Outputs a structured summary report via fpdf2 with full UTF-8 / Greek character support.

🛠️ Tech Stack
Language: Python 3.x

Libraries: fpdf2 (PDF Generation), os, datetime

🚀 Getting Started
Prerequisites
Install fpdf2 using pip:
pip install fpdf2

Running the Application
python main.py

Follow the interactive terminal prompts to input project metadata and select materials.

📈 Future Improvements
Add data visualization (matplotlib / pandas) for visual comparisons.

Integrate Data Science & Machine Learning modules to predict material costs based on historical data.

Expand the material database with updated Eurocode-aligned EPD data.

Built as part of my coding journey connecting Civil Engineering with Python.
