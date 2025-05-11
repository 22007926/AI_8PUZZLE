# 🧩 8-Puzzle Solver using BFS, DFS, and A\*

### 🔍 *Artificial Intelligence Assignment*

---

## 📌 Overview

This project implements an **AI-based 8-Puzzle solver** using three different search algorithms:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **A\* Search (A-star)** with Manhattan Distance heuristic

The user can interactively select which algorithm to use to solve a hardcoded 8-puzzle problem.

---

## 🎯 Objective

This project was created as part of an **Artificial Intelligence assignment** to:

- Understand and implement classical state-space search strategies.
- Explore the efficiency and behavior of uninformed (BFS, DFS) and informed (A*) search methods.
- Solve the 8-puzzle problem, a classic AI example, and display the solution steps.

---

## 🧠 What is the 8-Puzzle?

The 8-puzzle is a sliding tile puzzle consisting of a 3x3 grid with **8 numbered tiles** and **1 empty space (represented by 0)**. The goal is to reach the following target configuration:

```
1 2 3
4 5 6
7 8 0
```

---

## 🛠️ How It Works

### 📋 Initial Setup

The puzzle starts with the following **initial state**:

```
1 8 2
4 0 3
7 6 5
```

### 🔄 Moves

- You can move the blank tile (0) **up, down, left, or right**, if possible.
- The program automatically generates valid moves from a given state.

### ⚙️ Algorithms Implemented

#### 1. **Breadth-First Search (BFS)**
- Explores the shallowest nodes first.
- Guarantees the shortest path.
- May consume more memory.

#### 2. **Depth-First Search (DFS)**
- Explores the deepest nodes first.
- May not find the shortest path.
- Depth-limited to avoid infinite loops.

#### 3. **A\* Search**
- Informed search using **Manhattan Distance** as heuristic.
- Balances cost so far (`g(n)`) and estimated cost to goal (`h(n)`).
- Efficient and typically finds optimal solutions.

---

## 🖥️ Running the Program

### ✅ Requirements

- Python 3.x (no external libraries needed)

### ▶️ How to Run

1. Save the script as `eight_puzzle_solver.py`.
2. Run the program:
   ```bash
   python eight_puzzle_solver.py
   ```
3. Choose an algorithm from the menu:
   ```
   1. Breadth-First Search (BFS)
   2. Depth-First Search (DFS)
   3. A* Search
   4. Exit
   ```

---

## 📤 Output

After selecting an algorithm, the program will:
- Display each step from the initial to the goal state.
- If no solution is found (unlikely in this solvable case), it notifies the user.

Example:
```
--- A* Search Solution ---
Step 0:
[1, 8, 2]
[4, 0, 3]
[7, 6, 5]

Step 1:
...
```

---

## 📚 Learning Outcomes

- Deepened understanding of search strategies in AI.
- Learned how heuristics like Manhattan Distance can improve performance.
- Applied core concepts of problem-solving using state-space search.

---

## 📦 File Structure

```
eight_puzzle_solver.py  # Main program file with algorithm implementations and menu
README.md               # Project documentation
```

---

## 📜 License

This code is intended for educational purposes and as part of an Artificial Intelligence academic assignment.
