# How to set up the environment

## Setting up the Conda Virtual Environment

To set up a conda virtual environment for this project, follow these steps:

### Step 1: Create the Conda Environment

Run the following command to create a new conda environment named `google-adk` with Python 3.11.7:

```bash
conda create -n google-adk python=3.11.7
```

This command will:
- Create a new virtual environment named `google-adk`
- Install Python version 3.11.7 in that environment
- Set up all the necessary Python infrastructure

### Step 2: Activate the Conda Environment

Once the environment is created, activate it using:

```bash
conda activate google-adk
```

You should see `(google-adk)` appear in your terminal prompt, indicating that the environment is now active.

### Step 3: Verify the Installation

To verify that Python 3.11.7 is installed correctly, run:

```bash
python --version
```

You should see output showing `Python 3.11.7`.

### Step 4: Install Required Packages

Once your environment is activated, you can install the required packages for this project. You can typically do this with:

```bash
pip install -r requirements.txt
```

(Make sure a `requirements.txt` file exists in the project directory with all necessary dependencies listed.)

### Deactivating the Environment

When you're done working in the environment, you can deactivate it using:

```bash
conda deactivate
```
