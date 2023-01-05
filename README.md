
# stremio-gdrive

This is an updated version of https://github.com/ssnjr2002/stremio-gdrive


1. Go to https://console.cloud.google.com/projectcreate
2. Name the project whatever you want and click create. 
3. Next to "Google Cloud Platform," click the Down arrow ![image](https://user-images.githubusercontent.com/38104354/113966809-6d626200-984d-11eb-96df-ca21e06b44c1.png) and select your project.
4. At the top-left corner, click the hamburger menu icon: ![image](https://user-images.githubusercontent.com/38104354/113966919-9a167980-984d-11eb-94c9-44d0e329a250.png) Click APIs & Services > Credentials.
5. Click Configure Consent Screen. The "OAuth consent screen" screen appears.
6. Set user type to external and click create.
7. Fill in the required details, you can give your own email as dev and support email. Click save and continue.
8. For the scopes page leave it as it is and click save and continue.
9. Now add yourself (your email id) as the test user by pressing add users. Click save and continue.
10. Now on your left, under API & Services, you will see Dashboard. Click on it and then click on Enable APIs and Services.
11. Search for Google Drive and click on the result that says Google Drive API and then click on Enable.
12. Now do step 4 again.
13. Click Create Credentials > OAuth client ID.
14. Choose application type as Desktop, name it whatever you want and click create.
15. The newly created credential appears under "OAuth 2.0 Client IDs." Click the download button to the right of the newly-created OAuth 2.0 Client ID. We will get a client_secret.json file, we will need this for the next section.
16. Now once again, at the top-left corner, click the hamburger menu icon: ![image](https://user-images.githubusercontent.com/38104354/113966919-9a167980-984d-11eb-94c9-44d0e329a250.png) Click APIs & Services > OAuth Consent Screen.
17. Under Publishing Status you will see a button called PUBLISH APP, click on that and choose confrim. 


18. Use the colab notebook to easily obtain the token and the required code for the cloudflare proxy: 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ShuvamJaswal/Gdrive-Stremio-Update/blob/main/Get%20Token%20and%20CF%20Proxy%20Code.ipynb)

19. Run the cell of the  method number 1. Just press the circular play button beside the rectangular box. select your client-secret.json and follow the url that u receive click and login and authorize then u will be redirected to a error page (http://localhost:1/?state=dhjhvdhvdsu&code=    Copythis       &scope=https://www.googleapis.com/auth/drive, come back to colab tab and entered the copied text in authourization field then u will receive token.

20.copy the token string for later when we deploy the vercel backend, the token should look something like this:

```json
{"token": "jhgdfgdhgfh", "refresh_token": "1//sdhgbfdhghd", "token_uri": "https://oauth2.googleapis.com/token", "client_id": "hsdgfjhgfsd.apps.googleusercontent.com", "client_secret": "gfsdfsdgf", "scopes": ["https://www.googleapis.com/auth/drive"]}
```
21. goto vercel.com create a new project, click import third party repo.
22. enter https://github.com/ShuvamJaswal/Gdrive-Stremio-Update/
23. This will clone the repo to your github account.
24. Goto dashboard of newly created account.
25. goto settings> Environment variables> Enter TOKEN word in key and entered the text which u obtained in step 20 to value field.
26. goto deployments tab.
27. select top most entry and press menu button(vertical three dots) and tap redeploy uncheck build cache option
28. press on visit button.

### Installing the addon to your Stremio account:

1. Get the url of the vercel app you deployed. Add `/manifest.json` to the end. For example if my app url is `https://<your app url.vercel.app/' add `/manifest.json` to the end to get: `https://<your app url.vercel.app/manifest.json`. Copy this url.
2. Open stremio on desktop or android and go to addons section.
3. In the search bar paste the manifest link (`https://<your app url.vercel.app/manifest.json`) and press enter. Click install and you are done.

## How the addon works

The addon uses the drive api to search for video files in your drive (both your teamdrives and mydrive) kinda like using the google drive web search bar. 

So after setting up the addon go and search for something on stremio. When you open a search result, stremio will ask the addon if it has the video for the search result. The addon searches for the video in your google drive and if it gets any result it will give it to stremio and stremio will display the results. 

For example if I want to watch a movie, say its called **Pirates of the Goolag**, then:
* I will open stremio and search for **Pirates of the Goolag**. If its on imdb then it should appear on the stremio search results (stremio fetches search results from imdb).
* Open the search result for **Pirates of the Goolag** and stremio will ask the addon if it has a video stream for **Pirates of the Goolag**. 
* The addon searches in your Google Drive for **Pirates of the Goolag** and if its anywhere on your google drive, doesnt matter where as long as the video file has the _name_ and _year_ of the movie (for eg: **Pirates of the Goolag 2016.mkv** or **Pirates.of.the.Goolag.2016.UHD.BluRay.x265.mkv**), the addon will return the search results for **Pirates of the Goolag**. 
* Stremio will then display it as a video stream and all you have to do is tap on it and enjoy. 

The addon searches for:

* Movies by searching for Videos with their filename as the name of the movie and when it was released. 
  Eg video filename: **Pirates of the Goolag 2016.mkv**
* Series episodes by searching for Videos with their filename as the name of the series and which episode it was by a specifier. Supported specifiers are:

    * S01 E01
    * S1 E1
    * Season 1 Episode 1
    * 1x01
    * 1x1


