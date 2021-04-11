# ZeroFunkt
Zero font obfuscation for your html letters. Multiple alphabets


### Usage:

```html
     M""""""""`M                            MM""""""""`M                   dP       M""""""""M
     Mmmmmm   .M                            MM  mmmmmmmM                   88       Mmmm  mmmM
     MMMMP  .MMM .d8888b. 88d888b. .d8888b. M'      MMMM dP    dP .d8888b. 88  .dP  MMMM  MMMM
     MMP  .MMMMM 88ooood8 88'  `88 88'  `88 MM  MMMMMMMM 88    88 88'  `"" 88888"   MMMM  MMMM
     M' .MMMMMMM 88.  ... 88       88.  .88 MM  MMMMMMMM 88.  .88 88.  ... 88  `8b. MMMM  MMMM
     M         M `88888P' dP       `88888P' MM  MMMMMMMM `88888P' `88888P' dP   `YP MMMM  MMMM
     [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

                This module will obfuscate the strings in your letters in order to make your content
more difficult to detect by spam filters. The technique is called ZeroFont.
Which will look something like this:

 </span>,P <span style="font-size: 0.0000000000000000000000000000008349vh;">Farmer
 </span>,a <span style="font-size: 0.00000000000000000000000000000039632%;">soutien
 </span>,y <span style="font-size: 0.00000000000000000000000000000056979em;">océans
 </span>,P <span style="font-size: 0.0000000000000000000000000000005243%;">debout,
 </span>,a <span style="font-size: 0.00000000000000000000000000000067519vw;">enseignants,
 </span>,l <span style="font-size: 0.00000000000000000000000000000091066vw;">celui-ci

Please enter the path to your letter (if it is not in this directory)
>>>>>>> **test.html**
```

- Enter the path to your .html file, assuming it is not in the current directory in which case you only need enter the html and extension (ex. test.html)

```
Pick a number between 1 and 3!
This only decides what alphabet will be used to hide your strings examples below:

1. French/English/Latin
2. Russian/Cryillic
3. Arabic
4. Hindu
5. Japanese

You may make your selection now:

```

- Here you select the alphabet to use depending on the country the email is targeting. I may add more but each one has roughly 10k words it grabs randomly from.

```
Choose your level of obfuscation (1-10): 
```

- Self explanitory i think... the higher the number from 1-10 the more difficult it will be for the ESPs AI AND YOU to read. 

### Before/After Examples:
##### Before:
![before](https://github.com/kromatixx/ZeroFunkt/blob/main/htmlUnENC.png)

##### After:
![after](https://github.com/kromatixx/ZeroFunkt/blob/main/enchtml.png)
