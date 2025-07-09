# Graph Algorithms Implementation and Complexity Analysis
This project was carried out as part of the "Advanced Algorithms and Complexity" module for the Master 1 in Bioinformatics at USTHB (Year 2023/2024).
It is a Python implementation of fundamental graph operations, accompanied by an analysis of their complexity. The project explores the two main graph representations (adjacency matrix and adjacency list) and compares their performance.
## 📜 Description
The `graph_analyzer.py` program offers a command-line interface to:
- Build graphs, directed or undirected.
- Display graphically the created structures.
- Execute a series of algorithmic analyses on the current graph.
## ✨ Features
The program implements the following operations:
- **Creation and Display:**
  - Construction of directed and undirected graphs.
  - Graphical visualization using `matplotlib`.
- **Property Analysis:**
  - Calculation of graph **density**.
  - Calculation of **degrees** (simple degree, in-degree and out-degree).
  - Verification if a graph is **Eulerian**.
  - Verification if a graph is **Complete**.
  - Verification if a graph is a **Tree**.
- **Traversal and Search Algorithms:**
  - Search for **all simple paths** between two nodes.
  - Search for the **shortest path** between two nodes (based on number of edges).
  - Identification of all **cycles** in a directed graph.
## 🛠️ Prerequisites
- Python 3.6 or higher
- The libraries listed in `requirements.txt`
## 🚀 How to Run
1.  **Clone the repository (or download the files):**
    ```bash
    git clone https://github.com/aylaib/Projet-Analyse-Graphes.git
    cd Projet-Analyse-Graphes
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the program:**
    ```bash
    python graph_analyzer.py
    ```
4.  Follow the menu instructions to interact with the program.
## 📊 Reference Documents
- [Project Report](./rapport_projet.pdf): Contains theoretical analysis, complexity tables and experimental evaluation.
- [Assignment Statement](./enonce_devoir.pdf): The original project subject.
## 📸 Screenshots
Here are some examples of program usage.
**Construction of an undirected graph and adding edges:**
![Construction of an undirected graph](./screenshots/01.png)
**Construction of a directed graph and adding arcs:**
![Construction of a directed graph](./screenshots/02.png)
