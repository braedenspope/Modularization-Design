# Modularization Design Course

This repository contains all assignments and projects completed during my Modularization Design course. This advanced curriculum focuses on software engineering principles, modular programming, and complex system design through structured decomposition and analysis.

## Course Overview

The course emphasizes professional software development practices including:
- **Modular Design Principles**: Breaking complex problems into manageable components
- **Software Engineering Analysis**: Coupling, cohesion, and system architecture evaluation
- **Advanced Algorithm Implementation**: Recursive sorting, game logic, and mathematical computations
- **Structure Charts & Data Flow Diagrams**: Visual system design documentation
- **Professional Documentation**: Comprehensive design analysis and testing methodologies

## Repository Structure

```
Modularization-Design/
├── Lab01.py                           # Tic-Tac-Toe game with modular design
├── Lab03.py                           # Calendar program with function decomposition
├── Lab05.py                           # Sudoku draft with validation logic
├── Lab09.py                           # Sub-list sort implementation
├── Lab13.py                           # Segregation sort (quicksort variant)
├── Test Cases.txt                     # Comprehensive Sudoku testing scenarios
├── Advanced_Search_Design.pdf         # Binary search design and analysis
├── Calendar_Program_Design.pdf        # Calendar structure chart and flowchart
├── Numerical_Sequence_Design.pdf      # François sequence algorithm design
├── Prime_Number_Design.pdf           # Sieve of Eratosthenes design and trace
├── Segregation_Sort_Design.pdf       # Recursive quicksort design and analysis
├── Sort_Design.pdf                   # Selection sort design documentation
├── Sub-list_Sort_Analysis.pdf        # Merge sort analysis with coupling/cohesion metrics
├── Sub-list_Sort_Design.pdf          # Merge sort modular design
├── Sudoku_Design.pdf                 # Sudoku structure chart and data flow
└── README.md                         # This file
```

## Lab Assignments

### Lab 01: Tic-Tac-Toe Game
**File:** `Lab01.py`

A fully functional Tic-Tac-Toe game demonstrating modular programming principles.

**Modular Design Features:**
- **File I/O Module**: JSON-based game state persistence
- **Game Logic Module**: Turn management and win condition detection
- **Display Module**: User-friendly board visualization
- **Input Validation**: Robust error handling and user feedback

**Key Functions:**
- `read_board()` / `save_board()`: Game state management
- `is_x_turn()`: Turn determination logic
- `play_game()`: Main game loop with input processing
- `game_done()`: Comprehensive win/tie detection

---

### Lab 03: Calendar Program
**Files:** `Lab03.py`, `Calendar_Program_Design.pdf`

A sophisticated calendar display program with comprehensive input validation and mathematical date calculations.

**Modular Architecture:**
- **Input Module**: `get_month()`, `get_year()` with validation
- **Calculation Module**: `get_offset()`, `days_in_month()`, `is_leap_year()`
- **Display Module**: `display_table()` with formatted output

**Design Document Features:**
- Complete structure chart showing function relationships
- Detailed flowchart for input validation logic
- Pseudocode for offset calculation algorithm

**Advanced Features:**
- Leap year calculations following Gregorian calendar rules
- Day-of-week offset computation from base year 1753
- Formatted table output with proper alignment

---

### Lab 05: Sudoku Draft Program
**Files:** `Lab05.py`, `Sudoku_Design.pdf`, `Test Cases.txt`

An interactive Sudoku editor with comprehensive validation and modular design.

**System Architecture:**
- **Data Module**: JSON file I/O for board persistence
- **Validation Module**: Multi-layered rule checking (row, column, 3x3 box)
- **Interface Module**: Coordinate parsing and user interaction
- **Display Module**: Formatted grid visualization with dividers

**Design Documentation:**
- Structure chart showing hierarchical function relationships
- Data flow diagram illustrating information movement
- Detailed pseudocode for validation functions

**Comprehensive Testing:**
The `Test Cases.txt` file demonstrates professional testing methodology:
- **Edge Cases**: Invalid coordinates, out-of-bounds input
- **Rule Validation**: Duplicate detection across rows, columns, and boxes
- **User Interface**: Coordinate format flexibility, error messaging
- **Data Validation**: Number range checking, negative value handling

---

### Lab 09: Sub-list Sort Program (Merge Sort)
**Files:** `Lab09.py`, `Sub-list_Sort_Design.pdf`, `Sub-list_Sort_Analysis.pdf`

Advanced implementation of merge sort with detailed modularization analysis.

**Algorithm Details:**
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Approach:** Bottom-up merge sort with iterative implementation

**Modular Design:**
- **File Module**: `read_file()` with JSON parsing
- **Sort Module**: `sort()` main algorithm controller
- **Combine Module**: `combine()` for merging sorted sublists

**Design Analysis Features:**
- **Coupling Analysis**: Detailed evaluation of inter-module dependencies
- **Cohesion Metrics**: Assessment of function single-responsibility adherence
- **Structure Charts**: Visual representation of module relationships
- **Trace Tables**: Step-by-step algorithm execution documentation

**Professional Testing:**
Automated test case execution covering:
- Empty and singular arrays
- Pre-sorted and reverse-sorted data
- Duplicate value handling
- Various array sizes (even/odd lengths)

---

