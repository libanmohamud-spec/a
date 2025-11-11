# Quick Start Guide for Participants

## Step-by-Step Instructions

### Step 1: Access the Repository

1. **Go to:** https://github.com/libanmohamud-spec/a
2. **Sign in** to GitHub (if not already signed in)
3. If you see a "404 Not Found" or "Private repository" message:
   - The repository is private
   - Contact the organizer to add you as a collaborator
   - Or ask them to make the repository public

### Step 2: Create a Codespace

1. **Click the green "Code" button** (top right of the repository page)
2. **Click the "Codespaces" tab**
3. **Click "Create codespace on main"** (or the "+" button)
4. **Wait 2-3 minutes** for the Codespace to set up
   - You'll see a progress indicator
   - The Codespace will open automatically when ready

**Note:** If you don't see "Create codespace on main":
- Make sure you're signed in to GitHub
- Make sure you have access to the repository
- Try refreshing the page
- The option should appear after signing in

### Step 3: Start the Experiment

Once your Codespace is open:

1. **Open the terminal** (Terminal → New Terminal, or press `` Ctrl+` ``)

2. **Initialize your session:**
   ```bash
   bin/init <your_participant_id> <yes|no>
   ```
   Example: `bin/init p002 yes`
   - Use your assigned participant ID
   - Answer `yes` if you have programming experience, `no` if you're a beginner

3. **Follow the prompts** - the system will guide you through Round 1 and Round 2

## Troubleshooting

**"No codespace on main" message:**
- This is normal! You need to CREATE the codespace
- Click "Create codespace on main" - it will create a new one for you
- Each participant gets their own Codespace

**Can't see the repository:**
- Make sure you're signed in to GitHub
- Contact the organizer to add you as a collaborator
- Check that you're using the correct repository URL

**Codespace won't start:**
- Wait a few minutes (first-time setup takes 2-3 minutes)
- Try refreshing the page
- Contact the organizer if it still doesn't work

## Need Help?

Contact the experiment organizer with:
- Your GitHub username
- Any error messages you see
- Screenshots of what you're seeing

