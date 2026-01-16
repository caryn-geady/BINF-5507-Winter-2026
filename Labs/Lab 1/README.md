# Lab 1: Getting Set Up with GitHub! 🎉

Welcome to Lab 1! In this lab, we will guide you through the process of getting set up with GitHub and using it within Visual Studio Code (VS Code). This guide is aimed at absolute beginners, so don't worry if you're new to this!

## Step 1: Create a GitHub Account
1. Go to [GitHub](https://github.com/).
2. Click on the **Sign up** button.
3. Follow the prompts to create your account.

## Step 2: Create Your First Repository
1. Once logged in, click on the **+** icon in the top right corner.
2. Select **New repository**.
3. Fill in the repository name and description.
4. Choose whether to make it public or private.
5. Click **Create repository**.

## Step 3: Install Git (if necessary)
- If you don't have Git installed, download it from [git-scm.com](https://git-scm.com/).
- Follow the installation instructions for your operating system.

## Step 4: Install Required Extensions in VS Code
1. Open VS Code.
2. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side.
3. Search for and install the following extensions:
   - **GitHub Pull Requests**
   - **GitHub Repositories**
   - **GitHub Actions**

## Step 5: Clone Your Repository to Your Local Machine

**Option A: Using the Terminal**
1. In your GitHub repository, click on the **Code** button.
2. Copy the URL provided.
3. Open VS Code and open the terminal (View > Terminal).
4. Run the command: `git clone <your-repo-url>` (replace `<your-repo-url>` with the URL you copied).

**Option B: Using VS Code's Command Palette**
1. In your GitHub repository, click on the **Code** button and copy the URL.
2. In VS Code, press `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows/Linux) to open the Command Palette.
3. Type **Git: Clone (Recursive)** and select it.
4. Paste your repository URL and press Enter.
5. Choose a local directory to save your repository.
6. When prompted, click **Add to Workspace** to open the cloned repository in VS Code.

## Step 6: Stage, Commit, and Push Changes to GitHub
1. Make changes to your files in VS Code.
2. In the terminal, navigate to your repository folder.
3. Stage your changes with: `git add .`
4. Commit your changes with: `git commit -m "Your commit message"`
5. Push your changes to GitHub with: `git push origin main`

Congratulations! You've successfully set up GitHub and VS Code. 🎉 Now you're ready to start collaborating on projects!
