### 📌 README.md

````markdown
# 🚀 Graph-Theory-Visualizer

This project is a **Graph Theory Visualizer** created using the Manim animation library. It is designed to visually explain basic concepts of graph theory, focusing on graph counting, non-isomorphic graphs, and isomorphism. This project was developed as part of a homework assignment for a Graph Theory course at Akdeniz University.

---

## 🌐 Project Overview

This project includes:
- **Visualizing the concept of simple graphs and counting them.**
- **Illustrating the concept of isomorphic graphs.**
- **Animating graph structures to enhance understanding.**

The project currently focuses on:
- Counting simple graphs for **n=3** and **n=4**.
- Identifying and explaining isomorphic graphs.

---

## 🚀 How to Run

### ✅ Prerequisites
- Make sure you have **Manim Community (v0.19)** installed:
  ```bash
  pip install manim
````

* Ensure that **LaTeX (MikTeX)** is installed for mathematical formulas.

### ✅ Running the Animation

1. Clone the repository:

   ```bash
   git clone https://github.com/Akdeniz-CSE-Students/Graph-Theory-Visualizer.git
   cd Graph-Theory-Visualizer
   ```

2. Run the Manim animation:

   ```bash
   manim -pql graph_counting_n4_test.py CountingGraphsComplete
   ```

3. Your animation will be created in the `media/videos` directory.

---

## 📚 Understanding the Animation

### 🔹 Part 1: Introduction

* The animation begins with an introduction to the concept of graph counting.
* It introduces the mathematical formula for calculating the total number of edges in a graph:

  $$
  B(n, 2) = \frac{n(n - 1)}{2}
  $$

### 🔹 Part 2: Graphs for n=3

* It displays all 8 possible simple graphs for **n=3**.
* Isomorphic graphs are faded out for clarity.
* An isomorphism example is shown with a visual explanation.

### 🔹 Part 3: Graphs for n=4

* It presents the 11 unique non-isomorphic graphs for **n=4** among the 64 possible combinations.
* This section is designed to clearly show how isomorphism reduces the total number of unique graphs.

---

## 📌 Why This Project?

This project was created as part of a homework assignment for Graph Theory. The goal is to help students understand:

* How simple graphs can be counted.
* How isomorphic graphs are identified.
* The concept of non-isomorphic graphs for different values of **n**.

### ✨ Assigned Slide for Student ID: 20220808005

* This project is the visual representation of **Slide 23** in the assigned homework slides.

---

## 🌐 Contributing

If you are a student working on a similar homework, you can:

* Fork this repository.
* Create your own graph visualizations.
* Make a pull request with your contribution.

### ✅ Recommended Contribution:

* Create a new file for your slide (e.g., `example.py`).
* Follow the structure of the existing code.
* Add a brief description of your animation to the README.

---

## 👤 Author

* **Yahya Efe Kuruçay** - Student ID: 20220808005
* 📌 [My Website](https://efekurucay.com)
* 📌 [My GitHub Profile](https://github.com/efekurucay/)
* 📌 [Akdeniz CSE Students GitHub](https://github.com/Akdeniz-CSE-Students/)
---

## 📌 License

This project is open-source and available under the MIT License. Feel free to use and modify it for educational purposes. 😊

```

---
