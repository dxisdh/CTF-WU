We got a zip file that contains a .jar file. Unzip it and we will get a .class file and a .jar file. I will use a Java decompiler website to decompile the .class file.
In main() function, we can see a variable name encodeToString and it uses Base64 to encode. And we have this code block:
````
if (encodeToString.length() != 20) {
            failure();
        }
        else if (!encodeToString.endsWith("NoZXI=")) {
            failure();
        }
        else if (!encodeToString.startsWith("R2FsZU")) {
            failure();
        }
        else if (!encodeToString.substring(6, 14).equals("JvZXR0aW")) {
            failure();
        }
        else {
            success();
        }
````

First, it will check if the length of the string is 20. Next, if the end of the string isn't equal to "NoZXI=" or the beginning of the string doesn't start with "R2FsZU" or the substring doesn't equal to "JvZXR0aW", the failure() function will be executed.
Put three pieces of the flag together and use the Base64 decoder and we will get the flag.

Flag: `CACI{Gale_Boetticher}`