### Lab 13: Segregation Sort Program (Quicksort)
**Files:** `Lab13.py`, `Segregation_Sort_Design.pdf`

Recursive quicksort implementation with sophisticated partitioning logic.

**Algorithm Architecture:**
- **Time Complexity:** O(n log n) average, O(n²) worst case
- **Space Complexity:** O(log n) for recursion stack
- **Partitioning Strategy:** Three-way partitioning with pivot optimization

**Modular Design:**
- **Main Controller**: `sort()` with test case automation
- **Recursive Engine**: `sort_recursive()` with divide-and-conquer logic
- **Partitioning Module**: `segregate()` with sophisticated pivot handling

**Design Documentation Features:**
- Complete pseudocode with edge case handling
- Coupling and cohesion analysis for each function
- Algorithmic efficiency analysis with complexity reasoning
- Comprehensive test case coverage with expected outputs

## Advanced Design Documentation

### Segregation Sort Design Analysis
**File:** `Segregation_Sort_Design.pdf`

This document demonstrates advanced software engineering analysis:

**Structure Chart Analysis:**
- Hierarchical module relationships with data flow indicators
- Function dependency mapping
- Parameter passing documentation

**Coupling & Cohesion Metrics:**
- **Read Function**: Strong cohesion, simple coupling
- **Sort_Recursive Function**: Extraneous cohesion, interactive coupling
- **Segregate Function**: Extraneous cohesion, interactive coupling

**Algorithm Trace Documentation:**
- Line-by-line execution tracking
- Variable state monitoring
- Test case validation with [4,2] example

### Sub-list Sort Analysis
**File:** `Sub-list_Sort_Analysis.pdf`

Professional-grade software engineering analysis including:

**Modularization Metrics:**
- Detailed coupling analysis (Simple, Interactive, Extraneous)
- Cohesion evaluation (Strong, Extraneous)
- Recommendations for design improvement

**Algorithm Implementation:**
- Complete pseudocode with 23-line structured algorithm
- Comprehensive trace table for array [31,72,32]
- Step-by-step variable state tracking

**Efficiency Analysis:**
- O(n log n) complexity derivation
- Performance scaling discussion
- Memory usage optimization strategies

### Calendar Program Design
**File:** `Calendar_Program_Design.pdf`

Demonstrates complete system design methodology:

**Visual Design Elements:**
- Structure chart with clear data flow
- Function flowchart for input validation
- Pseudocode for mathematical calculations

**Implementation Strategy:**
- Modular decomposition of date calculation problem
- Error handling integration
- User interface design considerations

## Professional Development Skills

### Software Engineering Principles
1. **Modular Decomposition**: Breaking complex systems into manageable components
2. **Coupling Minimization**: Reducing dependencies between modules
3. **Cohesion Maximization**: Ensuring single-responsibility principle adherence
4. **Interface Design**: Creating clean, well-defined module boundaries

### Documentation Standards
1. **Structure Charts**: Hierarchical system visualization
2. **Data Flow Diagrams**: Information movement documentation
3. **Pseudocode**: Algorithm specification in structured English
4. **Trace Tables**: Execution verification and debugging support

### Testing Methodologies
1. **Comprehensive Test Coverage**: Edge cases, normal cases, error conditions
2. **Automated Testing**: Systematic validation across multiple scenarios
3. **Professional Test Documentation**: Clear expected outcomes and rationale

## Technical Achievements

### Algorithm Implementation Mastery
- **Recursive Algorithms**: Quicksort with sophisticated partitioning
- **Iterative Algorithms**: Bottom-up merge sort implementation
- **Mathematical Algorithms**: Calendar calculations with leap year logic
- **Game Logic**: Complex state management and win condition detection

### Software Architecture Skills
- **Modular Design**: Clean separation of concerns across all projects
- **Error Handling**: Robust exception management and user feedback
- **File I/O**: JSON-based data persistence with validation
- **User Interface**: Intuitive command-line interactions with clear messaging

### Analysis and Documentation
- **Complexity Analysis**: Formal Big O evaluation with reasoning
- **Design Analysis**: Professional coupling and cohesion assessment
- **Visual Documentation**: Structure charts and data flow diagrams
- **Testing Documentation**: Comprehensive test case specifications

## Course Reflection

This Modularization Design course represents a significant advancement from basic algorithm implementation to professional software engineering practices. Key learning outcomes include:

**Technical Progression:**
- From monolithic code to modular, maintainable systems
- From basic testing to comprehensive validation methodologies
- From simple algorithms to complex recursive and iterative implementations
- From informal documentation to professional design specifications

**Professional Skills Development:**
- Software architecture design and analysis
- Technical documentation creation and maintenance
- Systematic testing and validation approaches
- Code organization and maintainability principles

**Problem-Solving Evolution:**
- Complex system decomposition strategies
- Interface design and module communication
- Performance optimization and algorithmic efficiency
- Professional debugging and trace analysis techniques

The comprehensive design documents, detailed analysis, and sophisticated implementations demonstrate the transition from computer science student to software engineering professional, emphasizing not just what to build, but how to design, analyze, and document complex software systems effectively.

---

*This repository represents advanced coursework in software engineering and modular design, demonstrating professional-level skills in system architecture, algorithm implementation, and technical documentation.*
