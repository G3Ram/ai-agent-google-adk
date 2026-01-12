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

## Setting up the Google API Key

To use Google ADK and access Google's AI services, you'll need to set up your `GOOGLE_API_KEY` environment variable.

### Step 1: Get Your Google API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the required APIs (Generative AI API, etc.)
4. Go to **Credentials** → **Create Credentials** → **API Key**
5. Copy the generated API key

### Step 2: Set the Environment Variable

You have several options to set your `GOOGLE_API_KEY`:

**Option A: Export in Terminal (Temporary)**

For the current terminal session only, run:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Replace `your-api-key-here` with your actual API key.

**Option B: Add to Shell Profile (Persistent)**

For macOS/Linux, add the following line to your shell profile (`~/.zshrc`, `~/.bash_profile`, or `~/.bashrc`):

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Then reload the profile:

```bash
source ~/.zshrc  # or source ~/.bash_profile
```

**Option C: Create a `.env` File (Recommended for Development)**

1. Create a `.env` file in the project root directory:

```bash
touch .env
```

2. Add your API key to the `.env` file:

```
GOOGLE_API_KEY=your-api-key-here
```

3. Install `python-dotenv` if not already installed:

```bash
pip install python-dotenv
```

4. Load the environment variables in your Python code:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

### Step 3: Verify the Setup

To verify that your `GOOGLE_API_KEY` is set correctly, run:

```bash
echo $GOOGLE_API_KEY
```

You should see your API key printed in the terminal. If you see nothing, the environment variable is not set.

### Security Note

⚠️ **Important**: Never commit your API key to version control. Add `.env` to your `.gitignore` file:

```bash
echo ".env" >> .gitignore
```

This ensures your sensitive credentials remain private.
