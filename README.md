# Mountain Car Q-Learning

This project implements Q-Learning to train an agent to play the Mountain Car environment using a Q-table. The trained Q-table is saved to `mountain_car_q_table.pkl` to be used as a starting point for future trainings.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Q-Learning is a model-free reinforcement learning algorithm used to find the optimal action-selection policy for a given finite Markov decision process. In this project, Q-Learning is used to train an agent to solve the Mountain Car problem.

The Mountain Car problem is a classic reinforcement learning problem where an underpowered car must drive up a steep hill. The goal is to drive up the hill as quickly as possible.

## Installation

To set up the environment and install the required dependencies, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yosephberhanu/mountain-car-q-learning.git
    cd mountain-car-q-learning
    ```

2. **Create and activate the Conda environment:**

    ```bash
    conda env create -f environment.yml
    conda activate gym-env
    ```

3. **Install additional dependencies (if any):**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Training the agent:**

    Run the Jupyter notebook to train the agent. The notebook will save the Q-table to `mountain_car_q_table.pkl` once the training is completed.

    ```bash
    jupyter notebook mountain_car_q_learning.ipynb
    ```

2. **Using the pre-trained Q-table:**

    The saved Q-table can be loaded and used as a starting point for future trainings or to evaluate the agent's performance. In the Jupyter notebook, you can load the Q-table as follows:

    ```python
    import pickle

    with open('mountain_car_q_table.pkl', 'rb') as f:
        q_table = pickle.load(f)
    ```

## Results

The performance of the agent improves over time as the Q-learning algorithm updates the Q-table. The trained agent can successfully drive the car up the hill in the Mountain Car environment.

You can visualize the agent's performance by running the evaluation cell in the Jupyter notebook.

## Credit

This project is based on tutorial by [sentdex](https://www.youtube.com/@sentdex) from [here](https://www.youtube.com/watch?v=yMk_XtIEzH8&list=PLQVvvaa0QuDezJFIOU5wDdfy4e9vdnx-7)