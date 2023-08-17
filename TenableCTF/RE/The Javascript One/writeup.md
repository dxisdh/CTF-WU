We are given some obfuscated Javascript code:

``
var _0x4b0817=_0x3cdb;(function(_0x25abc1,_0x1b11ab){var _0x21dd4f=_0x3cdb,_0x15cf55=_0x25abc1();while(!![]){try{var...
``

Well, it's pretty hard to read so I will use a deobfuscator to make it look good to reverse then. I find a function that seems to be an encryption method:

````
function encryptFlag(_0xbf47e0) {
  var _0x381330 = _0x5114[2];
  for (var _0x191b0f = 0; _0x191b0f < _0xbf47e0[_0x5114[3]]; _0x191b0f++) {
    var _0x2bc446 = _0xbf47e0[_0x5114[4]](_0x191b0f);
    var _0x5e8a75 = _0x2bc446 ^ _0x191b0f;
    _0x381330 += String[_0x3e24(271)](_0x5e8a75);
  }
  ;
  return btoa(_0x381330);
}
````

btoa converts to base64 so we have to look for the base64 encoded value and I found: `Zm1jZH92N2tkcFVhbXs6fHNjI2NgaA==`

And here we go with the decryption:

````
import base64
encoded = base64.b64decode("Zm1jZH92N2tkcFVhbXs6fHNjI2NgaA=="
for i in range(0, len(encoded)):
    print(chr(encoded[i] ^ i), end = "")
````

Flag: `flag{s1lly_jav4scr1pt}`
