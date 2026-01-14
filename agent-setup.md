# Agent Setup Guide

This guide walks you through the steps to create and set up your first AI agent using Google ADK.

## Prerequisites

Before you begin, make sure you have:
- Conda environment activated (`conda activate google-adk`)
- Required packages installed (`pip install -r requirements.txt`)
- Google API Key configured (see [environment-setup.md](environment-setup.md) for instructions)

## Creating Your First Agent

### Step 1: Run the Agent Creation Command

Execute the following command to start creating a new agent:

```bash
adk create my_first_agent
```

Replace `my_first_agent` with your desired agent name.

### Step 2: Choose a Model for the Root Agent

When prompted, you'll see options for the root agent model:

```
Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models (fill later)
Choose model (1, 2): 1
```

**Available Options:**
- **1. gemini-2.5-flash** (Recommended): Google's latest fast and efficient model
- **2. Other models (fill later)**: Choose this if you want to configure additional models later

Select option `1` for `gemini-2.5-flash` or `2` to configure other models later.

### Step 3: Choose a Backend

Next, you'll be prompted to select a backend:

```
Choose a backend (1, 2): 1
1. Google AI
2. Vertex AI
```

**Backend Options:**
- **1. Google AI**: Use Google's generative AI API directly (recommended for getting started)
- **2. Vertex AI**: Use Google Cloud's Vertex AI for enterprise deployments

Select the backend based on your needs. For development, `Google AI` is typically easier to set up.

### Step 4: Verify Your API Key

After selection, you'll see a message about API Key requirements:

```
Don't have API Key? Create one in AI Studio: https://aistudio.google.com/apikey
```

**Important**: Ensure your `GOOGLE_API_KEY` is properly configured in your `.env` file before proceeding.

If you don't have an API key yet:
1. Visit [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Create a new API key
3. Add it to your `.env` file:
   ```
   GOOGLE_API_KEY=your-api-key-here
   ```
4. Reload your environment or restart your terminal

### Step 5: Agent Folder Structure

After successful creation, your agent will be structured like this:

```
my_first_agent/
├── agent.py          # Main agent logic
├── requirements.txt  # Agent dependencies
└── config.yaml       # Agent configuration
```

## What's Next?

Once your agent is created:

1. **Explore the agent files**: Review the generated agent code in `my_first_agent/agent.py`
2. **Configure tools**: Add custom functions and tools to your agent
3. **Test locally**: Run your agent locally before deployment
4. **Deploy**: Follow deployment guidelines to push your agent to production

## Troubleshooting

**Error: "Don't have API Key?"**
- Make sure your `GOOGLE_API_KEY` environment variable is set correctly
- Verify the key is valid and has the necessary permissions
- Check that your `.env` file is properly configured

**Error: "Model not found"**
- Ensure you have internet connectivity
- Verify that the model is available in your region
- Check your API key permissions

**Error: "Backend connection failed"**
- Verify your Google Cloud credentials (if using Vertex AI)
- Check that the required APIs are enabled in your Google Cloud project
- Ensure your API key has the necessary scopes

## Next Steps

- Read the [Readme.md](Readme.md) for a comprehensive overview of Google ADK
- Check out example agents in the `examples/` directory
- Explore the agent lifecycle: Build, Interact, Evaluate, Deploy
