## SUI
*a startpage for your server and / or new tab page*  
*Project inspired from fork source, i.e: https://github.com/jeroenpardon/sui and https://github.com/circa10a/Device-Monitor-Dashboard for the python part*

![screenshot](https://i.imgur.com/J4d7Q3D.png)

[More screenshots](https://imgur.com/a/FDVRIyw)

### Deploy with Docker compose

#### Prerequisites:
- python
- web server

#### Install:

 - `git clone` this repository
 - set a cron job with "*/2 * * * * cd /usr/share/nginx/html/ && /usr/bin/python report.py &> /dev/null"
 - The page should be available at  `http://localhost:4000` 

### Customization

#### Changing color themes
 - Click the options button on the left bottom

#### Apps
Add your apps by editing apps.json:

    {
	    "apps" : [
		    {"name":"Name of app 1","hostname":"sub1.example.com","port":80,"href":"https://sub1.example.com" ,"icon":"icon-name"},
		    {"name":"Name of app 2","hostname":"sub2.example.com""port":8080,"href":"https://sub1.example.com" ,"icon":"icon-name"}
	    ]
    }

Please note:

 - No `,` at the end of the last app's line
 - Find the names  of icons to use at [Material Design Icons](https://materialdesignicons.com/)

#### Bookmarks
Add your bookmarks by editing links.json:

```
{  
   "bookmarks":[  
      {  
         "category":"Category1",
         "links":[  
            {  
               "name":"Link1",
               "url":"http://example.com"
            },
            {  
               "name":"Link2",
               "url":"http://example.com"
            }
         ]
      },
      {  
         "category":"Category2",
         "links":[  
            {  
               "name":"Link1",
               "url":"http://example.com"
            },
            {  
               "name":"Link2",
               "url":"http://example.com"
            }
         ]
      }
   ]
}
```
Add names for the categories you wish to define and add the bookmarks for each category.

Please note:

 - No `,` at the end of the last bookmark in a category and at the end of the last category


#### Color themes
These can be added or customized in the themer.js file. When changing the name of a theme or adding one, make sure to edit this section in index.html accordingly:

```
    <section  class="themes">
```

I might add a simpler way to edit themes at some point, but adding the current ones should be pretty straight forward.
