# OAuth-2.0
This project demonstrates how OAuth works with various providers: Google, Facebook, GitHub, and Salesforce.

## What is OAuth?
OAuth is an open standard for access delegation, commonly used to grant websites or applications access to user information without exposing passwords.

## How it Works?
1. The user clicks the "Login with [Provider]" button on the frontend.
2. The backend redirects the user to [Provider]'s OAuth consent screen.
3. After granting permission, the [Provider] redirects the user back to the application with an authorization code.
4. The backend exchanges the authorization code for an access token and retrieves the user's profile information.

## End-to-End Flow Diagram
![googleOAuth2_0](https://github.com/user-attachments/assets/4aa05729-5ecb-49f7-84a4-0a0838ad6e51)

## How to get the OAuth `CLIENT_ID` and `CLIENT_SECRET`?

### 1. Getting Google OAuth Client ID and Secret
**Google Cloud Console:**
    * Go to the [Google Cloud Console](https://console.cloud.google.com/).
    * Create or select a project.
    * Navigate to **"APIs & Services"** -> **"Credentials"**.
    * Click **"Create Credentials"** -> **"OAuth client ID"**.
    * Select the appropriate application type (e.g., Web application, Desktop app).
    * Configure authorized redirect URIs (for web apps).
    * The Client ID and Client Secret will be displayed.
    * Download the JSON file for later use.


### 2. Getting Facebook OAuth Client ID and Secret
**Facebook for Developers:**
    * Go to [Facebook for Developers](https://developers.facebook.com/).
    * Create an app or select an existing one.
    * Add the **"Facebook Login"** product to your app.
    * Go to **"Facebook Login"** -> **"Settings"**.
    * Configure valid OAuth redirect URIs.
    * Navigate to **"Settings"** -> **"Basic"**.
    * Your App ID (Client ID) and App Secret (Client Secret) will be displayed.


### 3. Getting GitHub OAuth Client ID and Secret
**GitHub Developer Settings:**
    * Go to your GitHub profile settings: [GitHub Settings](https://github.com/settings/profile).
    * Navigate to **"Developer settings"** -> **"OAuth Apps"**.
    * Click **"New OAuth App"** or select an existing one.
    * Fill in the application name, homepage URL, and authorization callback URL.
    * Click **"Register application"**.
    * Your Client ID and Client Secret will be displayed.


### 4. Getting Salesforce OAuth Client ID and Secret
**Salesforce Setup:**
    * Log in to your Salesforce org.
    * Navigate to "Setup".
    * Use the Quick Find box to search for and select **"App Manager"**.
    * Click **"New Connected App"**.
    * Enter basic information for your app (Connected App Name, API Name, Contact Email).
    * In the **"API (Enable OAuth Settings)"** section:
        * Check "Enable OAuth Settings".
        * Enter the "Callback URL".
        * Select the OAuth scopes you need.
    * Click "Save".
    * Click **"Manage Consumer Details"** (you might need to verify your identity).
    * Your Consumer Key (Client ID) and Consumer Secret (Client Secret) will be displayed.


