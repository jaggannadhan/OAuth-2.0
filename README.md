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

### Getting Google OAuth Client ID and Secret
1.  **Google Cloud Console:**
    * Go to the [Google Cloud Console](https://console.cloud.google.com/).
    * Create or select a project.

2.  **Credentials:**
    * Navigate to **"APIs & Services"** -> **"Credentials"**.

3.  **Create Credentials:**
    * Click **"Create Credentials"** -> **"OAuth client ID"**.

4.  **Application Type:**
    * Select the appropriate application type (e.g., Web application, Desktop app).
    * Configure authorized redirect URIs (for web apps).

5.  **Client ID and Secret:**
    * The Client ID and Client Secret will be displayed.
    * Download the JSON file for later use.


### Getting Facebook OAuth Client ID and Secret
1.  **Facebook for Developers:**
    * Go to [Facebook for Developers](https://developers.facebook.com/).
    * Create an app or select an existing one.

2.  **Add Login Product:**
    * Add the **"Facebook Login"** product to your app.

3.  **Settings:**
    * Go to **"Facebook Login"** -> **"Settings"**.
    * Configure valid OAuth redirect URIs.

4.  **Basic Settings:**
    * Navigate to **"Settings"** -> **"Basic"**.

5.  **App ID and Secret:**
    * Your App ID (Client ID) and App Secret (Client Secret) will be displayed.


### Getting GitHub OAuth Client ID and Secret
1.  **GitHub Developer Settings:**
    * Go to your GitHub profile settings: [GitHub Settings](https://github.com/settings/profile).
    * Navigate to **"Developer settings"** -> **"OAuth Apps"**.

2.  **New OAuth App:**
    * Click **"New OAuth App"** or select an existing one.

3.  **Application Details:**
    * Fill in the application name, homepage URL, and authorization callback URL.

4.  **Client ID and Secret:**
    * Click **"Register application"**.
    * Your Client ID and Client Secret will be displayed.


### Getting Salesforce OAuth Client ID and Secret
1.  **Salesforce Setup:**
    * Log in to your Salesforce org.
    * Navigate to "Setup".

2.  **App Manager:**
    * Use the Quick Find box to search for and select **"App Manager"**.

3.  **New Connected App:**
    * Click **"New Connected App"**.

4.  **Basic Information:**
    * Enter basic information for your app (Connected App Name, API Name, Contact Email).

5.  **API (Enable OAuth Settings):**
    * In the **"API (Enable OAuth Settings)"** section:
        * Check "Enable OAuth Settings".
        * Enter the "Callback URL".
        * Select the OAuth scopes you need.

6.  **Save and Manage Consumer Details:**
    * Click "Save".
    * Click **"Manage Consumer Details"** (you might need to verify your identity).

7.  **Consumer Key and Secret:**
    * Your Consumer Key (Client ID) and Consumer Secret (Client Secret) will be displayed.