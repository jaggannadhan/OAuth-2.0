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
**Google Cloud Console:** <br/>
    * Go to the [Google Cloud Console](https://console.cloud.google.com/).<br/>
    * Create or select a project.<br/>
    * Navigate to **"APIs & Services"** -> **"Credentials"**.<br/>
    * Click **"Create Credentials"** -> **"OAuth client ID"**.<br/>
    * Select the appropriate application type (e.g., Web application, Desktop app).<br/>
    * Configure authorized redirect URIs (for web apps).<br/>
    * The Client ID and Client Secret will be displayed.<br/>
    * Download the JSON file for later use.<br/>


### 2. Getting Facebook OAuth Client ID and Secret
**Facebook for Developers:** <br/>
    * Go to [Facebook for Developers](https://developers.facebook.com/).<br/>
    * Create an app or select an existing one.<br/>
    * Add the **"Facebook Login"** product to your app.<br/>
    * Go to **"Facebook Login"** -> **"Settings"**.<br/>
    * Configure valid OAuth redirect URIs.<br/>
    * Navigate to **"Settings"** -> **"Basic"**. <br/>
    * Your App ID (Client ID) and App Secret (Client Secret) will be displayed. <br/>


### 3. Getting GitHub OAuth Client ID and Secret
**GitHub Developer Settings:** <br/>
    * Go to your GitHub profile settings: [GitHub Settings](https://github.com/settings/profile). <br/>
    * Navigate to **"Developer settings"** -> **"OAuth Apps"**. <br/>
    * Click **"New OAuth App"** or select an existing one. <br/>
    * Fill in the application name, homepage URL, and authorization callback URL. <br/>
    * Click **"Register application"**. <br/>
    * Your Client ID and Client Secret will be displayed. <br/>


### 4. Getting Salesforce OAuth Client ID and Secret
**Salesforce Setup:** <br/>
    * Log in to your Salesforce org. <br/>
    * Navigate to "Setup". <br/>
    * Use the Quick Find box to search for and select **"App Manager"**. <br/>
    * Click **"New Connected App"**. <br/>
    * Enter basic information for your app (Connected App Name, API Name, Contact Email). <br/>
    * In the **"API (Enable OAuth Settings)"** section: <br/>
        * Check "Enable OAuth Settings". <br/>
        * Enter the "Callback URL". <br/>
        * Select the OAuth scopes you need. <br/>
    * Click "Save".<br/>
    * Click **"Manage Consumer Details"** (you might need to verify your identity). <br/>
    * Your Consumer Key (Client ID) and Consumer Secret (Client Secret) will be displayed. <br/>


